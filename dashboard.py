# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dassh.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dash(object):
    def setupUi(self, dash):
        dash.setObjectName("dash")
        dash.setWindowModality(QtCore.Qt.ApplicationModal)
        dash.resize(802, 572)
        dash.setAutoFillBackground(False)
        self.logo = QtWidgets.QLabel(dash)
        self.logo.setGeometry(QtCore.QRect(350, 50, 91, 81))
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.semester = QtWidgets.QComboBox(dash)
        self.semester.setGeometry(QtCore.QRect(330, 210, 131, 21))
        self.semester.setObjectName("semester")
        self.semester.addItem("")
        self.semester.addItem("")
        self.semester.addItem("")
        self.semester.addItem("")
        self.semester.addItem("")
        self.semester.addItem("")
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
        QtCore.QMetaObject.connectSlotsByName(dash)

        self.takeA.clicked.connect(self.TakeAt)
        self.updateA.clicked.connect(self.UpdateAt)

    def retranslateUi(self, dash):
        _translate = QtCore.QCoreApplication.translate
        dash.setWindowTitle(_translate("dash", "Dashboard"))
        self.semester.setItemText(0, _translate("dash", "MCA 1"))
        self.semester.setItemText(1, _translate("dash", "MCA 2"))
        self.semester.setItemText(2, _translate("dash", "MCA 3"))
        self.semester.setItemText(3, _translate("dash", "MCA 4"))
        self.semester.setItemText(4, _translate("dash", "MCA 5"))
        self.semester.setItemText(5, _translate("dash", "MCA 6"))
        self.label.setText(_translate("dash", "Select Semester"))
        self.takeA.setText(_translate("dash", "Take Attendance"))
        self.updateA.setText(_translate("dash", "Update Attendance"))

    def TakeAt(self):
        semes = self.semester.currentText()
        print(semes)


    def UpdateAt(self):
        seme = self.semester.currentText()
        print(seme)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dash = QtWidgets.QWidget()
    ui = Ui_dash()
    ui.setupUi(dash)
    dash.show()
    sys.exit(app.exec_())
