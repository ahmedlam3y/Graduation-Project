
'''''
from PyQt5 import QtGui, QtWidgets
from PyQt5.uic.properties import QtCore
from SignIN import Ui_Form as SignInForm
from WelFrame import Ui_Form as WelFrameForm
from SignUp import Ui_Form as SignUpForm
from Accounting import Ui_Form as AccountForm

class MainWindow1(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow1, self).__init__(*args, **kwargs)

        self.pushButton = QtWidgets.QPushButton('pushButton')
        self.pushButton.released.connect(self.callSecondWindow)
        self.WelFramWindow = WelFrame()
        self.WelFramWindow.pushButton.released.connect(self.callSignIn)
        self.SignInWindow = SignIn()
        self.setCentralWidget(self.pushButton)

    def callSecondWindow(self):
        self.WelFramWindow.show()

    def callSignIn( self ):
        self.SignInWindow.show()

class SignIn(QtWidgets.QMainWindow, SignInForm):
    def __init__(self, parent=None):
        super(SignIn, self).__init__(parent)
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)




class WelFrame(QtWidgets.QMainWindow, WelFrameForm):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)



class SignUp(QtWidgets.QWidget, SignUpForm):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)


class Accout(QtWidgets.QWidget, AccountForm):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow1()
    mainWindow.show()
    sys.exit(app.exec_())


'''


'''
import sqlite3

connection = sqlite3.connect("SGDataBase.db")
result = connection.execute("SELECT * FROM Admin ")
for row in result:
    print row


if Name == "":
    print "Enter The Name"
elif Password == "":
    print "Enter The Password"
elif CarName == "":
    print "Enter The CarName"
elif CarModel == "":
    print "Enter The CarModel"
elif CarColor == "":
    print "Enter The CarColor"
else:
    x = False
AcountInsert(row["Name"], row["Password"], row["CarNumber"], row["CarModel"],
             row["CarColor"])
result.execute("SELECT * FROM Admin")
for row in result:
    AcountInsert(row[0], row[1], row[2], row[3],
                 row[4])
    '''
