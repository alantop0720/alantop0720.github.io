
## 欧拉同步网络时间

###### 修改配置

```java
vi /etc/chrony.conf #进入配置文件
```

###### 增加或修改一下两个配置

```java
server 192.168.8.5 iburst
allow 192.168.8.5   
```

###### 开启[时间同步](https://so.csdn.net/so/search?q=%E6%97%B6%E9%97%B4%E5%90%8C%E6%AD%A5&spm=1001.2101.3001.7020)

```java
timedatectl set-ntp true
```

###### 重启chronyd

```java
systemctl restart chronyd
```

###### 查看时间同步状态

```java
timedatectl status
```

###### 查看时间是否同步

`date`