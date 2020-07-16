# -*- coding: utf-8 -*-
from os.path import join,isdir,isfile,getsize,exists
from os import listdir,mkdir,sep
import shutil
import WindowsColoredCommandLine
import time
import argparse
import sys

#要检查是否有重复的目录,文件名中不可有“>”！！

DIRECTORY = []
IDENTIFY = None

ACTION = False
CHANGE_LIST_A = ""
CHANGE_LIST_B = ""
ERROR_REPORT = ""
WINDOWS = (sep=="\\")

def get_args():
	global DIRECTORY
	parser = argparse.ArgumentParser(
		usage="python Find_Duplicate_File_by_Size.py [文件夹、……]",
		description="查找文件夹中大小相同的文件。"
	)
	parser.add_argument('-d', type = str, default = None ,dest = "file_path", nargs = "+", help="文件夹路径")
	parser.add_argument('-i', type = str, default = None ,dest = "identify" ,action = "store", nargs = "+", help="重复识别标识 记得加双引号")
	parse_result = parser.parse_args()
	DIRECTORY = parse_result.file_path
	if parse_result.file_path==None:
		print("请输入-h显示帮助：python.exe Find_Duplicate_File_by_Size.py -h")
		sys.exit(1)
	IDENTIFY = parse_result.identify
	print(IDENTIFY)

#获取文件大小、路径。返回列表元素：%文件名%>%大小%>%路径%
def getEachFilePath(path):
	global ACTION
	global ERROR_REPORT
	FILE_INFO = []
	contents_list = listdir(path)
	for content in contents_list:
		if ">" in content:
			print("非法文件名包含“>”")
			ERROR_REPORT = ERROR_REPORT+"\ngetEachFilePath(path)在处理{}时发生了错误。[0]".format(str(join(path,content)))
		elif isdir(join(path,content)):
			file_list = getEachFilePath(join(path,content))
			FILE_INFO.extend(file_list)
		elif isfile(join(path,content)):
			file_path = join(path,content)
			info = "{}>{}>{}".format(str(content),str(getsize(file_path)),str(file_path))
			FILE_INFO.append(info)
		else:
			ERROR_REPORT = ERROR_REPORT+"\ngetEachFilePath(path)在处理{}时发生了错误:{}".format(str(join(contents_list,content),e))
			print("未知文件系统")
	if (not ACTION):
		# print("获取到的文件信息有：")
		for x in FILE_INFO:
			print("输出文件信息："+x)
			pass
	return FILE_INFO

def __mkdir(which_path,single_file_info):
	global ACTION
	file_path = single_file_info.split(">")[2]
	pathSplit = file_path.split(sep)
	pathLen = len(pathSplit)
	for x in range(1,pathLen-1):
		if(exists(join(which_path,pathSplit[x]))):
			print("Folder existed.")
		else:
			if ACTION:
				mkdir(join(which_path,pathSplit[x]))
			else:
				print("mkdir将创建文件夹："+str(join(which_path,pathSplit[x])))
		which_path = join(which_path,pathSplit[x])
	print("mkdir has done.")


#如果识别出文件名带有重复标识的，移动到IDENTIFY文件夹
def recognizeDuplicateSignal(file_info_list , identify_list):
	global ACTION
	global CHANGE_LIST_A
	Signal = False
	if identify_list==None:
		print("未定义重复识别符号")
	else:
		Signal = True
		for info in file_info_list:
			file_name = str(info.split(">")[0])
			file_path = str(info.split(">")[2])
			for each in identify_list:
				if each in file_name:
					print("在{}文件名中发现标记{}".format(info,each))
					src = file_path
					dst = file_path.replace(".{}".format(sep),".{0}FILE_IDENTIFY{0}".format(sep))
					try:
						__mkdir(".{}FILE_IDENTIFY".format(sep),info)
						if ACTION:
							shutil.move(src,dst)
						CHANGE_LIST_A = CHANGE_LIST_A + "文件{}移动到{}\n".format(src,dst)
					except Exception as e:
						print("recognizeDuplicateSignal(file_info_list , identify_list)文件移动出错。")
						ERROR_REPORT = ERROR_REPORT+"\nrecognizeDuplicateSignal(file_info_list , identify_list)在处理{}时发生了错误:{}".format(file_path,e)
	return Signal

