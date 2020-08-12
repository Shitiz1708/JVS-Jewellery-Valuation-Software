import sys
from PyQt5 import QtWidgets,QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtGui import QKeySequence
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
    def __init__(self,parent,table,c=0,columns=[],column='',a=0):
        QtWidgets.QMainWindow.__init__(self)
        # self.pressed=''
        self.databaseAccess()
        self.setupUi(self)
        self.parent=parent
        self.table=table
        self.columns=columns
        self.column=column
        self.a=a
        self.c=c
        if(self.c==0):
            self.default()
        else:
            self.CustomerDefault()
    
    def databaseAccess(self):
        self.connection = sqlite3.connect("MAINDB.db")
        self.cursor=self.connection.cursor()

    def __del__(self):
        self.connection.commit()
        self.connection.close()
    
    def CustomerDefault(self):
        headerlist=['Id','Customer Name','Customer Pan No.','Customer Address']
        c=0
        for i in headerlist:
            self.tableWidget.insertColumn(c)
            c=c+1
                    
        self.tableWidget.setHorizontalHeaderLabels(headerlist)
        format_str='''SELECT * FROM '{table}' WHERE Customer_name IN (SELECT DISTINCT Customer_name FROM '{table}');'''
        sql_command=format_str.format(table=self.table)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchall()
        print(res)
        c=0
        for i in res:
            self.tableWidget.insertRow(c)
            self.tableWidget.setItem(c,0,QTableWidgetItem(str(i[0])))
            self.tableWidget.setItem(c,1,QTableWidgetItem(str(i[12])))
            self.tableWidget.setItem(c,2,QTableWidgetItem(str(i[13])))
            self.tableWidget.setItem(c,3,QTableWidgetItem(str(i[14])))
            c=c+1

    
    def default(self):
        if(self.columns==[]):
            format_str='''PRAGMA table_info({table});'''
            sql_command=format_str.format(table=self.table)
            self.cursor.execute(sql_command)
            res=self.cursor.fetchall()
            list1=[]
            c=0
            for i in res:
                list1.append(i[1])
                self.tableWidget.insertColumn(c)
                c=c+1
            
            self.tableWidget.setHorizontalHeaderLabels(list1)
        
        else:
            c=0
            for i in self.columns:
                self.tableWidget.insertColumn(c)
                c=c+1
            self.tableWidget.setHorizontalHeaderLabels(self.columns)

        if(self.a==0):
            format_str='''SELECT * FROM {table}'''
            sql_command=format_str.format(table=self.table)
            self.cursor.execute(sql_command)
            res=self.cursor.fetchall()
            for row_number,row_data in enumerate(res):
                self.tableWidget.insertRow(row_number)
                for col_number,col_data in enumerate(row_data):
                    self.tableWidget.setItem(row_number,col_number,QTableWidgetItem(str(col_data)))
        else:
            format_str='''SELECT * FROM {table} WHERE {column}='{data}';'''
            sql_command=format_str.format(table=self.table,column=self.column,data=self.a)
            self.cursor.execute(sql_command)
            print(sql_command)
            res=self.cursor.fetchall()
            for row_number,row_data in enumerate(res):
                self.tableWidget.insertRow(row_number)
                for col_number,col_data in enumerate(row_data):
                    self.tableWidget.setItem(row_number,col_number,QTableWidgetItem(str(col_data)))


            
            


    
    # def default(self):
    #     if(self.c==1):
    #         header=['Customer_Name','Customer_Pan','Customer_Address']
    #         c=0
    #         for i in header:
    #             self.tableWidget.insertColumn(c)
    #             c=c+1
    #         self.tableWidget.setHorizontalHeaderLabels(header)
    #         format_str='''SELECT Customer_name,Customer_Pan,Customer_address FROM {table}'''
    #         sql_command=format_str.format(table=self.table)
    #         self.cursor.execute(sql_command)
    #         res=self.cursor.fetchall()
    #         for row_number,row_data in enumerate(res):
    #             self.tableWidget.insertRow(row_number)
    #             for col_number,col_data in enumerate(row_data):
    #                 self.tableWidget.setItem(row_number,col_number,QTableWidgetItem(str(col_data)))
        
    #     else:
    #         format_str='''PRAGMA table_info({table});'''
    #         sql_command=format_str.format(table=self.table)
    #         self.cursor.execute(sql_command)
    #         res=self.cursor.fetchall()
    #         print(res[1][1])
    #         list1=[]
    #         c=0
    #         for i in res:
    #             list1.append(i[1])
    #             self.tableWidget.insertColumn(c)
    #             # self.tableWidget.setHorizontalHeaderItem(c,QTableWidgetItem(i[1]))
    #             c=c+1
            
    #         self.tableWidget.setHorizontalHeaderLabels(list1)
    #         # self.tableWidget.setHorizontalHeaderLabels(str(res[0]))
    #         format_str='''SELECT * FROM {table}'''
    #         sql_command=format_str.format(table=self.table)
    #         self.cursor.execute(sql_command)
    #         res=self.cursor.fetchall()
    #         for row_number,row_data in enumerate(res):
    #             self.tableWidget.insertRow(row_number)
    #             for col_number,col_data in enumerate(row_data):
    #                 self.tableWidget.setItem(row_number,col_number,QTableWidgetItem(str(col_data)))
    
    def onTableClicked(self):
        print("xdgfhgfcdxgrsdcfvghfdgs")
        # print(text)
        print(self.tableWidget.currentRow())
        name=self.tableWidget.item(self.tableWidget.currentRow(),0).text()
        print(name)
        format_str='''UPDATE Popup SET Row='{text}';'''
        sql_command=format_str.format(text=name)
        print(sql_command)
        self.cursor.execute(sql_command)
        self.connection.commit()
        if((self.table=='Valuation' or self.table=='Auto_Valuation')and self.c==0):
            print("BEJFNCECNUCD JBCDJVC")
            self.parent.ReturnValuation()
        elif(self.table=='Firms'):
            self.parent.ReturnFirm()
        elif(self.table=='Valuers'):
            self.parent.ReturnValuers()
        elif((self.table=="Valuation" or self.table=='Auto_Valuation') and self.c==1):
            self.parent.ReturnCustomer()
        elif(self.table=='Rates'):
            self.parent.ReturnRate()
        self.close()
        # print(self.tableWidget.currentItem().text())
        # self.pressed=self.tableWidget.currentItem().text()
        # self.returnfunction()
        # print("A")
        # print(self.pressed)
    
    # def returnfunction(self):
    #      Ui_Selection.pressed='ABC'


    def search_btn(self):
        if(self.c==0):
            text=self.lineEdit.text()
            # format_str='''SELECT * FROM {table} 
            


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(403, 395)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setGeometry(500,150,403,395)
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
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(QtCore.Qt.DashLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 403, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.tableWidget.cellDoubleClicked.connect(self.onTableClicked)
        self.pushButton.clicked.connect(self.search_btn)
        self.lineEdit.returnPressed.connect(self.search_btn)
        self.shortcut1 = QShortcut(QKeySequence(QtCore.Qt.Key_Escape), self)
        self.shortcut1.activated.connect(self.close)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Search"))
        self.pushButton.setText(_translate("MainWindow", "Search"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Selection('Groups')
#     # w = QtWidgets.QMainWindow()
#     # print(ex.pressed)
#     # print(Ui_Selection.pressed)
    ex.show()
#     print(Ui_Selection.pressed)

#     # print(ex.pressed)
#     # print(ex.pressed)
#     # w.show()
    sys.exit(app.exec_())