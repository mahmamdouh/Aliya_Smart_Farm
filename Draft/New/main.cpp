#include "mainwindow.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
        // hide the window title bar, but let the window be closed using Alt + F4
    w.setWindowFlags(Qt::Window | Qt::FramelessWindowHint | Qt::WindowCloseButtonHint);
    
    //w.show();
    w.showFullScreen();

    return a.exec();
}
