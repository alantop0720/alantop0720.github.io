# [openEuler如何搭建nfs服务](https://www.itxm.cn/post/iaifc1a9.html "openEuler如何搭建nfs服务")

## 服务器端配置

openEuler可以通过安装nfs-utils软件包来搭建nfs服务。具体步骤如下：

1. 安装nfs-utils软件包

在终端中执行以下命令：


sudo dnf install nfs-utils 

2. 创建共享目录

在本地创建一个共享目录，例如：


sudo mkdir /mnt/nfs_share 

3. 配置nfs服务

编辑/etc/exports文件，添加以下内容：


/mnt/nfs_share *(rw,sync,no_root_squash) 

其中，/mnt/nfs_share为共享目录的路径，*表示允许任何IP地址访问，rw表示可读写访问，sync表示同步写入，no_root_squash表示允许root用户访问。

4. 启动nfs服务

执行以下命令启动nfs服务：


sudo systemctl start nfs-server 

5. 设置nfs服务开机自启动

执行以下命令设置nfs服务开机自启动：

sudo systemctl enable nfs-server 

## 客户端 配置：

至此，nfs服务已经搭建完成。其他主机可以通过挂载nfs共享目录来访问该目录。例如，在另一台主机上执行以下命令挂载共享目录：


sudo mount -t nfs  ip:/mnt/nfs_share /mnt/nfs_mount 

  

其中， 为openEuler主机的IP地址，/mnt/nfs_share为共享目录的路径，/mnt/nfs_mount为挂载点的路径。挂载成功后，即可在/mnt/nfs_mount目录下访问共享目录中的文件。

**