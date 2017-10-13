"""
some notes

            Powered By Ahmed Ellamey And his Team
    --------------------------------------------------------------
It is the main file
    var used:
        in Clock function:
            int -->  day, hour, mint, sec, q
        in Arduino function:
            global  --> state, t
            int  --> u
        in AcountDataChangeInsert:
            str -->  username, password, carName, carModel, carColor
            sqlite3 -->  connection, result
        in LogInCheck function:
            str  -->  username, password
            Q -->  window, error
            boole -->  x
            sqlite3 -->  connection ,result ,row
        in InsertData function:
            str -->  Name, Password, CarName, CarModel, CarColor, ComfPassword
            boole -->  x1, y1
            sqlite3 -->  connection ,result
            Q -->  window,error

"""


import sys
from PyQt5.QtCore import QSize
from PyQt5 import QtWidgets as Q
from PyQt5.QtGui import QImage, QPalette, QBrush
from SignIN import Ui_Form as SignInForm
from WelFrame import Ui_Form as WelFrameForm
from SignUp import Ui_Form as SignUpForm
from Accounting import Ui_Form as AccountForm
from AccountData import Ui_Form as AccountDataForm
import sqlite3
import time



# UnUsed Clock Function
def clock():
    day = 0
    hour = 0
    mint = 0
    sec = 0
    q = 0
    while q < 10:
        time.sleep(1)
        sec += 1
        if sec == 60:
            mint += 1
            sec = 0
        if mint == 60:
            hour += 1
            mint = 0
        if hour == 24:
            day += 1
            hour = 0
        account.lineEdit_4.setText("{}:{}:{}:{}".format(day, hour, mint, sec))
        q += 1


# UnFinished
# Send Order To Arduino
def Arduino():
    print "Connected To Arduino "
    # it take t and time everyTime
    global State
    if account.comboBox.currentText() == "Car IN":
        if State:
            global t
            t = time.time()
            account.lineEdit_4.setText("Timer Start At: ({})".format(time.asctime()))
            account.lineEdit_5.setText("0")
            State = False
    elif account.comboBox.currentText() == "Car OUT":
        if not State:
            u = int(((time.time()-t)/3600) * 300)
            account.lineEdit_4.setText("0")
            account.lineEdit_5.setText("{} $".format(u))
            State = True
        else:
            account.lineEdit_5.setText("   -----")
            account.lineEdit_4.setText("   -----")


# Finished
# Back From Account Form to Welcome Form
def AccountBack():
    foo(wel, account)
    AcountClear()


# Finished
# Clear Lines In SignUp Form
def SignUpClear():
    signUp.lineEdit.clear()
    signUp.lineEdit_3.clear()
    signUp.lineEdit_2.clear()
    signUp.lineEdit_4.clear()
    signUp.lineEdit_5.clear()
    signUp.lineEdit_6.clear()


# Finished
# Clear Lines In SignIn Form
def SignInClear():
    signIn.lineEdit.clear()
    signIn.lineEdit_2.clear()


# Finished
# Clear Account Lines in Account Form
def AcountClear():
    account.lineEdit.clear()
    account.lineEdit_2.clear()
    account.lineEdit_3.clear()
    account.lineEdit_4.clear()
    account.lineEdit_5.clear()


# Finished
# Used To Set Data In Account Form
def AcountInsert(x2, x3, x4):
    account.lineEdit.setText(x2)
    account.lineEdit_2.setText(x3)
    account.lineEdit_3.setText(x4)


# Islam
# UnFinished
# Unchanged Data In Data Base Work In It
def AcountDataChangeInsert():
    username = str(signIn.lineEdit.text())
    password = str(signIn.lineEdit_2.text())
    carName= str(accountData.lineEdit.Text())
    carModel = str(accountData.lineEdit_2.Text())
    carColor = str(accountData.lineEdit_3.Text())
    connection = sqlite3.connect("SGDataBase.db")

    # start
    result = connection.cursor()
    result.fetchall()
    result.execute("SELECT * FROM Admin WHERE Name = ? AND Password = ?", (username, password))
    if len(result.fetchall()) > 0:
        print result[0]
        result.execute("update Admin set CarName = ? AND CarModel = ? AND CarColor = ?", (carName, carModel, carColor))


# UnFinished
# Used To Show Data At Accout When DataChange Button Clicked
def AcountDataChangeShow(x2, x3, x4):
    accountData.lineEdit.setText(x2)
    accountData.lineEdit_2.setText(x3)
    accountData.lineEdit_3.setText(x4)


# Finished
# Control LogIn Form and Check DataBase
def LogInCheck():
    try:
        username = str(signIn.lineEdit.text())
        password = str(signIn.lineEdit_2.text())
        if username == "":
            raise EOFError
        elif password == "":
            raise EOFError
        else:
            x = False
    except EOFError:
        print("enter userName or Password correctly")
        window = Q.QWidget()
        window.resize(100, 50)
        window.move(500, 400)
        error = Q.QMessageBox.warning(window, "massage", "enter userName or Password correctly")

        x = True
    if not x:
        connection = sqlite3.connect("SGDataBase.db")
        result = connection.cursor()
        result.execute("SELECT * FROM Admin WHERE Name = ? AND Password = ?", (username, password))
        if len(result.fetchall()) > 0:
            print "User found"
            result.execute("SELECT * FROM Admin WHERE Name = ? AND Password = ?", (username, password))
            AcountClear()
            for row in result:
                AcountInsert(row[2], row[3], row[4])
                AcountDataChangeShow(row[2], row[3], row[4])

            foo(account, signIn)
        else:
            print "User not found"
            window = Q.QWidget()
            window.resize(100, 50)
            window.move(500, 400)
            error = Q.QMessageBox.warning(window, "massage", "The Password or UserName not correct")
    SignInClear()


