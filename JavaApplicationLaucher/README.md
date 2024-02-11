### 原理

Jink打包Java应用后，会在bin目录下生成一个bat(Windows)文件或者bash脚本(Linux)用于加载应用。这个Launcher就是用来加载bat脚本或者vbs脚本的。

### 目的

 -  **解压即用** 的Java桌面程序，用户不再需要到bin目录下寻找启动脚本。

 - 在Windows下，一个exe文件总比一个bat脚本看起来 **中规中矩** 吧？所以就写了这个Launcher，这样小白解压完就知道怎么运行了。

### 其他

 - 没学过C++，代码也是抄的，原代码可能看起来有些奇怪……？

 - 以下是VC6.0自动生成的README文件（ **问就是3000元的笔记本带不动VS2019** ，嘻嘻）


========================================================================

       CONSOLE APPLICATION : JavaApplicationLaucher

========================================================================
    

AppWizard has created this JavaApplicationLaucher application for you.  

This file contains a summary of what you will find in each of the files that
make up your JavaApplicationLaucher application.

JavaApplicationLaucher.dsp
    This file (the project file) contains information at the project level and
    is used to build a single project or subproject. Other users can share the
    project (.dsp) file, but they should export the makefiles locally.

JavaApplicationLaucher.cpp
    This is the main application source file.


/////////////////////////////////////////////////////////////////////////////

Other standard files:

StdAfx.h, StdAfx.cpp
    These files are used to build a precompiled header (PCH) file
    named JavaApplicationLaucher.pch and a precompiled types file named StdAfx.obj.


/////////////////////////////////////////////////////////////////////////////

Other notes:

AppWizard uses "TODO:" to indicate parts of the source code you
should add to or customize.

/////////////////////////////////////////////////////////////////////////////
