
# ubuntu22.04安装zabbix6.0 LTS


**安装环境**

Zabbix 采用 All-In-One 方式

Ubuntu 22.04.1 [LTS](https://so.csdn.net/so/search?q=LTS&spm=1001.2101.3001.7020)

PHP 7.4.3

mysql 8.0.28

nginx 1.18.0

# 2、6.0 LTS+Ubuntu22.04+MySQL+Apache

![](https://img-blog.csdnimg.cn/10439a27ea6d419fb35de01f8db8daa4.png)

# 3、安装Zabbix

# sudo wget https://repo.zabbix.com/zabbix/6.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_6.0-4%2Bubuntu22.04_all.deb

# sudo dpkg -i zabbix-release_6.0-4+ubuntu22.04_all.deb

# sudo apt update

**更新可用软件包列表**

#sudo apt update

**安装Zabbix server，Web前端，agent**

#sudo apt install zabbix-server-mysql zabbix-frontend-php zabbix-apache-conf zabbix-sql-scripts zabbix-agent

**安装Mysql**

# sudo apt install -y mysql-server


默认没有密码

**初始数据库**

**#登录数据库**

sudo mysql -uroot -p

password

**#创建zabbix数据库**

mysql> create database zabbix character set utf8mb4 collate utf8mb4_bin;

**#创建zabbix用户**

mysql> create user zabbix@localhost identified by 'password';

**#授权localhost访问**

mysql> grant all privileges on zabbix.* to zabbix@localhost;

**#启用log_bin_trust_function_creators选项**

mysql> set global log_bin_trust_function_creators = 1;

**#退出**

mysql> quit;

**导入初始架构和数据，系统将提示您输入新创建的密码。**

# sudo zcat /usr/share/zabbix-sql-scripts/mysql/server.sql.gz | mysql --default-character-set=utf8mb4 -uzabbix -p zabbix

**导入数据库模式后禁用log_bin_trust_function_creators选项。**

# mysql -uroot -p

password

mysql> set global log_bin_trust_function_creators = 0;

mysql> quit;

**为Zabbix server配置数据库**

**编辑配置文件 /etc/zabbix/zabbix_server.conf**

DBHost=localhost

DBPassword=password

**启动Zabbix server和agent进程**

**启动Zabbix server和agent进程，并为它们设置开机自启：**

# systemctl restart zabbix-server zabbix-agent apache2

# systemctl enable zabbix-server zabbix-agent apache2

# 3、Zabbix 6.0 LTS UI中文语言包

**安装中文语言包**

#sudo apt install language-pack-zh-hans

**找到zh_CN.UTF-8 UTF-8 并取消#号注释，然后保存并退出**

#sudo vim /etc/locale.gen

**编译语言包**

#sudo locale-gen

**修改默认语言为中文**

#sudo vi /etc/default/locale

LANG=zh_CN.UTF-8

**重启系统**

**Zabbix 6.0 LTS UI 中文乱码**

在Windows 系统中找到 C:\Windows\Fonts 中的楷体(常规)复制到 windows 桌面上,通过cecureFX或 lrzsz 长传在/usr/share/zabbix/assets/fonts/ 目录下

**上传前需要赋予文件夹权限**

# sudo chmod 777 /usr/share/zabbix/assets/fonts

# sudo chmod 777 /etc/alternatives

![](https://img-blog.csdnimg.cn/b9ab3bcec72b4e97917f7dcc7d014df1.png)

# cd /usr/share/zabbix/assets/fonts/

# ls graphfont.ttf simkai.ttf

# chmod 777 simkai.ttf

# cp graphfont.ttf graphfont.ttf.bak

# mv simkai.ttf graphfont.ttf

# rm -f /etc/alternatives/zabbix-web-font

# ln -s /usr/share/zabbix/assets/fonts/graphfont.ttf  /etc/alternatives/zabbix-web-font

**打开Zabbix UI网页**

**使用Apache web服务器时，Zabbix UI的默认URL是http://host/zabbix**

**Zabbix web初始化**

[http://server_ip](https://blog.csdn.net/qq_15514497/article/details/129317169 "http://server_ip") or name

![](https://img-blog.csdnimg.cn/d8d8ea43390a474096d6a5259fad6b7b.png)

![](https://img-blog.csdnimg.cn/7be831475a2d447bb5d3f96e55de2dc6.png)

**数据库连接配置**

![](https://img-blog.csdnimg.cn/7ed8920757d64e8c86187785391e26fe.png)**设置时区** 

![](https://img-blog.csdnimg.cn/4220a6972cc74db6b1028ac1cbe9f3b0.png) 

![](https://img-blog.csdnimg.cn/b40f81dc69ae47168e572a20ef9d629f.png) 

![](https://img-blog.csdnimg.cn/998ec5f98e2640ac87389d04a8a6aec1.png)**默认账号Admin密码zabbix** 

![](https://img-blog.csdnimg.cn/3cbe8488a6264c51977428b661a0b104.png) 

**安装好的仪表盘**

![](https://img-blog.csdnimg.cn/07e07941fcd94d0e86ab53d6e063db50.png)