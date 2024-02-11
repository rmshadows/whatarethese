#!/usr/bin/python3
# coding:utf-8
# Lsof2IPLocation

import os;
import requests;
import bs4;
import time;
import sys;
import signal

startTime = time.time();#开始计时

class InputTimeoutError(Exception):#自定义超时异常
	pass;

def interrupted(signum,frame):#异常信号
	raise InputTimeoutError('Input Timeout!');#抛出（挂起）指定异常

debugModeSwitch = False;#定义debugmodeswitch初始值
signal.signal(signal.SIGALRM,interrupted);#使用signal作为信号阻塞
signal.alarm(3);#超时定为3秒

try:
	UserChoose = input('\033[1;32;40mIs debug mode enable?(y = enable/any key or 3"later = disable)\033[0m');#用户输入界面
	if UserChoose in ('Y','y'):#输入y则开启debug模式
		debugModeSwitch = True;
		print('Debug Mode Enable!');
	else:
		debugModeSwitch = False;#任意键跳过
except InputTimeoutError:#捕获自定义异常
	print('Debug Mode Disable Due to input status : TIMEOUT.');#打印超时凭证
	debugModeSwitch = False;

print('\033[1;31;40mLsof2IPLocation start! Please use MAXIMIZING WINDOWS to show all information.\033[0m');
COMMANDs = [];#定义一个空COMMAND参数列表
IPs = [];#定义一个空IP列表
Locations = [];#新建地址列表
if debugModeSwitch == True:
	print('定义一个空COMMAND参数列表\n定义一个空IP列表\n新建Locations地址列表');
else:
	pass;
#测试网络连接
def  checkNetworking():
	try:
		getRequest = requests.get("http://www.baidu.com",timeout=0.5);#测试是否能链接百度
	except:
		print('You\'re offline.Check your networking !');#不行则返回错误
		sys.exit(1);#退出程序
	else:
		print('\033[1;34;40mNetwork-stat comfirmed.Checking IP to location now......\033[0m');#网络测试通过
	if debugModeSwitch == True:
		print('checkNetworking() running.');
		print(getRequest.status_code);
		print(getRequest.text);
	else:
		pass;
if debugModeSwitch == True:
	print('定义checkNetworking方法检查网络连接是否正常');

#执行bash命令
def gainCommandAndIPInfo():
	commandInput = 'lsof -i | grep \'>\'';#bash命令"lsof -i | grep '>'"
	commandImplementation = os.popen(commandInput);#执行命令
	terminalOutput = commandImplementation.readlines();#以行为单位生成数组
	if debugModeSwitch == True:
		print('gainCommandAndIPInfo() running.');
		print(terminalOutput);
	else:
		pass;
	#将COMMAND列数据导入COMMAND列表
	for command in terminalOutput:#commands是单个command参数
		COMMANDs.append(command[0:9]);#将command参数导入空列表
	#将IP列数据导入IP列表
	for ip in terminalOutput:#ip是单个IP参数
		bIndex = ip.find('->')+2;#IP开头
		eIndex = ip.rfind(':');#IP末尾
		IPs.append(ip[bIndex:eIndex]);#将IP参数导入空列表
	findBootc = '_gateway' in IPs;#查询是否有Network-Manager-bootc进程
	if findBootc == True:#有则剔除
		bootcIndex = IPs.index('_gateway');#获得索引
		del IPs[bootcIndex];#删除IPs中的信息
		del COMMANDs[bootcIndex];#删除COMMANDs中的信息
	print('\033[1;36;40m---------------------------------------------------Gain local info done.----------------------------------------------------------\033[0m');#完成
	if debugModeSwitch == True:
		for i in COMMANDs:
			print(i);
		else:
			print('--------------------COMMANDs listed.---------------------');
		for j in IPs:
			print(j);
		else:
			print('-----------------------IPs listed.-----------------------');
	return(COMMANDs,IPs);
if debugModeSwitch == True:
	print('定义gainCommandAndIPInfo方法获取本地端口信息。');

