// JavaApplicationLaucher.cpp : Defines the entry point for the console application.
//用于加载Jlink打包后的应用

#include "stdafx.h"
#include<windows.h>
#include<stdlib.h>

int main()
{
   char command[50];

   strcpy(command, "cmd.exe /C start /B .\\bin\\launcher.vbs");
   //strcpy(command, "cmd.exe /C start /B .\\bin\\launcher.bat");//加载bat
   system(command);

   return(0);
} 