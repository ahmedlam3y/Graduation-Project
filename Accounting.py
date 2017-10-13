# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Accounting.ui'
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
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 oblique 12pt \"URW Gothic L\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 oblique 12pt \"URW Gothic L\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 6, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 oblique 12pt \"URW Gothic L\";")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 9, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 oblique 12pt \"URW Gothic L\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setEditable(False)
        self.comboBox.setDuplicatesEnabled(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 7, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 oblique 12pt \"URW Gothic L\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 oblique 12pt \"URW Gothic L\";")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 oblique 12pt \"URW Gothic L\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 4, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 5, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 oblique 12pt \"URW Gothic L\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 9, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 oblique 12pt \"URW Gothic L\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 9, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "Your Cost Now"))
        self.label_6.setText(_translate("Form", "Operation"))
        self.pushButton.setText(_translate("Form", "Change Data"))
        self.label_3.setText(_translate("Form", "Car Color"))
        self.comboBox.setItemText(0, _translate("Form", "Car IN"))
        self.comboBox.setItemText(1, _translate("Form", "Car OUT"))
        self.label_4.setText(_translate("Form", "Time Use"))
        self.label.setText(_translate("Form", "Car Number"))
        self.label_2.setText(_translate("Form", "Car Model"))
        self.pushButton_2.setText(_translate("Form", "Exit"))
        self.pushButton_3.setText(_translate("Form", "OK"))


import image_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

