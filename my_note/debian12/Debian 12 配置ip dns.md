debian 12 配置ip，dns  
  
vim /etc/network/interfaces  
  
auto lo  
iface lo inet loopback  
  
auto eth0  
iface eth0 inet static  
address 192.168.1.100  
netmask 255.255.255.0  
gateway 192.168.1.1  
  
vim /etc/resolv.conf  
nameserver 114.114.114.114