## Ardupilot环境配置(一)

本文主要记录问题，快速配置建议直接转到《Ardupilot环境配置(二)》

> Ardpilot介绍：ArduPilot通过多种传感器的数据（GPS、加速度计、气压计、磁场计）等来估计飞行器的姿态，从而使飞行器能够保持稳定。被称为APM的飞控硬件，其实全称就是Ardu Pilot Mega，但是2013年后，这个系列的飞控硬件改名为Pixhawk，ArduPilot只用来指特定的飞控软件，但是约定俗称地也可以用APM来指ArduPilot。ArduPilot含有超过七十万条代码，所以很幸运我们不用自己去写飞控代码，直接用就可以了，大大降低了入门门槛。

- 因为需要git等命令，本次配置在clash的**TUN**模式下进行(使虚拟机能访问外网)

- 本文参考的文章为https://zhuanlan.zhihu.com/p/61616055  但是文章中部分问题笔者没有遇到，笔者同样遇到了文章中没有提到的问题，详细内容见下文所述。


### 安装：

#### 1.安装ardupilot文件

ubuntu命令行：

```
 git clone https://github.com/ArduPilot/ardupilot
 cd ardupilot
 git submodule update --init --recursive
```

1.通过 'git clone https://github.com/ArduPilot/ardupilot' 下载好的ardupilot文件最好手动找一下目录

2.没啥说的，直接运行

3.笔者在此处安装的时候出现了各种报错，以及安装不完全的情况，之后经过乱七八糟的搜索和运行乱七八糟的命令莫名其妙安装好了。

#### 2.运行.sh文件

此部分需要运行install-prereqs-ubuntu.sh文件，笔者为手动运行(和参考文章不同)。

笔者遇到的问题：![](https://gitee.com/Duangthef1rst/drawing-bed/raw/master//202305011224484.png)

笔者试过了chattr方法，不奏效，原因未知，最后解决办法如下：

###### 方法一(不完全正确，建议转到方法二)：

笔者Ubuntu(20.04)的install-prereqs-ubuntu.sh环境安装目录为/ardupilot/Tools/environment_install，手动找到改文件运行即可。

![image-20230501101747259](https://gitee.com/Duangthef1rst/drawing-bed/raw/master//202305011227804.png)

###### 方法二(可行)：

收到进入environment目录，打开终端，输入

```
./install-prereqs-ubuntu.sh -y
```

成功，正确回显如下：

![image-20230501235415479](https://gitee.com/Duangthef1rst/drawing-bed/raw/master//202305012354519.png)

经验证可用：

此部分需要等很多个小时，可以在本机下载：https://github.com/ilg-archived/arm-none-eabi-gcc

然后拖入虚拟机的/opt目录下，会节省很多时间。



#### 3.配置路径

同样需要看当前目录在哪

```
ardupilot/Tools/environment_install/install-prereqs-ubuntu.sh -y
```

```
. ~/.profile
```

到此Ardupilot环境已经搭配好。

正确回显如下：

![image-20230502115342777](https://gitee.com/Duangthef1rst/drawing-bed/raw/master//202305021153854.png)

![image-20230502115407231](https://gitee.com/Duangthef1rst/drawing-bed/raw/master//202305021154300.png)

## Reference

https://zhuanlan.zhihu.com/p/61616055

https://blog.csdn.net/weixin_44747240/article/details/104497893

https://www.cnblogs.com/wind-under-the-wing/p/14122985.html
