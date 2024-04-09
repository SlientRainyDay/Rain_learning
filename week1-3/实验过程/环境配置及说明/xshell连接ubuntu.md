xshell连接ubuntu

> 注：缺少的常用命令ubuntu会提示安装

1.安装 openssh-server

```
sudo apt-get openssh-server
```

2.查看是否开启了该服务(没开启的话执行/etc/init.d/ssh start)

```
ps -e | grep ssh
```

3.进入root

```
sudo su
```

需要输入密码

4.修改ssh配置

```
vim etc/ssh/sshd/
```

找到该段，'x'为删除   'insert'为插入   'Esc'为退出编辑      ' Shift+: '然后输入' wq! ' 回车保存

![](https://gitee.com/Duangthef1rst/drawing-bed/raw/master//202305010709246.png)

5.查看ubuntu ip

```
ifconfig -a
```