def fileWithTheSameSize(file_info_list):
	global ACTION
	global CHANGE_LIST_B
	global ERROR_REPORT
	file_duplicate = []
	file_list_part = file_info_list
	for each_info in file_info_list:
		file_size = str(each_info.split(">")[1])
		n = 0
		for each in file_list_part:
			if file_size == each.split(">")[1]:
				if each_info == each:
					pass
				else:
					file_duplicate.append(each)
					n+=1
			else:
				pass
		file_list_part.remove(each_info)
		if n>0:
			file_duplicate.append(each_info)
		else:
			pass
	# print("发现大小相同的文件{}个。".format(n))
	# print(file_duplicate
	if len(file_duplicate)!=0:
		for dup in file_duplicate:
			print("发现大小相同的文件：{}".format(str(dup.split(">")[2])))
			src = dup.split(">")[2]
			dst = dup.split(">")[2].replace(".{}".format(sep),".{0}FILE_PICK_UP_HERE{0}".format(sep))
			try:
				if ACTION:
					__mkdir(".{0}FILE_PICK_UP_HERE".format(sep),dup)
					shutil.move(src,dst)
				else:
					__mkdir(".{0}FILE_PICK_UP_HERE".format(sep),dup)
					print("大小一致：移动文件从{}到{}。".format(src,dst))
				CHANGE_LIST_B = CHANGE_LIST_B + "文件{}    移动到    {}    Size:{}\n".format(src,dst,dup.split(">")[1])
			except Exception as e:
				# raise e
				ERROR_REPORT = ERROR_REPORT+"\nfileWithTheSameSize(file_info_list)在处理{}时发生了错误:{}".format(dup,e)
	else:
		print("没有大小相同的文件")

if __name__ == '__main__':
	get_args()
	print(DIRECTORY,IDENTIFY)
	if exists((".{}FILE_PICK_UP_HERE".format(sep))):
		# shutil.rmtree(".{}FILE_PICK_UP_HERE".format(sep))
		pass
	else:
		mkdir(".{}FILE_PICK_UP_HERE".format(sep))
	if exists((".{}FILE_IDENTIFY".format(sep))):
		# shutil.rmtree(".{}FILE_IDENTIFY".format(sep))
		pass
	else:
		mkdir(".{}FILE_IDENTIFY".format(sep))
	if exists((".{}IDN_DEL".format(sep))):
		# shutil.rmtree(".{}IDN_DEL".format(sep))
		pass
	else:
		mkdir(".{}IDN_DEL".format(sep))
	for dir in DIRECTORY:
		file_info_main = getEachFilePath(dir)
	recognizeDuplicateSignal(file_info_main,IDENTIFY)
	time.sleep(3)
	for dir in DIRECTORY:
		file_info_main = getEachFilePath(dir)
	fileWithTheSameSize(file_info_main)
	if WINDOWS:
		print("\n找到重复标志的文件：")
		WindowsColoredCommandLine.printColor(4,CHANGE_LIST_A)
		print("\n找到大小一致的文件：")
		WindowsColoredCommandLine.printColor(5,CHANGE_LIST_B)
		print("\n错误日志：")
		WindowsColoredCommandLine.printColor(6,ERROR_REPORT)
	else:
		print("\n找到重复标志的文件：")
		print("\033[1;32;41m{0}\033[0m".format(CHANGE_LIST_A))
		print("\n找到大小一致的文件：")
		print("\033[1;33;41m{0}\033[0m".format(CHANGE_LIST_B))
		print("\n错误日志：")
		print("\033[1;31;41m{0}\033[0m".format(ERROR_REPORT))

	# print(CHANGE_LIST_B.replace("\n","\n,"))

	x = input("是否执行？(y/N)")
	if x in ["Y","y"]:
		file_handle=open('./A.csv',mode='w')
		file_handle.write(CHANGE_LIST_A.replace("\n",",\n"))
		file_handle.close()
		file_handle=open('./B.csv',mode='w')
		file_handle.write(CHANGE_LIST_B.replace("\n",",\n"))
		file_handle.close()
		ACTION=True
		for dir in DIRECTORY:
			file_info_main = getEachFilePath(dir)
		recognizeDuplicateSignal(file_info_main,IDENTIFY)
		time.sleep(3)
		for dir in DIRECTORY:
			file_info_main = getEachFilePath(dir)
		fileWithTheSameSize(file_info_main)
	else:
		pass
