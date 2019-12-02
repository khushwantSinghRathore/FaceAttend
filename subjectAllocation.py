# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subjectAllocation.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import  mysql.connector
from  mysql.connector.errors import Error
from errdilog import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(616, 477)
        self.Select = QtWidgets.QPushButton(Form)
        self.Select.setGeometry(QtCore.QRect(265, 230, 75, 23))
        self.Select.setObjectName("Select")
        self.Logo = QtWidgets.QLabel(Form)
        self.Logo.setGeometry(QtCore.QRect(260, 10, 100, 110))
        self.Logo.setText("")
        self.Logo.setObjectName("Logo")
        pixmap = QPixmap('faceAttend.png')
        self.Logo.setPixmap(pixmap)
        self.Users = QtWidgets.QComboBox(Form)
        self.Users.setGeometry(QtCore.QRect(250, 150, 110, 21))
        self.Users.setObjectName("Users")
        self.Tablevew = QtWidgets.QLabel(Form)
        self.Tablevew.setGeometry(QtCore.QRect(380, 150, 20, 20))
        self.Tablevew.setText("")
        self.Tablevew.setObjectName("Tablevew")
        self.SubjecBeAlloted = QtWidgets.QListWidget(Form)
        self.SubjecBeAlloted.setGeometry(QtCore.QRect(10, 190, 200, 260))
        self.SubjecBeAlloted.setObjectName("SubjecBeAlloted")
        self.AllocatedSubject = QtWidgets.QListWidget(Form)
        self.AllocatedSubject.setGeometry(QtCore.QRect(400, 190, 200, 260))
        self.AllocatedSubject.setObjectName("AllocatedSubject")
        self.AllocatedSubject.hide()
        self.Remove = QtWidgets.QPushButton(Form)
        self.Remove.setGeometry(QtCore.QRect(310, 320, 75, 23))
        self.Remove.setObjectName("Remove")
        self.Remove.hide()
        self.Add = QtWidgets.QPushButton(Form)
        self.Add.setGeometry(QtCore.QRect(220, 320, 75, 23))
        self.Add.setObjectName("Add")
        self.Add.hide()
        self.Allot = QtWidgets.QPushButton(Form)
        self.Allot.setGeometry(QtCore.QRect(265, 410, 75, 23))
        self.Allot.setObjectName("Allot")
        self.Allot.hide()

        self.retranslateUi(Form)
        self.loadUser()
        self.prepareList()
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.Select.clicked.connect(self.OnSelectUser)
        self.Add.clicked.connect(self.OnAddButton)
        self.Remove.clicked.connect(self.OnRemoveButton)
        self.Allot.clicked.connect(self.OnAllotButton)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Select.setText(_translate("Form", "Select"))
        self.Remove.setText(_translate("Form", "Remove"))
        self.Add.setText(_translate("Form", "Add"))
        self.Allot.setText(_translate("Form", "Update"))


    def loadUser(self):
        self.id = []
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                database="collegeattend",
                passwd=""
            )
            cursor = db.cursor()
            cursor.execute("select userid,teachername from userdatabase")
            result = cursor.fetchall()
            if result is None:
                print("nothing in object")
            else:
                for row in result:
                    self.Users.addItem(str(row[1]))
                    self.id.append(str(row[0]))
        except Error as er :
            print(er)



    def prepareList(self):
        AllSubjects = []
        ReservedSubject = []
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                database="collegeattend",
                passwd=""
            )
            mycursor = mydb.cursor()
            mycursor.execute("select subject1,subject2,subject3,subject4,subject5,subject6,subject7 from collgdatatable")
            myresult = mycursor.fetchall()
            if myresult is None:
                print("object blank ")
                pass
            else:
                for row in myresult:
                    for i in range(7):
                        if row[i] != "":
                            AllSubjects.append(str(row[i]))
                stp1 = len(AllSubjects)
        except Error as e:
            print(e)

        #this is for the already alloted subjects
        try:
            mycursor = mydb.cursor()
            mycursor.execute("select subject1,subject2,subject3,subject4,subject5,subject6,subject7 from subjectteacher")
            myresult = mycursor.fetchall()
            if myresult is None:
                print("object blank ")
                pass
            else:
                for row in myresult:
                    for i in range(7):
                        if row[i] != "":
                            ReservedSubject.append(str(row[i]))
                stp2 = len(ReservedSubject)
                # for j in range(stp2):
                #     print(ReservedSubject[j])
        except Error as e:
            print(e)

        #this is the final list that is going to be shown
        finalList = []
        for i  in  range(stp1):
            flag = 0
            for j in range(stp2):
                if str(AllSubjects[i]) == str(ReservedSubject[j]):
                    flag=1
            if flag == 0:
                finalList.append(str(AllSubjects[i]))

        r = len(finalList)
        for p in range(r):
            print(finalList[p])

        self.SubjecBeAlloted.addItems(finalList)

    def OnSelectUser(self):
        self.AllocatedSubject.clear()
        subList = []
        ind =  self.Users.currentIndex()
        self.tid = self.id[ind]
        print(self.tid)
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                database="collegeattend",
                passwd=""
            )
            mycursor = mydb.cursor()
            mycursor.execute("select subject1,subject2,subject3,subject4,subject5,subject6,subject7 from subjectteacher where teacherid = '"+ str(self.id[ind]) +"'")
            myresult = mycursor.fetchone()
            if myresult is None:
                print("object blank ")
                pass
            else:
                for row in myresult:
                    if row is not  None:
                        subList.append(str(row))

                self.AllocatedSubject.addItems(subList)
                self.AllocatedSubject.show()
                self.Add.show()
                self.Remove.show()
        except Error as e:
            print(e)



    def OnAddButton(self):
        if self.SubjecBeAlloted.selectedItems():
            text = self.SubjecBeAlloted.currentItem().text()
            add = self.SubjecBeAlloted.selectedItems()
            if not add: return
            for item in add:
                self.SubjecBeAlloted.takeItem(self.SubjecBeAlloted.row(item))
            if self.AllocatedSubject.count() < 7:
                self.AllocatedSubject.addItem(str(text))
                self.Allot.show()
            else:
                self.dilog = QtWidgets.QDialog()
                self.dl = Ui_Dialog()
                self.dl.setupUi(self.dilog)
                self.dilog.show()


    def OnRemoveButton(self):
        if self.AllocatedSubject.selectedItems():
            text = self.AllocatedSubject.currentItem().text()
            remv = self.AllocatedSubject.selectedItems()
            if not  remv: return
            for item in remv:
                self.AllocatedSubject.takeItem(self.AllocatedSubject.row(item))
            self.SubjecBeAlloted.addItem(str(text))
            self.Allot.show()

    def OnAllotButton(self):
        items = []
        for index in range(self.AllocatedSubject.count()):
                items.append(self.AllocatedSubject.item(index).text())
        print("all the list member")
        for i in range(len(items)):
            print(items[i])
        stp4 = len(items)
        empty = [None,None,None,None,None,None,None,None]
        items.extend(empty)


        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='collegeattend',
                                                 user='root',
                                                 password='')
            cursor = connection.cursor()
            cursor.execute("UPDATE `subjectteacher` SET `subject1`=%s,`subject2`=%s,`subject3`=%s,`subject4`=%s,`subject5`=%s,`subject6`=%s,`subject7`=%s WHERE `teacherid`=%s",(items[0], items[1], items[2], items[3],items[4], items[5], items[6], self.tid ,))
            connection.commit()
            print("Record inserted successfully into " + str(self.tid) + "table")

        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))


if __name__ == "__main__":
    import sys
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
