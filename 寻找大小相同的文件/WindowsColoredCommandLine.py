import ctypes
import sys

'''Windows CMD命令行颜色'''
# 句柄号
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE= -11
STD_ERROR_HANDLE = -12
# 前景色
FOREGROUND_BLACK = 0x0 # 黑
FOREGROUND_BLUE = 0x01 # 蓝
FOREGROUND_GREEN = 0x02 # 绿
FOREGROUND_RED = 0x04 # 红
FOREGROUND_INTENSITY = 0x08 # 加亮
# 背景色
BACKGROUND_BLUE = 0x10 # 蓝0
BACKGROUND_GREEN = 0x20 # 绿1
BACKGROUND_RED = 0x40 # 红2
BACKGROUND_INTENSITY = 0x80 # 加亮
colors = [FOREGROUND_BLUE, # 蓝字3
FOREGROUND_GREEN,# 绿字4
FOREGROUND_RED, # 红字5
FOREGROUND_BLUE | FOREGROUND_INTENSITY, # 蓝字(加亮)
FOREGROUND_GREEN | FOREGROUND_INTENSITY, # 绿字(加亮)
FOREGROUND_RED | FOREGROUND_INTENSITY, # 红字(加亮)
FOREGROUND_RED | FOREGROUND_INTENSITY | BACKGROUND_BLUE | BACKGROUND_INTENSITY] # 红字蓝底6

texts = ['蓝字','绿字','红字','蓝字(加亮)','绿字(加亮)','红字(加亮)','红字蓝底']

# See "http://msdn.microsoft.com/library/default.asp?url=/library/en-us/winprog/winprog/windows_api_reference.asp" for information on Windows APIs.
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
def __set_cmd_color(color, handle=std_out_handle):
	bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
	return bool
def __reset_color():
	__set_cmd_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)
def __print_color_text(color, text):
	__set_cmd_color(color)
	sys.stdout.write('%s\n' % text) # ==> print(text)
	__reset_color()
def __print_colors_texts(colors, texts):
	for color, text in zip(colors, texts):
		__print_color_text(color, text)

def printColor(color_num,text):
	__print_color_text(colors[color_num], text)

if __name__ == "__main__":
	__print_colors_texts(colors, texts)
	printColor(1,"666")