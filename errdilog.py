# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'errordilog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(509, 122)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        self.ErrorMessg = QtWidgets.QLabel(Dialog)
        self.ErrorMessg.setGeometry(QtCore.QRect(20, 50, 371, 21))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.ErrorMessg.setFont(font)
        self.ErrorMessg.setObjectName("ErrorMessg")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)




    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ErrorMessg.setText(_translate("Dialog", "Incorrect UserName or Password"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
