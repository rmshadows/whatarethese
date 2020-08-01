# -*- coding: utf-8 -*-
'''
Version:2.5
首先判断文件名是否带有自定义的重复标记（IDENTIFY），如果有就移动到FILE_IDENTIFY文件夹。
随后判断文件大小是否有一致的，有则移动到FILE_PICK_UP_HERE文件夹中。

#要检查是否有重复的目录,文件名中不可有“>”！！
#DIRECTORY中每个文件夹的名称都要带上“.\\”，或者“./” 或者是完整的绝对路径。比如文件夹A和B，写成：
# DIRECTORY = [".\\A",".\\B"]

要反复运行，要不效果不咋地。就是说：
1、运行-执行文件移动。
2、人工复查筛选结果，检查完毕，合并原始文件夹。
3、再次运行-执行。
4、再次人工
5、……………………
6、直到确认没有重复的文件。

'''
from os.path import join,isdir,isfile,getsize,exists
from os import listdir,mkdir,sep
import shutil
import WindowsColoredCommandLine
import time
import argparse
import sys

#要检查是否有重复的目录,文件名中不可有“>”！！
DIRECTORY = None
#自定义的重复标志
IDENTIFY = None

#不进行文件操作，只提供预览
ACTION = False
#TEMP_XXX是每次检查时要操作的文件
TEMP_CHANGE_LIST_A = ""
TEMP_CHANGE_LIST_B = ""
TEMP_ERROR_REPORT = ""
#下面是本次脚本的全部执行情况概览
CHANGE_LIST_A = ""
CHANGE_LIST_B = ""
ERROR_REPORT = ""
#是否是Windows系统
WINDOWS = (sep=="\\")

'''
从命令行获取参数
注意：当DIRECTORY和IDENTIFY中有一个不为None则该方法失效。
'''
def get_args():
	global DIRECTORY
	global IDENTIFY
	parser = argparse.ArgumentParser(
		usage="python Find_Duplicate_File_by_Size.py -d \"文件夹\"[ -i \"IDN\"]",
		description="查找文件夹中大小相同的文件。使用示例：python xxx.py -d \".\\A\" \".\\B\" -i \"(1)\" \"副本\""
	)
	parser.add_argument('-d', type = str, default = None ,dest = "file_path", nargs = "+", help="文件夹路径，相对路径前记得加上“.\\”等代表当前的路径。")
	parser.add_argument('-i', type = str, default = None ,dest = "identify" ,action = "store", nargs = "+", help="重复识别标识 记得加双引号")
	parse_result = parser.parse_args()
	DIRECTORY = parse_result.file_path
	if parse_result.file_path==None:
		print("请输入-h显示帮助：python.exe Find_Duplicate_File_by_Size.py -h")
		sys.exit(1)
	IDENTIFY = parse_result.identify
	print(IDENTIFY)

#获取文件大小、路径。返回列表元素：%文件名%>%大小%>%路径%
#                                0       1      2   索引
def getEachFilePath(path):
	global ACTION
	global TEMP_ERROR_REPORT
	FILE_INFO = []
	contents_list = listdir(path)
	for content in contents_list:
		if ">" in content:
			print("非法文件名包含“>”")
			TEMP_ERROR_REPORT = TEMP_ERROR_REPORT+"\ngetEachFilePath(path)在处理{}时发生了错误。[0]".format(str(join(path,content)))
		elif isdir(join(path,content)):
			file_list = getEachFilePath(join(path,content))
			FILE_INFO.extend(file_list)
		elif isfile(join(path,content)):
			file_path = join(path,content)
			info = "{}>{}>{}".format(str(content),str(getsize(file_path)),str(file_path))
			FILE_INFO.append(info)
		else:
			TEMP_ERROR_REPORT = TEMP_ERROR_REPORT+"\ngetEachFilePath(path)在处理{}时发生了错误:{}".format(str(join(contents_list,content),e))
			print("未知文件系统")
	if (not ACTION):
		# print("获取到的文件信息有：")
		for x in FILE_INFO:
			# print("输出文件信息："+x)
			pass
	return FILE_INFO

