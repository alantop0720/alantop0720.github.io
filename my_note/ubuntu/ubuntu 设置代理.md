
## 为 APT 设置代理

如果要从 Ubuntu 存储库安装软件包，则需要为 APT 设置代理。您可以通过在 /etc/apt/apt.conf.d/ 创建一个新的配置文件来做到这一点：

nano /etc/apt/apt.conf.d/proxy.conf

添加以下行：

Acquire::http::Proxy "http://username::8181/";
Acquire::https::Proxy "https://username::8182/";

图形化代理

这个只是配置了 apt代理

还有图形代理和命令行代理两个部分