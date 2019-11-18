# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dassh.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from choice import  Ui_Attendance
from  UpdateAttd import Ui_UpdateAttend

class Ui_dash(object):

    def __init__(self,userName):
       self.username = userName


    def setupUi(self, dash):
        dash.setObjectName("dash")
        dash.resize(802, 572)
        dash.setAutoFillBackground(False)
        self.logo = QtWidgets.QLabel(dash)
        self.logo.setGeometry(QtCore.QRect(340, 20, 100, 136))
        self.logo.setText("")
        self.logo.setObjectName("logo")
        pixmap = QPixmap('AttendPic.png')
        self.logo.setPixmap(pixmap)
        self.semester = QtWidgets.QComboBox(dash)
        self.semester.setGeometry(QtCore.QRect(330, 210, 131, 21))
        self.semester.setObjectName("semester")
        self.label = QtWidgets.QLabel(dash)
        self.label.setGeometry(QtCore.QRect(340, 170, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.takeA = QtWidgets.QPushButton(dash)
        self.takeA.setGeometry(QtCore.QRect(340, 300, 111, 21))
        self.takeA.setObjectName("takeA")
        self.updateA = QtWidgets.QPushButton(dash)
        self.updateA.setGeometry(QtCore.QRect(340, 350, 111, 21))
        self.updateA.setObjectName("updateA")

        self.retranslateUi(dash)
        self.tech()
        QtCore.QMetaObject.connectSlotsByName(dash)

        self.takeA.clicked.connect(self.TakeAt)
        self.updateA.clicked.connect(self.UpdateAt)

    def retranslateUi(self, dash):
        _translate = QtCore.QCoreApplication.translate
        dash.setWindowTitle(_translate("dash", "Dashboard"))
        self.label.setText(_translate("dash", "Select Semester"))
        self.takeA.setText(_translate("dash", "Take Attendance"))
        self.updateA.setText(_translate("dash", "Update Attendance"))

    def TakeAt(self):
        sub = self.semester.currentText()
        print(sub)

        self.window =   QtWidgets.QMainWindow()
        self.ui = Ui_Attendance(self.username,sub)
        self.ui.setupUi(self.window)
        self.window.show()



    def UpdateAt(self):
        seme = self.semester.currentText()
        print(seme)
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_UpdateAttend(self.username)
        self.ui.setupUi(self.window)
        self.window.show()

    def tech(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=""
        )
        mycursor = mydb.cursor()
        mycursor.execute("""SELECT * FROM collegeattend.subjectteacher where teacherid = %s""",(self.username,))
        myresult = mycursor.fetchone()
        for row in myresult:
            if row!=self.username:
                if row :
                    self.semester.addItem(row)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dash = QtWidgets.QWidget()
    ui = Ui_dash()
    ui.setupUi(dash)
    dash.show()
    sys.exit(app.exec_())
