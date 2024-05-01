## 虚拟机光驱加载目录：

```
run/media/root/openEuler-22.03-LTS-SP2-x86_64/
```

## 查看虚拟机光驱挂载目录

```
df -H

cd /media/root/openEuler-22.03-LTS-SP2-x86_64/

```

## 不存在目录 就建立目录

```
mkdir -p /home/repo/ 

cp -r /mnt/Packages /home/repo/ 

cp -r /mnt/repodata /home/repo/ 

cp -r /mnt/RPM-GPG-KEY-openEuler /home/repo/

cd /media/root/openEuler-22.03-LTS-SP2-x86_64/Packages

rpm -ivh --nodeps drpm*.rpm
rpm -ivh --nodeps createrepo*.rpm

createrepo --update --workers=10 /home/repo
````





##  repo配置本地源



```
cp /etc/yum.repos.d/openEuler.repo  /etc/yum.repos.d/openEuler.repo.bak
vim /etc/yum.repos.d/openEuler.repo
```




  ```
  [base]
  name=base
  baseurl=file:///home/repo
  enabled=1
  gpgcheck=1
  gpgkey=file:///home/repo/RPM-GPG-KEY-openEuler
  ```

  > ![img](配置本地repo.assets/icon-note.gif) **说明：**
  >
  > - [*repoid*]中的repoid为软件仓库（repository）的ID号，所有.repo配置文件中的各repoid不能重复，必须唯一。示例中repoid设置为**base**。
  > - name为软件仓库描述的字符串。
  > - baseurl为软件仓库的地址。
  > - enabled为是否启用该软件源仓库，可选值为1和0。默认值为1，表示启用该软件源仓库。
  > - gpgcheck可设置为1或0，1表示进行gpg（GNU Private Guard）校验，0表示不进行gpg校验，gpgcheck可以确定rpm包的来源是有效和安全的。
  > - 
  > - gpgkey为验证签名用的公钥。

- 

- ```
   dnf history
  ```

- 清除缓存目录

  ```
  dnf clean all
  ```

- 更新缓存

  ```
  dnf makecache
  dnf install mc nano
  ```



