Dim var
var = Msgbox("�Ƿ������رռ������(Y/n)",1+48+0,"���ļ���������رգ�ע�Ᵽ�湤�����ļ���")
REM Msgbox var
If var=1 Then
	Dim shell
	set shell= WScript.CreateObject("WScript.Shell")
	shell.Run"cmd /c shutdown -s -f -t 0",0
	REM Msgbox "�������ȷ��"
ElseIf var=2 Then
	REM Msgbox "�������ȡ��"
End If