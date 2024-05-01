
# SSH使用篇：Windows登录Ubuntu虚拟机&设置免密登录



**目录**

[一、ssh的安装与启动](https://blog.csdn.net/one__leaf/article/details/128343857#t0)

[1、安装](https://blog.csdn.net/one__leaf/article/details/128343857#t1)

[2、启动服务器的SSH服务](https://blog.csdn.net/one__leaf/article/details/128343857#t2)

[二、口令登录](https://blog.csdn.net/one__leaf/article/details/128343857#t3)

 [1、登录命令](https://blog.csdn.net/one__leaf/article/details/128343857#t4)

[2、验证过程](https://blog.csdn.net/one__leaf/article/details/128343857#t5)

[3、登录失败：1、服务器变更 + 2、服务器IP变化](https://blog.csdn.net/one__leaf/article/details/128343857#t6)

[三、免密登录（公钥登录）](https://blog.csdn.net/one__leaf/article/details/128343857#t7)

[大致的三步](https://blog.csdn.net/one__leaf/article/details/128343857#t8)

[0、准备工作（不一定要弄）](https://blog.csdn.net/one__leaf/article/details/128343857#t9)

[1、客户端生成公私钥](https://blog.csdn.net/one__leaf/article/details/128343857#t10)

[2、将公钥复制到服务器中](https://blog.csdn.net/one__leaf/article/details/128343857#t11)

[3、第三步](https://blog.csdn.net/one__leaf/article/details/128343857#t12)  

[4、第四步](https://blog.csdn.net/one__leaf/article/details/128343857#t13)

[5、第五步](https://blog.csdn.net/one__leaf/article/details/128343857#t14)

[6、第六步](https://blog.csdn.net/one__leaf/article/details/128343857#t15)

---

## 一、ssh的安装与启动

### 1、安装

        SSH分为客户端 [openssh](https://so.csdn.net/so/search?q=openssh&spm=1001.2101.3001.7020)-client 和服务器 openssh-server，可以利用以下命令确认电脑上是否安装了客户端和服务器。

```perl
dpkg -l | grep ssh
```

        如果只是想远程登陆别的机器只需要安装客户端（Ubuntu默认安装了客户端），如果要开放本机的[SSH服务](https://so.csdn.net/so/search?q=SSH%E6%9C%8D%E5%8A%A1&spm=1001.2101.3001.7020)就需要安装服务器。

```csharp
sudo apt update        
    #更新数据sudo apt upgrade        
    #更新软件
    
    sudo apt install openssh-server  
    
    #下载安装ssh服务的服务器
    sudo apt install openssh-client  
    #下载安装ssh服务的客户端 # 上面命令下载失败可以使用下面的命令尝试下载
    
    sudo apt-get install openssh-client sudo apt-get install openssh-server 
```

这里给出的是ubuntu安装命令，其它系统请参考具体的安装命令

###   
2、启动服务器的SSH服务

首先确认ssh-server是否已经启动了

```perl
ps -e | grep ssh
```

![](https://img-blog.csdn.net/20180923111022766?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpNTI4NDA1MTc2/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

如图，sshd 表示ssh-server已经启动了。如果没有启动，可以使用如下命令启动：

```cobol
sudo /etc/init.d/ssh start 
```

停止和重启ssh服务的命令如下：

```cobol
sudo /etc/init.d/ssh stop  #server停止ssh服务 sudo /etc/init.d/ssh restart  #server重启ssh服务
```

接下来就可以进行使用客户机远程登录服务器了~

## 二、口令登录

###  **1、登录命令**

口令登录非常简单，只需要一条命令，命令格式为： ssh 客户端用户名@服务器ip地址  eg:

```java
ssh lee@IP(服务器的username和IP)
```

如果需要调用图形界面程序可以使用 -X 选项

```crystal
ssh -X lee@192.168.52.144
```

如果客户机的用户名和服务器的用户名相同，登录时可以省略用户名。

```cobol
ssh 192.168.52.1
```

还要说明的是，SSH服务的默认端口是22，也就是说，如果你不设置端口的话登录请求会自动送到远程主机的22端口。我们可以使用 -p 选项来修改端口号，比如连接到服务器的1234端口：

```css
ssh -p 1234 lee@192.168.52.1
```

客户机必须要知道**服务器的ip地址**。可以在**服务器端电脑上利用 ifconfig 命令**查看该机的ip地址：

### 2、验证过程

ssh 连接远程服务器后，首先有一个验证过程，验证远程服务器是否为陌生地址。**如果是第一次登录远程主机，系统会给出下面提示：**

![](https://img-blog.csdn.net/20180923122318374?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpNTI4NDA1MTc2/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

上面这段文字告诉用户，这台服务器的指纹是陌生的，让用户选择是否要继续连接（输入 yes 或 no）。所谓“服务器指纹”，指的是 SSH 服务器公钥的哈希值。每台 SSH 服务器都有唯一一对密钥，用于跟客户端通信，其中公钥的哈希值就可以用来识别服务器。

下面的命令可以查看某个公钥的指纹。

```cobol
ssh-keygen -l -f /etc/ssh/ssh_host_ecdsa_key.pub
```

上面的例子中，ssh-keygen -l -f命令会输出公钥/etc/ssh/ssh_host_ecdsa_key.pub的指纹。

        ssh 会将本机连接过的所有服务器公钥的指纹，都储存在本机的~/.ssh/known_hosts文件中。每次连接服务器时，通过该文件判断是否为陌生主机（陌生公钥）。

        上面输入yes即可。这时系统会提示远程主机被添加到已知主机列表，即本机的~/.ssh/known_hosts文件中。

![](https://img-blog.csdn.net/20180923123736916?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpNTI4NDA1MTc2/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

然后会要求我们输入远程主机的密码，输入的密码正确就可以成功登录了。命令提示符会修改为远程主机的提示符，现在开始，终端中输入的命令都将在服务器中执行。

我们可以通过 Ctrl+D 或者 exit 命令退出远程登录。  


### 3、登录失败：1、服务器变更 + 2、服务器IP变化

        服务器指纹可以防止有人恶意冒充远程主机。如果**服务器的密钥发生变更**（比如重装了 SSH 服务器），客户端再次连接时，就会发生公钥指纹不吻合的情况。这时，客户端就会中断连接，并显示一段警告信息。

```cobol
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!Someone could be eavesdropping on you right now (man-in-the-middle attack)!It is also possible that the RSA host key has just been changed.The fingerprint for the RSA key sent by the remote host is77:a5:69:81:9b:eb:40:76:7b:13:04:a9:6c:f4:9c:5d.Please contact your system administrator.Add correct host key in /home/me/.ssh/known_hosts to get rid of this message.Offending key in /home/me/.ssh/known_hosts:36
```

        上面这段文字的意思是，该主机的公钥指纹跟~/.ssh/known_hosts文件储存的不一样，必须处理以后才能连接。这时，你需要确认是什么原因，使得公钥指纹发生变更，到底是恶意劫持，还是管理员变更了 SSH 服务器公钥。

        如果新的公钥确认可以信任，需要继续执行连接，**你可以执行下面的命令，将原来的公钥指纹从~/.ssh/known_hosts文件删除。**

```undefined
ssh-keygen -R hostname
```

上面命令中，hostname是发生公钥变更的主机名。

**除了使用上面的命令，你也可以手工修改known_hosts文件，将公钥指纹删除。**

删除了原来的公钥指纹以后，**重新执行 ssh 命令连接远程服务器，将新的指纹加入known_hosts文件，就可以顺利连接了。**

## **三、免密登录（公钥登录）**

        **每次登录远程主机都需要输入密码是很不方便的，如果想要省去这一步骤，可以利用密钥对进行连接，还可以提高安全性。**

### 大致的三步

1.本地机器生成公[私钥](https://so.csdn.net/so/search?q=%E7%A7%81%E9%92%A5&spm=1001.2101.3001.7020 "私钥")  
2.上传公钥到目标机器  
3.测试免密登录

### **0、准备工作（不一定要弄）**

首先我们需要准备两台或两台以上服务器或[虚拟机](https://so.csdn.net/so/search?q=%E8%99%9A%E6%8B%9F%E6%9C%BA&spm=1001.2101.3001.7020 "虚拟机")，配置好静态ip，配置静态ip参见博文：[虚拟机配置静态ip](https://blog.csdn.net/snail_bing/article/details/81737695 "虚拟机配置静态ip")

**使用root权限分别修改每台机器的hosts，添加每台机器所对应的IP和主机名**  


```cobol
sudo vim /etc/hosts
```


在其中添加所有服务器或虚拟机节点ip和对应的域名，如下图所示：

![](https://img-blog.csdn.net/2018081710080832?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NuYWlsX2Jpbmc=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

然后输入：wq保存退出。

在每个节点分别设置其hostname，如下图所示：

![](https://img-blog.csdn.net/20180817100959188?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NuYWlsX2Jpbmc=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

hostname后为当前服务器或虚拟机的域名，是让此域名立即生效，不需要重启虚拟机。

### 1**、****客户端**生成公[私钥](https://so.csdn.net/so/search?q=%E7%A7%81%E9%92%A5&spm=1001.2101.3001.7020 "私钥")

```csharp
 [root@Hadoop-Master ~]#cd ~/.ssh 
```

如果没有该目录，先执行一次

```undefined
ssh  localhost
```

不要手动创建，不然配置好还要输入密码。

**使用ssh-keygen命令生成密钥对：**

```crystal
[hadoop@localhost ~]$ ssh-keygen -t  rsa
```

```csharp
ssh-keygenssh-keygen -t rsa   #-t表示类型选项，这里采用rsa加密算法
```

        **然后根据提示一步步的按enter键即可（其中有一个提示是要求设置私钥口令passphrase，不设置则为空，这里看心情吧，如果不放心私钥的安全可以设置一下），执行结束以后会在 /home/当前用户 目录下生成一个 .ssh 文件夹,其中包含私钥文件 id_rsa 和公钥文件 id_rsa.pub。**

### **2、将公钥复制到**服务器**中**

**使用ssh-copy-id命令将公钥复制到远程主机。ssh-copy-id会将公钥写到远程主机的 ~/ .ssh/authorized_key 文件中**

```cobol
ssh-copy-id -i .ssh/id_rsa.pub root@192.168.135.102	#复制密钥ssh-copy-id -i .ssh/id_rsa.pub root@192.168.135.103	#复制密钥  ssh-copy-id -i /root/.ssh/id_rsa.pub master  //依次输入yes,123456(root用户的密码)ssh-copy-id -i /root/.ssh/id_rsa.pub slave1 //同上ssh-copy-id -i /root/.ssh/id_rsa.pub slave2 //同上ssh-copy-id -i /root/.ssh/id_rsa.pub slave3 //同上
```

```csharp
[root@localhost .ssh]# cat  id_rsa.pub >>authorized_keys
```

**说明 ：cat  file1 >> file2  将file1 的内容追加到file2中，并不覆盖file2 中的内容，如果file2不存在则创建一个文件。**

可以看到客户端写入到服务器的 id_rsa.pub （公钥）内容。

```bash
cd ~/.sshvim authorized_keys
```

### 

### 3、复制完成即可实现免密登录，测试一下：

```csharp
ssh 192.168.35.102									#直接登录
```

如果成功登录到192.168.35.102这台服务器，说明你的免密登录配置成功。

### 设置本机免密：

```typescript
ssh-keygen -t dsa -P '' -f ~/.ssh/id_dsa cat ~/.ssh/id_dsa.pub >> ~/.ssh/authorized_keys
```

## 方案二

###  3、第三步  

在要连接的Slave1 和 Slave2机器上也生成公钥和私钥。并将slave1 和 slave2 机器中生成的公钥id_rsa.pub文件copy到Master机器上。

```cobol
[root@localhost .ssh]# scp id_rsa.pub root@172.16.254.107:~/.ssh/id_rsa.pub_s1[root@localhost .ssh]# scp id_rsa.pub root@172.16.254.107:~/.ssh/id_rsa.pub_s2
```

### 4、第四步

切换到Master机器上的Slave1、Slave2 的id_rsa.pub_s1 和id_rsa.pub_s2追加合并到authorized_keys文件中。

```csharp
 [root@Hadoop-Master .ssh]# cat id_rsa.pub_s1>> authorized_keys   [root@Hadoop-Master .ssh]# cat id_rsa.pub_s2>> authorized_keys  
```

### 5、第五步

将master机器上合并后的authorized_keyscopy文件复制到Slave1、Slave2机器上

```cobol
 [root@Hadoop-Master.ssh]# scp authorized_keys root@172.16.254.108:~/.ssh/ [root@Hadoop-Master.ssh]# scp authorized_keys root@172.16.254.109:~/.ssh/
```

### 6、第六步

将master 、Slave1 、Slave2 等各台机器的 .ssh/文件夹权限改为700，authorized_keys文件权限改为600（or 644）。

```cobol
[root@localhost .ssh]# chmod 700 ~/.ssh[root@localhost .ssh]# chmod 600 ~/.ssh/authorized_keys
```

[(17条消息) SSH](https://blog.csdn.net/lichenglong33/article/details/81627042?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-1-81627042-blog-121597189.pc_relevant_3mothn_strategy_and_data_recovery&spm=1001.2101.3001.4242.2&utm_relevant_index=4 "(17条消息) SSH免密登录（超详细）_我是搬砖工人的博客-CSDN博客")



/etc/init.d/ssh restart

1. 检查是否安装了SSH服务：sudo apt-get install openssh-server
2. 检查SSH服务是否已经启动：sudo systemctl status ssh
3. 如果SSH服务没有启动，则可以手动启动服务：sudo systemctl start ssh
4. 设置SSH服务在开机时自动启动：sudo systemctl enable ssh



