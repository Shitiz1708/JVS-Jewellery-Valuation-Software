#Save Button Theek Karna hai
#Add button ka function
#Word Document at Valuation Bill


import sys
from PyQt5 import QtWidgets,QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, pyqtSlot
import sqlite3
from docx import Document
from docx.shared import Inches
import Firm
import Groups
import Items
import Rates
import Valuers
import Change_Password
import Products

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

class Ui_Valuation(QtWidgets.QMainWindow):
    val_id=0
    def __init__(self):
        print(Ui_Valuation.val_id)
        QtWidgets.QMainWindow.__init__(self)
        self.databaseAccess()
        self.setupUi(self)
        self.default()
        # self.printDB()
        # self.databaseAccess()

    def default(self):
        sql_command='''SELECT * FROM Rates ;'''
        self.cursor_1.execute(sql_command)
        res=self.cursor_1.fetchall()
        for i in res:
            self.comboBox.addItem(str(i[1]))
        sql_command='''SELECT * FROM Valuation ;'''
        self.cursor.execute(sql_command)
        res=self.cursor.fetchall()
        for i in res:
            self.comboBox_2.addItem(str(i[1]))
        sql_command='''SELECT id FROM Last_Valuation_id ;'''
        self.cursor.execute(sql_command)
        res=self.cursor.fetchone()
        Ui_Valuation.val_id=res[0]
        print(Ui_Valuation.val_id)
    
    def Calculate(self):
        format_str='''SELECT * FROM Products WHERE Valuation_Id={id} AND Metal='Gold' ;'''
        sql_command=format_str.format(id=Ui_Valuation.val_id)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchall()
        print(res)
        quantity=0
        gross=0
        wt=0
        value=0
        for i in res:
            quantity=quantity+i[5]
            gross=gross+i[6]
            wt=wt+i[7]
            value=value+i[8]
        self.lineEdit_17.setText(str(quantity))
        self.lineEdit_19.setText(str(gross))
        self.lineEdit_25.setText(str(wt))
        self.lineEdit_22.setText(str(value))
        format_str='''SELECT * FROM Products WHERE Valuation_Id={id} AND Metal='Silver' ;'''
        sql_command=format_str.format(id=Ui_Valuation.val_id)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchall()
        quantity=0
        gross=0
        wt=0
        value=0
        for i in res:
            quantity=quantity+i[5]
            gross=gross+i[6]
            wt=wt+i[7]
            value=value+i[8]
        self.lineEdit_18.setText(str(quantity))
        self.lineEdit_20.setText(str(gross))
        self.lineEdit_26.setText(str(wt))
        self.lineEdit_23.setText(str(value))
        format_str='''SELECT * FROM Products WHERE Valuation_Id={id} AND Stone='Diamond' ;'''
        sql_command=format_str.format(id=Ui_Valuation.val_id)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchall()
        quantity=0
        gross=0
        # wt=0
        value=0
        for i in res:
            quantity=quantity+i[11]
            gross=gross+i[11]
            # wt=wt+i[7]
            value=value+i[13]
        self.lineEdit_16.setText(str(quantity))
        self.lineEdit_21.setText(str(gross))
        # self.lineEdit_25.setText(str(wt))
        self.lineEdit_24.setText(str(value))

        format_str='''SELECT * FROM Products WHERE Valuation_Id={id} ;'''
        sql_command=format_str.format(id=Ui_Valuation.val_id)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchall()
        # quantity=0
        # gross=0
        # wt=0
        # value=0
        total=0
        for i in res:
            # quantity=quantity+i[5]
            # gross=gross+i[6]
            # wt=wt+i[7]
            # value=value+i[8]
            total=total+i[14]
        self.lineEdit_27.setText(str(total))
        
    def UpdateIndex(self):
        id=Ui_Valuation.val_id+1
        format_str='''UPDATE Last_Valuation_id SET id={id};'''
        sql_command=format_str.format(id=id)
        self.cursor.execute(sql_command)
        
        # self.tableWidget.clearContents()
        # for i in range(self.tableWidget.rowCount()):
        #     self.tableWidget.removeRow(i)
        # c=0
        # for i in res:
            # self.tableWidget.insertRow(c)
            # self.tableWidget.setItem(c,0,QTableWidgetItem(i[18]))
            # self.tableWidget.setItem(c,1,QTableWidgetItem(str(i[19])))
            # self.tableWidget.setItem(c,2,QTableWidgetItem(str(i[20])))
            # self.tableWidget.setItem(c,3,QTableWidgetItem(str(i[21])))
            # self.tableWidget.setItem(c,4,QTableWidgetItem(str(i[22])))
            # self.tableWidget.setItem(c,5,QTableWidgetItem(str(i[23])))
            # self.tableWidget.setItem(c,6,QTableWidgetItem(i[24]))
            # self.tableWidget.setItem(c,7,QTableWidgetItem(str(i[25])))
            # self.tableWidget.setItem(c,8,QTableWidgetItem(str(i[26])))
            # self.tableWidget.setItem(c,9,QTableWidgetItem(str(i[27])))
            # self.tableWidget.setItem(c,10,QTableWidgetItem(str(i[28])))
            # self.tableWidget.setItem(c,11,QTableWidgetItem(i[29]))
            # self.tableWidget.setItem(c,12,QTableWidgetItem(str(i[30])))
            # self.tableWidget.setItem(c,13,QTableWidgetItem(str(i[31])))
            # self.tableWidget.setItem(c,14,QTableWidgetItem(str(i[32])))
            # c=c+1
        
    def fillRates(self,text):
        format_str='''SELECT * FROM Rates WHERE From_Date='{date}';'''
        sql_command=format_str.format(date=text)
        self.cursor_1.execute(sql_command)
        res=self.cursor_1.fetchone()
        self.lineEdit.setText(str(res[3]))
        self.lineEdit_2.setText(str(res[4]))
        self.lineEdit_3.setText(str(res[5]))
        self.lineEdit_4.setText(str(res[6]))
        self.lineEdit_5.setText(str(res[7]))
        self.lineEdit_6.setText(str(res[8]))

    def fillValuation(self,text):
        format_str='''SELECT * FROM Valuation WHERE Valuation_date='{date}';'''
        sql_command=format_str.format(date=text)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchone()
        id=res[0]
        self.lineEdit.setText(str(res[3]))
        self.lineEdit_2.setText(str(res[4]))
        self.lineEdit_3.setText(str(res[5]))
        self.lineEdit_4.setText(str(res[6]))
        self.lineEdit_5.setText(str(res[7]))
        self.lineEdit_6.setText(str(res[8]))
        self.lineEdit_8.setText(str(res[9]))
        self.lineEdit_9.setText(str(res[10]))
        self.lineEdit_7.setText(str(res[11]))
        self.lineEdit_13.setText(str(res[12]))
        self.lineEdit_14.setText(str(res[13]))
        self.lineEdit_10.setText(str(res[14]))
        self.lineEdit_11.setText(str(res[15]))
        self.lineEdit_12.setText(str(res[16]))
        self.lineEdit_17.setText(str(res[17]))
        self.lineEdit_19.setText(str(res[18]))
        self.lineEdit_25.setText(str(res[19]))
        self.lineEdit_22.setText(str(res[20]))
        self.lineEdit_18.setText(str(res[21]))
        self.lineEdit_20.setText(str(res[22]))
        self.lineEdit_26.setText(str(res[23]))
        self.lineEdit_23.setText(str(res[24]))
        self.lineEdit_16.setText(str(res[25]))
        self.lineEdit_21.setText(str(res[26]))
        self.lineEdit_24.setText(str(res[27]))
        self.lineEdit_27.setText(str(res[28]))

        format_str='''SELECT * FROM Products WHERE Valuation_Id='{id}';'''
        sql_command=format_str.format(id=id)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchall()
        self.tableWidget.clearContents()
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.removeRow(i)
        
        c=0
        for i in res:
            self.tableWidget.insertRow(c)
            self.tableWidget.setItem(c,0,QTableWidgetItem(i[2]))
            self.tableWidget.setItem(c,1,QTableWidgetItem(str(i[3])))
            self.tableWidget.setItem(c,2,QTableWidgetItem(str(i[4])))
            self.tableWidget.setItem(c,3,QTableWidgetItem(str(i[5])))
            self.tableWidget.setItem(c,4,QTableWidgetItem(str(i[6])))
            self.tableWidget.setItem(c,5,QTableWidgetItem(str(i[7])))
            self.tableWidget.setItem(c,6,QTableWidgetItem(str(i[8])))
            self.tableWidget.setItem(c,7,QTableWidgetItem(i[9]))
            self.tableWidget.setItem(c,8,QTableWidgetItem(i[10]))
            self.tableWidget.setItem(c,9,QTableWidgetItem(str(i[11])))
            self.tableWidget.setItem(c,10,QTableWidgetItem(str(i[12])))
            self.tableWidget.setItem(c,11,QTableWidgetItem(str(i[13])))
            self.tableWidget.setItem(c,12,QTableWidgetItem(str(i[14])))
            self.tableWidget.setItem(c,13,QTableWidgetItem(i[15]))
            self.tableWidget.setItem(c,14,QTableWidgetItem(i[16]))
            self.tableWidget.setItem(c,14,QTableWidgetItem(i[17]))
            self.tableWidget.setItem(c,15,QTableWidgetItem(str(i[18])))
            format_str='''INSERT INTO Products(Valuation_Id,Description,Rate,Purity,Quantity,Gross_Wt,Metal_Wt,Metal_Value,Stone_Description,Stone,Stone_Wt,Stone_Rate,Stone_Value,Total_Value,Metal,Item_Ratewise,Stone_Weightwise,Is_Soverign) VALUES ({id},'{item_description}',{rate},{purity},{quantity},{gross_wt},{metal_weight},{metal_value},'{stone_description}','{stone}',{stone_wt},{stone_rate},{stone_value},{total_value},'{metal}','{item_ratewise}','{stone_weightwise}',{is_soverign});'''
            sql_command=format_str.format(id=Ui_Valuation.val_id,item_description=i[2],rate=i[3],purity=i[4],quantity=i[5],gross_wt=i[6],metal_weight=i[7],metal_value=i[8],stone_description=i[9],stone=i[10],stone_wt=i[11],stone_rate=i[12],stone_value=i[13],total_value=i[14],metal=i[15],item_ratewise=i[16],stone_weightwise=i[17],is_soverign=i[18])
            self.cursor.execute(sql_command)
            c=c+1
        self.connection.commit()
        # self.connection.close()
        # self.connection = sqlite3.connect("Valuation_1.db")
        # self.cursor=self.connection.cursor()
        
    
    def UpdateTable(self):
        format_str='''SELECT * FROM Products WHERE Valuation_Id='{id}';'''
        sql_command=format_str.format(id=Ui_Valuation.val_id)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchall()
        print("A")
        print(res)
        self.tableWidget.clearContents()
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.removeRow(i)
        
        c=0
        for i in res:
            self.tableWidget.insertRow(c)
            self.tableWidget.setItem(c,0,QTableWidgetItem(i[2]))
            self.tableWidget.setItem(c,1,QTableWidgetItem(str(i[3])))
            self.tableWidget.setItem(c,2,QTableWidgetItem(str(i[4])))
            self.tableWidget.setItem(c,3,QTableWidgetItem(str(i[5])))
            self.tableWidget.setItem(c,4,QTableWidgetItem(str(i[6])))
            self.tableWidget.setItem(c,5,QTableWidgetItem(str(i[7])))
            self.tableWidget.setItem(c,6,QTableWidgetItem(str(i[8])))
            self.tableWidget.setItem(c,7,QTableWidgetItem(i[9]))
            self.tableWidget.setItem(c,8,QTableWidgetItem(i[10]))
            self.tableWidget.setItem(c,9,QTableWidgetItem(str(i[11])))
            self.tableWidget.setItem(c,10,QTableWidgetItem(str(i[12])))
            self.tableWidget.setItem(c,11,QTableWidgetItem(str(i[13])))
            self.tableWidget.setItem(c,12,QTableWidgetItem(str(i[14])))
            self.tableWidget.setItem(c,13,QTableWidgetItem(i[15]))
            self.tableWidget.setItem(c,14,QTableWidgetItem(i[16]))
            self.tableWidget.setItem(c,14,QTableWidgetItem(i[17]))
            self.tableWidget.setItem(c,15,QTableWidgetItem(str(i[18])))
            c=c+1


    def add_item(self):
        self.UpdateTable()
        gold=self.lineEdit.text()
        silver=self.lineEdit_2.text()
        platinum=self.lineEdit_3.text()
        diamond=self.lineEdit_4.text()
        soverign=self.lineEdit_5.text()
        coin=self.lineEdit_6.text()
        self.item=Products.Ui_Products(Ui_Valuation.val_id,gold,silver,platinum,diamond,soverign,coin,'')
        self.item.show()
        self.UpdateTable()
        self.Calculate()
    
    def OnTableClicked(self,name):
        gold=self.lineEdit.text()
        silver=self.lineEdit_2.text()
        platinum=self.lineEdit_3.text()
        diamond=self.lineEdit_4.text()
        soverign=self.lineEdit_5.text()
        coin=self.lineEdit_6.text()
        self.item=Products.Ui_Products(Ui_Valuation.val_id,gold,silver,platinum,diamond,soverign,coin,name.text())
        self.item.show()
        self.UpdateTable()
        self.Calculate()

        

    def __del__(self):
        self.UpdateIndex()
        self.connection.commit()
        self.connection.close()
        self.connection_1.commit()
        self.connection_1.close()
    
    def databaseAccess(self):
        self.connection = sqlite3.connect("Valuation_1.db")
        self.cursor=self.connection.cursor()
        self.connection_1 = sqlite3.connect("Rates.db")
        self.cursor_1=self.connection_1.cursor()

    
    
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_19.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_3.addWidget(self.lineEdit_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_4.addWidget(self.lineEdit_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_5.addWidget(self.lineEdit_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_6.addWidget(self.lineEdit_6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_19.addLayout(self.horizontalLayout_3)
        self.verticalLayout_20.addLayout(self.verticalLayout_19)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_7.addWidget(self.label_25)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_6.addWidget(self.lineEdit_8)
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_6.addWidget(self.toolButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_7.addWidget(self.lineEdit_9)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_5.addWidget(self.lineEdit_7)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_14.addLayout(self.verticalLayout_7)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_9.addWidget(self.label_26)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_11.addWidget(self.label_15)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.horizontalLayout_11.addWidget(self.lineEdit_13)
        self.verticalLayout_9.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_12.addWidget(self.label_16)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.horizontalLayout_12.addWidget(self.lineEdit_14)
        self.verticalLayout_9.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_13.addWidget(self.label_17)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.horizontalLayout_13.addWidget(self.lineEdit_15)
        self.verticalLayout_9.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14.addLayout(self.verticalLayout_9)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_8.addWidget(self.label_27)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_8.addWidget(self.label_12)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_8.addWidget(self.lineEdit_10)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_9.addWidget(self.label_13)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_9.addWidget(self.lineEdit_11)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_10.addWidget(self.label_14)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.horizontalLayout_10.addWidget(self.lineEdit_12)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_14.addLayout(self.verticalLayout_8)
        self.verticalLayout_20.addLayout(self.horizontalLayout_14)
        self.verticalLayout_21.addLayout(self.verticalLayout_20)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(17)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(131)
        self.verticalLayout_21.addWidget(self.tableWidget)
        self.verticalLayout_22.addLayout(self.verticalLayout_21)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_17.addItem(spacerItem1)
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_17.addWidget(self.label_22)
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_17.addWidget(self.label_24)
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_17.addWidget(self.label_23)
        self.horizontalLayout_15.addLayout(self.verticalLayout_17)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_11.addWidget(self.label_18)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.verticalLayout_10.addWidget(self.lineEdit_17)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.verticalLayout_10.addWidget(self.lineEdit_18)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.verticalLayout_10.addWidget(self.lineEdit_16)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        self.horizontalLayout_15.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_12.addWidget(self.label_19)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.verticalLayout_13.addWidget(self.lineEdit_19)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.verticalLayout_13.addWidget(self.lineEdit_20)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.verticalLayout_13.addWidget(self.lineEdit_21)
        self.verticalLayout_12.addLayout(self.verticalLayout_13)
        self.horizontalLayout_15.addLayout(self.verticalLayout_12)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_16.addWidget(self.label_21)
        self.lineEdit_25 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.verticalLayout_16.addWidget(self.lineEdit_25)
        self.lineEdit_26 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.verticalLayout_16.addWidget(self.lineEdit_26)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_16.addItem(spacerItem2)
        self.horizontalLayout_15.addLayout(self.verticalLayout_16)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_14.addWidget(self.label_20)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.verticalLayout_15.addWidget(self.lineEdit_22)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.verticalLayout_15.addWidget(self.lineEdit_23)
        self.lineEdit_24 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.verticalLayout_15.addWidget(self.lineEdit_24)
        self.verticalLayout_14.addLayout(self.verticalLayout_15)
        self.horizontalLayout_15.addLayout(self.verticalLayout_14)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_18.addWidget(self.pushButton)
        self.lineEdit_27 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.verticalLayout_18.addWidget(self.lineEdit_27)
        self.horizontalLayout_15.addLayout(self.verticalLayout_18)
        spacerItem3 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem3)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_24.addWidget(self.pushButton_6)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_24.addItem(spacerItem4)
        self.horizontalLayout_15.addLayout(self.verticalLayout_24)
        self.verticalLayout_22.addLayout(self.horizontalLayout_15)
        self.verticalLayout_23.addLayout(self.verticalLayout_22)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_16.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_16.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_16.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_16.addWidget(self.pushButton_5)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem5)
        self.verticalLayout_23.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17.addLayout(self.verticalLayout_23)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1241, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.actionFirm = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons8-organization-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFirm.setIcon(icon)
        self.actionFirm.setObjectName("actionFirm")
        self.actionValuer = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons8-user-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionValuer.setIcon(icon1)
        self.actionValuer.setObjectName("actionValuer")
        self.actionGroups = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons8-list-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGroups.setIcon(icon2)
        self.actionGroups.setObjectName("actionGroups")
        self.actionItems = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons8-ring-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionItems.setIcon(icon3)
        self.actionItems.setObjectName("actionItems")
        self.actionMarket_Rates = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons8-us-dollar-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMarket_Rates.setIcon(icon4)
        self.actionMarket_Rates.setObjectName("actionMarket_Rates")
        self.actionValuation = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons8-contract-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionValuation.setIcon(icon5)
        self.actionValuation.setObjectName("actionValuation")
        self.actionChange_Password = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons8-password-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionChange_Password.setIcon(icon6)
        self.actionChange_Password.setObjectName("actionChange_Password")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons8-about-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon7)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons8-exit-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon8)
        self.actionExit.setObjectName("actionExit")
        self.toolBar.addAction(self.actionFirm)
        self.toolBar.addAction(self.actionValuer)
        self.toolBar.addAction(self.actionGroups)
        self.toolBar.addAction(self.actionItems)
        self.toolBar.addAction(self.actionMarket_Rates)
        self.toolBar.addAction(self.actionValuation)
        self.toolBar.addAction(self.actionChange_Password)
        self.toolBar.addAction(self.actionAbout)
        self.toolBar.addAction(self.actionExit)
        self.pushButton_2.clicked.connect(self.new_btn)
        self.pushButton_4.clicked.connect(self.save_btn)
        self.pushButton_5.clicked.connect(self.cancel_btn)
        self.comboBox.activated[str].connect(self.fillRates)
        self.comboBox_2.activated[str].connect(self.fillValuation)
        self.tableWidget.itemPressed.connect(self.OnTableClicked)
        self.pushButton_6.clicked.connect(self.add_item)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Rate Date:"))
        self.label_2.setText(_translate("MainWindow", "Valuation Date:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "12/12/12"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "1/1/1"))
        self.label_3.setText(_translate("MainWindow", "Gold(10 g)"))
        self.label_4.setText(_translate("MainWindow", "Silver(1 kg)"))
        self.label_5.setText(_translate("MainWindow", "Platinum"))
        self.label_6.setText(_translate("MainWindow", "Diamond"))
        self.label_7.setText(_translate("MainWindow", "Soverign"))
        self.label_8.setText(_translate("MainWindow", "Coin"))
        self.label_25.setText(_translate("MainWindow", "Valuers"))
        self.label_10.setText(_translate("MainWindow", "Name"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label_11.setText(_translate("MainWindow", "R.No."))
        self.label_9.setText(_translate("MainWindow", "Purpose"))
        self.label_26.setText(_translate("MainWindow", "Customer"))
        self.label_15.setText(_translate("MainWindow", "Name"))
        self.label_16.setText(_translate("MainWindow", "Address 1"))
        self.label_17.setText(_translate("MainWindow", "Address 2"))
        self.label_27.setText(_translate("MainWindow", "Firm"))
        self.label_12.setText(_translate("MainWindow", "Name"))
        self.label_13.setText(_translate("MainWindow", "Address"))
        self.label_14.setText(_translate("MainWindow", "Under O/S with"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Description"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Rate"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Purity"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Qty."))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Gross Wt."))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Metal Wt."))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Value(Metal)"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Stone(Description)"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Stone"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Wt (Stone)"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Rate(Stone)"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Value(Stone)"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Total Value"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Metal"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Item Ratewise"))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Stone Weightwise"))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "Is Soverign"))
        self.label_22.setText(_translate("MainWindow", "Gold"))
        self.label_24.setText(_translate("MainWindow", "Silver"))
        self.label_23.setText(_translate("MainWindow", "Diamond"))
        self.label_18.setText(_translate("MainWindow", "Total Qty."))
        self.label_19.setText(_translate("MainWindow", "Gross Wt."))
        self.label_21.setText(_translate("MainWindow", "Metal Wt."))
        self.label_20.setText(_translate("MainWindow", "Value"))
        self.pushButton.setText(_translate("MainWindow", "Check Purity Wise Total"))
        self.pushButton_6.setText(_translate("MainWindow", "Add Item"))
        self.pushButton_2.setText(_translate("MainWindow", "New"))
        self.pushButton_3.setText(_translate("MainWindow", "Valuation Bill"))
        self.pushButton_4.setText(_translate("MainWindow", "Save"))
        self.pushButton_5.setText(_translate("MainWindow", "Close"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionFirm.setText(_translate("MainWindow", "Firm"))
        self.actionFirm.setToolTip(_translate("MainWindow", "Firm"))
        self.actionFirm.setShortcut(_translate("MainWindow", "Alt+F"))
        self.actionValuer.setText(_translate("MainWindow", "Valuer"))
        self.actionValuer.setToolTip(_translate("MainWindow", "Valuer"))
        self.actionValuer.setShortcut(_translate("MainWindow", "Alt+V"))
        self.actionGroups.setText(_translate("MainWindow", "Groups"))
        self.actionGroups.setToolTip(_translate("MainWindow", "Groups"))
        self.actionGroups.setShortcut(_translate("MainWindow", "Alt+G"))
        self.actionItems.setText(_translate("MainWindow", "Items"))
        self.actionItems.setToolTip(_translate("MainWindow", "Items"))
        self.actionItems.setShortcut(_translate("MainWindow", "Alt+I"))
        self.actionMarket_Rates.setText(_translate("MainWindow", "Market Rates"))
        self.actionMarket_Rates.setToolTip(_translate("MainWindow", "Market Rates"))
        self.actionMarket_Rates.setShortcut(_translate("MainWindow", "Alt+M"))
        self.actionValuation.setText(_translate("MainWindow", "Valuation"))
        self.actionValuation.setToolTip(_translate("MainWindow", "Valuation"))
        self.actionValuation.setShortcut(_translate("MainWindow", "Alt+A"))
        self.actionChange_Password.setText(_translate("MainWindow", "Change Password"))
        self.actionChange_Password.setToolTip(_translate("MainWindow", "Change Password"))
        self.actionChange_Password.setShortcut(_translate("MainWindow", "Alt+P"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout.setToolTip(_translate("MainWindow", "About"))
        self.actionAbout.setShortcut(_translate("MainWindow", "Alt+B"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setToolTip(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Esc"))

    def cancel_btn(self):
        self.close()
    
    def new_btn(self):
        valuation_date=self.comboBox.lineEdit().text()
        rate_date=self.comboBox_2.lineEdit().text()
        gold=self.lineEdit.text()
        silver=self.lineEdit_2.text()
        platinum=self.lineEdit_3.text()
        diamond=self.lineEdit_4.text()
        soverign=self.lineEdit_5.text()
        coin=self.lineEdit_6.text()
        V_Name=self.lineEdit_8.text()
        V_Reg_No=self.lineEdit_9.text()
        V_Purpose=self.lineEdit_7.text()
        C_Name=self.lineEdit_13.text()
        C_Address=self.lineEdit_14.text()
        F_Name=self.lineEdit_10.text()
        F_Address=self.lineEdit_11.text()
        OS_With=self.lineEdit_12.text()
        Gold_total=self.lineEdit_17.text()
        Gold_gross=self.lineEdit_19.text()
        Gold_metal=self.lineEdit_25.text()
        Gold_value=self.lineEdit_22.text()
        Silver_total=self.lineEdit_18.text()
        Silver_gross=self.lineEdit_20.text()
        Silver_metal=self.lineEdit_26.text()
        Silver_value=self.lineEdit_23.text()
        Diamond_total=self.lineEdit_16.text()
        Diamond_gross=self.lineEdit_21.text()
        Diamond_value=self.lineEdit_24.text()
        Grand_Total=self.lineEdit_27.text()

        format_str='''INSERT INTO `Valuation`(`Valuation_id`,`Valuation_date`,`Rate_date`,`Gold_rate`,`Silver_rate`,`Platinum_rate`,`Soverign_rate`,`Coin_rate`,`Diamond_rate`,`Valuer_name`,`Valuer_reg_no`,`Purpose`,`Customer_name`,`Customer_address`,`Firm_name`,`Firm_address`,`OS`,`Gold_total`,`Gold_gross`,`Gold_metal`,`Gold_value`,`Silver_total`,`Silver_gross`,`Silver_metal`,`Silver_value`,`Stone_total`,`Stone_gross`,`Stone_value`,`Grand_Total`) VALUES ({id},'{valuation_date}','{rate_date}',{gold},{silver},{platinum},{soverign},{coin},{diamond},'{V_Name}',{V_Reg_No},'{V_Purpose}','{C_Name}','{C_Address}','{F_Name}','{F_Address}','{OS_With}',{Gold_total},{Gold_gross},{Gold_metal},{Gold_value},{Silver_total},{Silver_gross},{Silver_metal},{Silver_value},{Diamond_total},{Diamond_gross},{Diamond_value},{Grand_Total});'''
        sql_command=format_str.format(id=Ui_Valuation.val_id,valuation_date=valuation_date,rate_date=rate_date,gold=gold,silver=silver,platinum=platinum,diamond=diamond,soverign=soverign,coin=coin,V_Name=V_Name,V_Reg_No=V_Reg_No,V_Purpose=V_Purpose,C_Name=C_Name,C_Address=C_Address,F_Name=F_Name,F_Address=F_Address,OS_With=OS_With,Gold_total=Gold_total,Gold_gross=Gold_gross,Gold_metal=Gold_metal,Gold_value=Gold_value,Silver_total=Silver_total,Silver_gross=Silver_gross,Silver_metal=Silver_metal,Silver_value=Silver_value,Diamond_total=Diamond_total,Diamond_gross=Diamond_gross,Diamond_value=Diamond_value,Grand_Total=Grand_Total)
        self.cursor.execute(sql_command)
        

        # sql_command='''SELECT MAX(Valuation_id) FROM Valuation ;'''
        # # sql_command=format_str.format(from_date=from_date)
        # self.cursor.execute(sql_command)
        # res=self.cursor.fetchone()
        # self.Val_id=res[0]

                

        # for i in range(self.tableWidget.rowCount()):
        #     item=self.tableWidget.item(i,0)
        #     rate=self.tableWidget.item(i,1)
        #     purity=self.tableWidget.item(i,2)
        #     quantity=self.tableWidget.item(i,3)
        #     gross_wt=self.tableWidget.item(i,4)
        #     metal_wt=self.tableWidget.item(i,5)
        #     metal_value=self.tableWidget.item(i,6)
        #     s_description=self.tableWidget.item(i,7)
        #     s_wt=self.tableWidget.item(i,8)
        #     s_rate=self.tableWidget.item(i,9)
        #     s_value=self.tableWidget.item(i,10)
        #     total=self.tableWidget.item(i,11)
        #     metal=self.tableWidget.item(i,12)
        #     item_ratewise=self.tableWidget.item(i,13)
        #     stone_weightwise=self.tableWidget.item(i,14)
        #     is_soverign=self.tableWidget.item(i,15)
        #     format_str='''INSERT INTO Products(Valuation_Id,Description,Rate,Purity,Quantity,Gross_Wt,Metal_Wt,Metal_Value,Stone_Description,Stone_Wt,Stone_Rate,Stone_Value,Total_Value,Metal,Item_Ratewise,Stone_Weightwise,Is_Soverign) VALUES ({Val_id},{'item}',{rate},{purity},{quantity},{gross_wt},{metal_wt},{metal_value},'{s_description}',{s_wt},{s_rate},{s_value},{total},'{metal}','{item_ratewise}',{stone_weightwise},{is_soverign});'''
        #     sql_command=format_str.format(Val_id=Val_id,item=item,rate=rate,purity=purity,quantity=quantity,gross_wt=gross_wt,metal_value=metal_value,s_description=s_description,s_wt=s_wt,s_rate=s_rate,s_value=s_value,total=total,metal=metal,item_ratewise=item_ratewise,stone_weightwise=stone_weightwise,is_soverign=is_soverign)
        #     self.cursor.execute(sql_command)


        return
    
    # def delete_btn(self):
    #     from_date = self.lineEdit.text()
    #     to_date=self.lineEdit.text()
    #     gold=self.lineEdit_2.text()
    #     silver=self.lineEdit_7.text()
    #     platinum=self.lineEdit_6.text()
    #     diamond=self.lineEdit_3.text()
    #     soverign=self.lineEdit_5.text()
    #     coin=self.lineEdit_4.text()
    #     format_str='''SELECT * FROM Rates WHERE From_Date=""{from_date}"";'''
    #     sql_command=format_str.format(from_date=from_date)
    #     self.cursor.execute(sql_command)
    #     res=self.cursor.fetchone()
    #     if(res is None):
    #         QtWidgets.QMessageBox.warning(self, 'Error', 'Firm Does Not Exists')
    #         self.close()
    #     else:
    #         format_str='''DELETE FROM Rates WHERE From_Date=""{from_date}"";'''
    #         sql_command=format_str.format(from_date=from_date)
    #         self.cursor.execute(sql_command)
    #         return
    
    def save_btn(self):
        valuation_date=self.comboBox.lineEdit().text()
        rate_date=self.comboBox_2.lineEdit().text()
        gold=self.lineEdit.text()
        silver=self.lineEdit_2.text()
        platinum=self.lineEdit_3.text()
        diamond=self.lineEdit_4.text()
        soverign=self.lineEdit_5.text()
        coin=self.lineEdit_6.text()
        V_Name=self.lineEdit_8.text()
        V_Reg_No=self.lineEdit_9.text()
        V_Purpose=self.lineEdit_7.text()
        C_Name=self.lineEdit_13.text()
        C_Address=self.lineEdit_14.text()
        F_Name=self.lineEdit_10.text()
        F_Address=self.lineEdit_11.text()
        OS_With=self.lineEdit_12.text()
        Gold_total=self.lineEdit_17.text()
        Gold_gross=self.lineEdit_19.text()
        Gold_metal=self.lineEdit_25.text()
        Gold_value=self.lineEdit_22.text()
        Silver_total=self.lineEdit_18.text()
        Silver_gross=self.lineEdit_20.text()
        Silver_metal=self.lineEdit_26.text()
        Silver_value=self.lineEdit_23.text()
        Diamond_total=self.lineEdit_16.text()
        Diamond_gross=self.lineEdit_21.text()
        Diamond_value=self.lineEdit_24.text()
        Grand_Total=self.lineEdit_27.text()
        format_str='''SELECT * FROM Valuation WHERE Valuation_date={valuation_date};'''
        sql_command=format_str.format(valuation_date=valuation_date)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchone()
        if(res is None):
            QtWidgets.QMessageBox.warning(self, 'Error', 'Valuation Does Not Exists')
            self.close()
        else:
            # format_str='''INSERT INTO `Valuation`('Valuation_date`,`Rate_date`,`Gold_rate`,`Silver_rate`,`Platinum_rate`,`Soverign_rate`,`Coin_rate`,`Diamond_rate`,`Valuer_name`,`Valuer_reg_no`,`Purpose`,`Customer_name`,`Customer_address`,`Firm_name`,`Firm_address`,`O/S`,`Gold_total`,`Gold_gross`,`Gold_metal`,`Gold_value`,`Silver_total`,`Silver_gross`,`Silver_metal`,`Silver_value`,`Stone_total`,`Stone_gross`,`Stone_value`,`Grand_Total`) VALUES ('{valuation_date}','{rate_date}',{gold},{silver},{platinum},{soverign},{coin},{diamond},'{V_Name}',{V_Reg_No},'{V_Purpose}','{C_Name}','{C_Address}','{F_Name}','{F_Address}','{OS_With}',{Gold_total},{Gold_gross},{Gold_metal},{Gold_value},{Silver_total},{Silver_gross},{Silver_metal},{Silver_value},{Diamond_total},{Diamond_gross},{Diamond_value},{Grand_Total});'''
            format_str='''UPDATE Valuation SET Valuation_date={valuation_date},Rate_date={rate_date},Gold_rate={gold},Silver_rate={silver},Platinum_rate={platinum},Soverign_rate={soverign},Coin_rate={coin},Diamond_rate={diamond},Valuer_name='{V_Name}',Valuer_reg_no={V_Reg_No},Purpose='{V_Purpose}',Customer_name='{C_Name}',Customer_address='{C_Address}',Firm_name='{F_Name}',Firm_address='{F_Address}',O/S='{OS_With}',Gold_total={Gold_total},Gold_gross={Gold_gross},Gold_metal={Gold_metal},Gold_value={Gold_value},Silver_total={Silver_total},Silver_gross={Silver_gross},Silver_metal={Silver_metal},Silver_value={Silver_value},Stone_total={Diamond_total},Stone_gross={Diamond_gross},Stone_value={Diamond_value},Grand_Total={Grand_Total} WHERE From_Date={from_date};'''
            sql_command=format_str.format(valuation_date=valuation_date,rate_date=rate_date,gold=gold,silver=silver,platinum=platinum,diamond=diamond,soverign=soverign,coin=coin,V_Name=V_Name,V_Reg_No=V_Reg_No,V_Purpose=V_Purpose,C_Name=C_Name,C_Address=C_Address,F_Name=F_Name,F_Address=F_Address,OS_With=OS_With,Gold_total=Gold_total,Gold_gross=Gold_gross,Gold_metal=Gold_metal,Gold_value=Gold_value,Silver_total=Silver_total,Silver_gross=Silver_gross,Silver_metal=Silver_metal,Silver_value=Silver_value,Diamond_total=Diamond_total,Diamond_gross=Diamond_gross,Diamond_value=Diamond_value,Grand_Total=Grand_Total)
            self.cursor.execute(sql_command)
            return
    
    # def search_btn(self):
    #     search=self.lineEdit_8.text()
    #     format_str='''SELECT * FROM Rates WHERE From_Date={search} OR To_Date={search} OR Gold={search} OR Silver={search} OR Platinum={search} OR Diamond={search} OR Soverign={search} OR Coin={search};'''
    #     sql_command=format_str.format(search=search)
    #     self.cursor.execute(sql_command)
    #     res=self.cursor.fetchall()
    #     self.tableWidget.setRowCount(0)

    #     for row_number,row_data in enumerate(res):
    #         self.tableWidget.insertRow(row_number)
    #         for column_number,data in enumerate(row_data):
    #             self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
    #     return

    def fillDropDown(self):
        sql_command='''SELECT From_Date FROM Rates;'''
        self.cursor.execute(sql_command)
        res=self.cursor.fetchall()
        print(res)
        for i in res:
            self.comboBox.addItem(str(i))
        return
    
    def fillTable(self):
        sql_command='''SELECT * FROM Rates;'''
        self.cursor.execute(sql_command)
        res=self.cursor.fetchall()
        self.tableWidget.setRowCount(0)

        for row_number,row_data in enumerate(res):
            self.tableWidget.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
        return

    def ExitTool(self):
        self.close()

    def AboutTool(self):
        About=""
        QtWidgets.QMessageBox.information(self, 'About', About)

    def ChangePasswordTool(self):
        self.change=Change_Password.Ui_ChangePassword()
        self.change.show()

    def ValuationTool(self):
        self.close()
        self.valuation=Ui_Valuation()
        self.valuation.show()

    def RatesTool(self):
        self.close()
        self.rates=Rates.Ui_Rates()
        self.rates.show()

    def ItemTool(self):
        self.close()
        self.items=Items.Ui_Items()
        self.items.show()

    def GroupsTool(self):
        self.close()
        self.groups=Groups.Ui_Groups()
        self.groups.show()

    def ValuerTool(self):
        self.close()
        self.valuer=Valuers.Ui_Valuer_setup()
        self.valuer.show()

    def FirmTool(self):
        self.close()
        self.firm=Firm.Ui_Firm_setup()
        self.firm.show()

    def toolbtnpressed(self,a):
        print(a.text())
        # switch(a.text()){
        #     case 'Exit':
        #     self.ExitTool()
        # }
        if(a.text()=='Exit'):
            self.ExitTool()
        elif(a.text()=='About'):
            self.AboutTool()
        elif(a.text()=='Change Password'):
            self.ChangePasswordTool()
        elif(a.text()=='Valuation'):
            self.ValuationTool()
        elif(a.text()=='Market Rates'):
            self.RatesTool()
        elif(a.text()=='Items'):
            self.ItemTool()
        elif(a.text()=='Groups'):
            self.GroupsTool()
        elif(a.text()=='Valuer'):
            self.ValuerTool()
        else:
            self.FirmTool()


    def Document(self):
        valuation_date=self.comboBox.lineEdit().text()
        format_str='''SELECT * FROM Valuation WHERE Valuation_date={valuation_date};'''
        sql_command=format_str.format(valuation_date=valuation_date)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchone()
        id=res(0)

        format_str='''SELECT * FROM Products WHERE Valuation_id={id};'''
        sql_command=format_str.format(valuation_date=valuation_date)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchall()

        
        doc = DocxTemplate("template.docx")
        context = { 'Name':
        doc.render(context)
        doc.save("generated_doc.docx")







if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Valuation()
    # w = QtWidgets.QMainWindow()
    ex.show()
    # w.show()
    sys.exit(app.exec_())