'编码：GBK
On Error Resume Next

Msgbox"请将需要填充的文件重命名为“0”[保留扩展名]。| Plz rename your JPG file to '0' [Keep extension !]" 

Dim uni,sec,str0,str1,fsi,fex,inf,ins,nes,com
uni = inputbox("选择计量单位(输入对应的数字即可)：字节(0)、千字节(1)、默认兆字节(2)、千兆字节(3)。| Select unit of measurement(Default:Megabytes(2) | Alternative: Bytes(0),Kilobytes(1),Gigabytes(3)):","Setting(1/3)")
if (uni = "") then 
	str1 = "Mib"
	sec = 2
elseif (uni="0") then 
	str1 = "Byte"
	sec = 0
elseif (uni="1") then
	str1 = "Kib"
	sec = 1
elseif (uni="2") then 
	str1 = "Mib"
	sec = 2
elseif (uni="3") then 
	str1 = "Gib"
	sec = 3
else
	Msgbox "Unit choosen failed."
End If
str0 = "设置输出文件大小。Set output file size by " & str1 
fsi = inputbox(str0,"Setting(2/3)") 
if (sec = 0) then 
	fsi = fsi*1
elseif (sec = 1) then 
	fsi = fsi*1024
elseif (sec = 2) then
	fsi = fsi*1024*1024
elseif (sec = 3) then 
	fsi = fsi*1024*1024*1024
else
	Msgbox "Size setting failed."
End If
fex = inputbox("指定输入文件的扩展名。 | Set output file type(EXTENSION):","Setting(3/3)") 
inf = ".\0." & fex 

if (IsExitAFile(inf)) then
	REM File Existed:
	ins = CalcSize(inf)
	'Msgbox fsi+ins
	if (fsi-ins<0) then 
		Msgbox "ERROR(0): File has exceeded the specified size !"
	elseif (fsi-ins=0) then
		Msgbox "ERROR(1): File has exceeded the specified size !"
	else
		nes = fsi - ins
		com = "fsutil file createnew .\cfTempFile " & nes
		'Msgbox com
		call rShell(com,1)
		com = "CMD /c " & chr(34) & "copy /b 0." & fex & "+cfTempFile OutputFile." & fex & chr(34)
		'Msgbox com
		call rShell(com,1)
		com = "CMD /c " & chr(34) & "del cfTempFile" & chr(34)
		'Msgbox com
		call rShell(com,0)
		Msgbox "Finished!感谢使用！脚本文件编码为GBK。by R -2020-06-16-"
	end if
else
	Msgbox "ERROR."
End If

Function CalcSize(filespec)
	Dim fso, f, s
	Set fso = CreateObject("Scripting.FileSystemObject")
	Set f = fso.GetFile(filespec)
	s = f.size
	CalcSize = s
End Function

Function IsExitAFile(filespec)
    Dim fso
    Set fso=CreateObject("Scripting.FileSystemObject")        
    If fso.fileExists(filespec) Then         
    	IsExitAFile=True        
   	else 
   	    IsExitAFile=False        
    End If
End Function 

Function rShell(c,t)
	set WshShell = WScript.CreateObject("WScript.Shell")
	WshShell.run(c),t,true
End Function