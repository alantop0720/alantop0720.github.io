
```
apt update
apt install vsftpd
vim /etc/vsftpd.conf

anonymous_enable=NO
local_enable=YES
chroot_local_user=YES

add
allow_writeable_chroot=YES
pasv_min_port=40000
pasv_max_port=50000

systemctl restart vsfptd
ufw allow 20:21/tcp
ufw allow 40000:50000/tcp
ufw status

adduser ftpuser


```

