## Ardupilot仿真环境说明：

https://blog.csdn.net/weixin_44747240/article/details/104497893



```
../Tools/autotest/sim_vehicle.py --map --console
```

慢慢等，启动仿真环境，整体如图所示：

![image-20230502174224250](https://gitee.com/Duangthef1rst/drawing-bed/raw/master//202305021742416.png)



#### 左上：命令终端

![image-20230502174322058](https://gitee.com/Duangthef1rst/drawing-bed/raw/master//202305021743095.png)

```
1.使用默认参数文件../Tools/autotest/default_params/copter.parm，启动ArduCopter模拟器，并记录启动日志；
2.启动MavProxy，将通信输出到127.0.0.1:14550端口，同时使用tcp:127.0.0.1:5760作为主机连接地址进行通信；
3.当前程序连接到主机的5760端口，并等待来自主机的心跳信号；
4.检测到连接的无人机编号为1，连通性正常；
5.接收到1339个参数设置信息，并将这些信息保存到mav.parm文件中。
```



#### 右上：仿真地图

可以观察到无人机的实时位置

![image-20230502174535141](https://gitee.com/Duangthef1rst/drawing-bed/raw/master//202305021745280.png)



#### 左下：

控制台，可以看到无人机的实时状态

![image-20230502174638815](https://gitee.com/Duangthef1rst/drawing-bed/raw/master//202305021746852.png)



#### 右下：启动日志(对本项目没用)

```
是ArduCopter程序的启动日志。根据日志内容，可以看到程序将模拟速度设置为1.0，并提示推荐的EK3_DRAG_BCOEF和EK3_DRAG_MCOEF参数值。接着，程序启动了sketch 'ArduCopter'，开始初始化SITL输入，并使用端口号9005连接Irlock。然后程序绑定了三个端口：5760、5762和5763，分别用于串行通信和TCP/IP通信。程序从../Tools/autotest/default_params/copter.parm读取默认参数文件，并输出无人机的起飞位置和朝向信息。最后，程序验证了结构体的有效性。
```

![image-20230502175153962](https://gitee.com/Duangthef1rst/drawing-bed/raw/master//202305021751997.png)