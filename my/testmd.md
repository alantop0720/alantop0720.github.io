- # 使用国内源解决Qt在线更新慢的问题

  

  先用更新组件功能更新维护工具

  

  然后 再升级

  

  镜像地址写下面的

  

  

  Qt在线安装更新工具默认使用官方的源，国内访问比较慢，可以在setting中增加国内的源来提高更新速度，如下面的源：

  http://mirrors.ustc.edu.cn/qtproject/online/qtsdkrepository/windows_x86/root/qt/





# qt6编译mysql8 



[![img](https://www.toutiao.com/article/7051768371221758496/?log_from=422341af668eb_1662824336696)
](javascript:void(0))



- 关注
- 推荐
- 热点
- 北京
- [西瓜视频](https://www.ixigua.com/)
- 财经
- 科技
- 娱乐
- 更多

搜索

发作品

[![img](https://sf1-cdn-tos.toutiaostatic.com/img/user-avatar/bec2847e134e954b93959e0f007c00d0~300x300.image)](https://www.toutiao.com/c/user/token/MS4wLjABAAAAS1_hbeCs6lxJHPIxmNildqLOBpXfVI7HQXuqv7aefIU/?source=tuwen_detail)

13

4



收藏

分享

# qt 6.2.2 用vc2019 编译MySQL 8.0.27驱动

原创2022-01-11 10:59·[alantop](https://www.toutiao.com/c/user/token/MS4wLjABAAAAS1_hbeCs6lxJHPIxmNildqLOBpXfVI7HQXuqv7aefIU/?source=tuwen_detail)

QT 6.2.2 与以前qt5.15编译mysql的方法大不一样，以前是通过pro工程编译，新版的是要通过cmake编译mysql。具体编译过程如下：

# 准备工作

安装qt 6.2.2

官方下载地址：
https://download.qt.io/official_releases/online_installers/qt-unified-windows-x86-online.exe

安装mysql 8.0.27

官方下载地址 ：
https://dev.mysql.com/downloads/installer/

下载 420m的安装包

![img](https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/a8ff49612c474e79b7fee0ff19052b68~noop.image?_iz=58558&from=article.pc_detail&x-expires=1663429138&x-signature=BzLIkAMwmatg079l%2Fkr1fs9MBFM%3D)



安装vs 2019 专业版

官方安装地址：
https://visualstudio.microsoft.com/zh-hans/vs/older-downloads/

![img](https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/bffb0d61b9894c90b45305fe62a7eb63~noop.image?_iz=58558&from=article.pc_detail&x-expires=1663429138&x-signature=DCOGUUJlVIQlK%2Bkzx%2BvW8aHaqhU%3D)





# 编译安装过程

准备工作安装好以后，按照如下提示键入代码即可。

以管理员身份进入powershell

```
# 进入源码目录
cd D:\alantop_dir\alantop_sde\QT\6.2.2\Src\qtbase\src\plugins\sqldrivers
# 准备工作
mkdir build
cd build
# 进入cmd, 调用VS环境进行构建
cmd

@REM 调用VS环境
call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\VC\Auxiliary\Build\vcvars64.bat"
@REM configure(DEBUG)
D:\alantop_dir\alantop_sde\QT\6.2.4\msvc2019_64\bin\qt-cmake.bat .. -G Ninja -DCMAKE_INSTALL_PREFIX="D:\alantop_dir\alantop_sde\QT\6.2.4\msvc2019_64" -DMySQL_INCLUDE_DIR="D:\alantop_dir\alantop_data\mysql-8.0.20-winx64\include" -DMySQL_LIBRARY="D:\alantop_dir\alantop_data\mysql-8.0.20-winx64\lib\libmysql.lib"
@REM 构建(DEBUG)
cmake --build .
@REM 安装(DEBUG)
cmake --install .
@REM configure(RELEASE)
D:\alantop_dir\alantop_sde\QT\6.2.4\msvc2019_64\bin\qt-cmake.bat .. -G Ninja -DCMAKE_INSTALL_PREFIX="D:\alantop_dir\alantop_sde\QT\6.2.2\msvc2019_64" -DMySQL_INCLUDE_DIR="D:\alantop_dir\alantop_data\mysql-8.0.20-winx64\include" -DMySQL_LIBRARY="D:\alantop_dir\alantop_data\mysql-8.0.20-winx64\lib\libmysql.lib" -DCMAKE_BUILD_TYPE=Release
@REM 构建(RELEASE)
cmake --build .
@REM 安装(RELEASE)
cmake --install .
```

![img](https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/77168046f17e4f1abe6259d80d7e17c4~noop.image?_iz=58558&from=article.pc_detail&x-expires=1663429138&x-signature=MiDtiZtJKa0AQrxTWP2z%2FXz0jos%3D)



# 测试是否成功

拷贝C:\Program Files\MySQL\MySQL Server 8.0\lib\libmysql.dll到项目生成目录下。.

用qt建立新的工程，在工程文件里加入模块sql，选择使用qmake编译，编译器选vc2019

![img](https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/7f14d2e4c42d4e909b84844a0fa23ad0~noop.image?_iz=58558&from=article.pc_detail&x-expires=1663429138&x-signature=pzdvMtWQ%2FJR7mfzZERS6qV8zOvc%3D)



![img](https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/b6ab5d50e1ee48bc9a8426d14acd0293~noop.image?_iz=58558&from=article.pc_detail&x-expires=1663429138&x-signature=ownNYTRQAX8wSGxNnil4VyawHu0%3D)



![img](https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/ff745f71749d4e238b1e900fec2bb4fc~noop.image?_iz=58558&from=article.pc_detail&x-expires=1663429138&x-signature=MyxOo43g03l5XLrHQYjjhioJHoo%3D)



![img](https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/92df2c816bca4142bc6dd480f9d4cd20~noop.image?_iz=58558&from=article.pc_detail&x-expires=1663429138&x-signature=xqLTX7ismTbswTvnR3uXBNsKulc%3D)



![img](https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/aaa77c1bd2e3446ba6baa484cb37a81c~noop.image?_iz=58558&from=article.pc_detail&x-expires=1663429138&x-signature=kLSKl%2FFWTusij%2Bj5UW9Ux%2FkRrxs%3D)



键入如下代码：

```
#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <QSqlQueryModel>
#include <QSqlDatabase>

QT_BEGIN_NAMESPACE
namespace Ui { class Widget; }
QT_END_NAMESPACE

class Widget : public QWidget
{
    Q_OBJECT

public:
    Widget(QWidget *parent = nullptr);
    ~Widget();
    void connectDB();
    QSqlDatabase db;
    QSqlQueryModel model;

private:
    Ui::Widget *ui;
};
#endif // WIDGET_H
```



```
#include "widget.h"
#include "ui_widget.h"

#include <QSqlDatabase>
#include <QDebug>
#include <QMessageBox>
#include <QSqlError>

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);

    connectDB();
}

Widget::~Widget()
{
    delete ui;
}

void Widget::connectDB()
{

    qDebug() << QSqlDatabase::drivers();
    db = QSqlDatabase::addDatabase("QMYSQL");
    db.setHostName("127.0.0.1");
    db.setUserName("root");
    db.setPassword("123");

    db.setDatabaseName("world");

    if (db.open()==true)
    {
        qDebug() << "ok";
    }
    else
    {
        QMessageBox::warning(this, "fail", db.lastError().text());
    }

    model.setQuery("select * from city");
    ui->tableView->setModel(&model);


}
```



调试可以输出 QList("QSQLITE", "QMARIADB", "QMYSQL", "QODBC", "QPSQL") ，读取到数据库，即可代表成功。

![img](https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/1bfef38a914843899a861eedf5b5d704~noop.image?_iz=58558&from=article.pc_detail&x-expires=1663429138&x-signature=xVz80WTeGajnB42v4GYItYUnAYI%3D)





qt 6.2.2 用vc2019 编译MySQL 8.0.27编译视频：



qt5系列配置文档和视频

# [QT 5.15.2 配置MySQL 8.0 文档](https://www.toutiao.com/a7008498076813951526/?log_from=4f3f8c6e23cdb_1641869782045)

# [QT5.15.2 配置mysql 8.0视频教程](https://www.ixigua.com/6929803008054460935)

举报

评论 4

![img](https://sf1-cdn-tos.toutiaostatic.com/img/user-avatar/bec2847e134e954b93959e0f007c00d0~300x300.image)

评论

- [![img](https://sf1-cdn-tos.toutiaostatic.com/img/motor-img/6e055f53d87ba57800b8cdf244b0e7e4~300x300.image)](https://www.toutiao.com/c/user/273127610521934/?source=tuwen_detail)

  [随性自由的铅笔0i](https://www.toutiao.com/c/user/273127610521934/?source=tuwen_detail)

  1

  转发了

  回复·01月12日

- [![img](https://sf6-cdn-tos.toutiaostatic.com/img/user-avatar/2x_b00138f7ba699c7dd1950c09d932f3a8~300x300.image)](https://www.toutiao.com/c/user/5946678644/?source=tuwen_detail)

  [大道至简999](https://www.toutiao.com/c/user/5946678644/?source=tuwen_detail)

  赞

  转发了

  回复·01月11日

- [![img](https://sf1-cdn-tos.toutiaostatic.com/img/user-avatar/2x_bc941cf7cd3468faf60d51794c6939ea~300x300.image)](https://www.toutiao.com/c/user/110501817564/?source=tuwen_detail)

  [徐军steven](https://www.toutiao.com/c/user/110501817564/?source=tuwen_detail)

  赞

  转发了

  回复·01月11日

查看全部 4 条评论

[![img](https://p3-sign.toutiaoimg.com/tos-cn-i-0004/cd78ffe717c444c09e47d20ea8f82373~tplv-tt-cs0:640:360.jpg?_iz=31127&from=ttvideo.headline&x-expires=1663429139&x-signature=uekYQGMjjJYNARntGV8HzykwRRE%3D)](https://www.toutiao.com/video/7127234220074009096/)

17:39

[再造：美国大片从不让人失望，全程18分钟震撼精彩，经典就是经典](https://www.toutiao.com/video/7127234220074009096/)

[南瓜之战](https://www.toutiao.com/c/user/token/MS4wLjABAAAAXj2mTYTmT3kPx09z1bedQ0UcBDbb_-O84eP12ymU9H6jhZhfZjIpvugIQiO2VvEg/?source=tuwen_detail)

[63评论](https://www.toutiao.com/video/7127234220074009096/)

08月02日

[![img](https://p3-sign.toutiaoimg.com/tos-cn-i-0004/9e3777e7de9945e099396248a78abb6d~tplv-tt-cs0:1919:1079.jpg?_iz=31127&from=ttvideo.headline&x-expires=1663429139&x-signature=eVOShPIY1K9Eee4%2ByM4JAEXOruA%3D)](https://www.toutiao.com/video/7111249338000474628/)

07:33

[法国惊悚片：荒漠狙杀目标，暴力复仇不死不休，惊险刺激！](https://www.toutiao.com/video/7111249338000474628/)

[鑫鑫影视精彩剧](https://www.toutiao.com/c/user/token/MS4wLjABAAAAzh5Q7G39n_LNgLv-qQIgNMm5CNREJ3gAyQc8CyoJhPPoHd0mprO85BndoldAkrg_/?source=tuwen_detail)

[20评论](https://www.toutiao.com/video/7111249338000474628/)

06月20日

[![img](https://p3-sign.toutiaoimg.com/tos-cn-i-0004/3f27b9ead5bd4af39e9936d701bd6e16~tplv-tt-cs0:960:540.jpg?_iz=31127&from=ttvideo.headline&x-expires=1663429139&x-signature=igVLJ7xALsGnsl%2BPjyDxNlPQ6iY%3D)](https://www.toutiao.com/video/7131297915796095502/)

13:40

[马云珍惜影像 回顾25年前走街串巷，怯怯的推销，自己都忍不住笑](https://www.toutiao.com/video/7131297915796095502/)

[大侠混剪秀](https://www.toutiao.com/c/user/token/MS4wLjABAAAAP4e9kV-wCc7QDWLnj-3VlCUjk7GWial25zGxgbnSrsAovAQLMk3BOfzq6EYacJhN/?source=tuwen_detail)

[58评论](https://www.toutiao.com/video/7131297915796095502/)

08月13日

[![img](https://p3-sign.toutiaoimg.com/tos-cn-i-0026/4596f17e631c4d15b89fda91a9ae0168~tplv-tt-cs0:640:360.jpg?_iz=31127&from=ttvideo.headline&x-expires=1663429139&x-signature=v889M0WPe452E7j%2BYpE3U2tl9LE%3D)](https://www.toutiao.com/video/7140391717923979816/)

02:27

[韩剧《美丽》（3）～～走向深渊的女神](https://www.toutiao.com/video/7140391717923979816/)

[陆陆谈教育](https://www.toutiao.com/c/user/token/MS4wLjABAAAArWhG8zAAh7yti8wMpngI8XH1GEkU0uaE2AwkdRaa1Gs/?source=tuwen_detail)

[0评论](https://www.toutiao.com/video/7140391717923979816/)

3天前

[自主网络安全新技术亮相合肥](https://www.toutiao.com/article/7141517829336990246/)

[经济日报](https://www.toutiao.com/c/user/token/MS4wLjABAAAA5JuEG4IbWQVcLLZHN-v2J880oGjJOgG0K5H7bYpCHbI/?source=tuwen_detail)

[2240评论](https://www.toutiao.com/article/7141517829336990246/#comment)

16小时前

[三代院士，两脚泥巴](https://www.toutiao.com/article/7141729412437131787/)

[新华网](https://www.toutiao.com/c/user/token/MS4wLjABAAAAP09LrX61xFpIWrgGdBDqkp-5om9Lans_kuIZ_ipAGRE/?source=tuwen_detail)

[0评论](https://www.toutiao.com/article/7141729412437131787/#comment)

3小时前

- [![img](https://p3-sign.toutiaoimg.com/tos-cn-i-0004/f76983977c75469eb97389b13aeed3fd~tplv-tt-cs0:640:360.jpg?_iz=31127&from=ttvideo.headline&x-expires=1663429141&x-signature=T8j3se04Mga8VqASFeluA2e5Qzc%3D)](https://www.toutiao.com/video/7139064099937354276/)

  16:53

  [王力宏电梯录像彻底曝光，内容令人意外！关键人放出重要视频](https://www.toutiao.com/video/7139064099937354276/)

  [九六mike](https://www.toutiao.com/c/user/token/MS4wLjABAAAAIGw6oovNth48bGMDUR0aEHK0XexbYx3TAglkPKKkY0SFfclRy4JSXUI90lhzgt01/?source=tuwen_detail)

  [2评论](https://www.toutiao.com/video/7139064099937354276/)

  21小时前

- [![img](https://p3-sign.toutiaoimg.com/tos-cn-i-0004/14dc4cd0ea464f1a9be531c16ce75b4c~tplv-tt-cs0:640:360.jpg?_iz=31127&from=ttvideo.headline&x-expires=1663429141&x-signature=puYuBTfQliIyMocRGWZ3F2qbfMA%3D)](https://www.toutiao.com/video/6809496692262437387/)

  23:42

  [【Linux教程】10：Vim编辑器的使用](https://www.toutiao.com/video/6809496692262437387/)

  [遇见狂神说](https://www.toutiao.com/c/user/token/MS4wLjABAAAATHMQmxb2-Nb6kCSnPKw8oXIuSXmkm1TrfTuwsjlFIoo/?source=tuwen_detail)

  [10评论](https://www.toutiao.com/video/6809496692262437387/)

  2020年03月29日

[![img](https://p3-sign.toutiaoimg.com/tos-cn-i-tjoges91tu/TH0YEUpAXJDgFS~tplv-tt-cs0:640:360.jpg?_iz=31826&from=feed&x-expires=1664120341&x-signature=3KtP8UXGde4LfUr4ic6y9iMAu%2FY%3D)](https://www.toutiao.com/article/7141625456393978406/)

[北京又一高校出现初筛阳性在校生，学校凌晨通报](https://www.toutiao.com/article/7141625456393978406/)

[光明网](https://www.toutiao.com/c/user/token/MS4wLjABAAAA9Lz0MeLdJDmqpU26Xi9O_M-cYI9z530wjM7eDKvzZTw/?source=tuwen_detail)

[0评论](https://www.toutiao.com/article/7141625456393978406/)

9小时前

[![img](https://p3-sign.toutiaoimg.com/tos-cn-i-0004/014c45b7f8a546e0bcc59c3d40e98822~tplv-tt-cs0:640:360.jpg?_iz=31127&from=ttvideo.headline&x-expires=1663429141&x-signature=F9xaUsX958cL0%2BCf2pH0u%2BMNy4U%3D)](https://www.toutiao.com/video/7052975599903572510/)

04:33

[北京夫妻的12年极简人生：房子素极了，却美到让人羡慕](https://www.toutiao.com/video/7052975599903572510/)

[一条](https://www.toutiao.com/c/user/token/MS4wLjABAAAAIlkg8p67TbbR0SBVopgqtCm9aCcGA7HeMw8FMkn7cDw/?source=tuwen_detail)

[3110评论](https://www.toutiao.com/video/7052975599903572510/)

01月14日

[6月以来上海警方查处涉疫犯罪99起，其中代做核酸占比最高](https://www.toutiao.com/article/7141550760026309151/)

[澎湃新闻](https://www.toutiao.com/c/user/token/MS4wLjABAAAApOspM7AnWqplD9FIBGnhJRfUjFT_msD1KZMfNPBZa-c/?source=tuwen_detail)

[11评论](https://www.toutiao.com/article/7141550760026309151/#comment)

14小时前

[![img](https://p3-sign.toutiaoimg.com/tos-cn-i-0004/dafc6864ca4b467b92c2449d87d04d27~tplv-tt-cs0:1742:980.jpg?_iz=31127&from=ttvideo.headline&x-expires=1663429141&x-signature=Jj01SZtL5QV12WT%2FulDWN6myAa0%3D)](https://www.toutiao.com/video/7141354335874581033/)

10:54

[《国产凌凌漆》凌凌漆随口吐痰，到底是什么用意？](https://www.toutiao.com/video/7141354335874581033/)

[细思飞影](https://www.toutiao.com/c/user/token/MS4wLjABAAAAzm89C0AVF-6xF9qNV4LhZ8WAjm8x0pb60FZzoKWjfzInQP1_2vhU8m_qi2kiNAXG/?source=tuwen_detail)

[375评论](https://www.toutiao.com/video/7141354335874581033/)

昨天20:22

[救命，全裸也救不了这烂片](https://www.toutiao.com/article/7141611575223566852/)

- [![救命，全裸也救不了这烂片-图1](https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/941c61627db24fa69b6e73451eb974d9~tplv-tt-cs0:640:360.jpg?_iz=31826&from=feed&x-expires=1664120341&x-signature=B8y8pvdSV5NUvQsd6wFKSSJSKpE%3D)](https://www.toutiao.com/article/7141611575223566852/)
- [![救命，全裸也救不了这烂片-图2](https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/cf538de1d598494e842c5743423fafc3~tplv-tt-cs0:1280:528.jpg?_iz=31826&from=feed&x-expires=1664120341&x-signature=OA4gBXrBFC3yq38Ya6%2BWfZTcGf8%3D)](https://www.toutiao.com/article/7141611575223566852/)
- [![救命，全裸也救不了这烂片-图3](https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/0c8181c087db49aebf93234d508f4352~tplv-tt-cs0:706:551.jpg?_iz=31826&from=feed&x-expires=1664120341&x-signature=R5PjpNU5nts4eNQMbdWZo71NfOM%3D)](https://www.toutiao.com/article/7141611575223566852/)
- [![救命，全裸也救不了这烂片-图4](https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/cc21ed7b6cde42469db04a0d2e9df879~tplv-tt-cs0:1080:450.jpg?_iz=31826&from=feed&x-expires=1664120341&x-signature=LLGArLFWhRkep7X%2BKT1Vgm%2BR69c%3D)](https://www.toutiao.com/article/7141611575223566852/)

[独立鱼](https://www.toutiao.com/c/user/token/MS4wLjABAAAACB2nkN6_w4mj5Ty4NfCuAr-mBDDOaImI96Wp9_GZS3Y/?source=tuwen_detail)

[119评论](https://www.toutiao.com/article/7141611575223566852/#comment)

9小时前

[![img](https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/c34d554e442d4f32aad2406bb9e1a6d3~tplv-tt-cs0:640:360.jpg?_iz=31826&from=feed&x-expires=1664120341&x-signature=V9EyGuX5hM%2B8%2BEIxp1Z%2B%2B8hKflg%3D)](https://www.toutiao.com/article/7140087545987072551/)

[6年换5帅，百度资本的家为何如此难当？](https://www.toutiao.com/article/7140087545987072551/)

[投资人说](https://www.toutiao.com/c/user/token/MS4wLjABAAAAfflcJLhWxF5EZy5eO3BLctSmbdFhn6CNe4Pije-OFwo/?source=tuwen_detail)

[8评论](https://www.toutiao.com/article/7140087545987072551/#comment)

4天前

[人民日报发布做家务年龄对照表，舍不得用孩子，才是害了他](https://www.toutiao.com/article/7141619811657925161/)

- [![人民日报发布做家务年龄对照表，舍不得用孩子，才是害了他-图1](https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/07976bd912e14697b4d98e157e40f7d5~tplv-tt-cs0:640:360.jpg?_iz=31826&from=feed&x-expires=1664120341&x-signature=Hmxc%2BaLg6IQ8IMhx5Kb6%2BjB6Kw0%3D)](https://www.toutiao.com/article/7141619811657925161/)
- [![人民日报发布做家务年龄对照表，舍不得用孩子，才是害了他-图2](https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/be9cc770f4e3438692110ff5e8278840~tplv-tt-cs0:502:585.jpg?_iz=31826&from=feed&x-expires=1664120341&x-signature=LSGMPVRYFE1MueE%2B7gOeqe16Lqw%3D)](https://www.toutiao.com/article/7141619811657925161/)
- [![人民日报发布做家务年龄对照表，舍不得用孩子，才是害了他-图3](https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/bb288080e21f4040a4fb80903eefaf22~tplv-tt-cs0:500:540.jpg?_iz=31826&from=feed&x-expires=1664120341&x-signature=fyP7GI%2Fmrbl8UF6%2BkVIBEDeScUg%3D)](https://www.toutiao.com/article/7141619811657925161/)
- [![人民日报发布做家务年龄对照表，舍不得用孩子，才是害了他-图4](https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/401c24eb3ac6446cb9f7b3a874045daf~tplv-tt-cs0:500:750.jpg?_iz=31826&from=feed&x-expires=1664120341&x-signature=oe9Ct1MbYcqnpd1hDw%2B5w1JExHs%3D)](https://www.toutiao.com/article/7141619811657925161/)

[礼县融媒](https://www.toutiao.com/c/user/token/MS4wLjABAAAAkbbS1ArhJyFArQ78KQMH1rnNurXfDkSm9M6Bzk2YGi8/?source=tuwen_detail)

[11评论](https://www.toutiao.com/article/7141619811657925161/#comment)

10小时前

[![img](https://p3-sign.toutiaoimg.com/dfic-imagehandler/c8e649e5-42a1-4c3b-900f-4a655141e61f~tplv-tt-cs0:640:360.jpg?_iz=31826&from=feed&x-expires=1664120341&x-signature=TMTKjdlFpKsvXE4qyRAPW7vZCD0%3D)](https://www.toutiao.com/article/6762344313247498765/)

[「手把手教python3接口自动化」: 搭建接口自动化测试框架](https://www.toutiao.com/article/6762344313247498765/)

[听海8](https://www.toutiao.com/c/user/token/MS4wLjABAAAAiIxifdZGu_BNo_t9nd-a4EF68NekRXDEpeN3PE_mW9qfZsMUKVQCCnA-MsllEmtT/?source=tuwen_detail)

[33评论](https://www.toutiao.com/article/6762344313247498765/#comment)

2019年11月23日

[换手机、手机号前，一定要做的事](https://www.toutiao.com/article/7141530174989795881/)

- [![换手机、手机号前，一定要做的事-图1](https://p3-sign.toutiaoimg.com/tos-cn-i-tjoges91tu/TGz363y2hrIyBU~tplv-tt-cs0:640:360.jpg?_iz=31826&from=feed&x-expires=1664120341&x-signature=OwKtT5xC77ObB%2FGRIPV7FfPaoBY%3D)](https://www.toutiao.com/article/7141530174989795881/)
- [![换手机、手机号前，一定要做的事-图2](https://p3-sign.toutiaoimg.com/tos-cn-i-tjoges91tu/TGz364b6etjHLN~tplv-tt-cs0:600:600.jpg?_iz=31826&from=feed&x-expires=1664120341&x-signature=ZiAgU53w2ncqpEBorSrt7wMCkt8%3D)](https://www.toutiao.com/article/7141530174989795881/)
- [![换手机、手机号前，一定要做的事-图3](https://p3-sign.toutiaoimg.com/tos-cn-i-tjoges91tu/TGz365I5Re6Ofe~tplv-tt-cs0:600:600.jpg?_iz=31826&from=feed&x-expires=1664120341&x-signature=nPidtCv4ayhgVhkRnA1XM%2BpvoYA%3D)](https://www.toutiao.com/article/7141530174989795881/)
- [![换手机、手机号前，一定要做的事-图4](https://p3-sign.toutiaoimg.com/tos-cn-i-tjoges91tu/TGz369R82idfjn~tplv-tt-cs0:600:600.jpg?_iz=31826&from=feed&x-expires=1664120341&x-signature=qwaI7%2Fcke4LnRdXslqQLDhnpwlE%3D)](https://www.toutiao.com/article/7141530174989795881/)

[光明网](https://www.toutiao.com/c/user/token/MS4wLjABAAAA9Lz0MeLdJDmqpU26Xi9O_M-cYI9z530wjM7eDKvzZTw/?source=tuwen_detail)

[0评论](https://www.toutiao.com/article/7141530174989795881/)

16小时前

[手工耿自制洗剪吹机械手臂：气势不输灭霸](https://www.toutiao.com/article/7141476191910904359/)

- [![手工耿自制洗剪吹机械手臂：气势不输灭霸-图1](https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/4d17626e321d4f3ba94ff7b805314f26~tplv-tt-cs0:640:360.jpg?_iz=31826&from=feed&x-expires=1664120341&x-signature=XAv73N14oUmcO4U9Pk9GD3L69ag%3D)](https://www.toutiao.com/article/7141476191910904359/)
- [![手工耿自制洗剪吹机械手臂：气势不输灭霸-图2](https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/3098f7d1d87d4e37884ce4baafeb089b~tplv-tt-cs0:1043:574.jpg?_iz=31826&from=feed&x-expires=1664120341&x-signature=Kw2JbR8Cz6ZdgJmMVBzE4o4DLXA%3D)](https://www.toutiao.com/article/7141476191910904359/)
- [![手工耿自制洗剪吹机械手臂：气势不输灭霸-图3](https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/f062ce82da5f4aecbecf2dda09978541~tplv-tt-cs0:1031:589.jpg?_iz=31826&from=feed&x-expires=1664120341&x-signature=934e30Fyby0hI7ELpZrE%2F7DhIVs%3D)](https://www.toutiao.com/article/7141476191910904359/)
- [![手工耿自制洗剪吹机械手臂：气势不输灭霸-图4](https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/5e40d0cd542f4842b1860d612c9d2480~tplv-tt-cs0:1033:572.jpg?_iz=31826&from=feed&x-expires=1664120341&x-signature=eALxLu%2BdRzdkhmtZtjLVxmPKMOo%3D)](https://www.toutiao.com/article/7141476191910904359/)

[环球Tech](https://www.toutiao.com/c/user/token/MS4wLjABAAAAhmrKbgu0ouA5k-wuKpU-HPEyv0pKzdKAv6QeKFw4eu8/?source=tuwen_detail)

[11评论](https://www.toutiao.com/article/7141476191910904359/#comment)

19小时前

[![img](https://p3-sign.toutiaoimg.com/tos-cn-i-0004/e67b763b075a4ca5896cd590f3f3c324~tplv-tt-cs0:5925:3333.jpg?_iz=31127&from=ttvideo.headline&x-expires=1663429141&x-signature=ZThOkbFf7cE6vVIrZo8%2FW9PhWvM%3D)](https://www.toutiao.com/video/7128331359998870046/)

08:22

[Smartisan T1：8年后我才知道锤子原来是艺术品](https://www.toutiao.com/video/7128331359998870046/)

[Tech不器说](https://www.toutiao.com/c/user/token/MS4wLjABAAAA8SIiFe92oP3IU-_nQUs95Nf3M-b0nzDzTHj9YZLx3jU/?source=tuwen_detail)

[492评论](https://www.toutiao.com/video/7128331359998870046/)

08月05日

[![img](https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/280f5a758d234f2d8296930dd0a24f5c~tplv-tt-cs0:640:360.jpg?_iz=31826&from=feed&x-expires=1664120341&x-signature=3E5Xpn6w5nyjopXAjhvtpnbY6Zo%3D)](https://www.toutiao.com/article/7140922673718100491/)

[overlord：能秒杀死亡骑士的朱红露滴的真实实力 实则全场最弱](https://www.toutiao.com/article/7140922673718100491/)

[懒惰的黑蛇](https://www.toutiao.com/c/user/token/MS4wLjABAAAAMoDIvcN9TCy4gtuLz1pphY7WXIHJfoaPC3KsXfgSLas/?source=tuwen_detail)

[15评论](https://www.toutiao.com/article/7140922673718100491/#comment)

昨天23:18

热门：

- [新豹T5](https://www.dongchedi.com/auto/series/5421)
- [Lacoste](https://www.dongchedi.com/auto/series/3301)
- [Routan](https://www.dongchedi.com/auto/series/3302)
- [Copen](https://www.dongchedi.com/auto/series/3303)
- [二手车](https://www.dongchedi.com/usedcar/x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x)
- [ms sql](https://backend.devrank.cn/traffic-aggregation/1202000)
- [大型系统的ja](https://backend.devrank.cn/traffic-aggregation/1202021)
- [嵌入式 lin](https://backend.devrank.cn/traffic-aggregation/1202022)
- [python如](https://backend.devrank.cn/traffic-aggregation/1202023)
- [unreal](https://backend.devrank.cn/traffic-aggregation/1202024)

[![alantop 头像](https://p3.toutiaoimg.com/large/daec000fe7051d55d9ee)](https://www.toutiao.com/c/user/token/MS4wLjABAAAAS1_hbeCs6lxJHPIxmNildqLOBpXfVI7HQXuqv7aefIU/?source=tuwen_detail)[alantop](https://www.toutiao.com/c/user/token/MS4wLjABAAAAS1_hbeCs6lxJHPIxmNildqLOBpXfVI7HQXuqv7aefIU/?source=tuwen_detail)

诚意、正心、格物、致知、修身、齐家、交易、助人。【专注于量化交易】

TA的热门作品

- 

  [centos 7 安装（man）中文帮助](https://www.toutiao.com/article/7109772421510578688/)

  825阅读06月16日

- 

  [· 用命令行操作windows服务](https://www.toutiao.com/article/7110212084817822241/)

  689阅读06月17日

- 

  [pyqt6开发的第一个程序](https://www.toutiao.com/article/7132465547102470671/)

  685阅读08月16日

- 

  [win10 命令行定时任务自动关机](https://www.toutiao.com/article/7111694193885921805/)

  547阅读06月21日

- 

  [hexo 安装配置 （推送gitee版本）](https://www.toutiao.com/article/7106407271520911911/)

  348阅读06月07日

[查看更多](https://www.toutiao.com/c/user/token/MS4wLjABAAAAS1_hbeCs6lxJHPIxmNildqLOBpXfVI7HQXuqv7aefIU/?source=tuwen_detail)

## 头条热榜

换一换

1. 

   为建设世界科技强国厚植土壤

2. **1**

   央视中秋晚会精彩节目集锦

   

3. **2**

   中国传媒大学多名学生感染新冠

   

4. **3**

   中国外贸是世界经济的“一池活水”

5. **4**

   李易峰回应“有关个人生活言论”

   

6. **5**

   查尔斯三世宣誓登基

   

7. **6**

   教师晒礼物感谢家长 教育局：将处理

   

8. **7**

   班主任为51个娃设53个班干部岗位

9. **8**

   宋佳辛柏青含泪再唱《人世间》

10. **9**

    玲花汪苏泷合唱《望星辰》好燃

11. **10**

    五年级开学女生比男生高一头

## ![精彩视频](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAMAAABiM0N1AAAAPFBMVEVHcEzvQEDwQUHwQEHwQULwQULvQEDwQUHvQEDwQELxQULwQUHxQEHwQUL////6urr3lpb95+fyUVL0bm8V8ewmAAAADXRSTlMAIJBZvIA85RBwnc9n3O4v5QAAAZhJREFUWMPNmNtyhDAIhk2MIRmHGN33f9d6aKvWFYhhZ/pfO99wEAI0zb2Cj9YB4CzonY2+eaIQ3Yo4ybWmmII3cm0BpgMkBJ3RwGwoAcezmBXFBT5YFMoGimMAxQJT69Yv6TZ/EQsV33M6LFanYs+NTS0+kq/JF5W78JAzk87/k8XHsgoBuoYJakAH5zqsUlebsYtJlQbtJkEt6NukFqu1VYojvphyzgKQW0NNfTGmlIaJJwXGs5wWjZPIN8qzIW2kl8Q35EEpZT5vXgRiSZ5ujDuIC3mkG8gBxITckrE+geiQu6YXg8hAAV1of0AECcjsX0AEqRA0/jsQ4VpRsAelrBHp7/V+SLUSUStaYRsZ2DZCziHixoaarTZqNP9lwA3UsyZ9jgz3QGLOLx6zPZDPxtmrZzXz415oymNNrUn7iKw1+lWaBMf9Sms8VhvY9VYItaXmcZjazy1+equo3nI8D7hl67r//AFB76Shd2RZsyc4+wTRBclwh6ggP2q196exGMrObOYNC4opP4GP1vXb+RCW8yFF+QLsLs/tCfTGZwAAAABJRU5ErkJggg==)精彩视频

![img](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADEAAAAwCAMAAACPHmKLAAAAM1BMVEVHcEzxQEHwQEHwQUHvQEDwQUHwQELvQEDwQUHvQEDwQEHwQEHvQEDwQELwQEHwQELwQULQdpGMAAAAEHRSTlMAn2DvEL+AIN86kFAhcM+vUcBIKwAAAVJJREFUSMfVVduChCAIVVTwsmn//7W76kybilbzNrwFnLgfhfgi0UQPnMFHtf+JMj7oa3+Xivch0q39yeyDpFV+284KTgt4BzBbICLn8FDwYcgWq8JTtYRVaTmIrjbfdYd8hTBNKxkopjOu/MoMepwGFz8FsvVFsACQMplo64Q6o8y6PiVoZzmG8H06coGQbBFNjNasJ5MF6REBgnP9KgemsrV4tuErMat1e2do46mXueHh4s7yRvx/csPoB599dDMNuoGgzxHiBsI1WQnbfE0Rp8pdtHDR3HwN8fHI5BNAKbwbWSaPAIDoJUx4STNE8hJgD1cOuzg7njcLuMW5ATeM1FVR2dxGk+RQRyUT4kpbsQ/yDGcfMNzBol0Y7efE+2qwxZNRo5oDzq8BZvKgsB0KvVo3RrbVqyZHf3NxOR1GJXfjdQ7e1HlGD/r+ehNp8U3yC/YPH/jMrgU4AAAAAElFTkSuQmCC)换一换

[55:04](https://www.toutiao.com/video/7140843101127606818/)

[遭遇极品制片人，我经历的狗血你不懂](https://www.toutiao.com/video/7140843101127606818/)

14万次播放

[03:51](https://www.toutiao.com/video/7141003211929813535/)

[直播间面包蟹骗局，无论谎言多低级，都能割到韭菜](https://www.toutiao.com/video/7141003211929813535/)

44万次播放

[09:01](https://www.toutiao.com/video/7139510513012048397/)

[女司机在贵州撞车了，吉普车受损严重，小微坐瘦猴车去挑战攀岩](https://www.toutiao.com/video/7139510513012048397/)

21万次播放

[02:42](https://www.toutiao.com/video/7140982697169519112/)

[iPhone 14 Pro的药丸灵动岛有多牛？安卓不敢抄，可能抄不到精髓](https://www.toutiao.com/video/7140982697169519112/)

23万次播放

[06:01](https://www.toutiao.com/video/7139822655120605726/)

[记录二手车从收到卖全过程！1台车能赚多少？真是暴利吗？](https://www.toutiao.com/video/7139822655120605726/)

34万次播放

- 首页
- 反馈
- 顶部