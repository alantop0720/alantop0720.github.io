
方法一：
grant all privileges on *.* to root@'%' identified by "123456";
flush privileges;

方法二：
use mysql; 
update user set host = '%' where user = 'root';

select host,user,password from user;