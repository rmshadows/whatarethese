当前版本：2.5
使用：

`python Find_Duplicate_File_by_Size.py -d "文件夹1" "文件夹2" "……" -i "标识1" "标识2" "……"`

 - `-d`：文件夹，必给参数。相对路径记得加上`./`或者`.\`。支持绝对路径

 - `-i` ：重复识别标识，可选。例如`-i "(1)" "(2)" "副本"`表示：如果文件名带有“（1）”、“（2）”或者 “副本”的就判定为重复文件。


![CSV](https://images.gitee.com/uploads/images/2020/0801/153033_9eb39dc6_7423713.png "屏幕截图.png")

![ps](https://images.gitee.com/uploads/images/2020/0801/153108_a0e56178_7423713.png "屏幕截图.png")

![found](https://images.gitee.com/uploads/images/2020/0801/153217_4b9f1d5d_7423713.png "屏幕截图.png")

![notfound](https://images.gitee.com/uploads/images/2020/0801/153258_58eee415_7423713.png "屏幕截图.png")