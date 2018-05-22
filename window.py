#########################################################################
# File Name: window.py
# Author: fluency
# mail: 1005068694@qq.com
# Created Time: 2018年05月05日 星期六 09时22分30秒
#########################################################################
#!/usr/bin/python3
#!coding:utf-8
import sys
from PyQt5.QtWidgets import QApplication,QLineEdit,QTextEdit,QVBoxLayout,QGroupBox, QWidget, QLabel, QPushButton, QDesktopWidget,QGridLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication
from PyQt5 import Qt
import spider_weather

TEXTSIZE = 12

class App(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):        
        self.center() 
        self.laout()
        self.show()
        
    def center(self):
        #去掉边框和title
        #self.setWindowFlags(Qt.Qt.CustomizeWindowHint)
        self.setWindowFlags(Qt.Qt.FramelessWindowHint | Qt.Qt.Dialog)
        #self.setGeometry(10, 10, 500, 281)
        #获得窗口
        qr = self.frameGeometry()
        #获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        #显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())
            
    def laout(self):
        
        weather = QLabel('天气')
        weather.setStyleSheet("color:rgb(0, 201, 184);background:transparent")
        weather.setFont(QFont("微软雅黑", TEXTSIZE, QFont.Bold, False))
        weatherData = QLabel(spider_weather.get_weather())
        weatherData.setStyleSheet("color:rgb(0, 201, 184);background:transparent")
        weatherData.setFont(QFont("微软雅黑", TEXTSIZE, QFont.Bold, False))
        
        tem = QLabel('气温')
        tem.setStyleSheet("color:rgb(0, 201, 184);background:transparent")
        tem.setFont(QFont("微软雅黑", TEXTSIZE, QFont.Bold, False))
        tem_text = spider_weather.get_temperatureLow()+'-'+spider_weather.get_temperatureHigh()+'℃'
        temData = QLabel(tem_text)
        temData.setStyleSheet("color:rgb(0, 201, 184);background:transparent")
        temData.setFont(QFont("微软雅黑", TEXTSIZE, QFont.Bold, False))
        
        win = QLabel('风力')
        win.setStyleSheet("color:rgb(0, 201, 184);background:transparent")
        win.setFont(QFont("微软雅黑", TEXTSIZE, QFont.Bold, False))
        winData = QLabel(spider_weather.get_winf())
        winData.setStyleSheet("color:rgb(0, 201, 184);background:transparent")
        winData.setFont(QFont("微软雅黑", TEXTSIZE, QFont.Bold, False))
        
        ziwai = QLabel('紫外线指数')
        ziwai.setStyleSheet("color:rgb(0, 201, 184);background:transparent")
        ziwai.setFont(QFont("微软雅黑", TEXTSIZE, QFont.Bold, False))
        ziwai_index, ziwai_suggest = spider_weather.get_ziwai()
        ziwai_text = ziwai_index
        ziwaiData = QLabel(ziwai_text)
        ziwaiData.setStyleSheet("color:rgb(0, 201, 184);background:transparent")
        ziwaiData.setFont(QFont("微软雅黑", TEXTSIZE, QFont.Bold, False))
        
        air = QLabel('空气指数')
        air.setStyleSheet("color:rgb(0, 201, 184);background:transparent")
        air.setFont(QFont("微软雅黑", TEXTSIZE, QFont.Bold, False))
        air_index, air_suggest = spider_weather.get_air()
        air_text = air_index
        airData = QLabel(air_text)
        airData.setStyleSheet("color:rgb(0, 201, 184);background:transparent")
        airData.setFont(QFont("微软雅黑", TEXTSIZE, QFont.Bold, False))
        
        chuanyi = QLabel('穿衣指数')
        chuanyi.setStyleSheet("color:rgb(0, 201, 184);background:transparent")
        chuanyi.setFont(QFont("微软雅黑", TEXTSIZE, QFont.Bold, False))
        chuanyi_index, chuanyi_suggest = spider_weather.get_chuanyi()
        chuanyi_text = chuanyi_index
        chuanyiData = QLabel(chuanyi_text)
        chuanyiData.setStyleSheet("color:rgb(0, 201, 184);background:transparent")
        chuanyiData.setFont(QFont("微软雅黑", TEXTSIZE, QFont.Bold, False))
        
        cleancar = QLabel('洗车指数')
        cleancar.setStyleSheet("color:rgb(0, 201, 184);background:transparent")
        cleancar.setFont(QFont("微软雅黑", TEXTSIZE, QFont.Bold, False))
        cleancar_index, cleancar_suggest = spider_weather.get_cleancar()
        cleancar_text = cleancar_index
        cleancarData = QLabel(cleancar_text)
        cleancarData.setStyleSheet("color:rgb(0, 201, 184);background:transparent")
        cleancarData.setFont(QFont("微软雅黑", TEXTSIZE, QFont.Bold, False))
        
        #qtn = QPushButton('关闭',self)
        qtn = QPushButton(self)
        qtn.setStyleSheet("color:rgb(0, 201, 184);background:transparent")
        cleancar.setFont(QFont("微软雅黑", TEXTSIZE, QFont.Bold, False))
        qtn.clicked.connect(QCoreApplication.instance().quit)
        #qtn.setIcon(QIcon("close.png"))
        qtn.resize(18,18)
        
        grid = QGridLayout()
        grid.setSpacing(10)        
        grid.addWidget(weather, 1, 1)
        grid.addWidget(weatherData, 1, 2)
        grid.addWidget(tem, 2, 1)
        grid.addWidget(temData, 2, 2)
        grid.addWidget(win, 3, 1)
        grid.addWidget(winData, 3, 2)
        grid.addWidget(air, 4, 1)
        grid.addWidget(airData, 4, 2)
        grid.addWidget(chuanyi, 5, 1)
        grid.addWidget(chuanyiData, 5, 2)
        grid.addWidget(cleancar, 6, 1)
        grid.addWidget(cleancarData, 6, 2)
        grid.addWidget(ziwai, 7, 1)
        grid.addWidget(ziwaiData, 7, 2)
        grid.addWidget(qtn, 1, 3)
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
    
    #设置背景图片
    def paintEvent(self ,event):
        #设置透明度
        self.setWindowOpacity(0.6)  
        
        painter = QPainter ()
        painter.begin(self)
        painter.drawPixmap(self.rect(), QPixmap("bg.jpg"))
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
