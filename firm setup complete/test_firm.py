import sys
from PyQt5 import QtWidgets,QtWidgets,QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, pyqtSlot
import sqlite3

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

class Ui_Firm_setup(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.databaseAccess()
        self.setupUi(self)
        self.default()
        self.printDB()
    
    def __del__(self):
        self.connection.commit()
        self.connection.close()
    
    def databaseAccess(self):
        self.connection = sqlite3.connect("firm_setup.db")
        self.cursor=self.connection.cursor()
    
    def default(self):
        sql_command='''SELECT * FROM Firms;'''
        self.cursor.execute(sql_command)
        res = self.cursor.fetchall()
        self.tableWidget.clearContents()
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.removeRow(i)
        c=0
        for i in res:
            self.tableWidget.insertRow(c)
            self.tableWidget.setItem(c,0,QTableWidgetItem(i[1]))
            c=c+1
    
    # def tableOnClick(self):

    def printDB(self):
        sql_command='''SELECT * FROM Firms;'''
        self.cursor.execute(sql_command)
        res = self.cursor.fetchall()
        print(res)
    
    # def printRandom(self):
    #     print("jbvuwbvvbwvw")
    #     print(self.tableWidget.currentItem().text())

    def tableClicked(self):
        name=self.tableWidget.currentItem().text()
        format_str='''SELECT * FROM Firms WHERE Firm_Name="{name}";'''
        sql_command=format_str.format(name=name)
        self.cursor.execute(sql_command)
        res = self.cursor.fetchone()
        self.lineEdit_2.setText(str(res[1]))
        self.lineEdit_3.setText(str(res[2]))
        self.lineEdit_4.setText(str(res[3]))
        self.lineEdit_5.setText(str(res[4]))
        self.lineEdit_6.setText(str(res[5]))
        self.lineEdit_7.setText(str(res[6]))
        self.lineEdit_8.setText(str(res[7]))



        
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(575, 431)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.verticalHeader().setVisible(True)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        spacerItem = QtWidgets.QSpacerItem(20, 90, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout_4.setItem(7, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.verticalLayout_3.addLayout(self.formLayout_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 575, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_4.clicked.connect(self.new_btn)
        self.pushButton_3.clicked.connect(self.delete_btn)
        self.pushButton_2.clicked.connect(self.save_btn)
        self.pushButton.clicked.connect(self.cancel_btn)
        self.pushButton_5.clicked.connect(self.search_btn)
        self.tableWidget.itemPressed.connect(self.tableClicked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FIRM SETUP"))
        self.label.setText(_translate("MainWindow", "Search:"))
        self.pushButton_5.setText(_translate("MainWindow", "Search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Firms"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "ADDRESS"))
        self.label_4.setText(_translate("MainWindow", "DESCRIPTION 1"))
        self.label_5.setText(_translate("MainWindow", "DESCRIPTION 2"))
        self.label_6.setText(_translate("MainWindow", "PHONE"))
        self.label_7.setText(_translate("MainWindow", "PHONE 1"))
        self.label_8.setText(_translate("MainWindow", "PHONE 2"))
        self.pushButton_4.setText(_translate("MainWindow", "NEW"))
        self.pushButton_3.setText(_translate("MainWindow", "DELETE"))
        self.pushButton_2.setText(_translate("MainWindow", "SAVE"))
        self.pushButton.setText(_translate("MainWindow", "CLOSE"))

    
    def cancel_btn(self):
        self.close()
    
    def new_btn(self):
        name=self.lineEdit_2.text()
        address=self.lineEdit_3.text()
        description_1=self.lineEdit_4.text()
        description_2=self.lineEdit_5.text()
        phone=self.lineEdit_6.text()
        phone_1=self.lineEdit_7.text()
        phone_2=self.lineEdit_8.text()
        format_str='''SELECT * FROM Firms WHERE Firm_Name="{name}";'''
        sql_command=format_str.format(name=name)
        self.cursor.execute(sql_command)
        res = self.cursor.fetchone()
        print (res)
        if(res is None):
                # QtWidgets.QMessageBox.warning(self, 'Dang it!', 'Password incorrect...')
                # addfirm
                format_str='''INSERT INTO Firms(Firm_Name,Firm_Address,Firm_Description_1,Firm_Description_2,Firm_Phone,Firm_Phone_1,Firm_Phone_2) VALUES("{name}","{address}","{description_1}","{description_2}","{phone}","{phone_1}","{phone_2}");'''
                sql_command=format_str.format(name=name,address=address,description_1=description_1,description_2=description_2,phone=phone,phone_1=phone_1,phone_2=phone_2)
                self.cursor.execute(sql_command)
                QtWidgets.QMessageBox.information(self, 'Success', 'New Firm Created')
                self.default()
                self.clear()
                return
        else:
                QtWidgets.QMessageBox.warning(self, 'Error', 'Firm Already Exists')
                self.close()
    
    def delete_btn(self):
        name=self.lineEdit_2.text()
        address=self.lineEdit_3.text()
        description_1=self.lineEdit_4.text()
        description_2=self.lineEdit_5.text()
        phone=self.lineEdit_6.text()
        phone_1=self.lineEdit_7.text()
        phone_2=self.lineEdit_8.text()
        format_str='''SELECT * FROM Firms WHERE Firm_Name="{name}";'''
        sql_command=format_str.format(name=name)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchone()
        if(res is None):
            QtWidgets.QMessageBox.warning(self, 'Error', 'Firm Does Not Exists')
            self.close()
        else:
            format_str='''DELETE FROM Firms WHERE Firm_Name="{name}";'''
            sql_command=format_str.format(name=name)
            self.cursor.execute(sql_command)
            QtWidgets.QMessageBox.information(self, 'Success', 'Firm Deleted Successfully')
            self.default()
            self.clear()
            return

    def clear(self):
        self.lineEdit_2.setText(str(""))
        self.lineEdit_3.setText(str(""))
        self.lineEdit_4.setText(str(""))
        self.lineEdit_5.setText(str(""))
        self.lineEdit_6.setText(str(""))
        self.lineEdit_7.setText(str(""))
        self.lineEdit_8.setText(str(""))

    
    def save_btn(self):
        name=self.lineEdit_2.text()
        address=self.lineEdit_3.text()
        description_1=self.lineEdit_4.text()
        description_2=self.lineEdit_5.text()
        phone=self.lineEdit_6.text()
        phone_1=self.lineEdit_7.text()
        phone_2=self.lineEdit_8.text()
        format_str='''SELECT * FROM Firms WHERE Firm_Name="{name}";'''
        sql_command=format_str.format(name=name)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchone()
        if(res is None):
            QtWidgets.QMessageBox.warning(self, 'Error', 'Firm Does Not Exists')
            self.close()
        else:
            format_str='''UPDATE Firms SET Firm_Name="{name}",Firm_Address="{address}",Firm_Description_1="{description_1}",Firm_Description_2="{description_2}",Firm_Phone={phone},Firm_Phone_1={phone_1},Firm_Phone_2={phone_2} WHERE Firm_Name="{name}";'''
            sql_command=format_str.format(name=name,address=address,description_1=description_1,description_2=description_2,phone=phone,phone_1=phone_1,phone_2=phone_2)
            self.cursor.execute(sql_command)
            QtWidgets.QMessageBox.information(self, 'Success', 'Firm Updated Successfully')
            self.default()
            self.clear()
            return
    
    def search_btn(self):
        name=self.lineEdit.text()
        format_str='''SELECT * FROM Firms WHERE Firm_Name="{name}";'''
        sql_command=format_str.format(name=name)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchall()
        self.tableWidget.clearContents()
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.removeRow(i)
        c=0
        for i in res:
            self.tableWidget.insertRow(c)
            self.tableWidget.setItem(c,0,QTableWidgetItem(i[1]))
            c=c+1
    
    






if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Firm_setup()
    # w = QtWidgets.QMainWindow()
    ex.show()
    # w.show()
    sys.exit(app.exec_())