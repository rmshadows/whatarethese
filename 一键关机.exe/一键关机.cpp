#include <iostream>
#include <wtypes.h>
using namespace std;

int WINAPI WinMain(HINSTANCE hInstance1,
    HINSTANCE hPrevInstance,
    PSTR szCmdLine,
    int iCmdShow) {
    if (MessageBox(NULL, TEXT("       是否立即关闭计算机？(Y/n)"), TEXT("您的计算机即将关闭，请检查工作区是否保存！"), MB_OKCANCEL| MB_ICONEXCLAMATION)==1)
    {
        string command = "shutdown -s -f -t 0";
        WinExec(command.c_str(), SW_HIDE);
        //system(command.c_str());
    }
    return 0;
}