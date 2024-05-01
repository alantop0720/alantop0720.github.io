https://mirrors.aliyun.com/qt/official_releases/online_installers/?spm=a2c6h.13651104.d-5201.6.3e264773hPfvI4

```
.\qt-unified-windows-x86-online.exe --mirror https://mirrors.aliyun.com/qt；
```


碰到这个我问题
./qt-unified-linux-x64-4.3.0-1-online.run: error while loading shared libraries: libxcb-xinerama.so.0: cannot open shared object file: No such file or directory



sudo apt install --reinstall libxcb-xinerama0

问题：from 6.5.0 xcb-cursor0 or libxcb-cursor0 is needed to load the qt xcb platfo
sudo apt-get install libxcb-cursor0


问题：The program "make" does not exist or is not executable.
apt-get install build-essential


编译出现  error: cannot find -lGL
sudo apt-get install libgl1-mesa-dev


有关链接
https://www.toutiao.com/article/7306395408618504743/?log_from=ab88ea86866a1_1702649924055




