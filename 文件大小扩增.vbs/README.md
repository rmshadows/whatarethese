### 使用

 - Windows下直接运行即可。
 - 原理：就是用Windows自带的 `copy /b [InputFile]+[AttachedFile] [OutputFile]` 命令而已。生成指定大小填充物用的是 `fsutil file createnew [FilePath] [Size]`
 - 首先将需要扩增大小的文件重命名为“0”，扩展名保持不变。比如演示中使用的是一张jpg图片，首先重命名为“0.jpg”

![图1](https://images.gitee.com/uploads/images/2020/0621/214338_71bc8e42_7423713.png "屏幕截图.png")

![图2](https://images.gitee.com/uploads/images/2020/0621/214535_aeab55db_7423713.png "屏幕截图.png")

 - 然后选择单位，默认是Mib，直接回车。假如你要用Kib作为单位，就输入“1”（没有引号）。本次演示将jpg图片扩增至2G，所以单位选择的是Gib，输入数字“3”。

![图3](https://images.gitee.com/uploads/images/2020/0621/214802_d1509e9f_7423713.png "屏幕截图.png")
 
 - 然后下个框框设置大小，单位是上一步选择的Gib，此处填入“2”，即2Gib。

![图4](https://images.gitee.com/uploads/images/2020/0621/215020_95eba637_7423713.png "屏幕截图.png")

 - 接下来选择扩展名，这次输入文件扩展名是jpg，所以此处填入“jpg”。如果你是其他文件，扩展名是啥就写啥，比如zip压缩包就写“zip”，mp4视频就写“mp4”。

![图5](https://images.gitee.com/uploads/images/2020/0621/215245_5cd79314_7423713.png "屏幕截图.png")

 - 再次回车，等待任务结束即可。

![图6](https://images.gitee.com/uploads/images/2020/0621/215323_59d52be0_7423713.png "屏幕截图.png")

 - 可以看到桌面生成了Output.jpg，大小2Gib。

![图7](https://images.gitee.com/uploads/images/2020/0621/215419_d6b5358e_7423713.png "屏幕截图.png")

 - 图片质量并被有实质性优化，只是体积变大罢了，所以叫做“虚胖”。

### 备注

- 没有备注。为什么写这破玩意儿啊。。问的好，我也不知道。

