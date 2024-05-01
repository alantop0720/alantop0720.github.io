目录 /usr/share/nginx/html
conf /etc/nginx

dnf clean all
dnf makecache

dnf install nginx

dnf list all | grep nginx

systemctl start nginx
systtemctl enable nginx

systemctl reload nginx


firewall-cmd  --add-service=http --permanent
firewall-cmd --reload

curl http://127.0.0.1
