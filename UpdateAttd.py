# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updateScreen.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UpdateAttend(object):
    def __init__(self,username):
        self.username = username
        self.SemesterChoice = QtWidgets.QComboBox()
        self.SelectedDate = QtWidgets.QComboBox()
        print(username)


    def setupUi(self, UpdateAttend):
        UpdateAttend.setObjectName("UpdateAttend")
        UpdateAttend.resize(806, 593)
        self.semesterLabel = QtWidgets.QLabel(UpdateAttend)
        self.semesterLabel.setGeometry(QtCore.QRect(330, 70, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.semesterLabel.setFont(font)
        self.semesterLabel.setObjectName("semesterLabel")
        self.SemesterChoice = QtWidgets.QComboBox(UpdateAttend)
        self.SemesterChoice.setGeometry(QtCore.QRect(330, 140, 111, 21))
        self.SemesterChoice.setObjectName("SemesterChoice")
        self.SelectedDate = QtWidgets.QComboBox(UpdateAttend)
        self.SelectedDate.setGeometry(QtCore.QRect(330, 290, 111, 21))
        self.SelectedDate.setObjectName("SelectedDate")
        self.pushButton = QtWidgets.QPushButton(UpdateAttend)
        self.pushButton.setGeometry(QtCore.QRect(340, 360, 81, 21))
        self.pushButton.setObjectName("pushButton")
        self.DateLabel = QtWidgets.QLabel(UpdateAttend)
        self.DateLabel.setGeometry(QtCore.QRect(340, 240, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.DateLabel.setFont(font)
        self.DateLabel.setObjectName("DateLabel")

        self.retranslateUi(UpdateAttend)
        self.tecupd()
        QtCore.QMetaObject.connectSlotsByName(UpdateAttend)
        self.SemesterChoice.currentTextChanged.connect(self.dateUpdate)
        # self.SemesterChoice.changeEvent()

    def retranslateUi(self, UpdateAttend):
        _translate = QtCore.QCoreApplication.translate
        UpdateAttend.setWindowTitle(_translate("UpdateAttend", "Form"))
        self.semesterLabel.setText(_translate("UpdateAttend", "Select Semester"))
        self.DateLabel.setText(_translate("UpdateAttend", "Select Date"))
        self.pushButton.setText(_translate("UpdateAttend", "Update"))

    def tecupd(self):
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd=""
            )
            mycursor = mydb.cursor()
            mycursor.execute("""SELECT * FROM collegeattend.subjectteacher where teacherid = %s""", (self.username,))
            myresult = mycursor.fetchone()
            for row in myresult:
                if row != self.username:
                    if row:
                        self.SemesterChoice.addItem(row)


    def dateUpdate(self,newValue):
        print(newValue)
        connection  = mysql.connector.connect(
            host="localhost",
            database="collegeattend",
            user="root",
            passwd=""
        )
        cursor = connection.cursor()
        sql = "SELECT classdate FROM `"+str(newValue)+"` ORDER BY classdate ASC"
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        self.SelectedDate.clear()
        for i in result:
            print(i[0])
            self.SelectedDate.addItem(str(i[0]))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UpdateAttend = QtWidgets.QWidget()
    ui = Ui_UpdateAttend()
    ui.setupUi(UpdateAttend)
    UpdateAttend.show()
    sys.exit(app.exec_())
