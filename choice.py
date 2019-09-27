# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choice.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Attendance(object):
    def setupUi(self, Attendance):
        Attendance.setObjectName("Attendance")
        Attendance.setWindowModality(QtCore.Qt.WindowModal)
        Attendance.resize(815, 583)
        self.logo = QtWidgets.QLabel(Attendance)
        self.logo.setGeometry(QtCore.QRect(350, 170, 91, 71))
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.Heading = QtWidgets.QLabel(Attendance)
        self.Heading.setGeometry(QtCore.QRect(330, 90, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Heading.setFont(font)
        self.Heading.setObjectName("Heading")
        self.OpenCam = QtWidgets.QPushButton(Attendance)
        self.OpenCam.setGeometry(QtCore.QRect(350, 280, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.OpenCam.setFont(font)
        self.OpenCam.setObjectName("OpenCam")
        self.TakeManual = QtWidgets.QPushButton(Attendance)
        self.TakeManual.setGeometry(QtCore.QRect(350, 330, 91, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(True)
        font.setWeight(75)
        self.TakeManual.setFont(font)
        self.TakeManual.setObjectName("TakeManual")

        self.retranslateUi(Attendance)
        QtCore.QMetaObject.connectSlotsByName(Attendance)




    def retranslateUi(self, Attendance):
        _translate = QtCore.QCoreApplication.translate
        Attendance.setWindowTitle(_translate("Attendance", "Attendance"))
        self.Heading.setText(_translate("Attendance", "Take Attendance"))
        self.OpenCam.setText(_translate("Attendance", "Open Camera"))
        self.TakeManual.setText(_translate("Attendance", "Take Manually"))








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Attendance = QtWidgets.QWidget()
    ui = Ui_Attendance()
    ui.setupUi(Attendance)
    Attendance.show()
    sys.exit(app.exec_())
