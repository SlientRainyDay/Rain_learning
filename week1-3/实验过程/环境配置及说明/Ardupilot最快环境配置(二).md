## Ardupilot环境配置(二)

全程需要保持clash的**TUN**模式下**！！！！！！**

只需要命令行即可完成：

```
git clone https://github.com/ArduPilot/ardupilot
cd ardupilot
git submodule update --init --recursive
```

```
Tools/environment_install/install-prereqs-ubuntu.sh -y
. ~/.profile
```

```
cd ~/ardupilot/ArduCopter
```

```
../Tools/autotest/sim_vehicle.py --map --console
```

耐心等待，出现下图即为成功标志：

![](C:\Users\yu\AppData\Roaming\Typora\typora-user-images\image-20230502173429232.png)

![image-20230502173455944](https://gitee.com/Duangthef1rst/drawing-bed/raw/master//202305021734976.png)

启动界面：

![image-20230502134818725](C:\Users\yu\AppData\Roaming\Typora\typora-user-images\image-20230502134818725.png)



全程截图如下：

![image-20230502173102153](https://gitee.com/Duangthef1rst/drawing-bed/raw/master//202305021731213.png)

![image-20230502173147611](https://gitee.com/Duangthef1rst/drawing-bed/raw/master//202305021731659.png)

ls打错了，忽略lls：

![image-20230502173220629](https://gitee.com/Duangthef1rst/drawing-bed/raw/master//202305021732663.png)

![image-20230502173234940](https://gitee.com/Duangthef1rst/drawing-bed/raw/master//202305021732973.png)



![image-20230502173304779](https://gitee.com/Duangthef1rst/drawing-bed/raw/master//202305021733825.png)

![image-20230502173402377](https://gitee.com/Duangthef1rst/drawing-bed/raw/master//202305021734414.png)

![](https://gitee.com/Duangthef1rst/drawing-bed/raw/master//202305021735768.png)

