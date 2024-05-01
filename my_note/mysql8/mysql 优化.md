

mysqld配置

```
innodb_buffer_pool_size=2G
innodb_buffer_pool_instances=1
```


```
- innodb_buffer_pool_size ：InnoDB缓冲区大小。这个参数通常设置为总内存的70%～80%。
- key_buffer_size：MyISAM索引缓冲区的大小。
- max_connections ： MySQL服务器同时处理的最大连接数。
- query_cache_size：查询缓存大小，通常设置为总内存的5%。
```

