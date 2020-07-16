# -*- coding: utf-8 -*-
from os.path import join,isdir,isfile,getsize,exists
from os import listdir,mkdir,sep
import shutil
import WindowsColoredCommandLine
import time
# import Find_Duplicate_File_by_Size as FDFS

#要检查是否有重复的目录,文件名中不可有“>”！！
IDN = ".{}FILE_IDENTIFY".format(sep)
PICK = ".{}FILE_PICK_UP_HERE".format(sep)
IDENTIFY = ["(1)","(2)","(3)","(4)"]
ACTION = False
CHANGE_LIST_A = ""
CHANGE_LIST_B = ""
ERROR_REPORT = ""
WINDOWS = (sep=="\\")

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
	# if ACTION:
		# print("获取到的文件信息有：")
		# for x in FILE_INFO:
			# print("输出文件信息："+x)
	return FILE_INFO

def __mkdir(which_path,single_file_info):
	global ACTION
	file_path = single_file_info.split(">")[2]
	pathSplit = file_path.split(sep)
	pathLen = len(pathSplit)
	for x in range(1,pathLen-1):
		if(exists(join(which_path,pathSplit[x]))):
			# print("Folder existed.")
			pass
		else:
			if ACTION:
				mkdir(join(which_path,pathSplit[x]))
			else:
				# print("mkdir将创建文件夹："+str(join(which_path,pathSplit[x])))
				pass
		which_path = join(which_path,pathSplit[x])
	# print("mkdir has done.")

def fileWithTheSameSize(file_info_list):
	global ACTION
	global CHANGE_LIST_A
	global CHANGE_LIST_B
	global ERROR_REPORT
	file_duplicate = []
	file_list_part = file_info_list
	for each_info in file_info_list:
		file_size = str(each_info.split(">")[1])
		n = 0
		for each in file_list_part:
			if file_size each.split(">")[1]:
				if each_info == each:
					pass
				else:
					file_duplicate.append(each)
					n+=1
			else:
				pass
		file_list_part.remove(each_info)
		if n>0:
			# file_duplicate.append(each_info)
			pass
		else:
			pass

	if len(file_duplicate)!=0:
		for dup in file_duplicate:
			# print("发现大小相同的文件：{}".format(str(each_info.split(">")[2])))
			CHANGE_LIST_A = CHANGE_LIST_A + "\n发现大小相同的文件：  {}  ".format(str(dup.split(">")[2]))
			src = dup.split(">")[2]
			dst = dup.split(">")[2].replace(".{}".format(sep),".{0}IDN_DEL{0}".format(sep))
			try:
				if ACTION:
					__mkdir(".{0}IDN_DEL".format(sep),dup)
					shutil.move(src,dst)
				else:
					__mkdir(".{0}IDN_DEL".format(sep),dup)
					# print("大小一致：移动文件从{}到{}。".format(src,dst))
				CHANGE_LIST_B = CHANGE_LIST_B + "\n文件  {}  移动到  {}  ".format(src,dst)
			except Exception as e:
				# raise e
				ERROR_REPORT = ERROR_REPORT+"\nfileWithTheSameSize(file_info_list)在处理{}时发生了错误:{}".format(dup,e)
	else:
		print("没有大小相同的文件")

if __name__ == '__main__':
	file_list = getEachFilePath(IDN)
	fileWithTheSameSize(file_list)

	if WINDOWS:
		print("\n大小一致的文件：")
		WindowsColoredCommandLine.printColor(4,CHANGE_LIST_A)
		print("\n文件处理预告：")
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
	x = input("是否执行？(y/N)")
	if x in ["Y","y"]:
		ACTION=True
		file_list = getEachFilePath(IDN)
		fileWithTheSameSize(file_list)
	else:
		pass

