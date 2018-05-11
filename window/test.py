#-*-coding:utf-8-*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.Qt import *
import sys
# from push_button import PushButton
import globalvar as gv
import socket
import binascii
import login_encode
import time
# import yatigers_7
# import yatigers_threading
# import yatigers_0925
# import yatigers_28MHz

import yatigers_app_test
# import yatigers_latest
# import yatigers
class Login(QDialog):
    fid=open('userip_yatigers.txt','r+')
    data=fid.readlines(5)
    fid.close()
    user_list=data[0].split(' ')
    def __init__(self,parent=None):
        super(Login,self).__init__(parent)
        self.resize(560,400)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        
        self.initTitle()
        self.initLogin()
        self.initButton()
        self.init_copyright()
        self.mylayout()
        
    def initTitle(self):
        self.title_label=QLabel()
        self.icon_label=QLabel()
        # self.close_button=PushButton()
        # self.close_button.loadPixmap("./img/sysButton/close.png")
        
        self.title_label.setStyleSheet("color:white")
        # self.title_label.setStyleSheet("color:rgb(0, 120, 230);background:transparent")
        self.title_label.setFont(QFont("微软雅黑", 27, QFont.Bold, False))
        
        self.title_label.setText(u'HC8000系统管理')
    
    def initLogin(self):
        # self.name=QLabel(u'用户：')
        # self.word=QLabel(u'密码：')
        # self.ip_addr=QLineEdit(u'192.168.1.38')
        self.ip_addr=QComboBox()
        self.ip_addr.setEditable(True)
        self.ip_addr.addItems(self.user_list)
        self.ip_addr.setCurrentIndex(0)
        self.ip_addr.setStyleSheet("color:black")
        self.ip_addr.setFixedHeight(28)
        self.textName=QLineEdit(u'root')
        self.textName.setStyleSheet("color:black")
        self.textName.setFixedHeight(28)
        self.password=QLineEdit(u'12345')
        self.password.setFixedHeight(28)
        self.password.setStyleSheet("color:black")
        self.password.setEchoMode(QLineEdit.Password)
        
        self.remember=QCheckBox('记住密码')
        
        
    
    def initButton(self):
        self.buttonLogin=QPushButton(u'登录',self)
        self.buttonExit=QPushButton(u'退出',self)
        self.buttonLogin.setFixedSize(75, 25)
        self.buttonExit.setFixedSize(75, 25)
        self.buttonLogin.clicked.connect(self.handleLogin)
        self.buttonExit.clicked.connect(self.exitLogin)
    
    def init_copyright(self):
        self.copyright=QLabel()
        self.copyright.setText(u'Copyright2017 版权所有  雅泰歌思')
        
    def mylayout(self):
        title_layout=QHBoxLayout()
        title_layout.addStretch()
        title_layout.addWidget(self.icon_label)
        title_layout.addWidget(self.title_label)
        # title_layout.addSpacing(0)
        title_layout.addStretch()
        
        # close_layout=QHBoxLayout()
        # close_layout.addStretch()
        # close_layout.addWidget(self.close_button)
        # close_layout.setContentsMargins(10, 0, 5, 10)
    
        self.login_box=QGroupBox()
        self.login_box.setFixedSize(220,240)
        
        self.ipaddr_box=QGroupBox()
        self.ipaddr_box.setTitle('IP address:')
        self.ipaddr_box.setStyleSheet("color:white")
        self.ipaddr_box.setFixedSize(200,40)
        layout_ipaddr=QHBoxLayout()
        layout_ipaddr.addWidget(self.ip_addr)
        layout_ipaddr.setContentsMargins(0,0,0,0)
        self.ipaddr_box.setLayout(layout_ipaddr)
        
        self.username_box=QGroupBox()
        self.username_box.setTitle('Username:')
        self.username_box.setStyleSheet("color:white")
        self.username_box.setFixedSize(200,40)
        layout_name=QHBoxLayout()
        layout_name.addWidget(self.textName)
        layout_name.setContentsMargins(0,0,0,0)
        self.username_box.setLayout(layout_name)
        
        self.passw_box=QGroupBox()
        self.passw_box.setTitle('Password:')
        self.passw_box.setStyleSheet("color:white")
        self.passw_box.setFixedSize(200,40)
        layout_pass=QHBoxLayout()
        layout_pass.addWidget(self.password)
        layout_pass.setContentsMargins(0,0,0,0)
        self.passw_box.setLayout(layout_pass)
        
        
        self.pb_layout=QHBoxLayout()
        self.pb_layout.addWidget(self.buttonLogin)
        self.pb_layout.addWidget(self.buttonExit)
        self.pb_layout.setContentsMargins(0, 0, 0, 0)
        
        login_layout=QVBoxLayout(self)
        login_layout.addWidget(self.ipaddr_box)
        login_layout.addSpacing(10)
        login_layout.addWidget(self.username_box)
        login_layout.addSpacing(10)
        login_layout.addWidget(self.passw_box)
        login_layout.addSpacing(20)
        # login_layout.addStretch()
        login_layout.addLayout(self.pb_layout)
        
        self.login_box.setLayout(login_layout)
        
        groupbox_layout=QHBoxLayout()
        groupbox_layout.addStretch()
        groupbox_layout.addWidget(self.login_box)
        groupbox_layout.addStretch()
        groupbox_layout.setContentsMargins(180, 0, 180, 10)
        
        copyright_layout=QHBoxLayout()
        copyright_layout.addStretch()
        copyright_layout.addWidget(self.copyright)
        copyright_layout.addStretch()
        
        
        main_layout=QVBoxLayout(self)
        # main_layout.addLayout(close_layout)
        main_layout.addLayout(title_layout)
        login_layout.addSpacing(20)
        main_layout.addLayout(groupbox_layout)
        main_layout.addLayout(copyright_layout)
        self.setLayout(main_layout)
    
    def handleLogin(self,*args,**kwargs):
        debug_flag=0
        self.tcp=None
        if debug_flag:
            if self.ip_addr.currentText()=='192.168.1.38' and self.textName.text()=='root' and self.password.text()=='12345':
                self.window=yatigers_28MHz.TitleWidget()    #切换到功能界面
                # self.connect(self.window.close_button,SIGNAL("clicked()"),self,SLOT("close()"))
                # self.connect(self.window,SIGNAL("_signal()"),self,SLOT("close()"))
                self.window._signal.connect(self.relogin)
                self.window.show()
                self.hide()
            else:
                QMessageBox.critical(self,'Error',u'请检查账户密码')
        else:
            # print self.ip_addr.text(),self.textName.text(),self.password.text()
            # print time.time()
            ip=str(self.ip_addr.currentText())
            port=32000
            address=(ip,port)
            self.tcp=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            # self.tcp.setsockopt(socket.SOL_SOCKET,socket.SO_RCVTIMEO,5)
            # self.tcp.setsockopt(socket.SOL_SOCKET,socket.SO_SNDTIMEO,5)
            self.tcp.settimeout(2)
            state=1
            name_pass=[str(self.textName.text()),str(self.password.text())]
            login_info=login_encode.mystruct(state,name_pass)
            try:
                self.tcp.connect(address)
                self.tcp.send(login_info)
                permit=self.tcp.recv(1500)
            except:
                QMessageBox.critical(self,'Error',u'网络连接不可用')
            else:
                # print permit[0:13]
                if(permit[0:14]=='login success!'):
                    gv.set_clientsock(self.tcp)
                    # print self.tcp
                    self.hide()                    #关闭/隐藏原来的登录界面
                    # self.window=yatigers_threading.TitleWidget()    #切换到功能界面
                    self.window=yatigers_app_test.TitleWidget()    #切换到功能界面
                    # self.window=yatigers_latest.TitleWidget()    #切换到功能界面
                    self.window._signal.connect(self.relogin)
                    # self.window.tcpsocket=self.tcp
                    self.window.show()                    #界面有内存显示到显示器
                    # print time.time()
                    # print  'time is over'
                    # print ip
                    if ip not in self.user_list:
                        for ii in self.user_list:
                            ip+=' '+ii
                    else:
                        self.user_list.remove(ip)
                        for ii in self.user_list:
                            ip+=' '+ii
                    # print self.user_list
                    # print ip
                    fid=open('userip_yatigers.txt','w+')
                    fid.write(ip.strip())
                    fid.close()
                else:
                    QMessageBox.critical(self,'Error',u'访问拒止，请检查用户名和密码')
    def relogin(self):
        print u'心跳包文检测网络断开，请重连'
        # self.tcpsocket.close()
        # self.tcp=gv.get_clientsock()
        # print "tcp:",tcp
        # self.tcp.close()
        self.show()
        QMessageBox.critical(self,'Error',u'网络已断开，请重连！')
    
    def exitLogin(self):
        # gv.set_clientsock(1)
        reply=QMessageBox.question(self, 'Message',"Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                # tcp=gv.get_clientsock()
                # print "tcp:",tcp
                self.tcp.close()
                # sys.exit(0)
            except:
                print 'the tcp socket is no inuse'
            self.close()
        else:
            self.ignore()
        # # ###################################
        # # print 'kkkkkkk'
        # # self.window=yatigers_2.TitleWidget(self)    #切换到功能界面
        # # self.window.show()                    #界面有内存显示到显示器
        # ###################################

            
    def paintEvent(self ,event):
        painter = QPainter ()
        painter.begin(self)
        painter.drawPixmap(self.rect(), QPixmap("./images/1_big"))
        # painter.drawPixmap(self.rect(), QPixmap("./images/14_big"))
        painter.end()
        
    m_Drag=False
    def mousePressEvent(self,event):
        if event.button() == Qt.LeftButton:
            self.m_Drag=True
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self,event):
        if (self.m_Drag and event.buttons() == Qt.LeftButton):
            self.move(event.globalPos() - self.dragPosition)
            event.accept()
    def mouseReleaseEvent(self,event):
        self.m_Drag=False
    
    # def mousePressEvent(self,event):
        # if ReleaseCapture():
            # SendMessage(HWND)
    
if __name__=='__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    app=QApplication(sys.argv)
    login=Login()
    app.setActiveWindow(login)
    login.show()
    sys.exit(app.exec_())
    # if login.exec_()==QDialog.Accepted:
        