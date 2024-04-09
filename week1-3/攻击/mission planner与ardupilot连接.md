## mission planner与ardupilot连接

虚拟机首先应为桥接模式。

![image-20230502213038644](	https://image-1311319331.cos.ap-beijing.myqcloud.com/image/202305022130700.png)

关闭winodws主机和ubuntu虚拟机的防火墙，保证两者能ping通

查询windows主机ip地址：

![image-20230502212800274](	https://image-1311319331.cos.ap-beijing.myqcloud.com/image/202305022128338.png)



查询仿真无人机ip地址：

![image-20230502202558149](	https://image-1311319331.cos.ap-beijing.myqcloud.com/image/202305022025318.png)

192.168.56.139

![image-20230502202700120](	https://image-1311319331.cos.ap-beijing.myqcloud.com/image/202305022027205.png)

再确认能够相互ping通。



关键一步： 

在虚拟无人机终端加入

```
 output add 主机ip：14552
```

然后在地面站(笔者用的mission planner)的连接配置中，添加连接类行为UDP， 目标主机地址为虚拟机中有线网络地址192.168.xx.xx， 填写和刚刚对应的端口号，我这里是14552 。然后创建连接

![image-20230502213251807](	https://image-1311319331.cos.ap-beijing.myqcloud.com/image/202305022132901.png)

![image-20230502213319723](	https://image-1311319331.cos.ap-beijing.myqcloud.com/image/202305022133817.png)

![](	https://image-1311319331.cos.ap-beijing.myqcloud.com/image/202305022133781.png)

连接成功，笔者这边显示有些问题，但是是连接成功的。

![image-20230502214239632](	https://image-1311319331.cos.ap-beijing.myqcloud.com/image/202305022142680.png)

![image-20230502213852775](	https://image-1311319331.cos.ap-beijing.myqcloud.com/image/202305022138824.png)

![image-20230502213823185](	https://image-1311319331.cos.ap-beijing.myqcloud.com/image/202305022138367.png)

可以看到，mission planner设定的路径和map上显示相对应



## Reference

https://zhuanlan.zhihu.com/p/368471044