import sys
import os
import inflect
from PyQt5 import QtWidgets,QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import QObject, pyqtSlot,QDate
import sqlite3
import Firm
import Groups
import Items
import Rates
import Valuers
import Change_Password
import Products
import Valuation
import testselection
import testValuationExpert
from docxtpl import DocxTemplate
import datetime
# from threading import *



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

class MyLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(MyLineEdit, self).__init__(parent)

    def focusInEvent(self, e):
        self.selectAll()      



class Ui_Split_Valuation(QtWidgets.QMainWindow):
    val_id=0
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.databaseAccess()
        self.setupUi(self)
        self.default()

    def databaseAccess(self):
        self.connection = sqlite3.connect("MAINDB.db")
        self.cursor=self.connection.cursor()

    def __del__(self):
        self.connection.commit()
        self.connection.close()
    
    def default(self):
        # for i in range(self.tableWidget.rowCount()):
        #     self.tableWidget.removeRow(i)
        self.tableWidget.setRowCount(0)
        self.createRow()
        date=datetime.date.today().strftime('%d-%m-%y')
        self.dateEdit.lineEdit().setText(date)
        self.dateEdit_2.lineEdit().setText(date)
        
        self.lineEdit.setText(str(0))
        self.lineEdit_2.setText(str(0))
        self.lineEdit_3.setText(str(0))
        self.lineEdit_4.setText(str(0))
        self.lineEdit_5.setText(str(0))
        self.lineEdit_6.setText(str(0))
        self.lineEdit_7.setText(str(0))
        self.lineEdit_8.setText(str(0))
        self.lineEdit_9.setText(str(0))
        self.lineEdit_10.setText(str(0))
        self.lineEdit_11.setText(str(0))
        self.lineEdit_12.setText(str(0))
        self.lineEdit_13.setText(str(0))
        self.lineEdit_14.setText(str(0))
        self.lineEdit_15.setText(str(0))
        self.lineEdit_16.setText(str(0))
        self.lineEdit_17.setText(str(0))
        self.lineEdit_18.setText(str(0))
        self.lineEdit_19.setText(str(0))
        self.lineEdit_20.setText(str(0))
        self.lineEdit_21.setText(str(0))
        self.lineEdit_22.setText(str(0))
        self.lineEdit_23.setText(str(0))
        self.lineEdit_24.setText(str(0))
        self.lineEdit_25.setText(str(0))
        self.lineEdit_26.setText(str(0))
        self.lineEdit_27.setText(str(0))
    

    def RatePopup(self):
        self.popup=testselection.Ui_Selection(self,'Rates')
        self.popup.show()
    
    def ReturnRate(self):
        format_str='''SELECT Row FROM Popup;'''
        self.cursor.execute(format_str)
        res=self.cursor.fetchone()
        print(res[0])
        format_str='''SELECT * FROM Rates WHERE Rates_Id={id};'''
        sql_command=format_str.format(id=res[0])
        self.cursor.execute(sql_command)
        res=self.cursor.fetchone()
        print(res[0])
        self.lineEdit.setText(str(res[3]))
        self.lineEdit_2.setText(str(res[4]))
        self.lineEdit_3.setText(str(res[5]))
        self.lineEdit_4.setText(str(res[6]))
        self.lineEdit_5.setText(str(res[7]))
        self.lineEdit_6.setText(str(res[8]))

    def FirmPopup(self):
        self.popup=testselection.Ui_Selection(self,'Firms')
        self.popup.show()
    
    def ReturnFirm(self):
        format_str='''SELECT Row FROM Popup;'''
        self.cursor.execute(format_str)
        res=self.cursor.fetchone()
        print(res[0])
        format_str='''SELECT * FROM Firms WHERE Firm_id={id};'''
        sql_command=format_str.format(id=res[0])
        self.cursor.execute(sql_command)
        res=self.cursor.fetchone()
        print(res[0])
        self.lineEdit_10.setText(res[1])
        self.lineEdit_11.setText(res[2])
        self.lineEdit_12.setCursorPosition(0)
    
    def CustomerPopup(self):
        self.popup=testselection.Ui_Selection(self,'Valuation',1)
        self.popup.show()
    
    def ReturnCustomer(self):
        format_str='''SELECT Row FROM Popup;'''
        self.cursor.execute(format_str)
        res=self.cursor.fetchone()
        print(res[0])
        format_str='''SELECT * FROM Valuation WHERE Valuation_id={id};'''
        sql_command=format_str.format(id=res[0])
        self.cursor.execute(sql_command)
        res=self.cursor.fetchone()
        print(res[0])
        self.lineEdit_13.setText(res[12])
        self.lineEdit_14.setText(str(res[13]))
        self.lineEdit_15.setText(res[14])

    def ValuerPopup(self):
        self.popup1=testselection.Ui_Selection(self,'Valuers')
        self.popup1.show()
    
    def ReturnValuers(self):
        format_str='''SELECT Row FROM Popup;'''
        self.cursor.execute(format_str)
        res=self.cursor.fetchone()
        print(res[0])
        format_str='''SELECT * FROM Valuers WHERE Valuer_id={id};'''
        sql_command=format_str.format(id=res[0])
        self.cursor.execute(sql_command)
        res=self.cursor.fetchone()
        print(res[0])
        self.lineEdit_8.setText(res[1])
        self.lineEdit_9.setText(res[2])

    def ValuationPopup(self):
        self.popup=testselection.Ui_Selection(self,'Valuation')
        self.popup.show()

        

    # @pyqtSlot()
    def ReturnValuation(self):
        
        # t=Thread(target=self.ValuationPopup1)
        # t.start()
        # while(t.is_alive()==True):
        #     pass
        
        # self.popup=testselection.Ui_Selection('Valuation')
        # print("C")
        # # self.popup.exec()
        # self.popup.show()
        # print("D")
        # # del self.popup
        format_str='''SELECT Row FROM Popup;'''
        self.cursor.execute(format_str)
        res=self.cursor.fetchone()
        # print()
        print(res[0])
        format_str='''SELECT * FROM Valuation WHERE Valuation_id={id};'''
        sql_command=format_str.format(id=res[0])
        self.cursor.execute(sql_command)
        res=self.cursor.fetchone()
        print(res[0])
        Ui_Split_Valuation.val_id=res[0]
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
        self.lineEdit_15.setText(str(res[14]))
        self.lineEdit_10.setText(str(res[15]))
        self.lineEdit_11.setText(str(res[16]))
        self.lineEdit_12.setText(str(res[17]))
        self.lineEdit_17.setText(str(res[18]))
        self.lineEdit_19.setText(str(res[19]))
        self.lineEdit_25.setText(str(res[20]))
        self.lineEdit_22.setText(str(res[21]))
        self.lineEdit_18.setText(str(res[22]))
        self.lineEdit_20.setText(str(res[23]))
        self.lineEdit_26.setText(str(res[24]))
        self.lineEdit_23.setText(str(res[25]))
        self.lineEdit_16.setText(str(res[26]))
        self.lineEdit_21.setText(str(res[27]))
        self.lineEdit_24.setText(str(res[28]))
        self.lineEdit_27.setText(str(res[29]))

        format_str='''SELECT * FROM Products WHERE Valuation_Id='{id}';'''
        sql_command=format_str.format(id=Ui_Split_Valuation.val_id)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchall()
        print("AAA")
        print(res)
        # for i in range(self.tableWidget.rowCount()+5):
        #     self.tableWidget.removeRow(i)
        self.tableWidget.setRowCount(0)
        # self.tableWidget.setColumnCount(0)
        c=0
        print(self.tableWidget.rowCount())
        for i in res:
            print(i[2])
            print("JNWD")
            self.createRow()
            print("JNadwdWD")
            print(self.tableWidget.rowCount())
            self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,0).setText(i[2])
            self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,1).setText(str(format((i[3]),'.2f')))
            self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,2).setText(str(format((i[4]),'.2f')))
            self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,3).setText(str(i[5]))
            self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,4).setText(str(format((i[6]),'.2f')))
            self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,5).setText(str(format((i[7]),'.2f')))
            self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,6).setText(str(format(round(i[8]),'.2f')))
            self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,7).setText(str(i[9]))
            self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,8).setText(str(format(i[10],'.2f')))
            self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,9).setText(str(format((i[11]))))
            self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,10).setText(str(format(round(i[12]),'.2f')))
            self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,11).setText(str(format(round(i[13]),'.2f')))
            self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,12).lineEdit().setText(str(i[14]))
            self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,13).lineEdit().setText(str(i[15]))
            self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,14).lineEdit().setText(str(i[16]))
            if(i[17]==1):
                self.tableWidget.cellWidget(c,15).setChecked()
            else:
                pass
            c=c+1

    
    def createCompleter(self,table,index):
        format_str='''SELECT * FROM {table};'''
        sql_command=format_str.format(table=table)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchall()
        data=[]
        for i in res:
            data.append(i[index])
        return QCompleter(data)

    
    def autoRate(self):
        self.curr_row=self.tableWidget.currentRow()
        name=self.tableWidget.cellWidget(self.curr_row,0).text()
        format_str='''SELECT Metal FROM Items WHERE Item_Description='{name}';'''
        sql_command=format_str.format(name=name)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchone()
        print(res)

        if(res is None):
            self.tableWidget.cellWidget(self.curr_row,1).setText(self.lineEdit.text())
            self.tableWidget.cellWidget(self.curr_row,12).lineEdit().setText('Gold')
        else:
            if(res[0]=='Platinum'):
                self.tableWidget.cellWidget(self.curr_row,1).setText(self.lineEdit_3.text())
                self.tableWidget.cellWidget(self.curr_row,12).lineEdit().setText(res[0])
            elif(res[0]=='Silver'):
                self.tableWidget.cellWidget(self.curr_row,1).setText(self.lineEdit_2.text())
                self.tableWidget.cellWidget(self.curr_row,12).lineEdit().setText(res[0])
            else:
                self.tableWidget.cellWidget(self.curr_row,1).setText(self.lineEdit.text())
                self.tableWidget.cellWidget(self.curr_row,12).lineEdit().setText(res[0])
        print(name)
        self.autoUpdateTotals()
    
    def autoMetalWt(self):
        self.curr_row=self.tableWidget.currentRow()
        self.tableWidget.cellWidget(self.curr_row,5).setText(str(format(float(self.tableWidget.cellWidget(self.curr_row,4).text()),'.2f')))
            # self.tableWidget.cellWidget.
        self.autoUpdateTotals()

        
    def autoChangeOnStoneEntered(self):
        self.curr_row=self.tableWidget.currentRow()
        gross=float(self.tableWidget.cellWidget(self.curr_row,4).text())
        # metal=float(self.tableWidget.cellWidget(self.curr_row,5).text())
        stone=float(self.tableWidget.cellWidget(self.curr_row,8).text())
        self.tableWidget.cellWidget(self.curr_row,5).setText(str(format(gross-stone,'.2f')))
        self.autoValue()
        self.autoUpdateTotals()
    
    def autoValue(self):
        # self.autoRate()
        # self.autoStoneWeight()
        self.curr_row=self.tableWidget.currentRow()
        rate=float(self.tableWidget.cellWidget(self.curr_row,1).text())
        purity=float(self.tableWidget.cellWidget(self.curr_row,2).text())
        wt=float(self.tableWidget.cellWidget(self.curr_row,5).text())
        metal=self.tableWidget.cellWidget(self.curr_row,12).lineEdit().text()
        if(metal=='Gold' or metal=='Platinum'):
            value=(purity*rate*wt)/240
        else:
            value=(purity*rate*wt)/100000
        self.tableWidget.cellWidget(self.curr_row,6).setText(str(format(round(value),'.2f')))
        self.autoTotal()
        self.autoUpdateTotals()
    
    
    def autoStoneRate(self):
        self.curr_row=self.tableWidget.currentRow()
        s_name=self.tableWidget.cellWidget(self.curr_row,7).text()
        if(s_name in 'Diamond' or s_name in 'diamond'):
            self.tableWidget.cellWidget(self.curr_row,7).setText("Diamond")
            self.tableWidget.cellWidget(self.curr_row,9).setText(self.lineEdit_4.text())
            self.tableWidget.cellWidget(self.curr_row,14).lineEdit().setText("Carats")
        self.autoUpdateTotals()

    def autoStoneValue(self):
        self.curr_row=self.tableWidget.currentRow()
        wt=float(self.tableWidget.cellWidget(self.curr_row,8).text())
        rate=float(self.tableWidget.cellWidget(self.curr_row,9).text())
        value=wt*rate
        self.tableWidget.cellWidget(self.curr_row,10).setText(str(format(round(value),'.2f')))
        self.autoUpdateTotals()
    
    def autoTotal(self):
        self.curr_row=self.tableWidget.currentRow()
        metal_total=float(self.tableWidget.cellWidget(self.curr_row,6).text())
        stone_total=float(self.tableWidget.cellWidget(self.curr_row,10).text())
        total=metal_total+stone_total
        self.tableWidget.cellWidget(self.curr_row,11).setText(str(format(round(total),'.2f')))
        self.autoUpdateTotals()
    
    def autoItemRateWise(self,a):
        self.curr_row=self.tableWidget.currentRow()
        # a=self.tableWidget.cellWidget(self.curr_row,13).lineEdit().text()
        if(a=='Quantitywise'):
            quantity=int(self.tableWidget.cellWidget(self.curr_row,3).text())
            self.autoValue()
            metal_value=float(self.tableWidget.cellWidget(self.curr_row,6).text())
            self.tableWidget.cellWidget(self.curr_row,6).setText(str(format(round(metal_value*quantity),'.2f')))
            self.autoTotal()
            self.autoUpdateTotals()
        else:
            self.autoValue()
            self.autoTotal()
            self.autoUpdateTotals()
    

    def autoStoneWeightwise(self,a):
        self.curr_row=self.tableWidget.currentRow()
        if(a=='Carats'):
            self.autoStoneValue()
            self.autoTotal()
            pass
        else:
            self.curr_row=self.tableWidget.currentRow()
            wt=float(self.tableWidget.cellWidget(self.curr_row,8).text())/5
            rate=float(self.tableWidget.cellWidget(self.curr_row,9).text())*5
            value=wt*rate
            self.tableWidget.cellWidget(self.curr_row,10).setText(str(format(round(value),'.2f')))
            self.autoTotal()
        self.autoUpdateTotals()



    def autoChangeMetal(self,a):
        self.curr_row=self.tableWidget.currentRow()
        if(a=='Gold' or a=='Platinum'):
            if(a=='Gold'):
                self.tableWidget.cellWidget(self.curr_row,1).setText(self.lineEdit.text())
                rate=float(self.tableWidget.cellWidget(self.curr_row,1).text())/10
            else:
                self.tableWidget.cellWidget(self.curr_row,1).setText(self.lineEdit_3.text())
                rate=float(self.tableWidget.cellWidget(self.curr_row,1).text())
        
            purity=float(self.tableWidget.cellWidget(self.curr_row,2).text())
            wt=float(self.tableWidget.cellWidget(self.curr_row,5).text())
            value=(purity*rate*wt)/24
            self.tableWidget.cellWidget(self.curr_row,6).setText(str(format(round(value),'.2f')))
            stone=float(self.tableWidget.cellWidget(self.curr_row,10).text())
            self.tableWidget.cellWidget(self.curr_row,11).setText(str(format(round(stone+value),'.2f')))

        else:
            self.tableWidget.cellWidget(self.curr_row,1).setText(self.lineEdit_2.text())
            rate=float(self.tableWidget.cellWidget(self.curr_row,1).text())/1000
            purity=float(self.tableWidget.cellWidget(self.curr_row,2).text())
            wt=float(self.tableWidget.cellWidget(self.curr_row,5).text())
            value=(purity*rate*wt)/100
            self.tableWidget.cellWidget(self.curr_row,6).setText(str(format(round(value),'.2f')))
            stone=float(self.tableWidget.cellWidget(self.curr_row,10).text())
            self.tableWidget.cellWidget(self.curr_row,11).setText(str(format(round(stone+value),'.2f')))
        # self.autoValue()
        self.autoUpdateTotals()
            
    
    def autoUpdateTotals(self):
        gold_qt=0
        gold_gross=0
        gold_metal=0
        gold_value=0
        silver_qt=0
        silver_gross=0
        silver_metal=0
        silver_value=0
        stone_qt=0
        stone_gross=0
        # silver_metal=0
        stone_value=0
        grand_total=0
        for i in range(self.tableWidget.rowCount()):
            if(self.tableWidget.cellWidget(i,12).lineEdit().text()=='Gold'):

                gold_qt=gold_qt+int(self.tableWidget.cellWidget(i,3).text())
                gold_gross=gold_gross+float(self.tableWidget.cellWidget(i,4).text())
                gold_metal=gold_metal+float(self.tableWidget.cellWidget(i,5).text())
                gold_value=gold_value+float(self.tableWidget.cellWidget(i,6).text())
            
            if(self.tableWidget.cellWidget(i,12).lineEdit().text()=='Silver'):
                silver_qt=silver_qt+int(self.tableWidget.cellWidget(i,3).text())
                silver_gross=silver_gross+float(self.tableWidget.cellWidget(i,4).text())
                silver_metal=silver_metal+float(self.tableWidget.cellWidget(i,5).text())
                silver_value=silver_value+float(self.tableWidget.cellWidget(i,6).text())

            if(self.tableWidget.cellWidget(i,7).text()=='Diamond'):
                stone_qt=stone_qt+int(self.tableWidget.cellWidget(i,3).text())
                stone_gross=stone_gross+float(self.tableWidget.cellWidget(i,8).text())
                # silver_metal=silver_metal+float(self.tableWidget.cellWidget(i,5).text())
                stone_value=stone_value+float(self.tableWidget.cellWidget(i,10).text())
            
            grand_total=grand_total+float(self.tableWidget.cellWidget(i,11).text())
            
        self.lineEdit_17.setText(str(format(round(gold_qt),'.2f')))
        self.lineEdit_19.setText(str(format(round(gold_gross),'.2f')))
        self.lineEdit_25.setText(str(format(round(gold_metal),'.2f')))
        self.lineEdit_22.setText(str(format(round(gold_value),'.2f')))
        self.lineEdit_18.setText(str(format(round(silver_qt),'.2f')))
        self.lineEdit_20.setText(str(format(round(silver_gross),'.2f')))
        self.lineEdit_26.setText(str(format(round(silver_metal),'.2f')))
        self.lineEdit_23.setText(str(format(round(silver_value),'.2f')))    
        self.lineEdit_16.setText(str(format(round(stone_qt),'.2f')))
        self.lineEdit_21.setText(str(format(round(stone_gross),'.2f')))
        self.lineEdit_24.setText(str(format(round(stone_value),'.2f')))
        self.lineEdit_27.setText(str(format(round(grand_total),'.2f')))
        # self.lineEdit_22.setText(str(gold_value))
    
    def deleteRow(self):
        # row = self.tableWidget.indexAt(self.tableWidget.currentRow())
        print("sbjhbsjhbfwsec")
        print(self.tableWidget.currentRow())
        self.tableWidget.removeRow(self.tableWidget.currentRow())
        print(self.tableWidget.currentRow())
        # self.tableWidget.setRowCount(self.-1)
    
    def SetCursor(self):
        self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,0).setCursorPosition(0)
    
    def ColumnIncrementer(self):
        self.curr_row=self.tableWidget.currentRow()
        self.curr_col=self.tableWidget.currentColumn()
        self.tableWidget.setCurrentCell(self.curr_row,self.curr_col+1)

    
    def createRow(self):
        # self.save()
        print("A")
        self.tableWidget.insertRow(self.tableWidget.rowCount())
        self.line=QLineEdit()
        self.line.setObjectName("LINE")
        completer=self.createCompleter('Items',1)
        # completer.activated.connect(self.autoRate)
        # self.line.editingFinished.connect(lambda:self.line.setCursorPosition(4))
        self.line.editingFinished.connect(self.SetCursor)
        self.line.editingFinished.connect(self.autoRate)
        self.line.setCompleter(completer)
        self.line.setCursorPosition(0)
        self.line.returnPressed.connect(self.ColumnIncrementer)
        # 8self.onlyInt = QIntValidator8
        self.tableWidget.setCellWidget(self.tableWidget.rowCount()-1,0,self.line)
        self.line=QLineEdit()
        self.line.setObjectName("LINE")
        self.line.setText(str(0))
        self.line.returnPressed.connect(self.ColumnIncrementer)
        self.validate=QtGui.QDoubleValidator()
        self.line.setValidator(self.validate)
        self.tableWidget.setCellWidget(self.tableWidget.rowCount()-1,1,self.line)
        self.line=QLineEdit()
        self.line.setObjectName("LINE")
        self.line.setText(str(19.20))
        self.line.editingFinished.connect(self.autoTotal)
        self.line.editingFinished.connect(self.autoUpdateTotals)
        self.line.returnPressed.connect(self.ColumnIncrementer)
        self.validate=QtGui.QDoubleValidator()
        self.line.setValidator(self.validate)
        self.tableWidget.setCellWidget(self.tableWidget.rowCount()-1,2,self.line)
        self.line=QLineEdit()
        self.line.setObjectName("LINE")
        self.line.setText(str(1))
        self.line.returnPressed.connect(self.ColumnIncrementer)
        self.validate=QtGui.QIntValidator()
        self.line.setValidator(self.validate)
        self.tableWidget.setCellWidget(self.tableWidget.rowCount()-1,3,self.line)
        self.line=MyLineEdit()
        self.line.setObjectName("LINE")
        self.line.setText(str(0.0))
        # self.line.mousePressEvent = lambda _ : self.line.selectAll()
        self.line.editingFinished.connect(self.autoMetalWt)
        self.line.returnPressed.connect(self.ColumnIncrementer)
        self.validate=QtGui.QDoubleValidator()
        self.line.setValidator(self.validate)
        self.tableWidget.setCellWidget(self.tableWidget.rowCount()-1,4,self.line)
        self.line=MyLineEdit()
        self.line.setObjectName("LINE")
        self.line.setText(str(0))
        # self.line.returnPressed.connect(self.autoValue)
        self.line.editingFinished.connect(self.autoValue)
        self.line.returnPressed.connect(self.ColumnIncrementer)
        self.validate=QtGui.QDoubleValidator()
        self.line.setValidator(self.validate)
        self.tableWidget.setCellWidget(self.tableWidget.rowCount()-1,5,self.line)
        self.line=QLineEdit()
        self.line.setObjectName("LINE")
        self.line.setText(str(0))
        self.line.returnPressed.connect(self.ColumnIncrementer)
        self.validate=QtGui.QDoubleValidator()
        self.line.setValidator(self.validate)
        self.tableWidget.setCellWidget(self.tableWidget.rowCount()-1,6,self.line)
        self.line=MyLineEdit()
        self.line.setObjectName("LINE")
        self.line.setText("...")
        # self.line.selectAll()
        print(self.line.selectedText())
        self.line.editingFinished.connect(self.autoStoneRate)
        self.line.returnPressed.connect(self.ColumnIncrementer)
        completer=QCompleter(['Diamond','Enamel','Kundan','Pearl','Ruby','Manik','Panna','Moti','Pukhraj','Gomed','Neelam'])
        completer.setCaseSensitivity(0)
        self.line.setCompleter(completer)
        self.tableWidget.setCellWidget(self.tableWidget.rowCount()-1,7,self.line)
        self.line=MyLineEdit()
        self.line.setObjectName("LINE")
        self.line.setText(str(0))
        self.line.editingFinished.connect(self.autoStoneValue)
        self.line.editingFinished.connect(self.autoTotal)
        self.line.editingFinished.connect(self.autoChangeOnStoneEntered)
        self.line.returnPressed.connect(self.ColumnIncrementer)
        self.validate=QtGui.QDoubleValidator()
        self.line.setValidator(self.validate)
        self.tableWidget.setCellWidget(self.tableWidget.rowCount()-1,8,self.line)
        self.line=QLineEdit()
        self.line.setObjectName("LINE")
        self.line.setText(str(0))
        self.line.editingFinished.connect(self.autoStoneValue)
        self.line.editingFinished.connect(self.autoTotal)
        self.line.editingFinished.connect(self.autoChangeOnStoneEntered)
        self.line.returnPressed.connect(self.ColumnIncrementer)
        self.validate=QtGui.QDoubleValidator()
        self.line.setValidator(self.validate)
        self.tableWidget.setCellWidget(self.tableWidget.rowCount()-1,9,self.line)
        self.line=QLineEdit()
        self.line.setObjectName("LINE")
        self.line.setText(str(0))
        self.line.returnPressed.connect(self.ColumnIncrementer)
        self.validate=QtGui.QDoubleValidator()
        self.line.setValidator(self.validate)
        self.tableWidget.setCellWidget(self.tableWidget.rowCount()-1,10,self.line)
        self.line=QLineEdit()
        self.line.setObjectName("LINE")
        self.line.setText(str(0))
        self.line.returnPressed.connect(self.ColumnIncrementer)
        self.validate=QtGui.QDoubleValidator()
        self.line.setValidator(self.validate)
        self.tableWidget.setCellWidget(self.tableWidget.rowCount()-1,11,self.line)
        self.comboBox_3 = QComboBox()
        self.comboBox_3.setEditable(True)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("Gold")
        self.comboBox_3.addItem("Silver")
        self.comboBox_3.addItem("Platinum")
        self.comboBox_3.lineEdit().setText("Gold")
        print("B")
        self.comboBox_3.activated[str].connect(self.autoChangeMetal)
        self.tableWidget.setCellWidget(self.tableWidget.rowCount()-1,12,self.comboBox_3)
        self.comboBox_4 = QtWidgets.QComboBox()
        self.comboBox_4.setEditable(True)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("Weightwise")
        self.comboBox_4.addItem("Quantitywise")
        self.comboBox_4.lineEdit().setText("Weightwise")
        self.comboBox_4.activated[str].connect(self.autoItemRateWise)
        # self.comboBox_4.addItem("Platinum")
        self.tableWidget.setCellWidget(self.tableWidget.rowCount()-1,13,self.comboBox_4)
        self.comboBox_5 = QtWidgets.QComboBox()
        self.comboBox_5.setEditable(True)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("Grams")
        self.comboBox_5.addItem("Carats")
        self.comboBox_5.lineEdit().setText("Grams")
        self.comboBox_5.activated[str].connect(self.autoStoneWeightwise)
        # self.comboBox_5.addItem("Platinum")
        self.tableWidget.setCellWidget(self.tableWidget.rowCount()-1,14,self.comboBox_5)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.tableWidget.setCellWidget(self.tableWidget.rowCount()-1,15,self.checkBox)
        # self.tableWidget.cellChanged.connect(self.print)
        self.comboBox_6 = QComboBox()
        self.comboBox_6.setEditable(True)
        self.comboBox_6.setObjectName("comboBox_6")
        # self.comboBox_6.addItem("Gold")
        # self.comboBox_6.addItem("Silver")
        # self.comboBox_6.addItem("Platinum")
        # self.comboBox_6.lineEdit().setText("Gold")
        self.tableWidget.setCellWidget(self.tableWidget.currentRow()+1,16,self.comboBox_6)
    

    def createValuation(self,data):
        rate_date=self.dateEdit.lineEdit().text()
        valuation_date=self.dateEdit_2.lineEdit().text()
        gold=float(self.lineEdit.text())
        silver=float(self.lineEdit_2.text())
        platinum=float(self.lineEdit_3.text())
        diamond=float(self.lineEdit_4.text())
        soverign=float(self.lineEdit_5.text())
        coin=float(self.lineEdit_6.text())
        V_Name=self.lineEdit_8.text()
        V_Reg_No=self.lineEdit_9.text()
        V_Purpose=self.lineEdit_7.text()
        Reference=self.lineEdit_13.text()
        C_Pan=int(self.lineEdit_14.text())
        C_Address=self.lineEdit_15.text()
        F_Name=self.lineEdit_10.text()
        F_Address=self.lineEdit_11.text()
        OS_With=self.lineEdit_12.text()
        Gold_total=float(self.lineEdit_17.text())
        Gold_gross=float(self.lineEdit_19.text())
        Gold_metal=float(self.lineEdit_25.text())
        Gold_value=float(self.lineEdit_22.text())
        Silver_total=float(self.lineEdit_18.text())
        Silver_gross=float(self.lineEdit_20.text())
        Silver_metal=float(self.lineEdit_26.text())
        Silver_value=float(self.lineEdit_23.text())
        Diamond_total=float(self.lineEdit_16.text())
        Diamond_gross=float(self.lineEdit_21.text())
        Diamond_value=float(self.lineEdit_24.text())
        Grand_Total=float(self.lineEdit_27.text())
        sql_command='''SELECT id FROM Last_Valuation_id;'''
        self.cursor.execute(sql_command)
        res=self.cursor.fetchone()
        id=res[0]+1
        for i in data:
            C_Name=i
            format_str='''INSERT INTO `Valuation`(`Valuation_id`,`Valuation_date`,`Rate_date`,`Gold_rate`,`Silver_rate`,`Platinum_rate`,`Soverign_rate`,`Coin_rate`,`Diamond_rate`,`Valuer_name`,`Valuer_reg_no`,`Purpose`,`Customer_name`,`Customer_Pan`,`Customer_address`,`Firm_name`,`Firm_address`,`OS`,`Gold_total`,`Gold_gross`,`Gold_metal`,`Gold_value`,`Silver_total`,`Silver_gross`,`Silver_metal`,`Silver_value`,`Stone_total`,`Stone_gross`,`Stone_value`,`Grand_Total`,`Reference_Name`) VALUES ({id},'{valuation_date}','{rate_date}',{gold},{silver},{platinum},{soverign},{coin},{diamond},'{V_Name}',{V_Reg_No},'{V_Purpose}','{C_Name}','{C_Pan}','{C_Address}','{F_Name}','{F_Address}','{OS_With}',{Gold_total},{Gold_gross},{Gold_metal},{Gold_value},{Silver_total},{Silver_gross},{Silver_metal},{Silver_value},{Diamond_total},{Diamond_gross},{Diamond_value},{Grand_Total},'{Reference_Name}');'''
            sql_command=format_str.format(id=id,valuation_date=valuation_date,rate_date=rate_date,gold=gold,silver=silver,platinum=platinum,diamond=diamond,soverign=soverign,coin=coin,V_Name=V_Name,V_Reg_No=V_Reg_No,V_Purpose=V_Purpose,C_Name=C_Name,C_Pan=C_Pan,C_Address=C_Address,F_Name=F_Name,F_Address=F_Address,OS_With=OS_With,Gold_total=Gold_total,Gold_gross=Gold_gross,Gold_metal=Gold_metal,Gold_value=Gold_value,Silver_total=Silver_total,Silver_gross=Silver_gross,Silver_metal=Silver_metal,Silver_value=Silver_value,Diamond_total=Diamond_total,Diamond_gross=Diamond_gross,Diamond_value=Diamond_value,Grand_Total=Grand_Total,Reference_Name=Reference)
            self.cursor.execute(sql_command)

            products=data[i]
            for j in products:
                description=j[0]
                metal_rate=j[1]
                purity=j[2]
                qty=j[3]
                gross_wt=j[4]
                metal_wt=j[5]
                metal_value=j[6]
                s_description=j[7]
                s_wt=j[8]
                s_rate=j[9]
                s_value=j[10]
                total=j[11]
                metal=j[12]
                item_ratewise=j[13]
                stone_weightwise=j[14]
                is_soverign=j[15]
                format_str='''INSERT INTO Products(Valuation_Id,Description,Rate,Purity,Quantity,Gross_Wt,Metal_Wt,Metal_Value,Stone_Description,Stone_Wt,Stone_Rate,Stone_Value,Total_Value,Metal,Item_Ratewise,Stone_Weightwise,Is_Soverign) VALUES ({id},'{item_description}',{rate},{purity},{quantity},{gross_wt},{metal_weight},{metal_value},'{stone_description}',{stone_wt},{stone_rate},{stone_value},{total_value},'{metal}','{item_ratewise}','{stone_weightwise}',{is_soverign});'''
                sql_command=format_str.format(id=id,item_description=description,rate=metal_rate,purity=purity,quantity=qty,gross_wt=gross_wt,metal_weight=metal_wt,metal_value=metal_value,stone_description=s_description,stone_wt=s_wt,stone_rate=s_rate,stone_value=s_value,total_value=total,metal=metal,item_ratewise=item_ratewise,stone_weightwise=stone_weightwise,is_soverign=is_soverign)
                self.cursor.execute(sql_command)
            id=id+1
        format_str='''UPDATE Last_Valuation_id SET id={id};'''
        sql_command=format_str.format(id=id)
        self.cursor.execute(sql_command)
        QtWidgets.QMessageBox.information(self, 'Success', 'New Split Created')
        self.connection.commit()
        # self.default()


    def Split_Btn(self):
        data={}
        for i in range(self.tableWidget.rowCount()):
            data[self.tableWidget.cellWidget(i,16).lineEdit().text()]=[]

        for i in range(self.tableWidget.rowCount()):
            row=[]
            for j in range(self.tableWidget.columnCount()):
                #DROPBOX
                if(j==12 or j==13 or j==14):
                    row.append(self.tableWidget.cellWidget(i,j).lineEdit().text())
                #CheckBox
                elif(j==15):
                    if(self.tableWidget.cellWidget(i,j).isChecked()):
                        row.append(1)
                    else:
                        row.append(0)
                #STRINGS
                elif(j==0 or j==7):
                    row.append(self.tableWidget.cellWidget(i,j).text())
                elif(j==3):
                    row.append(int(self.tableWidget.cellWidget(i,j).text()))
                elif(j==16):
                    pass
                else:
                    row.append(float(self.tableWidget.cellWidget(i,j).text()))
                
            data[self.tableWidget.cellWidget(i,16).lineEdit().text()].append(row)
        print(data)

        self.createValuation(data)
    

        
        
        






    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1328, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout()
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout()
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate(2019, 8, 6))
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_5.addWidget(self.dateEdit)
        self.toolButton_6 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_6.setObjectName("toolButton_6")
        self.horizontalLayout_5.addWidget(self.toolButton_6)
        spacerItem = QtWidgets.QSpacerItem(356, 18, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setDate(QtCore.QDate(2019, 8, 6))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout_6.addWidget(self.dateEdit_2)
        self.toolButton_7 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_7.setObjectName("toolButton_7")
        self.horizontalLayout_6.addWidget(self.toolButton_7)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_3.addWidget(self.lineEdit_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_4.addWidget(self.lineEdit_3)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_5.addWidget(self.lineEdit_4)
        self.horizontalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_6.addWidget(self.lineEdit_5)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_7.addWidget(self.lineEdit_6)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        spacerItem3 = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.groupBox_4)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setObjectName("label_10")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_8.addWidget(self.lineEdit_8)
        self.toolButton_8 = QtWidgets.QToolButton(self.groupBox_4)
        self.toolButton_8.setObjectName("toolButton_8")
        self.horizontalLayout_8.addWidget(self.toolButton_8)
        self.formLayout_4.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_8)
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label_11.setObjectName("label_11")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setObjectName("label_9")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.horizontalLayout_14.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.formLayout_5 = QtWidgets.QFormLayout(self.groupBox_5)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_15 = QtWidgets.QLabel(self.groupBox_5)
        self.label_15.setObjectName("label_15")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.horizontalLayout_9.addWidget(self.lineEdit_13)
        self.toolButton_9 = QtWidgets.QToolButton(self.groupBox_5)
        self.toolButton_9.setObjectName("toolButton_9")
        self.horizontalLayout_9.addWidget(self.toolButton_9)
        self.formLayout_5.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_9)
        self.label_16 = QtWidgets.QLabel(self.groupBox_5)
        self.label_16.setObjectName("label_16")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.label_17 = QtWidgets.QLabel(self.groupBox_5)
        self.label_17.setObjectName("label_17")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_14)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_15)
        self.horizontalLayout_14.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName("groupBox_6")
        self.formLayout_6 = QtWidgets.QFormLayout(self.groupBox_6)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_25 = QtWidgets.QLabel(self.groupBox_6)
        self.label_25.setObjectName("label_25")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_10.addWidget(self.lineEdit_10)
        self.toolButton_10 = QtWidgets.QToolButton(self.groupBox_6)
        self.toolButton_10.setObjectName("toolButton_10")
        self.horizontalLayout_10.addWidget(self.toolButton_10)
        self.formLayout_6.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_10)
        self.label_26 = QtWidgets.QLabel(self.groupBox_6)
        self.label_26.setObjectName("label_26")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_11)
        self.label_27 = QtWidgets.QLabel(self.groupBox_6)
        self.label_27.setObjectName("label_27")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_12)
        self.horizontalLayout_14.addWidget(self.groupBox_6)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem4)
        self.verticalLayout_8.addLayout(self.horizontalLayout_14)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem5)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setAutoScroll(True)
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
        self.verticalLayout_8.addWidget(self.tableWidget)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.verticalLayout_31.addLayout(self.verticalLayout_9)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_21.addItem(spacerItem6)
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_21.addWidget(self.label_29)
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_21.addWidget(self.label_30)
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_21.addWidget(self.label_31)
        self.horizontalLayout_17.addLayout(self.verticalLayout_21)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        spacerItem7 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_22.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_22.addItem(spacerItem8)
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_22.addWidget(self.label_32)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.verticalLayout_23.addWidget(self.lineEdit_17)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.verticalLayout_23.addWidget(self.lineEdit_18)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.verticalLayout_23.addWidget(self.lineEdit_16)
        self.verticalLayout_22.addLayout(self.verticalLayout_23)
        self.horizontalLayout_17.addLayout(self.verticalLayout_22)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_24.addItem(spacerItem9)
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setObjectName("label_33")
        self.verticalLayout_24.addWidget(self.label_33)
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.verticalLayout_25.addWidget(self.lineEdit_19)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.verticalLayout_25.addWidget(self.lineEdit_20)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(36)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_21.sizePolicy().hasHeightForWidth())
        self.lineEdit_21.setSizePolicy(sizePolicy)
        self.lineEdit_21.setBaseSize(QtCore.QSize(0, 5))
        self.lineEdit_21.setClearButtonEnabled(False)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.verticalLayout_25.addWidget(self.lineEdit_21)
        self.verticalLayout_24.addLayout(self.verticalLayout_25)
        self.horizontalLayout_17.addLayout(self.verticalLayout_24)
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        spacerItem10 = QtWidgets.QSpacerItem(13, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_26.addItem(spacerItem10)
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_26.addWidget(self.label_34)
        spacerItem11 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_26.addItem(spacerItem11)
        self.lineEdit_25 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.verticalLayout_26.addWidget(self.lineEdit_25)
        self.lineEdit_26 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.verticalLayout_26.addWidget(self.lineEdit_26)
        spacerItem12 = QtWidgets.QSpacerItem(20, 27, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_26.addItem(spacerItem12)
        self.horizontalLayout_17.addLayout(self.verticalLayout_26)
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_27.addItem(spacerItem13)
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_27.addWidget(self.label_35)
        self.verticalLayout_28 = QtWidgets.QVBoxLayout()
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.verticalLayout_28.addWidget(self.lineEdit_22)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.verticalLayout_28.addWidget(self.lineEdit_23)
        self.lineEdit_24 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.verticalLayout_28.addWidget(self.lineEdit_24)
        self.verticalLayout_27.addLayout(self.verticalLayout_28)
        self.horizontalLayout_17.addLayout(self.verticalLayout_27)
        self.verticalLayout_29 = QtWidgets.QVBoxLayout()
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        spacerItem14 = QtWidgets.QSpacerItem(20, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_29.addItem(spacerItem14)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_29.addWidget(self.pushButton_7)
        self.lineEdit_27 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_27.setReadOnly(True)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.verticalLayout_29.addWidget(self.lineEdit_27)
        self.horizontalLayout_17.addLayout(self.verticalLayout_29)
        spacerItem15 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem15)
        self.verticalLayout_30 = QtWidgets.QVBoxLayout()
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_30.addWidget(self.pushButton_8)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_30.addItem(spacerItem16)
        self.horizontalLayout_17.addLayout(self.verticalLayout_30)
        self.verticalLayout_31.addLayout(self.horizontalLayout_17)
        self.verticalLayout_32.addLayout(self.verticalLayout_31)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_32.addItem(spacerItem17)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_19.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_19.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_19.addWidget(self.pushButton_15)
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_19.addWidget(self.pushButton_16)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem18)
        self.verticalLayout_32.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_11.addLayout(self.verticalLayout_32)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1328, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setAllowedAreas(QtCore.Qt.AllToolBarAreas)
        self.toolBar.setFloatable(True)
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
        self.actionValuation = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons8-contract-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionValuation.setIcon(icon4)
        self.actionValuation.setObjectName("actionValuation")
        self.actionMarket_Rates = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons8-us-dollar-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMarket_Rates.setIcon(icon5)
        self.actionMarket_Rates.setObjectName("actionMarket_Rates")
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
        self.actionSplit_Valuation = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons8-separate-document-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSplit_Valuation.setIcon(icon9)
        self.actionSplit_Valuation.setObjectName("actionSplit_Valuation")
        self.toolBar.addAction(self.actionFirm)
        self.toolBar.addAction(self.actionValuer)
        self.toolBar.addAction(self.actionGroups)
        self.toolBar.addAction(self.actionItems)
        self.toolBar.addAction(self.actionValuation)
        self.toolBar.addAction(self.actionSplit_Valuation)
        self.toolBar.addAction(self.actionMarket_Rates)
        self.toolBar.addAction(self.actionChange_Password)
        self.toolBar.addAction(self.actionAbout)
        self.toolBar.addAction(self.actionExit)
        self.toolButton_7.clicked.connect(self.ValuationPopup)
        self.toolButton_8.clicked.connect(self.ValuerPopup)
        self.toolButton_10.clicked.connect(self.FirmPopup)
        self.toolButton_9.clicked.connect(self.CustomerPopup)
        self.toolButton_6.clicked.connect(self.RatePopup)
        self.pushButton_13.clicked.connect(self.Split_Btn)
        self.shortcut = QShortcut(QKeySequence(QtCore.Qt.Key_Insert), self)
        self.shortcut.activated.connect(self.createRow)
        self.pushButton_8.clicked.connect(self.createRow)
        self.pushButton_14.clicked.connect(self.Document)
        self.pushButton_7.clicked.connect(self.CheckPurityWise)
        self.pushButton_16.clicked.connect(self.close)
        self.pushButton_15.clicked.connect(self.save_btn)
        self.calender1=QCalendarWidget()
        self.calender1.clicked.connect(self.fillRates)
        self.dateEdit.setCalendarWidget(self.calender1)
        self.calender2=QCalendarWidget()
        self.calender2.setMaximumDate(QDate.fromString("22-8-2019", "d-M-yyyy"))
        print(QDate.fromString("22-8-2019", "d-M-yyyy"))
        # self.calender2.clicked.connect(self.MultipleValuation)
        self.dateEdit_2.setCalendarWidget(self.calender2)
        self.shortcut = QShortcut(QKeySequence("Delete"), self)
        self.shortcut.activated.connect(self.deleteRow)
        self.toolBar.actionTriggered[QAction].connect(self.toolbtnpressed)
        self.shortcut = QShortcut(QKeySequence("Ctrl+`"), self)
        self.shortcut.activated.connect(self.ShortcutDisplay)
        self.shortcut1 = QShortcut(QKeySequence("Ctrl+m"), self)
        self.shortcut1.activated.connect(self.OpenExpert)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Rate Date:"))
        self.toolButton_6.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "Valuation Date:"))
        self.toolButton_7.setText(_translate("MainWindow", "..."))
        self.label_3.setText(_translate("MainWindow", "Gold(10 g)"))
        self.label_4.setText(_translate("MainWindow", "Silver(1 kg)"))
        self.label_5.setText(_translate("MainWindow", "Platinum"))
        self.label_6.setText(_translate("MainWindow", "Diamond"))
        self.label_7.setText(_translate("MainWindow", "Soverign"))
        self.label_8.setText(_translate("MainWindow", "Coin"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Valuers"))
        self.label_10.setText(_translate("MainWindow", "Name"))
        self.toolButton_8.setText(_translate("MainWindow", "..."))
        self.label_11.setText(_translate("MainWindow", "R.No."))
        self.label_9.setText(_translate("MainWindow", "Purpose"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Customer"))
        self.label_15.setText(_translate("MainWindow", "Name"))
        self.toolButton_9.setText(_translate("MainWindow", "..."))
        self.label_16.setText(_translate("MainWindow", "Pan No."))
        self.label_17.setText(_translate("MainWindow", "Address"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Firm"))
        self.label_25.setText(_translate("MainWindow", "Name"))
        self.toolButton_10.setText(_translate("MainWindow", "..."))
        self.label_26.setText(_translate("MainWindow", "Address"))
        self.label_27.setText(_translate("MainWindow", "O/S With"))
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
        item.setText(_translate("MainWindow", "Wt (Stone)"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Rate(Stone)"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Value(Stone)"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Total Value"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Metal"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Item Ratewise"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Stone Weightwise"))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Is Soverign"))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "Name"))
        self.label_29.setText(_translate("MainWindow", "Gold"))
        self.label_30.setText(_translate("MainWindow", "Silver"))
        self.label_31.setText(_translate("MainWindow", "Diamond"))
        self.label_32.setText(_translate("MainWindow", "Total Qty."))
        self.label_33.setText(_translate("MainWindow", "Gross Wt."))
        self.label_34.setText(_translate("MainWindow", "Metal Wt."))
        self.label_35.setText(_translate("MainWindow", "Value"))
        self.pushButton_7.setText(_translate("MainWindow", "Check Purity Wise Total"))
        self.pushButton_8.setText(_translate("MainWindow", "Add Item"))
        self.pushButton_13.setText(_translate("MainWindow", "Split Valuation"))
        self.pushButton_14.setText(_translate("MainWindow", "Valuation Bill"))
        self.pushButton_15.setText(_translate("MainWindow", "Save"))
        self.pushButton_16.setText(_translate("MainWindow", "Close"))
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
        self.actionValuation.setText(_translate("MainWindow", "Valuation"))
        self.actionValuation.setToolTip(_translate("MainWindow", "Valuation"))
        self.actionValuation.setShortcut(_translate("MainWindow", "Alt+A"))
        self.actionMarket_Rates.setText(_translate("MainWindow", "Market Rates"))
        self.actionMarket_Rates.setToolTip(_translate("MainWindow", "Market Rates"))
        self.actionMarket_Rates.setShortcut(_translate("MainWindow", "Alt+M"))
        self.actionChange_Password.setText(_translate("MainWindow", "Change Password"))
        self.actionChange_Password.setToolTip(_translate("MainWindow", "Change Password"))
        self.actionChange_Password.setShortcut(_translate("MainWindow", "Alt+P"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout.setToolTip(_translate("MainWindow", "About"))
        self.actionAbout.setShortcut(_translate("MainWindow", "Alt+B"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setToolTip(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Esc"))
        self.actionSplit_Valuation.setText(_translate("MainWindow", "Split Valuation"))
    

    def ShortcutDisplay(self):
        QMessageBox.information(self,'Shortcuts'," Insert : To insert a row \n Delete : To delete a row \n Ctrl+M : To open Valuation Expert \n ")



    def OpenExpert(self):
        self.close()
        self.expert=testValuationExpert.Ui_Valuation_Expert()
        self.expert.show()

    
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

    def SplitTool(self):
        self.close()
        self.split=Ui_Split_Valuation()
        self.split.show()

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
        elif(a.text()=='Split Valuation'):
            self.SplitTool()
        else:
            self.FirmTool()
    

    def minPurity(self,data):
        if(data==[]):
            return 0
        return min(data)

    def count(self,data):
        return len(data)
    
    def CheckPurityWise(self):
        gold=[]
        silver=[]
        platinum=[]
        for i in range(self.tableWidget.rowCount()):
            if(self.tableWidget.cellWidget(i,12).lineEdit().text()=='Gold'):
                gold.append(float(self.tableWidget.cellWidget(i,2).text()))
            elif(self.tableWidget.cellWidget(i,12).lineEdit().text()=='Silver'):
                silver.append(float(self.tableWidget.cellWidget(i,2).text()))
            else:    
                platinum.append(float(self.tableWidget.lineEdit.cellWidget(i,2).text()))
        purity='Gold-'+ str(self.minPurity(gold)) + ' || ' + str(self.count(gold)) +'\n' + 'Silver-'+ str(self.minPurity(silver)) + ' || ' + str(self.count(silver)) +"\n" + 'Platinum-'+ str(self.minPurity(platinum)) + ' || ' + str(self.count(platinum)) 
        QtWidgets.QMessageBox.information(self, 'Purity Wise', purity, QMessageBox.Ok, QMessageBox.Ok)
    
    def Document(self):
        # date=self.comboBox.lineEdit().text()
        # try:
        #     a,valuation_date=self.comboBox_2.lineEdit().text().split("   ")
        # except:
        #     valuation_date=self.comboBox_2.lineEdit().text()
        valuation_date=self.dateEdit_2.lineEdit().text()
        print(valuation_date)
        format_str='''SELECT * FROM Valuation WHERE Valuation_id={id};'''
        sql_command=format_str.format(id=Ui_Valuation.val_id)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchone()
        if(res is None):
            QtWidgets.QMessageBox.warning(self,"Error","Please Save The Valuation First")
        else:
            print(res)
            id=res[0]
            p=inflect.engine()
            context={}
            context={'Name':res[9],'Company':res[14],'Address':res[15],'Reg_No':res[10],'Date':res[1],'Customer_Name':res[12],'Customer_Address':res[13],'OS_With':res[16],'Pupose':res[11],'rate_date':res[2],'In_Words':p.number_to_words(res[29])}

            format_str='''SELECT * FROM Products WHERE Valuation_id={id};'''
            sql_command=format_str.format(id=id)
            self.cursor.execute(sql_command)
            res=self.cursor.fetchall()
            labels=['S.No','Description','Gross Weight','Precious Metal Weight','Value of Precious Metal Contents','Description of precious stone','Weight of Precious Stone','Value Of Stone','Total Value Of each Item']
            contents=[]
            c=1
            for i in res:
                contents.append([c,i[2],i[6],i[7],i[8],i[9],i[10],i[12],i[13]])
                c=c+1
            context['table_content']=contents
            context['labels']=labels
            print(context)
            doc = DocxTemplate("template.docx")
            doc.render(context)
            filename="generated_doc_"+str(id)+".docx"
            doc.save(filename)
            print('SUCCESS')
            # reply=QtWidgets.QMessageBox.question(self, 'Success', 'Report Created')
            buttonReply = QMessageBox.question(self, 'Success', "Report Generated \n Do you want to open the Report?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if(buttonReply==QMessageBox.Yes):
                if(sys.platform=='linux'):
                    command='xdg-open ' + filename
                    os.system(command)
                elif(sys.platform=='darwin'):
                    command='open ' + filename
                    os.system(command)
                else:
                    command='lowriter ' + filename
                    os.system(command)
            else:
                pass
    
    def save_btn(self):
        rate_date=self.dateEdit.lineEdit().text()
        valuation_date=self.dateEdit_2.lineEdit().text()
        # valuation_date=self.comboBox_2.lineEdit().text()
        gold=float(self.lineEdit.text())
        silver=float(self.lineEdit_2.text())
        platinum=float(self.lineEdit_3.text())
        diamond=float(self.lineEdit_4.text())
        soverign=float(self.lineEdit_5.text())
        coin=float(self.lineEdit_6.text())
        V_Name=self.lineEdit_8.text()
        V_Reg_No=self.lineEdit_9.text()
        V_Purpose=self.lineEdit_7.text()
        C_Name=self.lineEdit_13.text()
        C_Pan=int(self.lineEdit_14.text())
        C_Address=self.lineEdit_15.text()
        F_Name=self.lineEdit_10.text()
        F_Address=self.lineEdit_11.text()
        OS_With=self.lineEdit_12.text()
        Gold_total=float(self.lineEdit_17.text())
        Gold_gross=float(self.lineEdit_19.text())
        Gold_metal=float(self.lineEdit_25.text())
        Gold_value=float(self.lineEdit_22.text())
        Silver_total=float(self.lineEdit_18.text())
        Silver_gross=float(self.lineEdit_20.text())
        Silver_metal=float(self.lineEdit_26.text())
        Silver_value=float(self.lineEdit_23.text())
        Diamond_total=float(self.lineEdit_16.text())
        Diamond_gross=float(self.lineEdit_21.text())
        Diamond_value=float(self.lineEdit_24.text())
        Grand_Total=float(self.lineEdit_27.text())

        if(Ui_Split_Valuation.val_id==0):
            sql_command='''SELECT id FROM Last_Valuation_id;'''
            self.cursor.execute(sql_command)
            res=self.cursor.fetchone()
            id=res[0]+1
            for i in range(self.tableWidget.rowCount()):
        # for j in range(self.tableWidget.colorCount()):
                description=self.tableWidget.cellWidget(i,0).text()
                metal_rate=float(self.tableWidget.cellWidget(i,1).text())
                purity=float(self.tableWidget.cellWidget(i,2).text())
                qty=float(self.tableWidget.cellWidget(i,3).text())
                gross_wt=float(self.tableWidget.cellWidget(i,4).text())
                metal_wt=float(self.tableWidget.cellWidget(i,5).text())
                metal_value=float(self.tableWidget.cellWidget(i,6).text())
                s_description=self.tableWidget.cellWidget(i,7).text()
                s_wt=float(self.tableWidget.cellWidget(i,8).text())
                s_rate=float(self.tableWidget.cellWidget(i,9).text())
                s_value=float(self.tableWidget.cellWidget(i,10).text())
                total=float(self.tableWidget.cellWidget(i,11).text())
                metal=self.tableWidget.cellWidget(i,12).lineEdit().text()
                item_ratewise=self.tableWidget.cellWidget(i,13).lineEdit().text()
                stone_weightwise=self.tableWidget.cellWidget(i,14).lineEdit().text()
                if(self.tableWidget.cellWidget(i,15).isChecked()):
                    is_soverign=1
                else:
                    is_soverign=0
                
                format_str='''INSERT INTO Products(Valuation_Id,Description,Rate,Purity,Quantity,Gross_Wt,Metal_Wt,Metal_Value,Stone_Description,Stone_Wt,Stone_Rate,Stone_Value,Total_Value,Metal,Item_Ratewise,Stone_Weightwise,Is_Soverign) VALUES ({id},'{item_description}',{rate},{purity},{quantity},{gross_wt},{metal_weight},{metal_value},'{stone_description}',{stone_wt},{stone_rate},{stone_value},{total_value},'{metal}','{item_ratewise}','{stone_weightwise}',{is_soverign});'''
                sql_command=format_str.format(id=id,item_description=description,rate=metal_rate,purity=purity,quantity=qty,gross_wt=gross_wt,metal_weight=metal_wt,metal_value=metal_value,stone_description=s_description,stone_wt=s_wt,stone_rate=s_rate,stone_value=s_value,total_value=total,metal=metal,item_ratewise=item_ratewise,stone_weightwise=stone_weightwise,is_soverign=is_soverign)
                self.cursor.execute(sql_command)
        
            format_str='''UPDATE Last_Valuation_id SET id={id};'''
            sql_command=format_str.format(id=id)
            self.cursor.execute(sql_command)
            QtWidgets.QMessageBox.information(self, 'Success', 'New Valuation Created')
        else:

            format_str='''UPDATE Valuation SET Valuation_date='{valuation_date}',Rate_date='{rate_date}',Gold_rate={gold},Silver_rate={silver},Platinum_rate={platinum},Soverign_rate={soverign},Coin_rate={coin},Diamond_rate={diamond},Valuer_name='{V_Name}',Valuer_reg_no='{V_Reg_No}',Purpose='{V_Purpose}',Customer_name='{C_Name}',Customer_Pan={C_Pan},Customer_address='{C_Address}',Firm_name='{F_Name}',Firm_address='{F_Address}',OS='{OS_With}',Gold_total={Gold_total},Gold_gross={Gold_gross},Gold_metal={Gold_metal},Gold_value={Gold_value},Silver_total={Silver_total},Silver_gross={Silver_gross},Silver_metal={Silver_metal},Silver_value={Silver_value},Stone_total={Diamond_total},Stone_gross={Diamond_gross},Stone_value={Diamond_value},Grand_Total={Grand_Total} WHERE Valuation_id={id};'''
            sql_command=format_str.format(id=Ui_Valuation.val_id,valuation_date=valuation_date,rate_date=rate_date,gold=gold,silver=silver,platinum=platinum,diamond=diamond,soverign=soverign,coin=coin,V_Name=V_Name,V_Reg_No=V_Reg_No,V_Purpose=V_Purpose,C_Name=C_Name,C_Pan=C_Pan,C_Address=C_Address,F_Name=F_Name,F_Address=F_Address,OS_With=OS_With,Gold_total=Gold_total,Gold_gross=Gold_gross,Gold_metal=Gold_metal,Gold_value=Gold_value,Silver_total=Silver_total,Silver_gross=Silver_gross,Silver_metal=Silver_metal,Silver_value=Silver_value,Diamond_total=Diamond_total,Diamond_gross=Diamond_gross,Diamond_value=Diamond_value,Grand_Total=Grand_Total)
            self.connection.commit()
            self.cursor.execute(sql_command)

            format_str='''DELETE FROM Products WHERE Valuation_id={id};'''
            sql_command=format_str.format(id=Ui_Valuation.val_id)
            self.cursor.execute(sql_command)

            for i in range(self.tableWidget.rowCount()):
                # for j in range(self.tableWidget.colorCount()):
                description=self.tableWidget.cellWidget(i,0).text()
                metal_rate=float(self.tableWidget.cellWidget(i,1).text())
                purity=float(self.tableWidget.cellWidget(i,2).text())
                qty=float(self.tableWidget.cellWidget(i,3).text())
                gross_wt=float(self.tableWidget.cellWidget(i,4).text())
                metal_wt=float(self.tableWidget.cellWidget(i,5).text())
                metal_value=float(self.tableWidget.cellWidget(i,6).text())
                s_description=self.tableWidget.cellWidget(i,7).text()
                s_wt=float(self.tableWidget.cellWidget(i,8).text())
                s_rate=float(self.tableWidget.cellWidget(i,9).text())
                s_value=float(self.tableWidget.cellWidget(i,10).text())
                total=float(self.tableWidget.cellWidget(i,11).text())
                metal=self.tableWidget.cellWidget(i,12).lineEdit().text()
                item_ratewise=self.tableWidget.cellWidget(i,13).lineEdit().text()
                stone_weightwise=self.tableWidget.cellWidget(i,14).lineEdit().text()
                if(self.tableWidget.cellWidget(i,15).isChecked()):
                    is_soverign=1
                else:
                    is_soverign=0
                
                format_str='''INSERT INTO Products(Valuation_Id,Description,Rate,Purity,Quantity,Gross_Wt,Metal_Wt,Metal_Value,Stone_Description,Stone_Wt,Stone_Rate,Stone_Value,Total_Value,Metal,Item_Ratewise,Stone_Weightwise,Is_Soverign) VALUES ({id},'{item_description}',{rate},{purity},{quantity},{gross_wt},{metal_weight},{metal_value},'{stone_description}',{stone_wt},{stone_rate},{stone_value},{total_value},'{metal}','{item_ratewise}','{stone_weightwise}',{is_soverign});'''
                sql_command=format_str.format(id=Ui_Valuation.val_id,item_description=description,rate=metal_rate,purity=purity,quantity=qty,gross_wt=gross_wt,metal_weight=metal_wt,metal_value=metal_value,stone_description=s_description,stone_wt=s_wt,stone_rate=s_rate,stone_value=s_value,total_value=total,metal=metal,item_ratewise=item_ratewise,stone_weightwise=stone_weightwise,is_soverign=is_soverign)
                self.cursor.execute(sql_command)

            QtWidgets.QMessageBox.information(self, 'Success', 'Valuation Updated')

        # self.default()

    def fillRates(self):
        date=self.dateEdit.lineEdit().text()
        print(date)
        try:
            format_str='''SELECT * FROM Rates WHERE From_Date='{date}';'''
            sql_command=format_str.format(date=date)
            print(sql_command)
            self.cursor.execute(sql_command)
            res=self.cursor.fetchone()
            self.lineEdit.setText(str(res[3]))
            self.lineEdit_2.setText(str(res[4]))
            self.lineEdit_3.setText(str(res[5]))
            self.lineEdit_4.setText(str(res[6]))
            self.lineEdit_5.setText(str(res[7]))
        except:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Rates Does Not Exist')
        
    def MultipleValuation(self):
        date=self.dateEdit_2.lineEdit().text()
        format_str='''SELECT COUNT(*) FROM Valuation WHERE Valuation_date='{date}';'''
        sql_command=format_str.format(date=date)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchall()
        if(res[0][0]>1):
            self.popup1=testselection.Ui_Selection(self,'Valuation',0,[],'Valuation_date',date)
            self.popup1.show()
            # self.ValuationPopup(self,'Valuation',0,[],'Valuation_date',date)
        else:
            self.fillValuation()
    
    def fillValuation(self):
        # print("ABCBABCBABC")
        # id,date=text.split('   ')
        # sql_command='''SELECT * FROM Valuation ;'''
        # self.cursor.execute(sql_command)
        # res=self.cursor.fetchall()
        # count=0
        # for i in res:
        #     if(i[1]==date):
        #         count=count+1
        
        # if(count>1):
        date=self.dateEdit_2.lineEdit().text()
        try:
            format_str='''SELECT * FROM Valuation WHERE Valuation_date='{date}';'''
            sql_command=format_str.format(date=date)
            self.cursor.execute(sql_command)
            res=self.cursor.fetchone()
            print(res[0])
            Ui_Valuation.val_id=res[0]
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
            self.lineEdit_15.setText(res[14])
            self.lineEdit_10.setText(str(res[15]))
            self.lineEdit_11.setText(str(res[16]))
            self.lineEdit_12.setText(str(res[17]))
            self.lineEdit_17.setText(str(res[18]))
            self.lineEdit_19.setText(str(res[19]))
            self.lineEdit_25.setText(str(res[20]))
            self.lineEdit_22.setText(str(res[21]))
            self.lineEdit_18.setText(str(res[22]))
            self.lineEdit_20.setText(str(res[23]))
            self.lineEdit_26.setText(str(res[24]))
            self.lineEdit_23.setText(str(res[25]))
            self.lineEdit_16.setText(str(res[26]))
            self.lineEdit_21.setText(str(res[27]))
            self.lineEdit_24.setText(str(res[28]))
            self.lineEdit_27.setText(str(res[29]))

            format_str='''SELECT * FROM Products WHERE Valuation_Id ='{id}';'''
            sql_command=format_str.format(id=Ui_Valuation.val_id)
            self.cursor.execute(sql_command)
            res=self.cursor.fetchall()
            print("AAA")
            print(res)
            # self.tableWidget.clearContents()
            # for i in range(self.tableWidget.rowCount()+5):
            #     self.tableWidget.removeRow(i)
            self.tableWidget.setRowCount(0)
            # self.tableWidget.setColumnCount(0)
            c=0
            print(self.tableWidget.rowCount())
            for i in res:
                print(i[2])
                print("JNWD")
                self.createRow()
                print("JNadwdWD")
                print(self.tableWidget.rowCount())
                self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,0).setText(i[2])
                self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,1).setText(str(i[3]))
                self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,2).setText(str(i[4]))
                self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,3).setText(str(i[5]))
                self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,4).setText(str(i[6]))
                self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,5).setText(str(i[7]))
                self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,6).setText(str(i[8]))
                self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,7).setText(str(i[9]))
                self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,8).setText(str(i[10]))
                self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,9).setText(str(i[11]))
                self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,10).setText(str(i[12]))
                self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,11).setText(str(i[13]))
                self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,12).lineEdit().setText(str(i[14]))
                self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,13).lineEdit().setText(str(i[15]))
                self.tableWidget.cellWidget(self.tableWidget.rowCount()-1,14).lineEdit().setText(str(i[16]))
                if(i[17]==1):
                    self.tableWidget.cellWidget(c,15).setChecked()
                else:
                    pass
                c=c+1
            self.autoUpdateTotals()
        except:
            pass




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Split_Valuation()
    # w = QtWidgets.QMainWindow()
    ex.show()
    # w.show()
    sys.exit(app.exec_())
