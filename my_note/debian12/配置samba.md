## 安装netstat工具

```
apt-get install net-tools
```



切换root用户

```
su -
```



把用户加入到sudo组

```
usermod -aG sudo alantop
```

 ```
 cat /etc/os-release
 ip a
 apt update
 apt install samba
 systemctl enable smbd
 systemctl restart smbd
 systemctl status smbd
 
 mkdir /smbshare
 nano /etc/samba/smb.conf
 
 [samba-share]
 comment = samba share
 path =/smbshare
 read only=no
 browsable=yes
 writeable=yes
 
 useadd smbuser
 smbpasswd -a smbuser
 chown smbuser:smbuser /smbshare/
 
 systmctl restart smbd
 
 
 
 ```