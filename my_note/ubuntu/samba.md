

我这里的安装环境是运行在`Vmware pro 17`的`Ubuntu22.04`系统，如下图：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/0044ac92659047ff96112b8f71b2f1e1.png)

---


## 二、在Ubuntu安装samba，并配置

### 2.1 安装samba服务器

Ubuntu22.04是默认安装了samba服务器的，在命令行终端输入`samba -V`，可以查看当前系统安装的samba版本，  
![在这里插入图片描述](https://img-blog.csdnimg.cn/173b22e150d7495a9d10672268923b6f.png)  
如果执行`samba -V`后，提示找不到命令，说明系统还没有安装samba服务器，可以执行下面命令安装：

```shell
sudo apt-get install samba
```

  

### 👉2.2 给已存在的用户添加samba密码

必须有系统用户

在命令行执行`who`命令可以查看当前用户，然后执行下面命令给该用户添加samba登录密码：

```sh
sudo smbpasswd -a wkd
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/4b0e41d811c845f4824b36805ef70b97.png)  
  

### 👉2.3 创建一个共享文件夹

这个共享文件夹可以使用已有的，也可以重新创建，主要是文件夹要设置好权限以及将路径写到samba配置文件中，这里执行下面命令新建一个文件夹，并设置权限给前面的用户：

```sh
sudo mkdir /home/samba
sudo chown wkd:wkd /home/samba/
```

  

### 👉2.4 修改samba配置文件

samba配置文件的路径是 `/etc/samba/smb.conf`,输入下面命令打开配置文件：

```shell
sudo vi /etc/samba/smb.conf 
```

然后在文件最后添加下面语句：

```
# Windows clients look for this share name as a source of downloadable
[samba]  # windows 显示的目录名称
  comment = samba server
  path = /home/samba
  browseable = yes
  read only = no
  guest ok = yes
  writable = yes
  valid users = wkd
```

  

### 👉2.5 重启samba服务器

配置完成后，使用下面命令重启samba服务器

```shell
sudo service smbd restart 
```

如果共享不能访问 ，gpedit.msc启用来宾账号即可。