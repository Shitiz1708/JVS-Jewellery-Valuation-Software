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
    def __init__(self,parent,table,c=0,columns=[],column='',a=0):
        QtWidgets.QMainWindow.__init__(self)
        self.databaseAccess()
        self.setupUi(self)
        self.parent=parent
        self.table=table
        self.columns=columns
        self.column=column
        self.a=a
        self.c=c
        if(self.c==0 and self.table=='Valuation'):
            self.ValuationDefault()
        elif(self.c==0 and self.table=='Auto_Valuation'):
            self.ExpertDefault()
        elif(self.c==0 and self.table=='Rates'):
            self.RatesDefault()
        elif(self.c==0 and self.table=='Valuers'):
            self.ValuerDefault()
        elif(self.c==0):
            self.default()
        else:
            self.CustomerDefault()
    
    def databaseAccess(self):
        self.connection = sqlite3.connect("./dbs/MAINDB.db")
        self.cursor=self.connection.cursor()

    def __del__(self):
        sql_command='''DELETE FROM SearchTable'''
        self.cursor.execute(sql_command)
        self.connection.commit()
        self.connection.close()
    

    def ValuerDefault(self):
        self.columns=['Valuer_id','Valuer Name','Valuer Registration No.']
        c=0
        for i in self.columns:
            self.tableWidget.insertColumn(c)
            c=c+1
        self.tableWidget.setHorizontalHeaderLabels(self.columns)
        format_str='''SELECT * FROM {table}'''
        sql_command=format_str.format(table=self.table)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchall()
        c=0
        self.tableWidget.setRowCount(0)
        for i in res:
            self.tableWidget.insertRow(c)
            self.tableWidget.setItem(c,0,QTableWidgetItem(str(i[0])))
            self.tableWidget.setItem(c,1,QTableWidgetItem(str(i[1])))
            self.tableWidget.setItem(c,2,QTableWidgetItem(str(i[2])))
            
            format_str='''INSERT INTO SearchTable(c1,c2,c3) VALUES("{a1}","{a2}","{a3}");'''
            sql_command=format_str.format(a1=i[1],a2=i[2],a3=i[3])
            self.cursor.execute(sql_command)
            self.connection.commit()
            c=c+1
        self.connection.commit()
    
    def FirmDefault(self):
        self.columns=['Firm Name','Firm Address','Firm Description']
        c=0
        for i in self.columns:
            self.tableWidget.insertColumn(c)
            c=c+1
        self.tableWidget.setHorizontalHeaderLabels(self.columns)
        format_str='''SELECT * FROM {table}'''
        sql_command=format_str.format(table=self.table)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchall()
        c=0
        self.tableWidget.setRowCount(0)
        for i in res:
            self.tableWidget.insertRow(c)
            self.tableWidget.setItem(c,0,QTableWidgetItem(str(i[1])))
            self.tableWidget.setItem(c,1,QTableWidgetItem(str(i[2])))
            self.tableWidget.setItem(c,1,QTableWidgetItem(str(i[3])))
            
            format_str='''INSERT INTO SearchTable(c1,c2,c3) VALUES("{a1}","{a2}","{a3}");'''
            sql_command=format_str.format(a1=i[1],a2=i[2],a3=i[3])
            self.cursor.execute(sql_command)
            c=c+1
        self.connection.commit()

    def ValuationDefault(self):
        self.columns=['Valuation Id','Valuation Date','Customer Name','Customer Address','Grand Total','Gold Total','Silver Total','Stone Total']
        c=0
        for i in self.columns:
            self.tableWidget.insertColumn(c)
            c=c+1
        self.tableWidget.setHorizontalHeaderLabels(self.columns)
        format_str='''SELECT * FROM {table}'''
        sql_command=format_str.format(table=self.table)
        self.cursor.execute(sql_command)
        
        res=self.cursor.fetchall()
        c=0
        self.tableWidget.setRowCount(0)
        for i in res:
            self.tableWidget.insertRow(c)
            self.tableWidget.setItem(c,0,QTableWidgetItem(str(i[0])))
            self.tableWidget.setItem(c,1,QTableWidgetItem((i[1])))
            self.tableWidget.setItem(c,2,QTableWidgetItem(str(i[12])))
            self.tableWidget.setItem(c,3,QTableWidgetItem(str(i[14])))
            self.tableWidget.setItem(c,4,QTableWidgetItem(str(i[29])))
            self.tableWidget.setItem(c,5,QTableWidgetItem(str(i[18])))
            self.tableWidget.setItem(c,6,QTableWidgetItem(str(i[22])))
            self.tableWidget.setItem(c,7,QTableWidgetItem(str(i[26])))
            format_str='''INSERT INTO SearchTable(c1,c2,c3,c4,c5,c6,c7,c8) VALUES("{a1}","{a2}","{a3}","{a4}","{a5}","{a6}","{a7}","{a8}");'''
            sql_command=format_str.format(a1=i[0],a2=i[1],a3=i[12],a4=i[14],a5=i[29],a6=i[18],a7=i[22],a8=i[26])
            self.cursor.execute(sql_command)
            self.connection.commit()
            c=c+1
        self.connection.commit()

    def ExpertDefault(self):
        self.columns=['Valuation Date','Customer Name','Customer Address','Valuation Amount',' Valuation Mode','Gold Total','Silver Total','Stone Total']
        c=0
        for i in self.columns:
            self.tableWidget.insertColumn(c)
            c=c+1
        self.tableWidget.setHorizontalHeaderLabels(self.columns)
        format_str='''SELECT * FROM {table}'''
        sql_command=format_str.format(table=self.table)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchall()
        c=0
        self.tableWidget.setRowCount(0)
        for i in res:
                self.tableWidget.insertRow(c)
                self.tableWidget.setItem(c,0,QTableWidgetItem(str(i[0])))
                self.tableWidget.setItem(c,1,QTableWidgetItem(str(i[1])))
                self.tableWidget.setItem(c,2,QTableWidgetItem(str(i[27])))
                self.tableWidget.setItem(c,3,QTableWidgetItem(str(i[29])))
                self.tableWidget.setItem(c,4,QTableWidgetItem(str(i[9])))
                self.tableWidget.setItem(c,5,QTableWidgetItem(str(i[10])))
                self.tableWidget.setItem(c,6,QTableWidgetItem(str(i[33])))
                self.tableWidget.setItem(c,7,QTableWidgetItem(str(i[37])))
                self.tableWidget.setItem(c,8,QTableWidgetItem(str(i[41])))
                format_str='''INSERT INTO SearchTable(c1,c2,c3,c4,c5,c6,c7,c8,c9) VALUES("{a1}","{a2}","{a3}","{a4}","{a5}","{a6}","{a7}","{a8}","{a9}");'''
                sql_command=format_str.format(a1=i[0],a2=i[1],a3=i[27],a4=i[29],a5=i[9],a6=i[10],a7=i[33],a8=i[37],a9=i[41])
                self.cursor.execute(sql_command)
                self.connection.commit()
                c=c+1

        self.connection.commit()
    

    def RatesDefault(self):
        self.columns=['Rates_Id','Date','Gold','Silver','Platinum','Diamond','Soverign','Coin']
        c=0
        for i in self.columns:
            self.tableWidget.insertColumn(c)
            c=c+1
        self.tableWidget.setHorizontalHeaderLabels(self.columns)
        format_str='''SELECT * FROM {table}'''
        sql_command=format_str.format(table=self.table)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchall()
        c=0
        self.tableWidget.setRowCount(0)
        for i in res:
            self.tableWidget.insertRow(c)
            self.tableWidget.setItem(c,0,QTableWidgetItem(str(i[0])))
            self.tableWidget.setItem(c,1,QTableWidgetItem(str(i[1])))
            self.tableWidget.setItem(c,2,QTableWidgetItem(str(i[3])))
            self.tableWidget.setItem(c,3,QTableWidgetItem(str(i[4])))
            self.tableWidget.setItem(c,4,QTableWidgetItem(str(i[5])))
            self.tableWidget.setItem(c,5,QTableWidgetItem(str(i[6])))
            self.tableWidget.setItem(c,6,QTableWidgetItem(str(i[7])))
            self.tableWidget.setItem(c,7,QTableWidgetItem(str(i[8])))
            self.connection.commit()
            
            format_str='''INSERT INTO SearchTable(c1,c2,c3,c4,c5,c6,c7,c8) VALUES("{a1}","{a2}","{a3}","{a4}","{a5}","{a6}","{a7}","{a8}");'''
            sql_command=format_str.format(a1=i[0],a2=i[1],a3=i[3],a4=i[4],a5=i[5],a6=i[6],a7=i[7],a8=i[8])
            self.cursor.execute(sql_command)
            c=c+1
        self.connection.commit()
    
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
            res=self.cursor.fetchall()
            for row_number,row_data in enumerate(res):
                self.tableWidget.insertRow(row_number)
                for col_number,col_data in enumerate(row_data):
                    self.tableWidget.setItem(row_number,col_number,QTableWidgetItem(str(col_data)))
    

    def search_btn(self):
        search=self.lineEdit.text()
        if(self.table=='Valuation' and self.c==0):
            format_str='''SELECT * FROM {table} WHERE Valuation_date LIKE '%{search}%' OR Valuation_id LIKE '%{search}%' OR Customer_name LIKE '%{search}%' OR Customer_address LIKE '%{search}%' OR Gold_total LIKE '%{search}%' OR Silver_total LIKE '%{search}%' OR Stone_total LIKE '%{search}%' OR Grand_Total LIKE '%{search}%';'''
            sql_command=format_str.format(table=self.table,search=search)
            self.cursor.execute(sql_command)
            
            res=self.cursor.fetchall()
            c=0
            self.tableWidget.setRowCount(0)
            for i in res:
                self.tableWidget.insertRow(c)
                self.tableWidget.setItem(c,0,QTableWidgetItem(str(i[0])))
                self.tableWidget.setItem(c,1,QTableWidgetItem((i[1])))
                self.tableWidget.setItem(c,2,QTableWidgetItem(str(i[12])))
                self.tableWidget.setItem(c,3,QTableWidgetItem(str(i[14])))
                self.tableWidget.setItem(c,4,QTableWidgetItem(str(i[29])))
                self.tableWidget.setItem(c,5,QTableWidgetItem(str(i[18])))
                self.tableWidget.setItem(c,6,QTableWidgetItem(str(i[22])))
                self.tableWidget.setItem(c,7,QTableWidgetItem(str(i[26])))
                c=c+1
        elif(self.table=='Rates'):
            format_str='''SELECT * FROM {table} WHERE Rates_Id LIKE '%{search}%' OR From_Date LIKE '%{search}%' OR Gold LIKE '%{search}%' OR Silver LIKE '%{search}%' OR Platinum LIKE '%{search}%' OR Diamond LIKE '%{search}%' OR Soverign LIKE '%{search}%' OR Coin LIKE '%{search}%';'''
            sql_command=format_str.format(table=self.table,search=search)
            self.cursor.execute(sql_command)
            res=self.cursor.fetchall()
            c=0
            self.tableWidget.setRowCount(0)
            for i in res:
                self.tableWidget.insertRow(c)
                self.tableWidget.setItem(c,0,QTableWidgetItem(str(i[0])))
                self.tableWidget.setItem(c,1,QTableWidgetItem(str(i[1])))
                self.tableWidget.setItem(c,2,QTableWidgetItem(str(i[3])))
                self.tableWidget.setItem(c,3,QTableWidgetItem(str(i[4])))
                self.tableWidget.setItem(c,4,QTableWidgetItem(str(i[5])))
                self.tableWidget.setItem(c,5,QTableWidgetItem(str(i[6])))
                self.tableWidget.setItem(c,6,QTableWidgetItem(str(i[7])))
                self.tableWidget.setItem(c,7,QTableWidgetItem(str(i[8])))
                c=c+1
        elif(self.table=='Auto_Valuation' and self.c==0):
            format_str='''SELECT * FROM {table} WHERE V_Date LIKE '%{search}%' OR Valuation_Amount LIKE '%{search}%' OR Valuation_Mode LIKE '%{search}%' OR Customer_address LIKE '%{search}%' OR Customer_name LIKE '%{search}%' OR G_Total LIKE '%{search}%' OR S_Total LIKE '%{search}%' OR Stone_Total LIKE '%{search}%' OR Grand_Total LIKE '%{search}%';'''
            sql_command=format_str.format(table=self.table,search=search)
            self.cursor.execute(sql_command)
            res=self.cursor.fetchall()
            c=0
            self.tableWidget.setRowCount(0)
            for i in res:
                self.tableWidget.insertRow(c)
                self.tableWidget.setItem(c,0,QTableWidgetItem(str(i[0])))
                self.tableWidget.setItem(c,1,QTableWidgetItem(str(i[1])))
                self.tableWidget.setItem(c,2,QTableWidgetItem(str(i[27])))
                self.tableWidget.setItem(c,3,QTableWidgetItem(str(i[29])))
                self.tableWidget.setItem(c,4,QTableWidgetItem(str(i[9])))
                self.tableWidget.setItem(c,5,QTableWidgetItem(str(i[10])))
                self.tableWidget.setItem(c,6,QTableWidgetItem(str(i[33])))
                self.tableWidget.setItem(c,7,QTableWidgetItem(str(i[37])))
                self.tableWidget.setItem(c,8,QTableWidgetItem(str(i[41])))
                c=c+1
        elif(self.table=='Valuers'):
            format_str='''SELECT * FROM {table} WHERE Valuer_id LIKE '%{search}%' OR Valuer_Name LIKE '%{search}%' OR Valuer_Registration_No LIKE '%{search}%';'''
            sql_command=format_str.format(table=self.table,search=search)
            self.cursor.execute(sql_command)
            res=self.cursor.fetchall()
            c=0
            self.tableWidget.setRowCount(0)
            for i in res:
                self.tableWidget.insertRow(c)
                self.tableWidget.setItem(c,0,QTableWidgetItem(str(i[0])))
                self.tableWidget.setItem(c,1,QTableWidgetItem(str(i[1])))
                self.tableWidget.setItem(c,2,QTableWidgetItem(str(i[2])))
                c=c+1
        elif(self.table=='Firm' ):
            format_str='''SELECT * FROM {table} WHERE Firm_Name LIKE '%{search}%' OR Firm_Address LIKE '%{search}%' OR Firm_Description_1 LIKE '%{search}%';'''
            sql_command=format_str.format(table=self.table)
            self.cursor.execute(sql_command)
            res=self.cursor.fetchall()
            c=0
            self.tableWidget.setRowCount(0)
            for i in res:
                self.tableWidget.insertRow(c)
                self.tableWidget.setItem(c,0,QTableWidgetItem(str(i[1])))
                self.tableWidget.setItem(c,1,QTableWidgetItem(str(i[2])))
                self.tableWidget.setItem(c,1,QTableWidgetItem(str(i[3])))
        else:
            format_str='''SELECT * FROM '{table}' WHERE Customer_name IN (SELECT DISTINCT Customer_name FROM '{table}') AND (Customer_name LIKE "%{search}%" OR Customer_Pan LIKE "%{search}%" OR Customer_address LIKE "%{search}%");'''
            sql_command=format_str.format(table=self.table)
            self.cursor.execute(sql_command)
            res=self.cursor.fetchall()
            c=0
            for i in res:
                self.tableWidget.insertRow(c)
                self.tableWidget.setItem(c,0,QTableWidgetItem(str(i[0])))
                self.tableWidget.setItem(c,1,QTableWidgetItem(str(i[12])))
                self.tableWidget.setItem(c,2,QTableWidgetItem(str(i[13])))
                self.tableWidget.setItem(c,3,QTableWidgetItem(str(i[14])))
                c=c+1


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
        self.pushButton.setFocus()
        self.tableWidget.cellDoubleClicked.connect(self.onTableClicked)
        self.pushButton.clicked.connect(self.search_btn)
        self.lineEdit.cursorPositionChanged.connect(self.search_btn)

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
    sys.exit(app.exec_())