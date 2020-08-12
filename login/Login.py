import sys
from PyQt5 import QtWidgets,QtWidgets,QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, pyqtSlot
import sqlite3
sys.path.insert(0, '/home/shitiz/Documents/Evaluation Report Software/Valuation Main')
import testValuation
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)    

class UiLogin(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.databaseAccess()
    
    def databaseAccess(self):
        self.connection = sqlite3.connect("testing.db")
        self.cursor=self.connection.cursor()

    def setupUi(self, Login_Dialog):
        Login_Dialog.setObjectName(_fromUtf8("Login_Dialog"))
        Login_Dialog.resize(285, 134)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Login_Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtWidgets.QGroupBox(Login_Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.user_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.user_lineEdit.setObjectName(_fromUtf8("user_lineEdit"))
        self.horizontalLayout.addWidget(self.user_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.password_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.password_lineEdit.setInputMask(_fromUtf8(""))
        self.password_lineEdit.setText(_fromUtf8(""))
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName(_fromUtf8("password_lineEdit"))
        self.horizontalLayout_2.addWidget(self.password_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        # self.newUser_btn = QtWidgets.QPushButton(self.groupBox)
        # self.newUser_btn.setObjectName(_fromUtf8("newUser_btn"))
        # self.newUser_btn.clicked.connect(self.NewUser_btn)
        # self.horizontalLayout_4.addWidget(self.newUser_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.login_btn = QtWidgets.QPushButton(self.groupBox)
        self.login_btn.setObjectName(_fromUtf8("login_btn"))
        self.login_btn.clicked.connect(self.Login_btn)
        self.horizontalLayout_4.addWidget(self.login_btn)
        self.cancel_btn = QtWidgets.QPushButton(self.groupBox)
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.cancel_btn.clicked.connect(self.Cancel_btn)
        self.horizontalLayout_4.addWidget(self.cancel_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Login_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Login_Dialog)

    def retranslateUi(self, Login_Dialog):
        Login_Dialog.setWindowTitle(_translate("Login_Dialog", "TPayne\'s User Login", None))
        self.groupBox.setTitle(_translate("Login_Dialog", "Super Ham!", None))
        self.label.setText(_translate("Login_Dialog", "Username", None))
        self.label_2.setText(_translate("Login_Dialog", "Password", None))
        # self.newUser_btn.setText(_translate("Login_Dialog", "New User", None))
        self.login_btn.setText(_translate("Login_Dialog", "Login", None))
        self.cancel_btn.setText(_translate("Login_Dialog", "Cancel", None))
    
    # @pyqtSlot("on_cancel_btn_clicked()")
    def Cancel_btn(self):
        self.close()


    # @QtCore.pyqtSignature("on_login_btn_clicked()")
    def Login_btn(self):
        username = self.user_lineEdit.text()
        password = self.password_lineEdit.text()
        if not username:
            QtWidgets.QMessageBox.warning(self, 'Guess What?', 'Username Missing!')
        elif not password:
            QtWidgets.QMessageBox.warning(self, 'Guess What?', 'Password Missing!')
        else:
            self.AttemptLogin(username, password)

    def AttemptLogin(self, username, password):
        format_str='''SELECT * FROM Users WHERE Username="{Username}" AND Password="{Password}";'''
        sql_command=format_str.format(Username=username,Password=password)
        self.cursor.execute(sql_command)
        res = self.cursor.fetchone()
        print (res)
        if(res is None):
                QtWidgets.QMessageBox.warning(self, 'Dang it!', 'Password incorrect...')
                return
        else:
                QtWidgets.QMessageBox.information(self, 'BOOYA!', 'Success!!')
                self.valuation=testValuation.Ui_Valuation()
                self.valuation.show()
                self.close()

    # @QtCore.pyqtSignature("on_newUser_btn_clicked()")
    # def NewUser_btn(self):
    #     self.newUser = Ui_Register()
    #     self.newUser.show()
    


# class Ui_Register(QtWidgets.QDialog):
#     def __init__(self):
#         QtWidgets.QDialog.__init__(self)
#         self.setupUi(self)
#         # self.dbu = dbu
#         self.databaseAccess()
    
#     def databaseAccess(self):
#         self.connection = sqlite3.connect("Users.db")
#         self.cursor=self.connection.cursor()
    

#     def setupUi(self, Register_Dialog):
#         Register_Dialog.setObjectName(_fromUtf8("Register_Dialog"))
#         Register_Dialog.resize(372, 187)
#         Register_Dialog.setModal(True)
#         self.verticalLayout_2 = QtWidgets.QVBoxLayout(Register_Dialog)
#         self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
#         self.verticalLayout = QtWidgets.QVBoxLayout()
#         self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
#         self.groupBox = QtWidgets.QGroupBox(Register_Dialog)
#         self.groupBox.setObjectName(_fromUtf8("groupBox"))
#         self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
#         self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
#         self.horizontalLayout = QtWidgets.QHBoxLayout()
#         self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
#         self.label_2 = QtWidgets.QLabel(self.groupBox)
#         self.label_2.setObjectName(_fromUtf8("label_2"))
#         self.horizontalLayout.addWidget(self.label_2)
#         self.username_lineEdit = QtWidgets.QLineEdit(self.groupBox)
#         self.username_lineEdit.setObjectName(_fromUtf8("username_lineEdit"))
#         self.horizontalLayout.addWidget(self.username_lineEdit)
#         self.verticalLayout_3.addLayout(self.horizontalLayout)
#         self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
#         self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
#         self.label = QtWidgets.QLabel(self.groupBox)
#         self.label.setObjectName(_fromUtf8("label"))
#         self.horizontalLayout_2.addWidget(self.label)
#         self.password_lineEdit = QtWidgets.QLineEdit(self.groupBox)
#         self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
#         self.password_lineEdit.setObjectName(_fromUtf8("password_lineEdit"))
#         self.horizontalLayout_2.addWidget(self.password_lineEdit)
#         self.verticalLayout_3.addLayout(self.horizontalLayout_2)
#         self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
#         self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
#         self.label_3 = QtWidgets.QLabel(self.groupBox)
#         self.label_3.setObjectName(_fromUtf8("label_3"))
#         self.horizontalLayout_4.addWidget(self.label_3)
#         self.confirmPassword_lineEdit = QtWidgets.QLineEdit(self.groupBox)
#         self.confirmPassword_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
#         self.confirmPassword_lineEdit.setObjectName(_fromUtf8("confirmPassword_lineEdit"))
#         self.horizontalLayout_4.addWidget(self.confirmPassword_lineEdit)
#         self.verticalLayout_3.addLayout(self.horizontalLayout_4)
#         self.label_4 = QtWidgets.QLabel(self.groupBox)
#         self.label_4.setAlignment(QtCore.Qt.AlignCenter)
#         self.label_4.setObjectName(_fromUtf8("label_4"))
#         self.verticalLayout_3.addWidget(self.label_4)
#         self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
#         self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
#         spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
#         self.horizontalLayout_3.addItem(spacerItem)
#         self.add_btn = QtWidgets.QPushButton(self.groupBox)
#         self.add_btn.setObjectName(_fromUtf8("add_btn"))
#         self.add_btn.clicked.connect(self.Add_btn)
#         self.horizontalLayout_3.addWidget(self.add_btn)
#         self.cancel_btn = QtWidgets.QPushButton(self.groupBox)
#         self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
#         self.add_btn.clicked.connect(self.Cancel_btn)
#         self.horizontalLayout_3.addWidget(self.cancel_btn)
#         self.verticalLayout_3.addLayout(self.horizontalLayout_3)
#         self.verticalLayout.addWidget(self.groupBox)
#         self.verticalLayout_2.addLayout(self.verticalLayout)

#         self.retranslateUi(Register_Dialog)
#         QtCore.QMetaObject.connectSlotsByName(Register_Dialog)

#     def retranslateUi(self, Register_Dialog):
#         Register_Dialog.setWindowTitle(_translate("Register_Dialog", "Register New User", None))
#         self.groupBox.setTitle(_translate("Register_Dialog", "I Love Ham!", None))
#         self.label_2.setText(_translate("Register_Dialog", "Username", None))
#         self.label.setText(_translate("Register_Dialog", "Password", None))
#         self.label_3.setText(_translate("Register_Dialog", "Confirm Password", None))
#         self.label_4.setText(_translate("Register_Dialog", "Not Included: Phone, Address, Social Security Number, Credit Card...", None))
#         self.add_btn.setText(_translate("Register_Dialog", "Add", None))
#         self.cancel_btn.setText(_translate("Register_Dialog", "Cancel", None))


#     # @QtCore.pyqtSignature("on_cancel_btn_clicked()")
#     def Cancel_btn(self):
#         self.close()

#     # @QtCore.pyqtSignature("on_add_btn_clicked()")
#     def Add_btn(self):
#         username = self.username_lineEdit.text()
#         password = self.password_lineEdit.text()
#         cpassword = self.confirmPassword_lineEdit.text()
#         if not username:
#             QtWidgets.QMessageBox.warning(self, 'Dang it!', 'Username Missing')
#         elif password != cpassword:
#             QtWidgets.QMessageBox.warning(self, 'Dang it!', 'Passwords Do Not Match')
#         else:
#             format_str='''SELECT * FROM Users WHERE Username="{Username};'''
#             sql_command=format_str.format(Username=username)
#             self.cursor.execute(sql_command)
#             res = self.cursor.fetchone()
#             if res is None:
#                     # QtWidgets.QMessageBox.warning(self, 'Dang it!', 'Username Taken. :(')
#                     format_str='''INSERT INTO Users values("{Username}","{Password}")'''
#                     sql_command=format_str.format(Username=username,Password=password)
#                     self.cursor.execute(sql_command)
#                     QtWidgets.QMessageBox.information(self, 'Awesome!!', 'User Added SUCCESSFULLY!')
#                     self.close()

#             else:
#                 QtWidgets.QMessageBox.warning(self, 'Dang it!', 'Username Taken. :(')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = UiLogin()
    ex.show()
    sys.exit(app.exec_())
