# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WelFrame.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 360)
        Form.setStyleSheet("background-image: url(:/new/prefix1/2017.jpg);")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 290, 75, 31))
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 oblique 12pt \"URW Gothic L\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 290, 75, 31))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 oblique 12pt \"URW Gothic L\";")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 40, 458, 34))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 22pt \"DejaVu Serif\";\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(460, 330, 131, 20))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 italic 10pt \"URW Chancery L\";")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "Sign In"))
        self.pushButton.setText(_translate("Form", "Sign Up"))
        self.label.setText(_translate("Form", "Welcome To Our Smart Garage"))
        self.label_2.setText(_translate("Form", "Power By AIET Students"))


import image_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

