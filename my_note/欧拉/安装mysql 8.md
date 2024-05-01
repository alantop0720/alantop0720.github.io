```
groupadd mysql
useradd -g mysql mysql
passwd mysql


mkdir -p /data/mysql
cd /data/mysql
mkdir data tmp run log
chown -R mysql:mysql /data

mount /alantop/alantop.iso /mnt

mkdir -p ~/srv/repo/
cp -r /mnt/Packages ~/srv/repo/
cp -r /mnt/repodata ~/srv/repo/
cp -r /mnt/RPM-GPG-KEY-openEuler ~/srv/repo/

createrepo --update --work=10 ~/srv/repo/


```



配置源

```
mv /etc/yum.repos.d/openeuler.repo /etc/yum.repos.d/openeuler.repo.bak

cd /etc/yum.repos.d/

vim openEuler.repo


```


```
[base] 
name=base 
baseurl=file:///home/openEuler/srv/repo 
enabled=1 
gpgcheck=1 
gpgkey=file:///home/openEuler/srv/repo/RPM-GPG-KEY-openEuler
```

```
dnf install mysql-server

vim /etc/my.cnf

```

```
[mysqld_safe]
log-error=/data/mysql/log/mysql.log
pid-file=/data/mysql/run/mysqld.pid
[mysqldump]
quick
[mysql]
no-auto-rehash
[client]
default-character-set=utf8
[mysqld]
basedir=/usr/local/mysql
socket=/data/mysql/run/mysql.sock
tmpdir=/data/mysql/tmp
datadir=/data/mysql/data
default_authentication_plugin=mysql_native_password
port=3306
user=mysql

```

```
chown mysql:mysql /etc/my.cnf

echo export  PATH=$PATH:/usr/local/mysql/bin  >> /etc/profile
source /etc/profile

mysqld --defaults-file=/etc/my.cnf --initialize

systemctl start mysqld

```

```
/usr/local/mysql/bin/mysql -uroot -p  -S /data/mysql/run/mysql.sock

alter user 'root'@'localhost' identified by "123456";

create user 'root'@'%' identified by '123456';
grant all privileges on *.* to 'root'@'%';
flush privileges;
```



