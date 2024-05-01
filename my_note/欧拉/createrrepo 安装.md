```bash
[root@repo ~]# createrepo --update --workers=10 /home/repo
-bash: createrepo：未找到命令
[root@repo ~]#
[root@repo ~]# dnf install createrepo -y
Last metadata expiration check: 1:11:41 ago on 2022年11月29日 星期二 20时22分38秒.
Dependencies resolved.
=============================================================================================================================
 Package                        Architecture             Version                              Repository                Size
=============================================================================================================================
Installing:
 createrepo_c                   x86_64                   0.17.6-1.oe2203                      OS                       137 k
Installing dependencies:
 drpm                           x86_64                   0.5.0-2.oe2203                       update                    60 k
​
Transaction Summary
=============================================================================================================================
Install  2 Packages
​
Total download size: 197 k
Installed size: 535 k
Downloading Packages:
(1/2): drpm-0.5.0-2.oe2203.x86_64.rpm                                                        331 kB/s |  60 kB     00:00    
(2/2): createrepo_c-0.17.6-1.oe2203.x86_64.rpm  
```







================================================================================
Installing:
 createrepo_c        x86_64        0.17.6-3.oe2203sp2           OS        136 k
Installing dependencies:
 drpm                x86_64        0.5.1-1.oe2203sp2            OS         59 k