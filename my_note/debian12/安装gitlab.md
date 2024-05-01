
debian 12.4 安装gitlab 奇怪的安装成功了  
apt update  
apt install wget ca-certificates curl apt-transport-https gnupg2 -y  
curl -s https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh  
sudo bash  
apt install gitlab-ce -y  
vim /etc/gitlab/gitlab.rb  
修改内容  
external_url ‘http://192.168.10.9’  
git_data_dirs  
{ "default" => { "path" => "/home/githome" } }  
gitlab-ctl reconfigure  
出现失败字样  
apt remove gitlab-ce  
rm -rf /opt/gitlab/  
rm -rf /var/log/gitlab/  
rm -rf /var/opt/gitlab/  
apt install gitlab-ce -y收起



查看登陆密码
cat /etc/gitlab/initial_root_password

无需启动服务 