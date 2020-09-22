#!/bin/python3
'''
用于生成派车信息
'''
from datetime import datetime

# 救护车司机名
driver = "老马"
# 派车单位
VDU = "后勤组"
# 用车事由
UF = "接送人员"
# 用车人
UN = "我自己"
# 联系电话
TEL = "166666"
# 用车出发点
where = "天安门"
# 出发时间是否与救护车同
DEP = True
# 出发时间
DEP_TIME = "2020年09月25日傍晚18点27分"

f = open("./wechat_demo.txt", "r")
name = ""
sex = ""
phone = ""
src = ""
dst = ""
appointed = ""

NAME = ""
SEX = ""
PHONE = ""
SRC = ""
DST = ""
TIME = ""

while True:
	lines = f.readlines(100000)
	if not lines:
		break
	for line in lines:
		if ("日期" in line):
			print("正在获取日期(年、月、日)：",end = "")
			y = line[3:7]
			m = line[7:9]
			d = line[9:].replace("\n","")
			appointed = "{0}-{1}-{2} ".format(y,m,d)
			TIME = "接送时间：{0}年{1}月{2}日".format(y,m,d)
			print(y,m,d)
		if ("姓名" in line):
			name = line[3:].replace("\n","")
			NAME = line.replace("\n","")
			print("获取名字："+name)
		if ("性别" in line):
			sex = line[3:].replace("\n","")
			SEX = line.replace("\n","")
			print("获取性别："+sex)
		if ("手机" in line):
			phone = line[3:].replace("\n","")
			PHONE = line.replace("\n","")
			print("获取手机号："+phone)
		if ("出发点" in line):
			src = line[4:].replace("\n","")
			SRC = line.replace("\n","")
			print("获取出发地:"+src)
		if ("目的地" in line):
			dst = line[4:].replace("\n","")
			DST = line.replace("\n","")
			print("获取目的地:"+dst)
		if ("接送时间" in line):
			time = line[5:]
			h = time[0:2]
			m = time[3:5]
			appointed = appointed + "{0}:{1}:00".format(h,m)
			if int(h) in range(0,5):
				day = "凌晨"
			elif int(h) in range(5,8):
				day = "早上"
			elif int(h) in range(8,11):
				day = "上午"
			elif int(h) in range(11,14):
				day = "中午"
			elif int(h) in range(14,18):
				day = "下午"
			elif int(h) in range(18,19):
				day = "傍晚"
			elif int(h) in range(19,25):
				day = "晚上"
			else:
				pass
			if int(m) == 0:
				TIME = TIME + "{0}{1}点".format(day,int(h))
			elif int(m) == 30:
				TIME = TIME + "{0}{1}点半".format(day,int(h))
			else:
				TIME = TIME + "{0}{1}点{2}分".format(day,int(h),int(m))
			TIME = TIME + "出发"
			time = time.replace("\n","")
			TIME = TIME.replace("\n","")
			print("获取时间:"+time)

today = str(datetime.now())[0:11]+"00:00:00"
# 格式：2019-01-02 00:00:00
today = datetime.strptime(today,'%Y-%m-%d %H:%M:%S')
appointed = datetime.strptime(appointed, '%Y-%m-%d %H:%M:%S')
print("时间区间:{}".format(today,appointed))
print("距离接送还有 "+str((appointed - today).days)+" 天")
slot = (appointed - today).days
if slot == 1:
	date = "明天"
elif slot == 2:
	date = "后天"
elif slot == 3:
	date = "大后天"
else:
	date = ""

######################################################################################################
if DEP:
	where = TIME[5:24] + " " + where + "出发"
else:
	where = DEP_TIME + " " + where + "出发"

print("\n\n开始输出救护车派车单：\n-----------------------------------------------------------------")
ambu = "{0}，这是{1}的接送信息。{2}{3}到{4} 接送隔离人员({5})，我出发前会给你打个电话，下面是具体信息:".format(driver,date,date,TIME[16:],src,name)
print(ambu+"\n")
print(NAME+"\n"+SEX+"\n"+PHONE+"\n"+SRC+"\n"+DST+"\n"+TIME+"\n-----------------------------------------------------------------")

print("\n开始输出拼车派车单：\n-----------------------------------------------------------------")
CP = "派车人：{}\n用车事由：{}\n用车人：{}\n联系电话：{}\n目的地：{}\n出发时间：{}".format(VDU,UF,UN,TEL,dst,where)
print(CP)
print("\n-----------------------------------------------------------------")