#创建文件夹 在whichPath中创建singlefileinfo的目录树。single_file_info是单个FILE_INFO(见上一行)
def __mkdir(which_path,single_file_info):
	global ACTION
	abs = False
	if single_file_info.split(">")[2][1:2]==":":
		file_path = single_file_info.split(">")[2].replace(":","",1)#0:/1/2/3 -> 0/1/2/3
		abs = True
	else:
		file_path = single_file_info.split(">")[2]#./1/2/3
	pathSplit = file_path.split(sep)# [0,1,2,3] [.,1,2,3]
	pathLen = len(pathSplit)
	if abs:
		for x in range(0,pathLen-1):# [0,1,2] [.,1,2]
			if(exists(join(which_path,pathSplit[x]))):# ./which/[0,1,2] [.,1,2,]
				#print("Folder existed.")
				pass
			else:
				if ACTION:
					mkdir(join(which_path,pathSplit[x]))# ./which/[0,1,2] [.,1,2,]
				else:
					#print("mkdir将创建文件夹："+str(join(which_path,pathSplit[x])))
					pass
			which_path = join(which_path,pathSplit[x])
	else:
		for x in range(1,pathLen-1):# [0,1,2] [.,1,2]
			if(exists(join(which_path,pathSplit[x]))):# ./which/[0,1,2] [.,1,2,]
				#print("Folder existed.")
				pass
			else:
				if ACTION:
					mkdir(join(which_path,pathSplit[x]))# ./which/[0,1,2] [.,1,2,]
				else:
					#print("mkdir将创建文件夹："+str(join(which_path,pathSplit[x])))
					pass
			which_path = join(which_path,pathSplit[x])
	#print("mkdir has done.")


#如果识别出文件名带有重复标识的，移动到IDENTIFY文件夹
def recognizeDuplicateSignal(file_info_list , identify_list):
	global ACTION
	global TEMP_CHANGE_LIST_A
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
					if file_path[1:2]==":":
						dst = ".{0}FILE_IDENTIFY{0}".format(sep)+file_path.replace(":","",1)
					else:
						dst = file_path.replace(".{}".format(sep),".{0}FILE_IDENTIFY{0}".format(sep))
					print(dst)
					try:
						__mkdir(".{}FILE_IDENTIFY".format(sep),info)
						if ACTION:
							shutil.move(src,dst)
						TEMP_CHANGE_LIST_A = TEMP_CHANGE_LIST_A + "文件{}         ▇▇移动到▇▇          {}\n".format(src,dst)
					except Exception as e:
						print("recognizeDuplicateSignal(file_info_list , identify_list)文件移动出错。")
						TEMP_ERROR_REPORT = TEMP_ERROR_REPORT+"\nrecognizeDuplicateSignal(file_info_list , identify_list)在处理{}时发生了错误:{}".format(file_path,e)
	return Signal

def fileWithTheSameSize(file_info_list):
	global ACTION
	global TEMP_CHANGE_LIST_B
	global TEMP_ERROR_REPORT
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
			if dup.split(">")[2][1:2]==":":
				dst = ".{0}FILE_PICK_UP_HERE{0}".format(sep)+dup.split(">")[2].replace(":","",1)
			else:
				dst = dup.split(">")[2].replace(".{}".format(sep),".{0}FILE_PICK_UP_HERE{0}".format(sep))
			try:
				if ACTION:
					__mkdir(".{0}FILE_PICK_UP_HERE".format(sep),dup)
					shutil.move(src,dst)
				else:
					__mkdir(".{0}FILE_PICK_UP_HERE".format(sep),dup)
					print("大小一致：移动文件从{}到{}。".format(src,dst))
				TEMP_CHANGE_LIST_B = TEMP_CHANGE_LIST_B + "文件{}          ▇▇移动到▇▇          {}---------Size:{}\n".format(src,dst,dup.split(">")[1])
			except Exception as e:
				# raise e
				TEMP_ERROR_REPORT = TEMP_ERROR_REPORT+"\nfileWithTheSameSize(file_info_list)在处理{}时发生了错误:{}".format(dup,e)
	else:
		print("没有大小相同的文件")

