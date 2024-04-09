

install-prereqs-ubuntu.sh安装问题解决：

问题为权限不够，即使按照下图所说也不行

搜到的教程：

![image-20230501101709527](https://gitee.com/Duangthef1rst/drawing-bed/raw/master//202305011017600.png)

我的问题：

![](https://gitee.com/Duangthef1rst/drawing-bed/raw/master//202305011020853.png)

经过搜索为使用chattr方法：

![image-20230501102148545](https://gitee.com/Duangthef1rst/drawing-bed/raw/master//202305011021598.png)

但是我仍然不行



我的最后解决方式：

高版本ubuntu的install-prereqs-ubuntu.sh环境安装目录为/ardupilot/Tools/environment_install

解决办法：找到目录手动运行：

![image-20230501101747259](https://gitee.com/Duangthef1rst/drawing-bed/raw/master//202305011017367.png)