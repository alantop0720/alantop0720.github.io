c


# 关闭防火墙

```
systemctl disable firewalld
```

# 关闭selinux

```
vim /etc/selinux/config
```

将

```
SELINUX=enforcing
改为
SELINUX=disabled
```

# ssh修改root可以登录

```
vim /etc/ssh/sshd_config

修改配置文件下
PermitRootLogin yes  

service sshd restart
重启服务
```


```

# 关闭图形界面登录

```
systemctl set-default multi-user.target  



\# 更新yum源

 yum update -y # 

安装net-tools 

yum install -y net-tools

# 查看网络 ifconfig





##  安装ukui桌面

```
dnf update
dnf install ukui
systemctl set-default graphical.target
```






## vim的常用操作



在使用`u`命令撤销操作后，可以使用

`ctrl+o`命令向前跳转到前一步操作
`ctrl+i`命令向后跳转到后一步操作

v y p 复制粘贴
2dd 删除2行

v d 删除

ctrl + w 2下切换窗口
多窗口
 ：sp 上下分屏
：vsp 左右分屏

gg 文件开头
G 文件结尾

0回到行首
shift + 4 行尾

2G 转到第二行
/text 顺搜索
?text 逆向搜索
n下一个
N 逆向下一个

:%s/old/new/gc文件全局替换，c表示每次替换的询问

：Explore 打开目录选择
：e c:\ 目录切换到c盘

:reg 查看剪贴板

:help config 查看配置文件存放位置

: files 查看当前打开的文件名称

o 在光标下面一行插入

u 撤销
ctrl + r 反撤销

'ls' 不是内部或外部命令，也不是可运行的程序
或批处理文件。
```

