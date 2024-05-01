```
apt-get install bind9

vim named.conf.local


zone "alantop.com" {
	type master;
file "www.alantop.com";
};




```

# 配置转发

```
vim /etc/bind/named.conf.options

8.8.8.8
```

cd /var/cache/bind

cp /etc/bind/db.local www.alantop.com

最后一行插入

@ IN a 192.168.1.2

systemctl restart bind9

