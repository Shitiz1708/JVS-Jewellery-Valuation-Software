import sys
from PyQt5 import QtWidgets,QtWidgets,QtCore,QtGui
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

class Ui_Selection(QtWidgets.QMainWindow):
    # pressed=''
    def __init__(self,table):
        QtWidgets.QMainWindow.__init__(self)
        # self.pressed=''
        self.setupUi(self)
        self.databaseAccess()
        self.table=table
        self.default()
    
    def databaseAccess(self):
        self.connection = sqlite3.connect("MAINDB.db")
        self.cursor=self.connection.cursor()

    def __del__(self):
        self.connection.commit()
        self.connection.close()
    
    def default(self):
        format_str='''PRAGMA table_info({table});'''
        sql_command=format_str.format(table=self.table)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchall()
        print(res[1][1])
        list1=[]
        c=0
        for i in res:
            list1.append(i[1])
            self.tableWidget.insertColumn(c)
            # self.tableWidget.setHorizontalHeaderItem(c,QTableWidgetItem(i[1]))
            c=c+1
        
        self.tableWidget.setHorizontalHeaderLabels(list1)
        # self.tableWidget.setHorizontalHeaderLabels(str(res[0]))
        format_str='''SELECT * FROM {table}'''
        sql_command=format_str.format(table=self.table)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchall()
        print(res)
        for row_number,row_data in enumerate(res):
            self.tableWidget.insertRow(row_number)
            for col_number,col_data in enumerate(row_data):
                self.tableWidget.setItem(row_number,col_number,QTableWidgetItem(str(col_data)))
    
    def onTableClicked(self):
        text=self.tableWidget.currentItem().text()
        print(text)
        format_str='''UPDATE Popup SET Row='{text}';'''
        sql_command=format_str.format(text=str(text))
        print(sql_command)
        self.cursor.execute(sql_command)
        self.connection.commit()
        self.close()
        # print(self.tableWidget.currentItem().text())
        # self.pressed=self.tableWidget.currentItem().text()
        # self.returnfunction()
        # print("A")
        # print(self.pressed)
    
    # def returnfunction(self):
    #      Ui_Selection.pressed='ABC'

            


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(365, 404)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
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
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 365, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.tableWidget.cellClicked.connect(self.onTableClicked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Search"))

# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     ex = Ui_Selection('Groups')
# #     # w = QtWidgets.QMainWindow()
# #     # print(ex.pressed)
# #     # print(Ui_Selection.pressed)
#     ex.show()
# #     print(Ui_Selection.pressed)

#     # print(ex.pressed)
#     # print(ex.pressed)
#     # w.show()
    # sys.exit(app.exec_())