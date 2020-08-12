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





class Ui_Products(QtWidgets.QMainWindow):
    def __init__(self,id,gold,silver,platinum,diamond,soverign,coin,name=''):
        QtWidgets.QMainWindow.__init__(self)
        self.databaseAccess()
        self.setupUi(self)
        self.default()
        # self.printDB()
        self.id=id
        self.gold_rate=gold
        self.silver_rate=silver
        self.platinum_rate=platinum
        self.diamond_rate=diamond
        self.soverign_rate=soverign
        self.coin=coin
        print("++++++++++++")
        print(name)
        if(name==''):
            pass
        else:
            self.CalledFromtable(name)
    
    
    # @classmethod
    def CalledFromtable(self,name):
        # self.__init__(self,0,0,0,0,0,0,0)
        description=name
        print(name)
        print(type(name))
        format_str='''SELECT * FROM Products WHERE Description="{name}";'''
        sql_command=format_str.format(name=name)
        self.cursor.execute(sql_command)
        res = self.cursor.fetchone()
        print(res)
        self.lineEdit.setText(str(res[2]))
        self.comboBox.lineEdit().setText(res[15])
        self.lineEdit_3.setText(str(res[3]))
        self.lineEdit_2.setText(str(res[4]))
        self.lineEdit_4.setText(str(res[5]))
        self.lineEdit_5.setText(str(res[6]))
        self.lineEdit_6.setText(str(res[7]))
        self.comboBox_3.lineEdit().setText(str(res[16]))
        self.lineEdit_11.setText(str(res[9]))
        self.comboBox_4.lineEdit().setText(str(res[10]))
        self.lineEdit_10.setText(str(res[11]))
        self.lineEdit_9.setText(str(res[12]))
        self.comboBox_2.lineEdit().setText(str(res[17]))
        soverign=res[18]
        if(soverign==1):
            self.checkBox.setChecked()
        else:
            pass






    def __del__(self):
        self.connection.commit()
        self.connection.close()
        self.connection_1.commit()
        self.connection_1.close()

    def databaseAccess(self):
        self.connection = sqlite3.connect("Valuation_1.db",timeout=10)
        self.cursor=self.connection.cursor()
        self.connection_1 = sqlite3.connect("Items.db")
        self.cursor_1=self.connection_1.cursor()
    
    def default(self):
        sql_command='''SELECT * FROM Items ;'''
        self.cursor_1.execute(sql_command)
        res=self.cursor_1.fetchall()
        c=0
        for i in res:
            self.tableWidget.insertRow(c)
            self.tableWidget.setItem(c,0,QTableWidgetItem(i[1]))
            c=c+1
        self.comboBox.addItem('Gold')
        self.comboBox.addItem('Silver')
        self.comboBox.addItem('Platinum')
        self.comboBox_3.addItem('Weightwise')
        self.comboBox_3.addItem('Quantitywise')
        self.comboBox_2.addItem('Grams')
        self.comboBox_2.addItem('Carats')
        self.comboBox_4.addItem('Diamond')
        self.comboBox_4.addItem('Others')
        
    
    def tableClicked(self):
        name=self.tableWidget.currentItem().text()
        format_str='''SELECT * FROM Items WHERE Item_Description="{name}";'''
        sql_command=format_str.format(name=name)
        self.cursor_1.execute(sql_command)
        res = self.cursor_1.fetchone()
        self.lineEdit.setText(str(res[1]))
        # self.lineEdit_3.setText(str(res[3]))
        self.lineEdit_2.setText(str(res[7]))
        # self.lineEdit_4.setText(str(res[12]))
        # self.lineEdit_2.setText(str(res[7]))
        wt=int((res[4]+res[5])/2)
        self.lineEdit_6.setText(str(wt))
        self.lineEdit_11.setText(str(res[8]))
        wt_s=int((res[10]+res[11])/2)
        self.lineEdit_10.setText(str(wt_s))
        self.comboBox_3.lineEdit().setText(str(res[3]))
        self.comboBox_2.lineEdit().setText(str(res[9]))

    # def getMetalRate(self,metal):
    #     if(metal=='Gold'):
    #         return self.gold_rate
    #     elif(metal=='Silver'):
    #         return self.silver_rate
    #     else:
    #         return self.platinum_rate
    
    def OnSelect(self,metal):
        if(metal=='Gold'):
            self.lineEdit_3.setText(str(self.gold_rate))
        elif(metal=='Silver'):
            self.lineEdit_3.setText(str(self.silver_rate))
        else:
            self.lineEdit_3.setText(str(self.platinum_rate))
    
    def OnSelect1(self,stone):
        if(stone=='Diamond'):
            self.lineEdit_9.setText(str(self.diamond_rate))
        else:
            self.lineEdit_9.setText(str(""))

    def cancel_btn(self):
        self.close()
        return
    
    def delete_btn(self):
        item_description = self.lineEdit.text()
        format_str='''SELECT * FROM Products WHERE Description="{item_description}";'''
        sql_command=format_str.format(item_description=item_description)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchone()
        if(res is None):
            QtWidgets.QMessageBox.warning(self, 'Error', 'Item Does Not Exists')
            self.close()
        else:
            format_str='''DELETE FROM Products WHERE Description="{item_description}";'''
            sql_command=format_str.format(item_description=item_description)
            self.cursor.execute(sql_command)
            QtWidgets.QMessageBox.information(self, 'Success', 'Item Deleted Successfully')
            self.default()
            # self.clear()
        return


    
    def save_btn(self):
        item_description = self.lineEdit.text()
        purity=int(self.lineEdit_2.text())
        rate=int(self.lineEdit_3.text())
        quantity=int(self.lineEdit_4.text())
        gross_wt=int(self.lineEdit_5.text())
        metal_weight=int(self.lineEdit_6.text())
        stone_wt=gross_wt-metal_weight
        self.lineEdit_10.setText(str(stone_wt))
        metal=self.comboBox.lineEdit().text()
        item_ratewise=self.comboBox_3.lineEdit().text()
        stone_description = self.lineEdit_11.text()
        stone=self.comboBox_4.lineEdit().text()
        stone_wt=int(self.lineEdit_10.text())
        stone_rate = int(self.lineEdit_9.text())
        stone_weightwise=self.comboBox_2.lineEdit().text()
        if(self.checkBox.isChecked()):
            is_soverign=1
        else:
            is_soverign=0
        
        if(item_ratewise=='Weightwise'):
            metal_value=rate*metal_weight
        else:
            metal_weight=metal_weight*quantity
            gross_wt=gross_wt*quantity
            # self.lineEdit_5.setText(str(gross_wt))
            # self.lineEdit_6.setText(str(metal_wt))
            metal_value=rate*metal_weight

        if(stone_weightwise=='Grams'):
            stone_value=stone_rate*stone_wt
        else:
            stone_wt=stone_wt/5
            stone_value=stone_rate*stone_wt

        total_value=stone_value+metal_value
        
        format_str='''SELECT * FROM Products WHERE Description="{item_description}";'''
        sql_command=format_str.format(item_description=item_description)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchone()
        if(res is None):
            format_str='''INSERT INTO Products(Valuation_id,Description,Rate,Purity,Quantity,Gross_Wt,Metal_Wt,Metal_Value,Stone_Description,Stone,Stone_Wt,Stone_Rate,Stone_Value,Total_Value,Metal,Item_Ratewise,Stone_Weightwise,Is_Soverign) VALUES ({id},'{item_description}',{rate},{purity},{quantity},{gross_wt},{metal_weight},{metal_value},'{stone_description}','{stone}',{stone_wt},{stone_rate},{stone_value},{total_value},'{metal}','{item_ratewise}','{stone_weightwise}',{is_soverign});'''
            sql_command=format_str.format(id=self.id,item_description=item_description,rate=rate,purity=purity,quantity=quantity,gross_wt=gross_wt,metal_weight=metal_weight,metal_value=metal_value,stone_description=stone_description,stone=stone,stone_wt=stone_wt,stone_rate=stone_rate,stone_value=stone_value,total_value=total_value,metal=metal,item_ratewise=item_ratewise,stone_weightwise=stone_weightwise,is_soverign=is_soverign)
            self.cursor.execute(sql_command)
            QtWidgets.QMessageBox.information(self, 'Success', 'New Item Created')
            self.default()
            # self.connection.commit()
            # QtWidgets.QMessageBox.warning(self, 'Error', 'Item Does Not Exists')
            self.close()
        else:
            format_str='''UPDATE Products SET Valuation_id={id},Description='{item_description}',Rate={rate},Purity={purity},Quantity={quantity},Gross_Wt={gross_wt},Metal_Wt={metal_weight},Metal_Value={metal_value},Stone_Description='{stone_description}',Stone='{stone}',Stone_Wt={stone_wt},Stone_Rate={stone_rate},Stone_Value={stone_value},Total_Value={total_value},Metal='{metal}',Item_Ratewise='{item_ratewise}',Stone_Weightwise='{stone_weightwise}',Is_Soverign={is_soverign};'''
            sql_command=format_str.format(id=self.id,item_description=item_description,rate=rate,purity=purity,quantity=quantity,gross_wt=gross_wt,metal_weight=metal_weight,metal_value=metal_value,stone_description=stone_description,stone=stone,stone_wt=stone_wt,stone_rate=stone_rate,stone_value=stone_value,total_value=total_value,metal=metal,item_ratewise=item_ratewise,stone_weightwise=stone_weightwise,is_soverign=is_soverign)
            self.cursor.execute(sql_command)
            QtWidgets.QMessageBox.information(self, 'Success', 'Item Updated Successfully')
            self.default()
            self.close()
            # self.clear()
        return
        
        


    
    # def new_btn(self):
    #     item_description = self.lineEdit.text()
    #     purity=int(self.lineEdit_2.text())
    #     rate=int(self.lineEdit_3.text())
    #     quantity=int(self.lineEdit_4.text())
    #     gross_wt=int(self.lineEdit_5.text())
    #     metal_weight=int(self.lineEdit_6.text())
    #     stone_wt=gross_wt-metal_weight
    #     self.lineEdit_10.setText(str(stone_wt))
    #     metal=self.comboBox.lineEdit().text()
    #     item_ratewise=self.comboBox_3.lineEdit().text()
    #     stone_description = self.lineEdit_11.text()
    #     stone_wt=int(self.lineEdit_10.text())
    #     stone_rate = int(self.lineEdit_9.text())
    #     stone_weightwise=self.comboBox_2.lineEdit().text()
    #     if(self.checkBox.isChecked()):
    #         is_soverign=1
    #     else:
    #         is_soverign=0
        
    #     if(item_ratewise=='Weightwise'):
    #         metal_value=rate*metal_weight
    #     else:
    #         metal_weight=metal_weight*quantity
    #         gross_wt=gross_wt*quantity
    #         # self.lineEdit_5.setText(str(gross_wt))
    #         # self.lineEdit_6.setText(str(metal_wt))
    #         metal_value=rate*metal_weight

    #     if(stone_weightwise=='Grams'):
    #         stone_value=stone_rate*stone_wt
    #     else:
    #         stone_wt=stone_wt/5
    #         stone_value=stone_rate*stone_wt

    #     total_value=stone_value+metal_value
        

        # rate=self.getMetalRate(metal)


    #     format_str='''SELECT * FROM Products WHERE Description="{name}";'''
    #     sql_command=format_str.format(name=item_description)
    #     self.cursor.execute(sql_command)
    #     res = self.cursor.fetchone()
    #     print (res)
    #     if(res is None):
            
    #         format_str='''INSERT INTO Products(Valuation_id,Description,Rate,Purity,Quantity,Gross_Wt,Metal_Wt,Metal_Value,Stone_Description,Stone_Wt,Stone_Rate,Stone_Value,Total_Value,Metal,Item_Ratewise,Stone_Weightwise,Is_Soverign) VALUES ({id},'{item_description}',{rate},{purity},{quantity},{gross_wt},{metal_weight},{metal_value},'{stone_description}',{stone_wt},{stone_rate},{stone_value},{total_value},'{metal}','{item_ratewise}','{stone_weightwise}',{is_soverign});'''
    #         sql_command=format_str.format(id=self.id,item_description=item_description,rate=rate,purity=purity,quantity=quantity,gross_wt=gross_wt,metal_weight=metal_weight,metal_value=metal_value,stone_description=stone_description,stone_wt=stone_wt,stone_rate=stone_rate,stone_value=stone_value,total_value=total_value,metal=metal,item_ratewise=item_ratewise,stone_weightwise=stone_weightwise,is_soverign=is_soverign)
    #         self.cursor.execute(sql_command)
    #         QtWidgets.QMessageBox.information(self, 'Success', 'New Item Created')
    #         self.default()
    #         # self.clear()
    #     else:
    #             QtWidgets.QMessageBox.warning(self, 'Error', 'Item Already Exists')
    #             self.default()
    #             # self.clear()
    #             self.close()

    
    def search_btn(self):
        item_description=self.lineEdit_12.text()
        format_str='''SELECT * FROM Items WHERE Item_Description="{name}";'''
        sql_command=format_str.format(name=item_description)
        self.cursor_1.execute(sql_command)
        res=self.cursor_1.fetchall()
        self.tableWidget.clearContents()
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.removeRow(i)
        c=0
        for i in res:
            self.tableWidget.insertRow(c)
            self.tableWidget.setItem(c,0,QTableWidgetItem(i[1]))
            c=c+1

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(589, 674)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_15.addWidget(self.label_16)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.horizontalLayout_15.addWidget(self.lineEdit_12)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_4.addWidget(self.pushButton_9)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(10)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.horizontalLayout_18.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_17.setObjectName("label_17")
        self.verticalLayout_3.addWidget(self.label_17)
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
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_8.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_4.addWidget(self.lineEdit_4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_5.addWidget(self.lineEdit_5)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_6.addWidget(self.lineEdit_6)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_17.addWidget(self.label_18)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setEditable(True)
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout_17.addWidget(self.comboBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_17)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_15.setObjectName("label_15")
        self.verticalLayout_2.addWidget(self.label_15)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_12.addWidget(self.label_12)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_12.addWidget(self.lineEdit_11)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setEditable(True)
        self.comboBox_4.setObjectName("comboBox_4")
        self.horizontalLayout_7.addWidget(self.comboBox_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_11.addWidget(self.lineEdit_10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_10.addWidget(self.lineEdit_9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_13.addWidget(self.label_13)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setEnabled(True)
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_13.addWidget(self.comboBox_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_14.addWidget(self.label_14)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_14.addWidget(self.checkBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_16.addWidget(self.pushButton_7)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_16.addWidget(self.pushButton_6)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_16.addWidget(self.pushButton_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_18.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 589, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # self.pushButton_5.clicked.connect(self.new_btn)
        self.pushButton_6.clicked.connect(self.delete_btn)
        self.pushButton_7.clicked.connect(self.save_btn)
        self.pushButton_8.clicked.connect(self.cancel_btn)
        self.pushButton_9.clicked.connect(self.search_btn)
        self.tableWidget.itemPressed.connect(self.tableClicked)
        self.comboBox.activated[str].connect(self.OnSelect)
        self.comboBox_4.activated[str].connect(self.OnSelect1)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_16.setText(_translate("MainWindow", "Search"))
        self.pushButton_9.setText(_translate("MainWindow", "Search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item Name"))
        self.label_17.setText(_translate("MainWindow", "Product"))
        self.label.setText(_translate("MainWindow", "Description"))
        self.label_8.setText(_translate("MainWindow", "Metal"))
        self.label_3.setText(_translate("MainWindow", "Rate"))
        self.label_2.setText(_translate("MainWindow", "Purity"))
        self.label_4.setText(_translate("MainWindow", "Quantity"))
        self.label_5.setText(_translate("MainWindow", "Gross Weight"))
        self.label_6.setText(_translate("MainWindow", "Metal Weight"))
        self.label_18.setText(_translate("MainWindow", "Item Ratewise"))
        self.label_15.setText(_translate("MainWindow", "Stone"))
        self.label_12.setText(_translate("MainWindow", "Description"))
        self.label_7.setText(_translate("MainWindow", "Stone:"))
        self.label_11.setText(_translate("MainWindow", "Weight"))
        self.label_10.setText(_translate("MainWindow", "Rate"))
        self.label_13.setText(_translate("MainWindow", "Stone Weightwise"))
        self.label_14.setText(_translate("MainWindow", "Is Soverign"))
        self.pushButton_7.setText(_translate("MainWindow", "Save"))
        self.pushButton_6.setText(_translate("MainWindow", "Delete"))
        self.pushButton_8.setText(_translate("MainWindow", "Cancel"))
