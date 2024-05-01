

RC_ICONS = alantop.ico


greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++17

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    demo_four.cpp \
    main.cpp \
    widget.cpp

HEADERS += \
    demo_four.h \
    widget.h

FORMS += \
    demo_four.ui \
    widget.ui

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

RESOURCES += \
    res.qrc


DESTDIR =../bin
MOC_DIR      = ./tmp/moc
OBJECTS_DIR  = ./tmp/obj
RCC_DIR = ./tmp/rcc
UI_DIR = ./tmp/ui
TARGET = "alantop"