def queryLocation():
	# Locations = [];#新建地址列表
	chinazURL = 'http://ip.tool.chinaz.com/';#爬取目标
	httpHeader = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'};#自定义http头部
	for i in range(0,len(IPs)):
		try:
			r = requests.get(chinazURL+IPs[i],headers = httpHeader,timeout=4);
			soup = bs4.BeautifulSoup(r.text , 'html.parser');#分析页面返回信息
			IPInfo = soup.find_all('span','Whwtdhalf w50-0');#<span class="Whwtdhalf w50-0">广东省广州市 北京百度网讯科技有限公司电信节点</span>
			if debugModeSwitch == True:
				print(r.status_code);
				print(r.text);
				print(r.request.headers);
				print(r.elapsed.total_seconds());#服务器响应时间
				print(soup);
				print(soup.prettify());
				for each in IPInfo:
					print(each);
			else:
				pass;
			del IPInfo[0];#只留下第二行信息
			gainStrIPInfo = str(IPInfo[0]);
			bIndex = gainStrIPInfo.find('w50-0">')+7;#Location开头
			eIndex = gainStrIPInfo.rfind('</span>');#Location末尾
			if debugModeSwitch == True:
				print(gainStrIPInfo[bIndex:eIndex]);
			else:
				pass;
			Locations.append(gainStrIPInfo[bIndex:eIndex]);
			print('\033[5;32;40m第{0:>2}次查询完成。\033[0m'.format(i+1));
			time.sleep(0.5);#延时时长
		except:
			print('\033[5;31;40m第{0:>2}次查询解析失败\033[0m'.format(i+1));#可能是由于电信反向域名解析等原因
			Locations.append('解析失败:{}'.format(IPs[i]));
	else:
		print('----------------------------------------------------------------------------------------------------------------------------------');
	if debugModeSwitch == True:
		print('queryLocation() done.');
		print('Locations列表:');
		for each in Locations:
			print(each);
	else:
		pass;
	return(Locations);

#输出格式处理:
def infoFormatOutput():
	#判断最长的数据(没用到):
	copy_list = COMMANDs+IPs+Locations;#合并三个列表
	num_list = [];#新建长度列表
	num_list=[len(everyParameter) for everyParameter in copy_list];#copy列表的长度
	resultLength = num_list.index(max(num_list));#得到最长的数据
	if debugModeSwitch == True:
		print('copy列表:');
		for c in copy_list:
			print(c);
		print('num列表:');
		for n in num_list:
			print(n);	
		print(resultLength);
	endTime = time.time();
	timer = endTime - startTime;#显示运行耗时
	print('\033[1;35;40m耗时：{:.2f}秒。\033[0m'.format(timer));
	print('\033[1;32;40mLsof2IPLocation v1.0-2020-03-10\033[0m');
	print('\033[1;32;40m_____     o O o                _____________#$_______________________________________%%%%_@@@@@@@@_________@@@_______________________________________________\033[0m');
	print('\033[1;32;40m_____            o O           ____________#$________________________________________%%_____@@___@@______@@@$@@@_____________________________________________\033[0m');
	print('\033[1;32;40m_____               o          ___________#$_____####__#####_____####_______\\\\______%%_____@@___@@_____@@$   $@@____________________________________________\033[0m');
	print('\033[1;32;40m_____|^^^^^^^^^^^^^^|l___      __________#$_____#_____#____#____#____________\\\\____%%_____@@@@@@______@@$    $@@____________________________________________\033[0m');
	print('_____|     \033[5;34;40m小火车\033[0m     |""\\___, _________#$______###__#_____#__######___========>__%%_____@@____________@@$__$@@_____________________________________________');
	print('\033[1;32;40m_____|________________|__|)__| ________#$_________#__#____#___#______________//__%%_____@@______________@@@@@_______________________________________________\033[0m');
	print('\033[1;32;40m_____|(@)(@)"""**|(@)(@)**|(@) _______#######_####____####___#______________//__%%%%___@@_______________@$$@________________________________________________\033[0m');
	print('\033[1;32;40m_____= = = = = = = = = = = = =___________________________________________________________________________@__________________________________________________\033[0m');
	print('--------------------------------------------------------------------------RESULT----------------------------------------------------------------------------');
	print('\033[1;31;40m{:10}\t\t{:<50}\t{:<50}\033[0m'.format('命令-command\t','IP地址-ip\t','位置-location\t'));
	for lineNum in range(0,len(COMMANDs)):
		print('\033[1;36;40m{:10}\t\t{:<50}\t\t{:<50}\033[0m'.format(COMMANDs[lineNum],IPs[lineNum],Locations[lineNum]));
	print('____________________________________________________________________________________________________________________________________________________________');
	print('------------------------------------------------------------------------\033[5;33;40mBy Ryan\033[0m-----------------------------------------------------------------------------');
	print('____________________________________________________________________________________________________________________________________________________________');

#主程序入口:
def main():
	checkNetworking();
	gainCommandAndIPInfo();
	queryLocation();
	infoFormatOutput();
print('\033[5;36;40mInitialization complete.............\033[0m');
main();#运行