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
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Weather RealTime'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
        self.setBG()
        self.quitBtn()

    def initUI(self):
        #self.setWindowTitle(self.title)
        self.setWindowFlags(Qt.Qt.CustomizeWindowHint)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
    def quitBtn(self):
        qtn = QPushButton('Quit',self)
        qtn.clicked.connect(QCoreApplication.quit)
        qtn.resize(qtn.sizeHint())
        qtn.move(40,50)


    def setBG(self):
        label = QLabel(self)
        pixmap = QPixmap('window.png')
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
