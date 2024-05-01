


```shell
sudo apt update
sudo apt install nginx
sudo systemctl status nginx
```


如你需要确定`80` 和`443`两个端口是否已打开，运行命令`sudo ufw status`查看结果。

```shell
sudo ufw allow 'Nginx Full'
sudo ufw status
```

```
Status: active

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW       Anywhere
Nginx Full                 ALLOW       Anywhere
22/tcp (v6)                ALLOW       Anywhere (v6)
Nginx Full (v6)            ALLOW       Anywhere (v6)
```

要测试已安装的Nginx，请在您的浏览器中打开`http://YOUR_IP`，您应该会看到默认的Nginx页面。

## Nginx配置文件的结构和最佳做法

Nginx配置文件存储在`/etc/nginx`目录中。主要的Nginx配置文件为`/etc/nginx/nginx.conf`。

虚拟主机配置文件存储在`/etc/nginx/sites-available`目录。仅当链接到`/etc/nginx/sites-enabled`目录时，Nginx才会使用此目录中的配置文件。

要激活虚拟主机，请从以下目录中的配置文件[创建软链接](https://www.myfreax.com/how-to-create-symbolic-links-in-linux-using-the-ln-command/)。将`sites-available`目录中文件软移到`sites-enabled`目录。

要编写更具可维护性的代码，遵循标准命名约定是个好主意。例如，如果您的域名是`mydomain.com`，则配置文件应命为`/etc/nginx/sitesavailable/mydomain.com.conf`。

`/etc/nginx/snippets`目录包含server上文的配置片段的文件。如果使用可重复的配置片段，则可以将这些指令重构为片段，并将片段文件include到server上下文中。

Nginx日志文件（`access.log`和`error.log`）位于`/var/log/nginx/`目录中。建议每个虚拟主机使用不同的`access`和`error`日志文件。

您可以将域文档根目录设置为所需的任何位置。 Webroot的最常见位置包括`/home/<user_name>/<site_name>`，`/var/www/<site_name>`。

`/var/www/html/<site_name>`，`/opt/<site_name>`。