**升级系统**
`cat /etc/debian_version`

`apt-get update`
`apt-get upgrade`
`apt-get dist-upgrade`
`apt-get autoremove`

`reboot`



**安装软件**

`apt install vim mc build-essential l timeshift gnome-shell-extension-manager snapd flatpak -y`

增加仓库
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

usermod -aG sudo alantop
usermod -aG sudo root

修改源
nano /etc/apt/sources.list

图形界面增加
添加 Contrib 和 Non-Free 软件源





