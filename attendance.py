# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'attend.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import mysql.connector
from datetime import date
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap


class Ui_Form(object):
    def __init__(self,username,sem,sub):
        self.username = username
        self.sem = sem
        self.sub = sub


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(609, 557)
        self.c1 = QtWidgets.QCheckBox(Form)
        self.c1.setGeometry(QtCore.QRect(80, 270, 70, 17))
        self.c1.setObjectName("c1")
        self.roll9 = QtWidgets.QLabel(Form)
        self.roll9.setGeometry(QtCore.QRect(370, 430, 47, 13))
        self.roll9.setObjectName("roll9")
        self.roll4 = QtWidgets.QLabel(Form)
        self.roll4.setGeometry(QtCore.QRect(370, 250, 47, 13))
        self.roll4.setObjectName("roll4")
        self.pic9 = QtWidgets.QLabel(Form)
        self.pic9.setGeometry(QtCore.QRect(370, 370, 51, 41))
        self.pic9.setText("")
        self.pic9.setObjectName("pic9")
        self.c7 = QtWidgets.QCheckBox(Form)
        self.c7.setGeometry(QtCore.QRect(160, 450, 70, 17))
        self.c7.setObjectName("c7")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(270, 40, 100, 136))
        self.label.setText("")
        self.label.setObjectName("label")
        pixmap = QPixmap('AttendPic.png')
        self.label.setPixmap(pixmap)
        self.pic1 = QtWidgets.QLabel(Form)
        self.pic1.setGeometry(QtCore.QRect(90, 190, 51, 51))
        self.pic1.setText("")
        self.pic1.setObjectName("pic1")
        self.roll7 = QtWidgets.QLabel(Form)
        self.roll7.setGeometry(QtCore.QRect(170, 430, 47, 13))
        self.roll7.setObjectName("roll7")
        self.pic6 = QtWidgets.QLabel(Form)
        self.pic6.setGeometry(QtCore.QRect(80, 370, 51, 41))
        self.pic6.setText("")
        self.pic6.setObjectName("pic6")
        self.roll8 = QtWidgets.QLabel(Form)
        self.roll8.setGeometry(QtCore.QRect(270, 430, 47, 13))
        self.roll8.setObjectName("roll8")
        self.roll1 = QtWidgets.QLabel(Form)
        self.roll1.setGeometry(QtCore.QRect(90, 250, 47, 13))
        self.roll1.setObjectName("roll1")
        self.c4 = QtWidgets.QCheckBox(Form)
        self.c4.setGeometry(QtCore.QRect(360, 270, 70, 17))
        self.c4.setObjectName("c4")
        self.roll5 = QtWidgets.QLabel(Form)
        self.roll5.setGeometry(QtCore.QRect(470, 250, 47, 13))
        self.roll5.setObjectName("roll5")
        self.pic7 = QtWidgets.QLabel(Form)
        self.pic7.setGeometry(QtCore.QRect(160, 370, 51, 41))
        self.pic7.setText("")
        self.pic7.setObjectName("pic7")
        self.pic4 = QtWidgets.QLabel(Form)
        self.pic4.setGeometry(QtCore.QRect(370, 190, 51, 51))
        self.pic4.setText("")
        self.pic4.setObjectName("pic4")
        self.pic3 = QtWidgets.QLabel(Form)
        self.pic3.setGeometry(QtCore.QRect(270, 190, 51, 51))
        self.pic3.setText("")
        self.pic3.setObjectName("pic3")
        self.c8 = QtWidgets.QCheckBox(Form)
        self.c8.setGeometry(QtCore.QRect(260, 450, 70, 17))
        self.c8.setObjectName("c8")
        self.roll10 = QtWidgets.QLabel(Form)
        self.roll10.setGeometry(QtCore.QRect(470, 430, 47, 13))
        self.roll10.setObjectName("roll10")
        self.c2 = QtWidgets.QCheckBox(Form)
        self.c2.setGeometry(QtCore.QRect(170, 270, 70, 17))
        self.c2.setObjectName("c2")
        self.pic5 = QtWidgets.QLabel(Form)
        self.pic5.setGeometry(QtCore.QRect(470, 190, 51, 51))
        self.pic5.setText("")
        self.pic5.setObjectName("pic5")
        self.c6 = QtWidgets.QCheckBox(Form)
        self.c6.setGeometry(QtCore.QRect(70, 450, 70, 17))
        self.c6.setObjectName("c6")
        self.c5 = QtWidgets.QCheckBox(Form)
        self.c5.setGeometry(QtCore.QRect(460, 270, 70, 17))
        self.c5.setObjectName("c5")
        self.roll2 = QtWidgets.QLabel(Form)
        self.roll2.setGeometry(QtCore.QRect(180, 250, 47, 13))
        self.roll2.setObjectName("roll2")
        self.c3 = QtWidgets.QCheckBox(Form)
        self.c3.setGeometry(QtCore.QRect(270, 270, 70, 17))
        self.c3.setObjectName("c3")
        self.pic10 = QtWidgets.QLabel(Form)
        self.pic10.setGeometry(QtCore.QRect(470, 370, 51, 41))
        self.pic10.setText("")
        self.pic10.setObjectName("pic10")
        self.pic8 = QtWidgets.QLabel(Form)
        self.pic8.setGeometry(QtCore.QRect(270, 370, 51, 41))
        self.pic8.setText("")
        self.pic8.setObjectName("pic8")
        self.c10 = QtWidgets.QCheckBox(Form)
        self.c10.setGeometry(QtCore.QRect(460, 450, 70, 17))
        self.c10.setObjectName("c10")
        self.roll3 = QtWidgets.QLabel(Form)
        self.roll3.setGeometry(QtCore.QRect(280, 250, 47, 13))
        self.roll3.setObjectName("roll3")
        self.roll6 = QtWidgets.QLabel(Form)
        self.roll6.setGeometry(QtCore.QRect(80, 430, 47, 13))
        self.roll6.setObjectName("roll6")
        self.pic2 = QtWidgets.QLabel(Form)
        self.pic2.setGeometry(QtCore.QRect(180, 190, 51, 51))
        self.pic2.setText("")
        self.pic2.setObjectName("pic2")
        self.c9 = QtWidgets.QCheckBox(Form)
        self.c9.setGeometry(QtCore.QRect(360, 450, 70, 17))
        self.c9.setObjectName("c9")
        self.submit = QtWidgets.QPushButton(Form)
        self.submit.setGeometry(QtCore.QRect(250, 500, 111, 23))
        self.submit.setObjectName("submit")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.loadingdata()
        self.cb[0].stateChanged.connect(lambda:self.checking(0))
        self.cb[1].stateChanged.connect(lambda:self.checking(1))
        self.cb[2].stateChanged.connect(lambda:self.checking(2))
        self.cb[3].stateChanged.connect(lambda:self.checking(3))
        self.cb[4].stateChanged.connect(lambda:self.checking(4))
        self.submit.clicked.connect(self.takingAttend)





    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.c1.setText(_translate("Form", "Roll No: 1"))
        self.roll9.setText(_translate("Form", "RollNum :"))
        self.roll4.setText(_translate("Form", "RollNum :"))
        self.c7.setText(_translate("Form", "Roll No: 7"))
        self.roll7.setText(_translate("Form", "RollNum :"))
        self.roll8.setText(_translate("Form", "RollNum :"))
        self.roll1.setText(_translate("Form", "RollNum :"))
        self.c4.setText(_translate("Form", "Roll No: 4"))
        self.roll5.setText(_translate("Form", "RollNum :"))
        self.c8.setText(_translate("Form", "Roll No: 8"))
        self.roll10.setText(_translate("Form", "RollNum :"))
        self.c2.setText(_translate("Form", "Roll No: 2"))
        self.c6.setText(_translate("Form", "Roll No: 6"))
        self.c5.setText(_translate("Form", "Roll No: 5"))
        self.roll2.setText(_translate("Form", "RollNum :"))
        self.c3.setText(_translate("Form", "Roll No: 3"))
        self.c10.setText(_translate("Form", "Roll No: 10"))
        self.roll3.setText(_translate("Form", "RollNum :"))
        self.roll6.setText(_translate("Form", "RollNum :"))
        self.c9.setText(_translate("Form", "Roll No: 9"))
        self.submit.setText(_translate("MainWindow", "Submit Attendance"))
        self.cb = [self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, self.c7, self.c8, self.c9, self.c10]
        self.pixx = [self.pic1,self.pic2,self.pic3,self.pic4,self.pic5,self.pic6,self.pic7,self.pic8,self.pic9,self.pic10]
        self.rollarr = [self.roll1,self.roll2,self.roll3,self.roll4,self.roll5,self.roll6,self.roll7,self.roll8,self.roll9,self.roll10]
        self.attendance = [0,0,0,0,0,0,0,0,0,0,0]

    def loadingdata(self):
        rollarr = ["roll1","roll2","roll3","roll4","roll5","roll6","roll7","roll8","roll9","roll10"]
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=""
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT s_roll, s_name, s_img FROM collegeattend.studentdetails WHERE s_sem = "+self.sem+"order by s_roll")
        myresult = mycursor.fetchall()
        i = 0
        pixmap1 = []
        namearr = []
        for row in myresult:
            pixmap1.append(QPixmap(row[2]))
            rn = row[0]
            nm = row[1]
            namearr.append(rn+'. '+nm)
            self.pixx[i].setPixmap(pixmap1[i])
            self.rollarr[i].setText(namearr[i])
            i = i + 1

        print(i)

    def checking(self,x):
            if  self.cb[x].isChecked() == True:
                self.cb[x].setText("Is Present")
                self.cb[x].setStyleSheet("color: Green")
                self.attendance[x] = 1
            else:
                self.cb[x].setText("Is Absent")
                self.cb[x].setStyleSheet("color: red")
                self.attendance[x] = 0

    def takingAttend(self):
        today = date.today()
        self.attendance[10] = today
        # print("Today's date:", self.attendance[10])
        # print(self.sub)
        # for j in range(11):
        #     print(self.attendance[j])
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='collegeattend',
                                                 user='root',
                                                 password='')
            cursor = connection.cursor()
            string = "(`1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `classdate`)"
            tab = "`" + str(self.sub) + "`" + string
            print(tab)
            cursor.execute("INSERT INTO "+ str(tab) +" VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s)",(self.attendance[0],self.attendance[1],self.attendance[2],self.attendance[3],self.attendance[4],self.attendance[5],self.attendance[6],self.attendance[7],self.attendance[8],self.attendance[9],self.attendance[10],))
            connection.commit()



            print("Record inserted successfully into "+ str(tab) + "table")

        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))

        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
