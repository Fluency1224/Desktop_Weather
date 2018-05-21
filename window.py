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
from PyQt5.QtWidgets import QApplication,QLineEdit,QTextEdit,QVBoxLayout,QGroupBox, QWidget, QLabel, QPushButton, QDesktopWidget,QGridLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication
from PyQt5 import Qt
import spider_weather


def get_text():
    temperatureHigh, temperatureLow, weather = spider_weather.get_weather()
    text = '最高气温：'+temperatureHigh+'\n'+'最低气温：'+temperatureLow+'\n'+'天气状况：'+weather
    
    return text

class App(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):        
        self.center() 
        self.setBG()
        self.quitBtn()
        self.laout()
        self.show()
        
    def center(self):
        #去掉边框和title
        #self.setWindowFlags(Qt.Qt.CustomizeWindowHint)
        self.setWindowFlags(Qt.Qt.FramelessWindowHint | Qt.Qt.Dialog)
        self.setGeometry(10, 10, 500, 281)
        #获得窗口
        qr = self.frameGeometry()
        #获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        #显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def setBG(self):
        #设置透明度
        self.setWindowOpacity(0.8)  
      
    def quitBtn(self):
        #qtn = QPushButton('关闭',self)
        qtn = QPushButton(self)
        qtn.clicked.connect(QCoreApplication.quit)
        #qtn.setIcon(QIcon("close.png"))
        qtn.resize(18,18)
        qtn.move(480,1)
        
        
    def laout(self):
        pixmap = QPixmap('md.png')
        
        weather = QLabel('天气：')
        weather.setStyleSheet("color:rgb(0, 201, 184);background:transparent")
        weather.setFont(QFont("微软雅黑", 20, QFont.Bold, False))
        
        weatherData = QLabel('晴天')
        weatherData.setStyleSheet("color:rgb(100, 201, 184);background:transparent")
        weatherData.setFont(QFont("微软雅黑", 20, QFont.Bold, False))
        
        tem = QLabel('气温')
        tem.setStyleSheet("color:rgb(0, 201, 184);background:transparent")
        tem.setFont(QFont("微软雅黑", 20, QFont.Bold, False))
        
        temData = QLabel('25-30℃')
        temData.setStyleSheet("color:rgb(0, 201, 184);background:transparent")
        temData.setFont(QFont("微软雅黑", 20, QFont.Bold, False))

        grid = QGridLayout()
        grid.setSpacing(10)
        
        grid.addWidget(weather, 1, 0)
        grid.addWidget(weatherData, 1, 1)

        grid.addWidget(tem, 2, 0)
        grid.addWidget(temData, 2, 1)
        
        #grid.setPixmap(pixmap)
        self.setLayout(grid) 

        
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
    sys.exit(app.exec_())
