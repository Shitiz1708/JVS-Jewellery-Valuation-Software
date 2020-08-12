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

class Ui_Groups(QtWidgets.QMainWindow):
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
        self.connection = sqlite3.connect("Groups.db")
        self.cursor=self.connection.cursor()
    
    def default(self):
        sql_command='''SELECT * FROM Groups;'''
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
        sql_command='''SELECT DISTINCT Group_Type FROM Groups;'''
        self.cursor.execute(sql_command)
        res = self.cursor.fetchall()
        print(res)
        for i in res:
            self.comboBox.addItem(i[0])
    
    # def tableOnClick(self):

    def printDB(self):
        sql_command='''SELECT * FROM Groups;'''
        self.cursor.execute(sql_command)
        res = self.cursor.fetchall()
        print(res)
    
    def tableClicked(self):
        name=self.tableWidget.currentItem().text()
        format_str='''SELECT * FROM Groups WHERE Group_Name="{name}";'''
        sql_command=format_str.format(name=name)
        self.cursor.execute(sql_command)
        res = self.cursor.fetchone()
        self.lineEdit_2.setText(str(res[1]))
        self.comboBox.lineEdit().setText(str(res[2]))
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(588, 485)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 300, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_5.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_5.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_5.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_5.addWidget(self.pushButton_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 588, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_5.clicked.connect(self.new_btn)
        self.pushButton_6.clicked.connect(self.delete_btn)
        self.pushButton_7.clicked.connect(self.save_btn)
        self.pushButton_8.clicked.connect(self.cancel_btn)
        self.pushButton.clicked.connect(self.search_btn)
        self.tableWidget.itemPressed.connect(self.tableClicked)
        self.lineEdit.returnPressed.connect(self.search_btn)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Search"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Groups"))
        self.label_2.setText(_translate("MainWindow", "Group Name"))
        self.label_3.setText(_translate("MainWindow", "Group Type"))
        self.pushButton_5.setText(_translate("MainWindow", "NEW"))
        self.pushButton_6.setText(_translate("MainWindow", "DELETE"))
        self.pushButton_7.setText(_translate("MainWindow", "SAVE"))
        self.pushButton_8.setText(_translate("MainWindow", "CLOSE"))
    
    def cancel_btn(self):
        self.close()
    
    def new_btn(self):
        group_name=self.lineEdit_2.text()
        group_type=self.comboBox.lineEdit().text()
        format_str='''SELECT * FROM Groups WHERE Group_Name="{name}";'''
        sql_command=format_str.format(name=group_name)
        self.cursor.execute(sql_command)
        res = self.cursor.fetchone()
        print (res)
        if(res is None):
                # QtWidgets.QMessageBox.warning(self, 'Dang it!', 'Password incorrect...')
                # addfirm
                format_str='''INSERT INTO Groups(Group_Name,Group_Type) VALUES("{name}","{type}");'''
                sql_command=format_str.format(name=group_name,type=group_type)
                self.cursor.execute(sql_command)
                QtWidgets.QMessageBox.information(self, 'Success', 'New Group Created')
                self.connection.commit()
                self.default()
                self.clear()
                return
        else:
                QtWidgets.QMessageBox.warning(self, 'Error', 'Group Already Exists')
                self.close()
    
    def delete_btn(self):
        group_name=self.lineEdit_2.text()
        group_type=self.comboBox.lineEdit().text()
        format_str='''SELECT * FROM Groups WHERE Group_Name="{name}";'''
        sql_command=format_str.format(name=group_name)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchone()
        if(res is None):
            QtWidgets.QMessageBox.warning(self, 'Error', 'Group Does Not Exists')
            self.close()
        else:
            format_str='''DELETE FROM Groups WHERE Group_Name="{name}";'''
            sql_command=format_str.format(name=group_name)
            self.cursor.execute(sql_command)
            QtWidgets.QMessageBox.information(self, 'Success', 'Group Deleted Successfully')
            self.default()
            self.clear()
            return

    def clear(self):
        self.lineEdit_2.setText(str(""))
        self.comboBox.lineEdit().setText(str(""))


    
    def save_btn(self):
        group_name=self.lineEdit_2.text()
        group_type=self.comboBox.lineEdit().text()
        format_str='''SELECT * FROM Groups WHERE Group_Name="{name}";'''
        sql_command=format_str.format(name=group_name)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchone()
        if(res is None):
            QtWidgets.QMessageBox.warning(self, 'Error', 'Group Does Not Exists')
            self.close()
        else:
            format_str='''UPDATE Groups SET Group_Name="{name}",Group_Type="{type}" WHERE Group_Name="{name}";'''
            sql_command=format_str.format(name=group_name,type=group_type)
            self.cursor.execute(sql_command)
            QtWidgets.QMessageBox.information(self, 'Success', 'Group Updated Successfully')
            self.default()
            self.clear()
            return
    
    def search_btn(self):
        group_name=self.lineEdit.text()
        format_str='''SELECT * FROM Groups WHERE Group_Name="{name}";'''
        sql_command=format_str.format(name=group_name)
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
    ex = Ui_Groups()
    # w = QtWidgets.QMainWindow()
    ex.show()
    # w.show()
    sys.exit(app.exec_())