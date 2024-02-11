import os

DIRECTORY = ".\\FILE_IDENTIFY\\"
TO_REMOVE = ["(1)","(2)","(3)","(4)","(5)"]
ERROR = ""

def rename(dirs):
	global ERROR
	global TO_REMOVE
	contents = os.listdir(dirs)
	for content in contents:
		#print(content)
		p = os.path.join(dirs,content)
		if os.path.isfile(p):
			for each in TO_REMOVE:
				if each in content:
					src = os.path.join(dirs,content)
					dst = str(src).replace(each,"")
					# print(dst)
					try:
						print("From  "+src+"       ==>         "+dst)
						os.rename(src,dst)
					except Exception as e:
						#raise e
						ERROR = ERROR + "\n文件{}出错:::::{}\n".format(src,e)
		else:
			print("目录:"+p)
			rename(p)

rename(DIRECTORY)
print("\n\n错误日志：:::\n"+ERROR)