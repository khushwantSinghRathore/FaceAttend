# -*- coding: utf-8 -*-

# Updation implementation generated from reading ui file 'attend.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import  mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap


class Ui_Updation(object):
    def __init__(self,username,sem,sub,dat):
        self.username = username
        self.sem = sem
        self.sub = sub
        self.dat = dat


    def setupUi(self, Updation):
        Updation.setObjectName("Updation")
        Updation.resize(609, 557)
        self.c1 = QtWidgets.QCheckBox(Updation)
        self.c1.setGeometry(QtCore.QRect(80, 270, 70, 17))
        self.c1.setObjectName("c1")
        self.roll9 = QtWidgets.QLabel(Updation)
        self.roll9.setGeometry(QtCore.QRect(370, 430, 47, 13))
        self.roll9.setObjectName("roll9")
        self.roll4 = QtWidgets.QLabel(Updation)
        self.roll4.setGeometry(QtCore.QRect(370, 250, 47, 13))
        self.roll4.setObjectName("roll4")
        self.pic9 = QtWidgets.QLabel(Updation)
        self.pic9.setGeometry(QtCore.QRect(370, 370, 51, 41))
        self.pic9.setText("")
        self.pic9.setObjectName("pic9")
        self.c7 = QtWidgets.QCheckBox(Updation)
        self.c7.setGeometry(QtCore.QRect(160, 450, 70, 17))
        self.c7.setObjectName("c7")
        self.label = QtWidgets.QLabel(Updation)
        self.label.setGeometry(QtCore.QRect(270, 40, 100, 136))
        self.label.setText("")
        self.label.setObjectName("label")
        pixmap = QPixmap('AttendPic.png')
        self.label.setPixmap(pixmap)
        self.pic1 = QtWidgets.QLabel(Updation)
        self.pic1.setGeometry(QtCore.QRect(90, 190, 51, 51))
        self.pic1.setText("")
        self.pic1.setObjectName("pic1")
        self.roll7 = QtWidgets.QLabel(Updation)
        self.roll7.setGeometry(QtCore.QRect(170, 430, 47, 13))
        self.roll7.setObjectName("roll7")
        self.pic6 = QtWidgets.QLabel(Updation)
        self.pic6.setGeometry(QtCore.QRect(80, 370, 51, 41))
        self.pic6.setText("")
        self.pic6.setObjectName("pic6")
        self.roll8 = QtWidgets.QLabel(Updation)
        self.roll8.setGeometry(QtCore.QRect(270, 430, 47, 13))
        self.roll8.setObjectName("roll8")
        self.roll1 = QtWidgets.QLabel(Updation)
        self.roll1.setGeometry(QtCore.QRect(90, 250, 47, 13))
        self.roll1.setObjectName("roll1")
        self.c4 = QtWidgets.QCheckBox(Updation)
        self.c4.setGeometry(QtCore.QRect(360, 270, 70, 17))
        self.c4.setObjectName("c4")
        self.roll5 = QtWidgets.QLabel(Updation)
        self.roll5.setGeometry(QtCore.QRect(470, 250, 47, 13))
        self.roll5.setObjectName("roll5")
        self.pic7 = QtWidgets.QLabel(Updation)
        self.pic7.setGeometry(QtCore.QRect(160, 370, 51, 41))
        self.pic7.setText("")
        self.pic7.setObjectName("pic7")
        self.pic4 = QtWidgets.QLabel(Updation)
        self.pic4.setGeometry(QtCore.QRect(370, 190, 51, 51))
        self.pic4.setText("")
        self.pic4.setObjectName("pic4")
        self.pic3 = QtWidgets.QLabel(Updation)
        self.pic3.setGeometry(QtCore.QRect(270, 190, 51, 51))
        self.pic3.setText("")
        self.pic3.setObjectName("pic3")
        self.c8 = QtWidgets.QCheckBox(Updation)
        self.c8.setGeometry(QtCore.QRect(260, 450, 70, 17))
        self.c8.setObjectName("c8")
        self.roll10 = QtWidgets.QLabel(Updation)
        self.roll10.setGeometry(QtCore.QRect(470, 430, 47, 13))
        self.roll10.setObjectName("roll10")
        self.c2 = QtWidgets.QCheckBox(Updation)
        self.c2.setGeometry(QtCore.QRect(170, 270, 70, 17))
        self.c2.setObjectName("c2")
        self.pic5 = QtWidgets.QLabel(Updation)
        self.pic5.setGeometry(QtCore.QRect(470, 190, 51, 51))
        self.pic5.setText("")
        self.pic5.setObjectName("pic5")
        self.c6 = QtWidgets.QCheckBox(Updation)
        self.c6.setGeometry(QtCore.QRect(70, 450, 70, 17))
        self.c6.setObjectName("c6")
        self.c5 = QtWidgets.QCheckBox(Updation)
        self.c5.setGeometry(QtCore.QRect(460, 270, 70, 17))
        self.c5.setObjectName("c5")
        self.roll2 = QtWidgets.QLabel(Updation)
        self.roll2.setGeometry(QtCore.QRect(180, 250, 47, 13))
        self.roll2.setObjectName("roll2")
        self.c3 = QtWidgets.QCheckBox(Updation)
        self.c3.setGeometry(QtCore.QRect(270, 270, 70, 17))
        self.c3.setObjectName("c3")
        self.pic10 = QtWidgets.QLabel(Updation)
        self.pic10.setGeometry(QtCore.QRect(470, 370, 51, 41))
        self.pic10.setText("")
        self.pic10.setObjectName("pic10")
        self.pic8 = QtWidgets.QLabel(Updation)
        self.pic8.setGeometry(QtCore.QRect(270, 370, 51, 41))
        self.pic8.setText("")
        self.pic8.setObjectName("pic8")
        self.c10 = QtWidgets.QCheckBox(Updation)
        self.c10.setGeometry(QtCore.QRect(460, 450, 70, 17))
        self.c10.setObjectName("c10")
        self.roll3 = QtWidgets.QLabel(Updation)
        self.roll3.setGeometry(QtCore.QRect(280, 250, 47, 13))
        self.roll3.setObjectName("roll3")
        self.roll6 = QtWidgets.QLabel(Updation)
        self.roll6.setGeometry(QtCore.QRect(80, 430, 47, 13))
        self.roll6.setObjectName("roll6")
        self.pic2 = QtWidgets.QLabel(Updation)
        self.pic2.setGeometry(QtCore.QRect(180, 190, 51, 51))
        self.pic2.setText("")
        self.pic2.setObjectName("pic2")
        self.c9 = QtWidgets.QCheckBox(Updation)
        self.c9.setGeometry(QtCore.QRect(360, 450, 70, 17))
        self.c9.setObjectName("c9")
        self.submit = QtWidgets.QPushButton(Updation)
        self.submit.setGeometry(QtCore.QRect(250, 500, 111, 23))
        self.submit.setObjectName("submit")


        self.retranslateUi(Updation)
        QtCore.QMetaObject.connectSlotsByName(Updation)
        self.loadAttend()
        self.loadingdata()
        self.cb[0].stateChanged.connect(lambda:self.checking(0))
        self.cb[1].stateChanged.connect(lambda:self.checking(1))
        self.cb[2].stateChanged.connect(lambda:self.checking(2))
        self.cb[3].stateChanged.connect(lambda:self.checking(3))
        self.cb[4].stateChanged.connect(lambda:self.checking(4))
        self.submit.clicked.connect(self.takingAttend)






    def retranslateUi(self, Updation):
        _translate = QtCore.QCoreApplication.translate
        Updation.setWindowTitle(_translate("Updation", "Updation"))
        self.c1.setText(_translate("Updation", "Roll No: 1"))
        self.roll9.setText(_translate("Updation", "RollNum :"))
        self.roll4.setText(_translate("Updation", "RollNum :"))
        self.c7.setText(_translate("Updation", "Roll No: 7"))
        self.roll7.setText(_translate("Updation", "RollNum :"))
        self.roll8.setText(_translate("Updation", "RollNum :"))
        self.roll1.setText(_translate("Updation", "RollNum :"))
        self.c4.setText(_translate("Updation", "Roll No: 4"))
        self.roll5.setText(_translate("Updation", "RollNum :"))
        self.c8.setText(_translate("Updation", "Roll No: 8"))
        self.roll10.setText(_translate("Updation", "RollNum :"))
        self.c2.setText(_translate("Updation", "Roll No: 2"))
        self.c6.setText(_translate("Updation", "Roll No: 6"))
        self.c5.setText(_translate("Updation", "Roll No: 5"))
        self.roll2.setText(_translate("Updation", "RollNum :"))
        self.c3.setText(_translate("Updation", "Roll No: 3"))
        self.c10.setText(_translate("Updation", "Roll No: 10"))
        self.roll3.setText(_translate("Updation", "RollNum :"))
        self.roll6.setText(_translate("Updation", "RollNum :"))
        self.c9.setText(_translate("Updation", "Roll No: 9"))
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
        mycursor.execute("""SELECT rollnum,name,pic FROM collegeattend.studentdetails WHERE  semester = %s order by rollnum""",(self.sem,))
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

        # self.pic1.setPixmap(pixmap1[0])
        # self.pic2.setPixmap(pixmap1[1])
        # self.pic3.setPixmap(pixmap1[2])
        # self.pic4.setPixmap(pixmap1[3])
        # self.pic5.setPixmap(pixmap1[4])
        # self.pic6.setPixmap(pixmap1[5])
        # self.pic7.setPixmap(pixmap1[6])
        # self.pic8.setPixmap(pixmap1[7])
        # self.pic9.setPixmap(pixmap1[8])
        # self.pic10.setPixmap(pixmap1[9])

        # self.roll1.setText(namearr[0])
        # self.roll2.setText(namearr[1])
        # self.roll3.setText(namearr[2])
        # self.roll4.setText(namearr[3])
        # self.roll5.setText(namearr[4])
        print(i)

    def loadAttend(self):
        db = mysql.connector.connect(
            host="localhost",
            database="collegeattend",
            user="root",
            passwd=""
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM `"+str(self.sub)+"` WHERE  classdate = %s ",(self.dat,))
        result = cursor.fetchall()
        for i in result:
            for j in range(5):
                self.attendance[j] = i[j]
                print(str(self.attendance[j]))
                if self.attendance[j] == 1:
                    self.cb[j].setText("Is Present")
                    self.cb[j].setStyleSheet("color: Green")
                    self.cb[j].setChecked(True)
                else:
                    self.cb[j].setText("Is Absent")
                    self.cb[j].setStyleSheet("color: red")




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
            cursor.execute("UPDATE `"+ str(self.sub) +"` SET `1`=%s, `2`=%s, `3`=%s, `4`=%s,`5`=%s, `6`=%s, `7`=%s, `8`=%s,`9`=%s, `10`=%s where `classdate`=%s",(self.attendance[0],self.attendance[1],self.attendance[2],self.attendance[3],self.attendance[4],self.attendance[5],self.attendance[6],self.attendance[7],self.attendance[8],self.attendance[9],self.dat,))
            connection.commit()



            print("Record inserted successfully into "+ str(self.sub) + "table")

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
    Updation = QtWidgets.QWidget()
    ui = Ui_Updation()
    ui.setupUi(Updation)
    Updation.show()
    sys.exit(app.exec_())
