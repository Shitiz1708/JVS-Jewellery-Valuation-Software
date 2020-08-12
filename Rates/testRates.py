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

class Ui_Rates(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.databaseAccess()
        self.setupUi(self)
        self.default()
        self.printDB()
        # self.databaseAccess()
    
    def __del__(self):
        self.connection.commit()
        self.connection.close()
    
    def databaseAccess(self):
        self.connection = sqlite3.connect("Rates.db")
        self.cursor=self.connection.cursor()
    
    def default(self):
        sql_command='''SELECT * FROM Rates;'''
        self.cursor.execute(sql_command)
        res = self.cursor.fetchall()
        self.tableWidget.clearContents()
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.removeRow(i)
        c=0
        for i in res:
            self.tableWidget.insertRow(c)
            self.tableWidget.setItem(c,0,QTableWidgetItem(i[1]))
            self.tableWidget.setItem(c,1,QTableWidgetItem(str(i[3])))
            self.tableWidget.setItem(c,2,QTableWidgetItem(str(i[4])))
            self.tableWidget.setItem(c,3,QTableWidgetItem(str(i[5])))
            self.tableWidget.setItem(c,4,QTableWidgetItem(str(i[6])))
            self.tableWidget.setItem(c,5,QTableWidgetItem(str(i[7])))
            self.tableWidget.setItem(c,6,QTableWidgetItem(str(i[8])))
            c=c+1
        
        sql_command='''SELECT From_Date FROM Rates;'''
        self.cursor.execute(sql_command)
        res = self.cursor.fetchall()
        print(res)
        for i in res:
            self.comboBox.addItem(i[0])
    
    # def tableOnClick(self):

    def printDB(self):
        sql_command='''SELECT * FROM Rates;'''
        self.cursor.execute(sql_command)
        res = self.cursor.fetchall()
        print(res)
    
    # def printRandom(self):
    #     print("jbvuwbvvbwvw")
    #     print(self.tableWidget.currentItem().text())

    def tableClicked(self):
        name=self.tableWidget.currentItem().text()
        print(name)
        format_str='''SELECT * FROM Rates WHERE From_Date="{name}";'''
        sql_command=format_str.format(name=name)
        self.cursor.execute(sql_command)
        res = self.cursor.fetchone()
        self.lineEdit_2.setText(str(res[3]))
        self.lineEdit_7.setText(str(res[4]))
        self.lineEdit_6.setText(str(res[5]))
        self.lineEdit_3.setText(str(res[6]))
        self.lineEdit_5.setText(str(res[7]))
        self.lineEdit_4.setText(str(res[8]))
    
    
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(626, 469)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_6.addWidget(self.lineEdit_7)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_5.addWidget(self.lineEdit_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_4.addWidget(self.lineEdit_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_3.addWidget(self.lineEdit_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_3.addWidget(self.lineEdit_8)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.verticalLayout_7.addWidget(self.tableWidget)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 626, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.new_btn)
        self.pushButton_2.clicked.connect(self.delete_btn)
        self.pushButton_3.clicked.connect(self.save_btn)
        self.pushButton_4.clicked.connect(self.cancel_btn)
        self.tableWidget.cellClicked.connect(self.tableClicked)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Date"))
        self.label_4.setText(_translate("MainWindow", "Gold(10 grams)"))
        self.label_8.setText(_translate("MainWindow", "Silver(1 kg)"))
        self.label_7.setText(_translate("MainWindow", "Platinum"))
        self.label_3.setText(_translate("MainWindow", "Diamond"))
        self.label_6.setText(_translate("MainWindow", "Soverign"))
        self.label_5.setText(_translate("MainWindow", "Coin"))
        self.label_2.setText(_translate("MainWindow", "Search"))
        self.pushButton_5.setText(_translate("MainWindow", "Search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Gold"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Platinum"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Silver"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Soverign"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Coin"))
        self.pushButton.setText(_translate("MainWindow", "New"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete"))
        self.pushButton_3.setText(_translate("MainWindow", "Save"))
        self.pushButton_4.setText(_translate("MainWindow", "Close"))
    
    def cancel_btn(self):
        self.close()
    
    def new_btn(self):
        from_date = self.comboBox.lineEdit().text()
        to_date=self.comboBox.lineEdit().text()
        gold=self.lineEdit_2.text()
        silver=self.lineEdit_7.text()
        platinum=self.lineEdit_6.text()
        diamond=self.lineEdit_3.text()
        soverign=self.lineEdit_5.text()
        coin=self.lineEdit_4.text()
        format_str='''INSERT INTO Rates(From_Date,to_Date,Gold,Silver,Platinum,Diamond,Soverign,Coin) VALUES("{from_date}","{to_date}",{gold},{silver},{platinum},{diamond},{soverign},{coin});'''
        sql_command=format_str.format(from_date=from_date,to_date=to_date,gold=gold,silver=silver,platinum=platinum,diamond=diamond,soverign=soverign,coin=coin)
        self.cursor.execute(sql_command)
        QtWidgets.QMessageBox.information(self, 'Success', 'Rates Created Successfully')
        self.default()
        return
    
    def delete_btn(self):
        from_date = self.comboBox.lineEdit().text()
        to_date=self.comboBox.lineEdit().text()
        gold=self.lineEdit_2.text()
        silver=self.lineEdit_7.text()
        platinum=self.lineEdit_6.text()
        diamond=self.lineEdit_3.text()
        soverign=self.lineEdit_5.text()
        coin=self.lineEdit_4.text()
        format_str='''SELECT * FROM Rates WHERE From_Date="{from_date}";'''
        sql_command=format_str.format(from_date=from_date)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchone()
        if(res is None):
            QtWidgets.QMessageBox.warning(self, 'Error', 'Rates Does Not Exists')
            self.close()
        else:
            format_str='''DELETE FROM Rates WHERE From_Date="{from_date}";'''
            sql_command=format_str.format(from_date=from_date)
            self.cursor.execute(sql_command)
            QtWidgets.QMessageBox.information(self, 'Success', 'Rates Deleted Successfully')
            self.default()
            return
    
    def save_btn(self):
        from_date = self.comboBox.lineEdit().text()
        to_date=self.comboBox.lineEdit().text()
        gold=self.lineEdit_2.text()
        silver=self.lineEdit_7.text()
        platinum=self.lineEdit_6.text()
        diamond=self.lineEdit_3.text()
        soverign=self.lineEdit_5.text()
        coin=self.lineEdit_4.text()
        format_str='''SELECT * FROM Rates WHERE From_Date="{from_date}";'''
        sql_command=format_str.format(from_date=from_date)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchone()
        if(res is None):
            QtWidgets.QMessageBox.warning(self, 'Error', 'Rates Does Not Exists')
            self.close()
        else:
            format_str='''UPDATE Rates SET From_Date="{from_date}",To_Date="{to_date}",Gold={gold},Silver={silver},Platinum={platinum},Diamond={diamond},Soverign={soverign},Coin={coin} WHERE From_Date={from_date};'''
            sql_command=format_str.format(from_date=from_date,to_date=to_date,gold=gold,silver=silver,platinum=platinum,diamond=diamond,soverign=soverign,coin=coin)
            self.cursor.execute(sql_command)
            self.default()
            return
    
    def search_btn(self):
        search=self.lineEdit_8.text()
        format_str='''SELECT * FROM Rates WHERE From_Date="{search}" OR To_Date="{search}" OR Gold={search} OR Silver={search} OR Platinum={search} OR Diamond={search} OR Soverign={search} OR Coin={search};'''
        sql_command=format_str.format(search=search)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchall()
        self.tableWidget.clearContents()
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.removeRow(i)
        c=0
        for i in res:
            self.tableWidget.insertRow(c)
            self.tableWidget.setItem(c,0,QTableWidgetItem(i[1]))
            self.tableWidget.setItem(c,1,QTableWidgetItem(i[3]))
            self.tableWidget.setItem(c,2,QTableWidgetItem(i[4]))
            self.tableWidget.setItem(c,3,QTableWidgetItem(i[5]))
            self.tableWidget.setItem(c,4,QTableWidgetItem(i[6]))
            self.tableWidget.setItem(c,5,QTableWidgetItem(i[7]))
            self.tableWidget.setItem(c,6,QTableWidgetItem(i[8]))
            c=c+1

    






if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Rates()
    # w = QtWidgets.QMainWindow()
    ex.show()
    # w.show()
    sys.exit(app.exec_())