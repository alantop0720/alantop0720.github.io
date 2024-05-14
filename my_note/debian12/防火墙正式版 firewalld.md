
删除所有规则

一条条的删除，麻烦且耗时，记录下重置所有规则的命令。

所有规则都在 `/etc/firewalld/zones` 或者 `/usr/etc/firewalld/zones` 下面，根据 Linux 发行版不同有所区别。

1. 删除 `firewalld` 规则：
   
    ```shell
    rm -rf /etc/firewalld/zones
    ```
    
    或者
    
    ```shell
    rm -rf /usr/etc/firewalld/zones
    ```
    
2. 清理 `iptables` 规则：
   
    ```shell
    iptables -X
    iptables -F
    iptables -Z
    ```
    
3. 重启防火墙服务
   
    ```shell
    systemctl restart firewalld
    ```
    
4. 清理自定义规则
   
    ```shell
    rm -f /etc/firewalld/direct.xml
    ```


## 查看防火墙规则

```
firewall-cmd --list-all
```



## 防火墙的基本操作

```shell

systemctl status firewalld

systemctl start firewalld

systemctl enable firewalld

systemctl disable firewalld

```

## 开启端口ip

```shell

firewall-cmd --permanent --add-rich-rule="rule family="ipv4" source address="38.125.0.8" port protocol="tcp" port="8118" accept"
firewall-cmd --reload
firewall-cmd --zone=public --list-rich-rules

```

上面的命令，相当于修改了配置文件

```/etc/firewalld/zones/public.xml```

## 开启端口

```bash
firewall-cmd --zone=public --add-port=21/tcp --permanent
firewall-cmd --reload 
firewall-cmd --list-all
firewall-cmd --zone= public --query-port=8117/tcp 
firewall-cmd --zone= public --remove-port=80/tcp --permanent
```



## 按照网络批量开通

```bash
firewall-cmd --permanent --add-rich-rule="rule family="ipv4" source address="192.168.0.0/16" accept"
```

## 禁止ip访问指定协议指定端口
```shell
firewall-cmd --permanent --add-rich-rule="rule family="ipv4" source address="192.168.100.1" port protocol="tcp" port="6379" reject" 
```

