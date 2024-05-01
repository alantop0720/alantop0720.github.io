
mysqld --initialize --console

mysqld --console
mysqld --console --shutdown
这将停止MySQL服务并关闭控制台终端。

mysqld--defaults-file=<path to my.ini>


MySQL在后台运行，请使用“--daemonize”参数。



启动

my.ini 增加 
default_authentication_plugin=mysql_native_password


修改验证方式
ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY '%&hl&)ory7Rg';


下面来介绍一下innodb_force_recovery设置各种值的作用
innodb_force_recovery=1 ( SRV_FORCE_IGNORE_CORRUPT )
此时MySQL数据库即使检测到损坏的page也可以运行。可以尝试使SELECT * FROM tab跳过损坏的索引记录和页面，可以恢复没有损坏的业务数据。

innodb_force_recovery=2 ( SRV_FORCE_NO_BACKGROUND )
阻止master thread和任何purge threads运行。如果在purge操作期间发生崩溃，则此恢复值将阻止它。

innodb_force_recovery=3 ( SRV_FORCE_NO_TRX_UNDO )
在crash recovery之后不执行事务rollbacks。

innodb_force_recovery=4 ( SRV_FORCE_NO_IBUF_MERGE )
防止insert buffer合并操作，不计算 tablestatistics。此时可能会永久损坏数据文件，需要删除并重新创建所有二级索引。

innodb_force_recovery=5 ( SRV_FORCE_NO_UNDO_LOG_SCAN )
启动数据库时不检查undo logs：InnoDB甚至将未完成的事务都视为已提交。此值可能会永久损坏数据文件。将InnoDB设置为只读。

innodb_force_recovery=6 ( SRV_FORCE_NO_LOG_REDO )
不进行与恢复有关的redo log前滚。此值可能会永久损坏数据文件。使数据库页面处于过时状态，从而可能导致 B 树和其他数据库结构遭受更多破坏。将InnoDB设置为只读。



命令行设置 校对规则

show VARIABLES LIKE '%collation%';
set collation_database=utf8mb4_general_ci;
set collation_connection=utf8mb4_general_ci; 
set collation_server=utf8mb4_general_ci; 
set default_collation_for_utf8mb4=utf8mb4_general_ci;