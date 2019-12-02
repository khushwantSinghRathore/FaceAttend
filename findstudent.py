# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subjecttoteacher.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
from distutils.log import Log

import  mysql.connector
from mysql.connector import Error , errorcode
from PyQt5.QtWidgets import (QApplication, QMainWindow)
from tests import Ui_Chart
from errdilog import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(616, 477)
        self.Submitdetails = QtWidgets.QPushButton(Form)
        self.Submitdetails.setGeometry(QtCore.QRect(260, 320, 75, 23))
        self.Submitdetails.setObjectName("Submitdetails")
        self.Logo_2 = QtWidgets.QLabel(Form)
        self.Logo_2.setGeometry(QtCore.QRect(240, 30, 100, 110))
        self.Logo_2.setText("")
        self.Logo_2.setObjectName("Logo_2")
        pixmap = QPixmap('faceAttend.png')
        self.Logo_2.setPixmap(pixmap)
        self.ForEnroll = QtWidgets.QRadioButton(Form)
        self.ForEnroll.setGeometry(QtCore.QRect(210, 175, 16, 16))
        self.ForEnroll.setText("")
        self.ForEnroll.setObjectName("ForEnroll")
        self.Enroll = QtWidgets.QLineEdit(Form)
        self.Enroll.setGeometry(QtCore.QRect(240, 170, 110, 20))
        self.Enroll.setObjectName("Enroll")
        self.Enroll.setPlaceholderText("  Enrollment Number")
        self.ForRollnum = QtWidgets.QRadioButton(Form)
        self.ForRollnum.setGeometry(QtCore.QRect(210, 225, 16, 16))
        self.ForRollnum.setText("")
        self.ForRollnum.setObjectName("ForRollnum")
        self.StudentRollNum = QtWidgets.QComboBox(Form)
        self.StudentRollNum.setGeometry(QtCore.QRect(240, 220, 110, 21))
        self.StudentRollNum.setObjectName("StudentRollNum")
        self.Semester = QtWidgets.QComboBox(Form)
        self.Semester.setGeometry(QtCore.QRect(240, 260, 110, 21))
        self.Semester.setObjectName("Semester")

        self.retranslateUi(Form)
        self.loaddata()
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.Submitdetails.clicked.connect(self.studentdet)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Submitdetails.setText(_translate("Form", "Search"))
        self.Semester.addItem("mca1")
        self.Semester.addItem("mca2")
        self.Semester.addItem("mca3")
        self.Semester.addItem("mca4")
        self.Semester.addItem("mca5")
        self.Semester.addItem("mca6")



    def loaddata(self):
        for x in range(1,11):
            self.StudentRollNum.addItem(str(x))
    #     mydb = mysql.connector.connect(
    #         host="localhost",
    #         user="root",
    #         database="collegeattend",
    #         passwd=""
    #     )
    #     mycursor = mydb.cursor()
    #     mycursor.execute("SELECT name FROM studentdetails")
    #     myresult = mycursor.fetchall()
    #     for row in myresult:
    #         self.StudentRollNum.addItem(row[0])


    def studentdet(self):
        if self.ForEnroll.isChecked() == True:
            if  str(self.Enroll.text()) != "":
                try:
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        database="collegeattend",
                        passwd=""
                    )
                    mycursor = mydb.cursor()
                    mycursor.execute("SELECT * FROM studentdetails where enrollement = "+str(self.Enroll.text()))
                    myresult = mycursor.fetchone()
                    if myresult is None:
                        self.ERrCall()
                    else:
                        self.RollNUM = myresult[0]
                        self.ListSEM = myresult[5]
                        for x in myresult:
                            print(x)
                except mysql.connector.Error as e:
                    print(e.errno)
                    print(e.sqlstate)
                    print("Error from Def Student Enoll".format(e))
            else:
                self.ERrCall()



        elif self.ForRollnum.isChecked() == True:
            try:
                mydatabase = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    database="collegeattend",
                    passwd=""
                )
                cursor = mydatabase.cursor()
                sql = "SELECT * FROM `studentdetails` where  rollnum = " + str(self.StudentRollNum.currentText()) + " and semester = '" + str(self.Semester.currentText())+"'"
                print(sql)
                cursor.execute(sql)
                result = cursor.fetchone()
                if result is None:
                    self.ERrCall()
                else:
                    self.RollNUM = result[0]
                    self.ListSEM = result[5]
                    for x in result:
                        print(x)

                    self.FindSub()
            except mysql.connector.Error as e:
                print(e.errno)
                print(e.sqlstate)
                print("Error from Def Student combo Box".format(e))
        else:
           self.ERrCall()



    def FindSub(self):
        self.ListSubj = []
        try:
            mydatabase = mysql.connector.connect(
                host="localhost",
                user="root",
                database="collegeattend",
                passwd=""
            )
            cursor = mydatabase.cursor()
            sql = "SELECT subject1,subject2,subject3,subject4,subject5,subject6,subject7 FROM `collgdatatable` where  semestername= '" + str(self.ListSEM) + "'"
            print(sql)
            cursor.execute(sql)
            result = cursor.fetchone()
            if result is None:
                self.ERrCall()
            else:
                for x in result:
                    self.ListSubj.append(str(x))

                # print(len(self.ListSubj))
                # for i in range(len(self.ListSubj)):
                #     print(self.ListSubj[i])
                self.AvgSem()
        except mysql.connector.Error as e:
            print(e.errno)
            print(e.sqlstate)
            print("Error from Def FindSUb ".format(e))

    def AvgSem(self):
        self.SutTotalAttd = []
        self.ToTalClass = []
        for i in range(7):
            try:
                mydatabase = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    database="collegeattend",
                    passwd=""
                )
                cursor = mydatabase.cursor()
                sql = "SELECT COUNT(`"+str(self.RollNUM)+"`) FROM `"+str(self.ListSubj[i])+"` where  `"+str(self.RollNUM)+"` = '1'"
                print(sql)
                cursor.execute(sql)
                result = cursor.fetchone()
                if result is None:
                    self.SutTotalAttd.append(str("Not"))
                else:
                    for x in result:
                        self.SutTotalAttd.append(str(result[0]))
            except mysql.connector.Error as e:
                print(e.errno)
                print(e.sqlstate)
                print("Error from Def Avg  and student total".format(e))

        for i in range(7):
            try:
                mydatabase = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    database="collegeattend",
                    passwd=""
                )
                cursor = mydatabase.cursor()
                sql = "SELECT COUNT(`classdate`) FROM `"+str(self.ListSubj[i])+"`"
                print(sql)
                cursor.execute(sql)
                result = cursor.fetchone()
                if result is None:
                    self.ToTalClass.append(str("hot"))
                else:
                    for x in result:
                        self.ToTalClass.append(str(result[0]))
            except mysql.connector.Error as e:
                print(e.errno)
                print(e.sqlstate)
                print("Error from Def Avg Total block".format(e))

        print(len(self.ToTalClass))
        print(len(self.SutTotalAttd))
        self.Percentage =  []
        print("total class")
        for j in range(len(self.ToTalClass)):
             self.Percentage.append(int(self.SutTotalAttd[j])/int(self.ToTalClass[j])*100)
        print("student Present")
        for k in range(len(self.Percentage)):
            print(self.Percentage[k])

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Chart(self.Percentage,self.ListSubj)
        self.ui.setupUi(self.window)
        self.window.show()


    def Outstring(self):
        return  self.Percentage


    def ERrCall(self):
        self.dilog = QtWidgets.QDialog()
        self.dl = Ui_Dialog()
        self.dl.setupUi(self.dilog)
        self.dilog.show()

if __name__ == "__main__":
    import  sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys._excepthook = sys.excepthook


    def my_exception_hook(exctype, value, traceback):
        # Print the error and traceback
        print(exctype, value, traceback)
        # Call the normal Exception hook after
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)


    # Set the exception hook to our wrapping function
    sys.excepthook = my_exception_hook
    sys.exit(app.exec_())

