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

class Ui_Valuer_setup(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.databaseAccess()
        self.setupUi(self)
        self.default()
        self.printDB()
    
    def __del__(self):
        self.connection.commit()
        self.connection.close()

    def printDB(self):
        sql_command='''SELECT * FROM Valuers;'''
        self.cursor.execute(sql_command)
        res = self.cursor.fetchall()
        print(res)
    
    def databaseAccess(self):
        self.connection = sqlite3.connect("Valuer_setup.db")
        self.cursor=self.connection.cursor()

    def default(self):
        sql_command='''SELECT * FROM Valuers;'''
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
    
    def tableClicked(self):
        name=self.tableWidget.currentItem().text()
        format_str='''SELECT * FROM Valuers WHERE Valuer_Name="{name}";'''
        sql_command=format_str.format(name=name)
        self.cursor.execute(sql_command)
        res = self.cursor.fetchone()
        self.lineEdit.setText(str(res[1]))
        self.lineEdit_2.setText(str(res[2]))
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(674, 567)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(300)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
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
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 400, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 674, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_3.clicked.connect(self.new_btn)
        self.pushButton_2.clicked.connect(self.delete_btn)
        self.pushButton.clicked.connect(self.save_btn)
        self.pushButton_4.clicked.connect(self.cancel_btn)
        self.tableWidget.itemPressed.connect(self.tableClicked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Search:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Valuers"))
        self.label.setText(_translate("MainWindow", "Name:"))
        self.label_2.setText(_translate("MainWindow", "Registration No."))
        self.pushButton_3.setText(_translate("MainWindow", "New"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.pushButton_4.setText(_translate("MainWindow", "Close"))

    
    def cancel_btn(self):
        self.close()
    
    def new_btn(self):
        name=self.lineEdit.text()
        registration_no=self.lineEdit_2.text()
        format_str='''SELECT * FROM Valuers WHERE Valuer_Name="{name}";'''
        sql_command=format_str.format(name=name)
        self.cursor.execute(sql_command)
        res = self.cursor.fetchone()
        print (res)
        if(res is None):
                # QtWidgets.QMessageBox.warning(self, 'Dang it!', 'Password incorrect...')
                # addfirm
                format_str='''INSERT INTO Valuers (Valuer_Name,Valuer_Registration_No) VALUES("{name}",{registration_no});'''
                sql_command=format_str.format(name=name,registration_no=registration_no)
                self.cursor.execute(sql_command)
                QtWidgets.QMessageBox.information(self, 'Success', 'Valuer Created Successfully')
                self.default()
                self.clear()
                return
        else:
                QtWidgets.QMessageBox.warning(self, 'Error', 'Valuer Already Exists')
                self.close()
    
    def clear(self):
        self.lineEdit.setText(str(""))
        self.lineEdit_2.setText(str(""))
    
    def delete_btn(self):
        name=self.lineEdit.text()
        registration_no=self.lineEdit_2.text()
        format_str='''SELECT * FROM Valuers WHERE Valuer_Name="{name}";'''
        sql_command=format_str.format(name=name)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchone()
        if(res is None):
            QtWidgets.QMessageBox.warning(self, 'Error', 'Valuer Does Not Exists')
            self.close()
        else:
            format_str='''DELETE FROM Valuers WHERE Valuer_Name="{name}";'''
            sql_command=format_str.format(name=name)
            self.cursor.execute(sql_command)
            QtWidgets.QMessageBox.information(self, 'Success', 'Valuer Deleted Successfully')
            self.default()
            self.clear()
            return
    
    def save_btn(self):
        name=self.lineEdit.text()
        registration_no=self.lineEdit_2.text()
        format_str='''SELECT * FROM Valuers WHERE Valuer_Name="{name}";'''
        sql_command=format_str.format(name=name)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchone()
        if(res is None):
            QtWidgets.QMessageBox.warning(self, 'Error', 'Valuer Does Not Exists')
            self.close()
        else:
            format_str='''UPDATE Valuers SET Valuer_Name="{name}",Valuer_Registration_No={registration_no};'''
            sql_command=format_str.format(name=name,registration_no=registration_no)
            self.cursor.execute(sql_command)
            QtWidgets.QMessageBox.information(self, 'Success', 'Valuer Updated Successfully')
            self.default()
            self.clear()
            return





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Valuer_setup()
    # w = QtWidgets.QMainWindow()
    ex.show()
    # w.show()
    sys.exit(app.exec_())