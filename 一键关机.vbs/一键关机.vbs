Dim var
var = Msgbox("是否立即关闭计算机？(Y/n)",1+48+0,"您的计算机即将关闭，注意保存工作区文件！")
REM Msgbox var
If var=1 Then
	Dim shell
	set shell= WScript.CreateObject("WScript.Shell")
	shell.Run"cmd /c shutdown -s -f -t 0",0
	REM Msgbox "您点击了确认"
ElseIf var=2 Then
	REM Msgbox "您点击了取消"
End If