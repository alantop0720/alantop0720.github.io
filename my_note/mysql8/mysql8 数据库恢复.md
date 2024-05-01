# 转换成可视化sql
```
mysqlbinlog --no-defaults -v --set-charset=utf8 binlog.000018> /home/binlog18.txt
```




# 查看备份

```
show variables like '%log_bin%'
```



# 显示对应事件

```
show binlog events in 'binlog.000018'
```



# 查看数据目录

```
SHOW VARIABLES LIKE '%datadir%'
```

# 查看当前日志

```
show master status
```

# 备份数据

```
mysqldump -uroot -p --single-transaction --master-data=2 employees > d:/sql.bak
```

# 日志替换

```
flush binary logs
```

# 重新初始化数据库

```
chown -R mysql:mysql /datadir
mysqld --datadir=/datadir --initilize-insecure &
```

# 备份数据库和所有的bin文件

# 启动mysql数据库

```
mysqld --datadir=/datadir &
```

# 创建数据库

```
create database wealth
```

```
use wealth

source /backups/back.sql
```

# 恢复数据 按照pos来

```
mysqlbinlog --start-position=66382337 /binlog.0000004 /binlog.000005 | mysql -u root
```

# 数据恢复2示例



```
mysqlbinlog --no-defaults --start-position=690 --stop-position=916 binlog.000362 | mysql -u root -p
```



# mysql 错误日志

```
SHOW VARIABLES LIKE 'log_error'
```

# mysql通用日志查询

```
show variables like '%general%'
```

# mysql回收站

```
restore table employees from recyclebin;

show recyclebin;
```

# 查看mysql日志模式

```
show global variables like "%binlog_format%";
```

# 日志保存时间

```
show variables like '%expire_log%';
```




python binlog2sql.py -h127.0.0.1 -P3306 -uroot -p -dcrmsb --start-file='binlog.000361' -B



```
python binlog2sql.py -h127.0.0.1 -P3306 -uroot -p'13601994674' -dtest -tuser --start-file='binlog.000362' --start-datetime='2023-12-22 08:44:00' --stop-datetime='2023-12-26 11:50:00'
```

# win下执行成功

## 恢复数据不需要在数据目录下

### 几个注意点：

1. python库 注意修改

2. windows下文件不要引号

   

python binlog2sql.py -h127.0.0.1 -P3306 -uroot -p -dtest -tuser --start-file=binlog.000362


虹口


python binlog2sql.py -h10.2.3.110 -P3306 -uroot -p -dhk_ejk -troot --start-file=binlog.000362