# Finished
# Insert Data In DataBase
def InsertData():
    try:
        Name = str(signUp.lineEdit.text())
        Password = str(signUp.lineEdit_2.text())
        CarName = str(signUp.lineEdit_4.text())
        CarModel = str(signUp.lineEdit_5.text())
        CarColor = str(signUp.lineEdit_6.text())
        ComfPassword = str(signUp.lineEdit_3.text())
        if Name == "":
            raise EOFError
        elif Password == "":
            raise EOFError
        elif CarName == "":
            raise EOFError
        elif CarModel == "":
            raise EOFError
        elif CarColor == "":
            raise EOFError
        elif ComfPassword == "":
            raise EOFError
        else:
            x1 = False

        connection = sqlite3.connect("SGDataBase.db")
        result = connection.cursor()
        result.execute("SELECT * FROM Admin WHERE Name = ? AND Password = ? ", (Name, Password))
        if len(result.fetchall()) > 0:
            raise Exception
        else:
            y1 = False
    except EOFError:
        print "Enter Data"
        x1 = True
        window = Q.QWidget()
        window.resize(100, 50)
        window.move(500, 400)
        error = Q.QMessageBox.warning(window, "massage", "Plz Enter All Data")
    except Exception:
        print "Same UserName"
        window = Q.QWidget()
        window.resize(100, 50)
        window.move(500, 400)
        error = Q.QMessageBox.warning(window, "massage", "The UserName Used Choose Anther One ")
        y1 = True
    if not x1:
        if not y1:
            connection = sqlite3.connect("SGDataBase.db")
            connection.execute("INSERT INTO Admin(Name ,Password, CarNumber, CarModel, CarColor) VALUES (?, ?, ?, ?, ?)", (Name, Password, CarName, CarModel, CarColor))
            connection.commit()
            connection.close()
            print "Data Insert"
            foo(signIn, signUp)
    SignUpClear()


# Finished
# Create SignIn Frame By call SignInForm.py
class SignIn(Q.QWidget, SignInForm):  # Widget
    def __init__(self, parent=None):
        super(SignIn, self).__init__(parent)
        Q.QWidget.__init__(self, parent)
        self.setupUi(self)
        oImage = QImage("2017.jpg")
        sImage = oImage.scaled(QSize(600, 360))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = WindowRole
        self.setPalette(palette)


# Finished
# Create Welcome Frame By Call WelFrameForm
class WelFrame(Q.QWidget, WelFrameForm):  # MainWindow
    def __init__(self, parent=None):
        Q.QWidget.__init__(self, parent)
        self.setupUi(self)
        oImage = QImage("2017.jpg")
        sImage = oImage.scaled(QSize(600, 360))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = WindowRole
        self.setPalette(palette)
        self.move(300, 200)


# Finished
# Create SignUp Frame By Call SignUpForm
class SignUp(Q.QWidget, SignUpForm):  # Widget
    def __init__(self, parent=None):
        Q.QWidget.__init__(self, parent)
        self.setupUi(self)
        oImage = QImage("2017.jpg")
        sImage = oImage.scaled(QSize(600, 360))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = WindowRole
        self.setPalette(palette)


# Finished
# Create Account Frame By Call AccountForm
class Account(Q.QWidget, AccountForm):  # Widget
    def __init__(self, parent=None):
        Q.QWidget.__init__(self, parent)
        self.setupUi(self)
        oImage = QImage("2017.jpg")
        sImage = oImage.scaled(QSize(600, 360))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = WindowRole
        self.setPalette(palette)


# Finished
# Create Account ChangeData By Call AccountDataForm
class AccountData(Q.QWidget, AccountDataForm):  # Widget
    def __init__(self, parent=None):
        Q.QWidget.__init__(self, parent)
        self.setupUi(self)
        oImage = QImage("2017.jpg")
        sImage = oImage.scaled(QSize(600, 360))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = WindowRole
        self.setPalette(palette)


# Finished
# Function To Open Frame And Closed the other
def foo(w1, w2):
    w1.show()
    w1.move(300, 200)
    w2.hide()


# Main Program  Start Here
if __name__ == '__main__':
    # Create An Application
    app = Q.QApplication(sys.argv)
    wel = WelFrame()
    signIn = SignIn()
    signUp = SignUp()
    account = Account()
    accountData = AccountData()
    # port = '/dev/ttyACM0'
    # arduino = serial.Serial(port, 9600, timeout=5)
    # arduino.flush()
    location = []
    for i in range(30):
        location.append(0)
    wel.pushButton_2.clicked.connect(lambda: foo(signIn, wel))
    wel.pushButton.clicked.connect(lambda: foo(signUp, wel))
    signIn.pushButton_2.clicked.connect(lambda: foo(wel, signIn))
    signIn.pushButton.clicked.connect(LogInCheck)
    signUp.pushButton_2.clicked.connect(lambda: foo(wel, signUp))
    signUp.pushButton.clicked.connect(InsertData)
    account.pushButton_2.clicked.connect(AccountBack)
    State = True
    account.pushButton_3.clicked.connect(Arduino)
    account.pushButton.clicked.connect(lambda: foo(accountData, account))
    accountData.pushButton_2.clicked.connect(lambda: foo(wel, accountData))
    accountData.pushButton_3.clicked.connect(lambda: foo(account, accountData))
    # It Active AccountDataChangeInsert So Not Work Now Until Fn Finish
    # accountData.pushButton.clicked.connect(AcountDataChangeInsert)
    wel.show()
    sys.exit(app.exec_())
