# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import  mysql.connector
import hashlib
from errdilog import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(616, 477)
        self.Logo_2 = QtWidgets.QLabel(Form)
        self.Logo_2.setGeometry(QtCore.QRect(240, 70, 100, 110))
        self.Logo_2.setText("")
        self.Logo_2.setObjectName("Logo_2")
        pixmap = QPixmap('faceAttend.png')
        self.Logo_2.setPixmap(pixmap)
        self.Tname = QtWidgets.QLineEdit(Form)
        self.Tname.setGeometry(QtCore.QRect(230, 210, 113, 20))
        self.Tname.setObjectName("Tname")
        self.Tname.setPlaceholderText(" Name ")
        self.TuserId = QtWidgets.QLineEdit(Form)
        self.TuserId.setGeometry(QtCore.QRect(230, 240, 113, 20))
        self.TuserId.setObjectName("TuserId")
        self.TuserId.setPlaceholderText(" UserId ")
        self.Tpass = QtWidgets.QLineEdit(Form)
        self.Tpass.setGeometry(QtCore.QRect(230, 270, 113, 20))
        self.Tpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Tpass.setObjectName("Tpass")
        self.Tpass.setPlaceholderText(" Password ")
        self.Tpass_2 = QtWidgets.QLineEdit(Form)
        self.Tpass_2.setGeometry(QtCore.QRect(230, 300, 113, 20))
        self.Tpass_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Tpass_2.setObjectName("Tpass_2")
        self.Tpass_2.setPlaceholderText(" Conform Password")
        self.Tcontact = QtWidgets.QLineEdit(Form)
        self.Tcontact.setGeometry(QtCore.QRect(230, 330, 113, 20))
        self.Tcontact.setObjectName("Tcontact")
        self.Tcontact.setPlaceholderText(" Contact ")
        self.SignUp = QtWidgets.QPushButton(Form)
        self.SignUp.setGeometry(QtCore.QRect(250, 370, 75, 23))
        self.SignUp.setObjectName("SignUp")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.SignUp.clicked.connect(self.sigupdel)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.SignUp.setText(_translate("Form", "Sign Up"))


    def sigupdel(self):

        if self.Tname.text() != "" and self.Tpass.text() != "" and self.Tpass_2.text() != "" and self.TuserId.text() != "" and  self.Tcontact.text() != "":
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    database="collegeattend",
                    passwd=""
                )
                mycursor = mydb.cursor()
                mycursor.execute("SELECT userid FROM userdatabase where userid = %s ",(self.TuserId.text(),))
                myresult = mycursor.fetchone()
                if myresult is None:
                    pas = hashlib.sha1(str(self.Tpass.text()).encode())
                    cpas = hashlib.sha1(str(self.Tpass_2.text()).encode())
                    if pas.hexdigest() == cpas.hexdigest():
                        spass = pas.hexdigest()
                        try:
                            mycursor.execute("insert into userdatabase values(%s ,%s ,%s ,%s)", (self.TuserId.text(), spass, self.Tname.text(), self.Tcontact.text()))
                            mydb.commit()
                        except mysql.connector.Error as error:
                            print("Failed to insert into MySQL table {}".format(error))
                    else:
                        self.dilog = QtWidgets.QDialog()
                        self.dl = Ui_Dialog()
                        self.dl.setupUi(self.dilog)
                        self.dilog.show()
            except Exception as e:
                print(e)
        else:
            self.dilog = QtWidgets.QDialog()
            self.dl = Ui_Dialog()
            self.dl.setupUi(self.dilog)
            self.dilog.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
