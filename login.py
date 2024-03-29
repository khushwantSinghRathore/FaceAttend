# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import  mysql.connector
import  hashlib
from dashboard import Ui_dash
from errdilog import Ui_Dialog

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 575)
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(320, 20, 100, 110))
        self.Logo.setText("")
        self.Logo.setObjectName("Logo")
        pixmap = QPixmap('faceAttend.png')
        self.Logo.setPixmap(pixmap)
        self.Loginbutton = QtWidgets.QPushButton(self.centralwidget)
        self.Loginbutton.setGeometry(QtCore.QRect(330, 220, 61, 21))
        self.Loginbutton.setObjectName("Loginbutton")
        self.Userid = QtWidgets.QLineEdit(self.centralwidget)
        self.Userid.setGeometry(QtCore.QRect(310, 150, 113, 20))
        self.Userid.setObjectName("Userid")
        self.Userid.setPlaceholderText("UserId")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(310, 180, 113, 20))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.password.setPlaceholderText("Password")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 780, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.Loginbutton.clicked.connect(self.checked)
        self.password.returnPressed.connect(self.checked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Loginbutton.setText(_translate("MainWindow", "Login"))

    def checked(self):
        userName = self.Userid.text()
        passwd = self.password.text()
        print(userName)
        print(passwd)
        pas = hashlib.sha1(str(self.password.text()).encode())
        passwd = pas.hexdigest()
        print(passwd)
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                database="collegeattend",
                passwd=""
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT userid FROM userdatabase where userid = %s and pass = %s",(userName, passwd,))
            myresult = mycursor.fetchone()
            if myresult is None:
                self.dilog = QtWidgets.QDialog()
                self.dl = Ui_Dialog()
                self.dl.setupUi(self.dilog)
                self.dilog.show()
            else:
                    self.window = QtWidgets.QMainWindow()
                    self.ui = Ui_dash(userName)
                    self.ui.setupUi(self.window)
                    MainWindow.hide()
                    self.window.show()
        except mysql.connector.Error as e:
            print(e.errno)
            print(e.sqlstate)
            print("Failed to insert into MySQL table {}".format(e))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
