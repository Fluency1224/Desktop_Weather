#########################################################################
# File Name: window.py
# Author: fluency
# mail: 1005068694@qq.com
# Created Time: 2018年05月05日 星期六 09时22分30秒
#########################################################################
#!/usr/bin/python3
#!coding:utf-8
import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication
from PyQt5 import Qt
import spider_weather

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Weather RealTime'
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 281
        self.initUI()
        self.setBG()
        self.mylabel()
        self.quitBtn()
       

    def initUI(self):
        #self.setWindowTitle(self.title)
        #self.setWindowFlags(Qt.Qt.CustomizeWindowHint)
        self.setWindowFlags(Qt.Qt.FramelessWindowHint | Qt.Qt.Dialog)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
    def quitBtn(self):
        #qtn = QPushButton('关闭',self)
        qtn = QPushButton(self)
        qtn.clicked.connect(QCoreApplication.quit)
        qtn.setIcon(QIcon("close.png"))
        qtn.resize(18,18)
        qtn.move(480,1)
        
    def mylabel(self):
        label2 = QLabel(self)
<<<<<<< HEAD:window/window.py
        label2.setText(u'测试label')
        #label2.setStyleSheet("color:red")
        label2.setStyleSheet("color:rgb(0224, 93, 0);background:transparent") 
=======
        #label2.setText(u'测试label')
        temperatureHigh, temperatureLow, weather = spider_weather.get_weather()
        text = '最高气温：'+temperatureHigh+'\n'+'最低气温：'+temperatureLow+'\n'+'天气状况：'+weather
        label2.setText(text)
        label2.setStyleSheet("color:red")
        label2.setStyleSheet("color:rgb(0, 201, 184);background:transparent")
#         label2.setFixedWidth(640) 
#         label2.setFixedHeight(400) 
>>>>>>> 6480194d074d2a856ea97369b8778d90ff640fa2:window.py
        label2.setFont(QFont("微软雅黑", 27, QFont.Bold, False))

        label3 = QLabel(self)
        label3.setText(u'测试label')
        #label3.setStyleSheet("color:red")
        label3.setStyleSheet("color:rgb(0224, 93, 0);background:transparent")
        label3.setFont(QFont("微软雅黑", 27, QFont.Bold, False))

    def setBG(self):
        label = QLabel(self)
        pixmap = QPixmap('md.png')
        label.setPixmap(pixmap)
        self.resize(self.width, self.height)

        #设置透明度
        self.setWindowOpacity(0.8)

    def mousePressEvent(self, event):  
        if event.button()==Qt.Qt.LeftButton:  
            self.m_flag=True  
            self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置  
            event.accept()  
            self.setCursor(QCursor(Qt.Qt.OpenHandCursor))  #更改鼠标图标  

    def mouseMoveEvent(self, QMouseEvent):  
        if Qt.Qt.LeftButton and self.m_flag:    
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置  
            QMouseEvent.accept()  

    def mouseReleaseEvent(self, QMouseEvent):  
        self.m_flag=False  
        self.setCursor(QCursor(Qt.Qt.ArrowCursor))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
