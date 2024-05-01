
```
SHOW VARIABLES LIKE 'character%'
```


设置不解析

my.ini

mysqld
skip-name-resolve

用mysql 命令行登录
set global max_connect_errors = 2048;


SHOW GLOBAL VARIABLES LIKE 'max_connect_errors'

performance_scheme

hosts
hosts.cache


查看字符集
```
SHOW VARIABLES WHERE Variable_name LIKE 'character_set_%' OR Variable_name LIKE 'collation%';
```