def showInfo():
	if WINDOWS:
		print("\n找到重复标志的文件：")
		WindowsColoredCommandLine.printColor(4,TEMP_CHANGE_LIST_A)
		print("\n找到大小一致的文件：")
		WindowsColoredCommandLine.printColor(5,TEMP_CHANGE_LIST_B)
		print("\n错误日志：")
		WindowsColoredCommandLine.printColor(6,TEMP_ERROR_REPORT)
	else:
		print("\n找到重复标志的文件：")
		print("\033[1;32;41m{0}\033[0m".format(TEMP_CHANGE_LIST_A))
		print("\n找到大小一致的文件：")
		print("\033[1;33;41m{0}\033[0m".format(TEMP_CHANGE_LIST_B))
		print("\n错误日志：")
		print("\033[1;31;41m{0}\033[0m".format(TEMP_ERROR_REPORT))

if __name__ == '__main__':
	CSV_ERROR = ""
	# print("TEMP:"+TEMP_CHANGE_LIST_A,TEMP_CHANGE_LIST_B,TEMP_ERROR_REPORT)
	if ((DIRECTORY == None) & (IDENTIFY == None)):
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
	file_info_main = []
	for dir in DIRECTORY:
		file_info_main.extend(getEachFilePath(dir))
	recognizeDuplicateSignal(file_info_main,IDENTIFY)
	time.sleep(3)
	file_info_main = []
	for dir in DIRECTORY:
		file_info_main.extend(getEachFilePath(dir))
	fileWithTheSameSize(file_info_main)
	showInfo()
	# print(TEMP_CHANGE_LIST_B.replace("\n","\n,"))

	x = input("是否执行？(y/N)")
	if x in ["Y","y"]:
		# try:
		# 	file_handle=open('./A.csv',mode='w')
		# 	file_handle.write(TEMP_CHANGE_LIST_A.replace("\n",",\n"))
		# 	file_handle.close()
		# 	file_handle=open('./B.csv',mode='w')
		# 	file_handle.write(TEMP_CHANGE_LIST_B.replace("\n",",\n"))
		# 	file_handle.close()
		# except Exception as e:
		# 	CSV_ERROR = CSV_ERROR + "\n{}".format(e)
		ACTION=True
		file_info_main = []
		for dir in DIRECTORY:
			file_info_main.extend(getEachFilePath(dir))
		recognizeDuplicateSignal(file_info_main,IDENTIFY)
		time.sleep(3)
		file_info_main = []
		for dir in DIRECTORY:
			file_info_main.extend(getEachFilePath(dir))
		fileWithTheSameSize(file_info_main)
		showInfo()
		n = 1
		CHANGE_LIST_A = CHANGE_LIST_A + TEMP_CHANGE_LIST_A
		CHANGE_LIST_B = CHANGE_LIST_B + TEMP_CHANGE_LIST_B
		ERROR_REPORT = ERROR_REPORT + TEMP_ERROR_REPORT
		while ((TEMP_CHANGE_LIST_A != "") | (TEMP_CHANGE_LIST_B != "")):
			print("进入While循环")
			#print("%%{}%%{}%%".format(TEMP_CHANGE_LIST_A,TEMP_CHANGE_LIST_B))
			print("重复查询   "+str(n)+"   次。")
			n = n + 1
			CHANGE_LIST_A = CHANGE_LIST_A + TEMP_CHANGE_LIST_A
			CHANGE_LIST_B = CHANGE_LIST_B + TEMP_CHANGE_LIST_B
			ERROR_REPORT = ERROR_REPORT + TEMP_ERROR_REPORT
			TEMP_CHANGE_LIST_A = ""
			TEMP_CHANGE_LIST_B = ""
			TEMP_ERROR_REPORT = ""
			ACTION=True
			file_info_main = []
			for dir in DIRECTORY:
				file_info_main.extend(getEachFilePath(dir))
			recognizeDuplicateSignal(file_info_main,IDENTIFY)
			time.sleep(3)
			file_info_main = []
			for dir in DIRECTORY:
				file_info_main.extend(getEachFilePath(dir))
			fileWithTheSameSize(file_info_main)
			showInfo()
		print("执行退出")
		try:
			file_handle=open('./A.csv',mode='w')
			file_handle.write(CHANGE_LIST_A.replace("\n",",\n"))
			file_handle.close()
			file_handle=open('./B.csv',mode='w')
			file_handle.write(CHANGE_LIST_B.replace("\n",",\n"))
			file_handle.close()
		except Exception as e:
			CSV_ERROR = CSV_ERROR + "\n{}".format(e)
	else:
		print("不执行，退出")

	WindowsColoredCommandLine.printColor(6,"▇▇▇▇▇▇▇▇▇▇▇▇最终运行结果：▇▇▇▇▇▇▇▇▇▇▇▇▇\n\n")
	if WINDOWS:
		if CHANGE_LIST_A == "":
			WindowsColoredCommandLine.printColor(4,"▇▇▇▇▇▇▇▇▇▇▇▇没有找到带有重复标志的文件▇▇▇▇▇▇▇▇▇▇▇▇")
		else:
			print("▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n找到重复标志的文件：")
			WindowsColoredCommandLine.printColor(4,CHANGE_LIST_A)
		if CHANGE_LIST_B == "":
			WindowsColoredCommandLine.printColor(4,"▇▇▇▇▇▇▇▇▇▇▇▇本次没有找到大小一致的文件▇▇▇▇▇▇▇▇▇▇▇▇")
		else:
			print("▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n找到大小一致的文件：")
			WindowsColoredCommandLine.printColor(5,CHANGE_LIST_B)
		if (ERROR_REPORT == "") & (CSV_ERROR == ""):
			WindowsColoredCommandLine.printColor(4,"▇▇▇▇▇▇▇▇▇▇▇▇程序正常运行，没有发现错误▇▇▇▇▇▇▇▇▇▇▇▇")
		else:
			print("▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n错误日志：")
			WindowsColoredCommandLine.printColor(6,ERROR_REPORT)
			print("▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\nCSV生成错误:"+CSV_ERROR)
	else:
		if CHANGE_LIST_A == "":
			print("\033[1;32;41m{0}\033[0m".format("▇▇▇▇▇▇▇▇▇▇▇▇没有找到带有重复标志的文件▇▇▇▇▇▇▇▇▇▇▇▇"))
		else:
			print("▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n找到重复标志的文件：")
			print("\033[1;32;41m{0}\033[0m".format(CHANGE_LIST_A))
		if CHANGE_LIST_B == "":
			print("\033[1;32;41m{0}\033[0m".format("▇▇▇▇▇▇▇▇▇▇▇▇本次没有找到大小一致的文件▇▇▇▇▇▇▇▇▇▇▇▇"))
		else:
			print("▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n找到大小一致的文件：")
			print("\033[1;33;41m{0}\033[0m".format(CHANGE_LIST_B))
		if (ERROR_REPORT == "") & (CSV_ERROR == ""):
			print("\033[1;32;41m{0}\033[0m".format("▇▇▇▇▇▇▇▇▇▇▇▇程序正常运行，没有发现错误▇▇▇▇▇▇▇▇▇▇▇▇"))
		else:
			print("▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n错误日志：")
			print("\033[1;31;41m{0}\033[0m".format(ERROR_REPORT))
			print("▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\nCSV生成错误:"+CSV_ERROR)
