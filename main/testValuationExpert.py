import sys
import os
import inflect
from PyQt5 import QtWidgets,QtWidgets,QtCore,QtGui
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import *
# from PyQt5.QtCore import QObject, pyqtSlot
import sqlite3
from docx import Document
from docx.shared import Inches
import numpy as np
import random
import time
from docxtpl import DocxTemplate
import Firm
import Groups
import Items
import Rates
import Valuers
import Change_Password
import Products
import Valuation
import testselection
import SplitValuation
import datetime
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

 
class Ui_Valuation_Expert(QtWidgets.QMainWindow):
	val_id=0
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		self.databaseAccess()
		self.setupUi(self)
		self.default()
	
	def __del__(self):
		self.connection.commit()
		self.connection.close()

	def databaseAccess(self):
		self.connection = sqlite3.connect("MAINDB.db")
		self.cursor=self.connection.cursor()
	
	def default(self):
		self.tableWidget_2.setRowCount(0)
		date=datetime.date.today().strftime('%d-%m-%y')
		print(date)
		self.dateEdit.lineEdit().setText(date)
		self.dateEdit_2.lineEdit().setText(date)

		# sql_command='''SELECT * FROM Rates ;'''
		# self.cursor.execute(sql_command)
		# res=self.cursor.fetchall()
		# for i in res:
		# 	self.comboBox_5.addItem(str(i[1]))
		
		# sql_command='''SELECT * FROM Valuation ;'''
		# self.cursor.execute(sql_command)
		# res=self.cursor.fetchall()
		# for i in res:
		# 	self.comboBox_6.addItem(str(i[1]))
		
		sql_command='''SELECT * FROM Groups ;'''
		self.cursor.execute(sql_command)
		res=self.cursor.fetchall()
		for i in res:
			self.comboBox_7.addItem(str(i[1]))
		
		self.lineEdit_48.setText(str(0))
		self.lineEdit_49.setText(str(0))
		self.lineEdit_50.setText(str(0))
		self.lineEdit_51.setText(str(0))
		self.lineEdit_52.setText(str(0))
		self.lineEdit_53.setText(str(0))
		self.lineEdit_54.setText(str(0))
		self.lineEdit_55.setText(str(0))
		self.lineEdit_56.setText(str(0))
		self.lineEdit_57.setText(str(0))
		self.lineEdit_58.setText(str(0))
		self.lineEdit_59.setText(str(0))
		self.lineEdit_60.setText(str(0))
		self.lineEdit_61.setText(str(0))
		self.lineEdit_62.setText(str(0))
		self.lineEdit_63.setText(str(0))
		self.lineEdit_64.setText(str(0))
		self.lineEdit_65.setText(str(0))
		self.lineEdit_66.setText(str(0))
		self.lineEdit_67.setText(str(0))
		self.lineEdit_68.setText(str(0))
		self.lineEdit_69.setText(str(0))
		self.lineEdit_70.setText(str(0))
		self.lineEdit_71.setText(str(0))
		self.lineEdit_72.setText(str(0))
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
		self.lineEdit_73.setText(str(0))
		self.lineEdit_74.setText(str(0))
	
	def copyQuantity1(self):
		diamond_qty=int(self.lineEdit_60.text())+int(self.lineEdit_59.text())
		self.lineEdit_60.setText(str(diamond_qty))
	def copyQuantity2(self):
		diamond_qty=int(self.lineEdit_60.text())+int(self.lineEdit_61.text())
		self.lineEdit_60.setText(str(diamond_qty))
	def copyQuantity3(self):
		diamond_qty=int(self.lineEdit_60.text())+int(self.lineEdit_62.text())
		self.lineEdit_60.setText(str(diamond_qty))
	
	def weightClicked(self):
		if(self.radioButton_6.isChecked()):
			self.label_59.setText('Weights')
			self.label_56.setText("Diamond")
			self.label_57.setText("Silver")
			self.label_58.setText("Platinum")
			self.checkBox.setEnabled(False)
			self.checkBox_2.setEnabled(False)
			self.checkBox_3.setEnabled(False)
			self.checkBox_4.setEnabled(False)
			# self.lineEdit_59.editingFinished.connect(self.copyQuantity1)
			# self.lineEdit_61.editingFinished.connect(self.copyQuantity2)
			# self.lineEdit_62.editingFinished.connect(self.copyQuantity3)
		
		elif(self.radioButton.isChecked()):
			self.label_59.setText('%')
			self.label_56.setText("Diamond")
			self.label_57.setText("Silver")
			self.label_58.setText("Platinum")
			self.checkBox.setEnabled(False)
			self.checkBox_2.setEnabled(False)
			self.checkBox_3.setEnabled(False)
			self.checkBox_4.setEnabled(False)

		
		else:
			self.label_59.setText('%')
			self.checkBox.setEnabled(True)
			self.checkBox_2.setEnabled(True)
			self.checkBox_3.setEnabled(True)
			self.checkBox_4.setEnabled(True)
			self.label_56.setText("Silver")
			self.label_57.setText("Platinum")
			self.label_58.setText("White Metal")

			



	def fillRowWithStone(self,res,weight_metal,weight_diamond):
		self.createRow()
		print(res)
		self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,0).setText(res[1])
		rate=0
		if(res[6]=='Gold'):
			rate=float(self.lineEdit_48.text())
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,1).setText(str(format(rate,'.3f')))
			purity_divider=240
		elif(res[6]=='Silver'):
			rate=float(self.lineEdit_49.text())
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,1).setText(str(format(rate,'.3f')))
			purity_divider=100000
		elif(res[6]=='Platinum'):
			rate=float(self.lineEdit_50.text())
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,1).setText(str(format(rate,'.3f')))
		else:
			# gold_rate=float(self.lineEdit_48.text())
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,1).setText("0")
		
		self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,2).setText(str(format(res[7],'.3f')))
		self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,3).setText(str(1))
		self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,4).setText(str(format(weight_metal,'.3f')))
		self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,5).setText(str(format(weight_metal,'.3f')))
		self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,6).setText(str(format(rate*res[7]*weight_metal/purity_divider,'.3f')))
		self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,7).setText(str(res[8]))
		self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,8).setText(str(format(weight_diamond,'.3f')))
		d_rate=float(self.lineEdit_51.text())
		self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,9).setText(str(d_rate))
		self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,10).setText(str(format(weight_diamond*d_rate,'.3f')))
		self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,11).setText(str(float(self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,10).text())+float(self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,6).text())))
		self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,12).lineEdit().setText(res[6])
		self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,13).lineEdit().setText(str(res[3]))
		self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,14).lineEdit().setText(str(res[9]))
		self.autoUpdateTotals()

		



	def fillRowWithoutStone(self,res,weight):
		self.createRow()
		print(res)
		self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,0).setText(res[1])
		rate=0
		if(res[6]=='Gold'):
			rate=float(self.lineEdit_48.text())
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,1).setText(format(rate,'.3f'))
			purity_divider=240
		elif(res[6]=='Silver'):
			rate=float(self.lineEdit_49.text())
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,1).setText(format(rate,'.3f'))
			purity_divider=100000
		elif(res[6]=='Platinum'):
			rate=float(self.lineEdit_50.text())
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,1).setText(format(rate,'.3f'))
			purity_divider=240
		else:
			# gold_rate=float(self.lineEdit_48.text())
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,1).setText("0")
		
		self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,2).setText(str(format(res[7],'.3f')))
		self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,3).setText(str(1))
		self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,4).setText(str(format(weight,'.3f')))
		self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,5).setText(str(format(weight,'.3f')))
		self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,6).setText(str(format(rate*res[7]*weight/purity_divider,'.3f')))
		self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,7).setText(str(res[8]))
		self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,8).setText(str(0.0))
		self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,9).setText(str(0.0))
		self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,10).setText(str(0.0))
		self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,11).setText(str(format(rate*res[7]*weight/purity_divider,'.3f')))
		self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,12).lineEdit().setText(res[6])
		self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,13).lineEdit().setText(str(res[3]))
		self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,14).lineEdit().setText(str(res[10]))
		self.autoUpdateTotals()
	

	def ValuateGold2(self):
		noise=random.uniform(-500,500)
		self.lineEdit_63.setText("Calculating...")
		self.tableWidget_2.setRowCount(0)
		if(self.radioButton_5.isChecked()):
			if(self.checkBox_4.isChecked()==0):
				Amount=int(self.lineEdit_54.text())+noise
				percent=int(self.lineEdit_55.text())
				qty=int(self.lineEdit_59.text())
				gold_rate=float(self.lineEdit_48.text())

				gold_amount=(Amount*percent)/100
				gold_wt=(gold_amount*24)/(19.2*(gold_rate/10))
				l=[]
				timeout=time.time()+3
				
				while(len(l)!=qty):
					if(time.time()>timeout):
						self.tableWidget_2.setRowCount(0)
						np.random.seed(None)

						self.ValuateGold2()
						break
					
					weights=np.random.dirichlet(np.ones(qty))*gold_wt
					format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Groups<>'{group}' AND Stone_Description='...' AND Purity=19.2;'''
					sql_command=format_str.format(metal='Gold',group=self.comboBox_7.lineEdit().text())
					print(sql_command)
					self.cursor.execute(sql_command)
					res=self.cursor.fetchall()
					# print(res)
					for i in weights:
						list1=[]
						print(len(res))
						print(i)
						for j in res:
							if(i>j[4] and i<j[5]):
								set=(j[0],abs(i-(j[4]+j[5])/2))
								print(set)
								list1.append(set)
						list1.sort(key = lambda x: x[1])
						# print(list1)
						# print(list1[0][0])
						if(len(list1)>0):
							format_str='''SELECT *  FROM Items WHERE Item_id={id};'''
							sql_command=format_str.format(id=list1[0][0])
							self.cursor.execute(sql_command)
							result=self.cursor.fetchone()
							l.append(result)
							self.fillRowWithoutStone(result,i)
							res.remove(result)
						else:
							break
			else:
				
				Amount=int(self.lineEdit_54.text())+noise
				percent=int(self.lineEdit_55.text())
				qty=int(self.lineEdit_59.text())
				gold_rate=float(self.lineEdit_48.text())
				diamond_rate=float(self.lineEdit_51.text())

				gold_amount=(Amount*percent*20)/10000
				gold_wt=(gold_amount*24)/(18*(gold_rate/10))
				diamond_amount=(Amount*percent*80)/10000
				diamond_wt=diamond_amount/diamond_rate

				l=[]
				# t1=time.time()
				timeout=time.time()+3
				while(len(l)!=qty):
					if(time.time()>timeout):
						self.tableWidget_2.setRowCount(0)
						print("####################################################################")
						np.random.seed(None)

						self.ValuateGold2()
						break
					weights_diamond=np.random.dirichlet(np.ones(qty))*diamond_wt
					weights_gold=np.random.dirichlet(np.ones(qty))*gold_wt
					weights=[]
					l=[]
					self.tableWidget_2.setRowCount(0)
					for i in range(qty):
						a=(weights_gold[i],weights_diamond[i])
						weights.append(a)
					print("*************************************")
					print(weights)
					print("*************************************")

					format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Stone_Description='Diamond'AND Purity=18;'''
					sql_command=format_str.format(metal='Gold')
					print(sql_command)
					self.cursor.execute(sql_command)
					res=self.cursor.fetchall()
					# print(res)
					for i in weights:
						list1=[]
						print(len(res))
						print(i)
						for j in res:
							if(i[0]>j[4] and i[0]<j[5] and i[1]>j[10] and i[1]<j[11]):
								set=(j[0],abs(abs(i[0]-(j[4]+j[5])/2)-abs(i[1]-(j[10]+j[11])/2)))
								print(set)
								list1.append(set)
						list1.sort(key = lambda x: x[1])
						# print(list1)
						# print(list1[0][0])
						if(len(list1)>0):
							format_str='''SELECT *  FROM Items WHERE Item_id={id};'''
							sql_command=format_str.format(id=list1[0][0])
							self.cursor.execute(sql_command)
							result=self.cursor.fetchone()
							l.append(result)
							self.fillRowWithStone(result,i[0],i[1])
							res.remove(result)
						else:
							break
		elif(self.radioButton_6.isChecked()):
			if(int(self.lineEdit_56.text())==0.0):
				gold_wt=float(self.lineEdit_55.text())
				qty=int(self.lineEdit_59.text())
				l=[]
				# t1=time.time()
				timeout=time.time()+3
				while(len(l)!=qty):
					if(time.time()>timeout):
						self.tableWidget_2.setRowCount(0)
						print("####################################################################")
						np.random.seed(None)

						self.ValuateGold2()
						break
					# weights_diamond=np.random.dirichlet(np.ones(qty))*diamond_wt
					weights_gold=np.random.dirichlet(np.ones(qty))*gold_wt
					# weights=[]
					l=[]
					self.tableWidget_2.setRowCount(0)
					# for i in range(qty):
					# 	a=(weights_gold[i],weights_diamond[i])
					# 	weights.append(a)
					print("*************************************")
					print(weights_gold)
					print("*************************************")

					format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Stone_Description='...';'''
					sql_command=format_str.format(metal='Gold')
					print(sql_command)
					self.cursor.execute(sql_command)
					res=self.cursor.fetchall()
					# print(res)
					for i in weights_gold:
						list1=[]
						print(len(res))
						print(i)
						for j in res:
							if(i>j[4] and i<j[5]):
								set=(j[0],abs(i-(j[4]+j[5])/2))
								print(set)
								list1.append(set)
						list1.sort(key = lambda x: x[1])
						# print(list1)
						# print(list1[0][0])
						if(len(list1)>0):
							format_str='''SELECT *  FROM Items WHERE Item_id={id};'''
							sql_command=format_str.format(id=list1[0][0])
							self.cursor.execute(sql_command)
							result=self.cursor.fetchone()
							l.append(result)
							self.fillRowWithoutStone(result,i)
							res.remove(result)
						else:
							break
			else:
				gold_wt=float(self.lineEdit_55.text())
				diamond_wt=float(self.lineEdit_56.text())
				qty=int(self.lineEdit_59.text())

				l=[]
				# t1=time.time()
				timeout=time.time()+3
				while(len(l)!=qty):
					if(time.time()>timeout):
						self.tableWidget_2.setRowCount(0)
						np.random.seed(None)

						self.ValuateGold2()
						break
					weights_diamond=np.random.dirichlet(np.ones(qty))*diamond_wt
					weights_gold=np.random.dirichlet(np.ones(qty))*gold_wt
					weights=[]
					l=[]
					self.tableWidget_2.setRowCount(0)
					for i in range(qty):
						a=(weights_gold[i],weights_diamond[i])
						weights.append(a)

					format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Stone_Description='Diamond' AND Purity=18;'''
					sql_command=format_str.format(metal='Gold')
					print(sql_command)
					self.cursor.execute(sql_command)
					res=self.cursor.fetchall()
					# print(res)
					for i in weights:
						list1=[]
						print(len(res))
						print(i)
						for j in res:
							if(i[0]>j[4] and i[0]<j[5] and i[1]>j[10] and i[1]<j[11]):
								set=(j[0],abs(abs(i[0]-(j[4]+j[5])/2)-abs(i[1]-(j[10]+j[11])/2)))
								print(set)
								list1.append(set)
						list1.sort(key = lambda x: x[1])
						# print(list1)
						# print(list1[0][0])
						if(len(list1)>0):
							format_str='''SELECT *  FROM Items WHERE Item_id={id};'''
							sql_command=format_str.format(id=list1[0][0])
							self.cursor.execute(sql_command)
							result=self.cursor.fetchone()
							l.append(result)
							self.fillRowWithStone(result,i[0],i[1])
							res.remove(result)
						else:
							break

		else:
			qty=int(self.lineEdit_59.text())
			gold_percent=float(self.lineEdit_55.text())
			diamond_percent=float(self.lineEdit_56.text())
			gold_rate=float(self.lineEdit_48.text())
			diamond_rate=float(self.lineEdit_51.text())
			Amount=int(self.lineEdit_54.text())+noise

			gold_amount=(Amount*gold_percent)/100
			gold_wt=(gold_amount*24)/(18*(gold_rate/10))
			diamond_amount=(Amount*diamond_percent)/100
			diamond_wt=diamond_amount/diamond_rate
			l=[]
			# t1=time.time()
			timeout=time.time()+3
			while(len(l)!=qty):
				if(time.time()>timeout):
					self.tableWidget_2.setRowCount(0)
					print("####################################################################")
					np.random.seed(None)

					self.ValuateGold2()
					break
				weights_diamond=np.random.dirichlet(np.ones(qty))*diamond_wt
				weights_gold=np.random.dirichlet(np.ones(qty))*gold_wt
				weights=[]
				l=[]
				self.tableWidget_2.setRowCount(0)
				for i in range(qty):
					a=(weights_gold[i],weights_diamond[i])
					weights.append(a)
				print("*************************************")
				print(weights)
				print("*************************************")

				format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Stone_Description='Diamond'AND Purity=18;'''
				sql_command=format_str.format(metal='Gold')
				print(sql_command)
				self.cursor.execute(sql_command)
				res=self.cursor.fetchall()
				# print(res)
				for i in weights:
					list1=[]
					print(len(res))
					print(i)
					for j in res:
						if(i[0]>j[4] and i[0]<j[5] and i[1]>j[10] and i[1]<j[11]):
							set=(j[0],abs(abs(i[0]-(j[4]+j[5])/2)-abs(i[1]-(j[10]+j[11])/2)))
							print(set)
							list1.append(set)
					list1.sort(key = lambda x: x[1])
					# print(list1)
					# print(list1[0][0])
					if(len(list1)>0):
						format_str='''SELECT *  FROM Items WHERE Item_id={id};'''
						sql_command=format_str.format(id=list1[0][0])
						self.cursor.execute(sql_command)
						result=self.cursor.fetchone()
						l.append(result)
						self.fillRowWithStone(result,i[0],i[1])
						res.remove(result)
					else:
						break
		self.lineEdit_63.setText("Calculation Complete..")
	

	def ValuateSilver2(self):
		self.lineEdit_63.setText("Calculating...")
		noise=random.uniform(-500,500)
		if(self.radioButton_5.isChecked()):
			if(self.checkBox_3.isChecked()==0):
				Amount=int(self.lineEdit_54.text())+noise
				percent=int(self.lineEdit_56.text())
				qty=int(self.lineEdit_60.text())
				silver_rate=float(self.lineEdit_49.text())

				silver_amount=(Amount*percent)/100
				silver_wt=(silver_amount*100)/(80*silver_rate/1000)
				l=[]
				# t1=time.time()
				timeout=time.time()+3
				while(len(l)!=qty):
					if(time.time()>timeout):
						self.tableWidget_2.setRowCount(0)
						print("####################################################################")
						np.random.seed(None)

						self.ValuateSilver2()
						break
					# weights_diamond=np.random.dirichlet(np.ones(qty))*diamond_wt
					weights_silver=np.random.dirichlet(np.ones(qty))*silver_wt
					# weights=[]
					l=[]
					self.tableWidget_2.setRowCount(0)
					# for i in range(qty):
					# 	a=(weights_gold[i],weights_diamond[i])
					# 	weights.append(a)
					print("*************************************")
					print(weights_silver)
					print("*************************************")

					format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Stone_Description='...' AND Purity=80;'''
					sql_command=format_str.format(metal='Silver')
					print(sql_command)
					self.cursor.execute(sql_command)
					res=self.cursor.fetchall()
					# print(res)
					for i in weights_silver:
						list1=[]
						print(len(res))
						print(i)
						for j in res:
							if(i>j[4] and i<j[5]):
								set=(j[0],abs(i-(j[4]+j[5])/2))
								print(set)
								list1.append(set)
						list1.sort(key = lambda x: x[1])
						# print(list1)
						# print(list1[0][0])
						if(len(list1)>0):
							format_str='''SELECT *  FROM Items WHERE Item_id={id};'''
							sql_command=format_str.format(id=list1[0][0])
							self.cursor.execute(sql_command)
							result=self.cursor.fetchone()
							l.append(result)
							self.fillRowWithoutStone(result,i)
							res.remove(result)
						else:
							break
			else:
				Amount=int(self.lineEdit_54.text())+noise
				percent=int(self.lineEdit_56.text())
				qty=int(self.lineEdit_60.text())
				silver_rate=float(self.lineEdit_49.text())
				diamond_rate=float(self.lineEdit_51.text())

				silver_amount=(Amount*percent*20)/100
				silver_wt=(silver_amount*100)/(80*silver_rate/1000)
				diamond_amount=(Amount*percent*80)/100
				diamond_wt=diamond_amount/diamond_rate

				l=[]
				# t1=time.time()
				timeout=time.time()+3
				while(len(l)!=qty):
					if(time.time()>timeout):
						self.tableWidget_2.setRowCount(0)
						print("####################################################################")
						np.random.seed(None)

						self.ValuateSilver2()
						break
					weights_diamond=np.random.dirichlet(np.ones(qty))*diamond_wt
					weights_silver=np.random.dirichlet(np.ones(qty))*silver_wt
					weights=[]
					l=[]
					self.tableWidget_2.setRowCount(0)
					for i in range(qty):
						a=(weights_silver[i],weights_diamond[i])
						weights.append(a)
					print("*************************************")
					print(weights)
					print("*************************************")

					format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Stone_Description='Diamond'AND Purity=80;'''
					sql_command=format_str.format(metal='Silver')
					print(sql_command)
					self.cursor.execute(sql_command)
					res=self.cursor.fetchall()
					# print(res)
					for i in weights:
						list1=[]
						print(len(res))
						print(i)
						for j in res:
							if(i[0]>j[4] and i[0]<j[5] and i[1]>j[10] and i[1]<j[11]):
								set=(j[0],abs(abs(i[0]-(j[4]+j[5])/2)-abs(i[1]-(j[10]+j[11])/2)))
								print(set)
								list1.append(set)
						list1.sort(key = lambda x: x[1])
						# print(list1)
						# print(list1[0][0])
						if(len(list1)>0):
							format_str='''SELECT *  FROM Items WHERE Item_id={id};'''
							sql_command=format_str.format(id=list1[0][0])
							self.cursor.execute(sql_command)
							result=self.cursor.fetchone()
							l.append(result)
							self.fillRowWithStone(result,i[0],i[1])
							res.remove(result)
						else:
							break
		elif(self.radioButton_6.isChecked()):
			if(int(self.lineEdit_56.text())==0.0):
				silver_wt=float(self.lineEdit_57.text())
				qty=int(self.lineEdit_61.text())
				l=[]
				# t1=time.time()
				timeout=time.time()+3
				while(len(l)!=qty):
					if(time.time()>timeout):
						self.tableWidget_2.setRowCount(0)
						print("####################################################################")
						np.random.seed(None)

						self.ValuateSilver2()
						break
					# weights_diamond=np.random.dirichlet(np.ones(qty))*diamond_wt
					weights_silver=np.random.dirichlet(np.ones(qty))*silver_wt
					# weights=[]
					l=[]
					self.tableWidget_2.setRowCount(0)
					# for i in range(qty):
					# 	a=(weights_gold[i],weights_diamond[i])
					# 	weights.append(a)
					print("*************************************")
					print(weights_silver)
					print("*************************************")

					format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Stone_Description='...';'''
					sql_command=format_str.format(metal='Silver')
					print(sql_command)
					self.cursor.execute(sql_command)
					res=self.cursor.fetchall()
					# print(res)
					for i in weights_silver:
						list1=[]
						print(len(res))
						print(i)
						for j in res:
							if(i>j[4] and i<j[5]):
								set=(j[0],abs(i-(j[4]+j[5])/2))
								print(set)
								list1.append(set)
						list1.sort(key = lambda x: x[1])
						# print(list1)
						# print(list1[0][0])
						if(len(list1)>0):
							format_str='''SELECT *  FROM Items WHERE Item_id={id};'''
							sql_command=format_str.format(id=list1[0][0])
							self.cursor.execute(sql_command)
							result=self.cursor.fetchone()
							l.append(result)
							self.fillRowWithoutStone(result,i)
							res.remove(result)
						else:
							break
			else:
				silver_wt=float(self.lineEdit_57.text())
				diamond_wt=float(self.lineEdit_56.text())
				qty=int(self.lineEdit_61.text())

				l=[]
				# t1=time.time()
				timeout=time.time()+3
				while(len(l)!=qty):
					if(time.time()>timeout):
						self.tableWidget_2.setRowCount(0)
						np.random.seed(None)

						self.ValuateSilver2()
						break
					weights_diamond=np.random.dirichlet(np.ones(qty))*diamond_wt
					weights_silver=np.random.dirichlet(np.ones(qty))*silver_wt
					weights=[]
					l=[]
					self.tableWidget_2.setRowCount(0)
					for i in range(qty):
						a=(weights_silver[i],weights_diamond[i])
						weights.append(a)

					format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Stone_Description='Diamond' AND Purity=80;'''
					sql_command=format_str.format(metal='Silver')
					print(sql_command)
					self.cursor.execute(sql_command)
					res=self.cursor.fetchall()
					# print(res)
					for i in weights:
						list1=[]
						print(len(res))
						print(i)
						for j in res:
							if(i[0]>j[4] and i[0]<j[5] and i[1]>j[10] and i[1]<j[11]):
								set=(j[0],abs(abs(i[0]-(j[4]+j[5])/2)-abs(i[1]-(j[10]+j[11])/2)))
								print(set)
								list1.append(set)
						list1.sort(key = lambda x: x[1])
						# print(list1)
						# print(list1[0][0])
						if(len(list1)>0):
							format_str='''SELECT *  FROM Items WHERE Item_id={id};'''
							sql_command=format_str.format(id=list1[0][0])
							self.cursor.execute(sql_command)
							result=self.cursor.fetchone()
							l.append(result)
							self.fillRowWithStone(result,i[0],i[1])
							res.remove(result)
						else:
							break

		else:
			qty=int(self.lineEdit_61.text())
			silver_percent=float(self.lineEdit_57.text())
			diamond_percent=float(self.lineEdit_56.text())
			silver_rate=float(self.lineEdit_49.text())
			diamond_rate=float(self.lineEdit_51.text())
			Amount=int(self.lineEdit_54.text())+noise

			silver_amount=(Amount*silver_percent)/100
			silver_wt=(silver_amount*100)/(80*(silver_rate/1000))
			diamond_amount=(Amount*diamond_percent)/100
			diamond_wt=diamond_amount/diamond_rate
			l=[]
			# t1=time.time()
			timeout=time.time()+3
			while(len(l)!=qty):
				if(time.time()>timeout):
					self.tableWidget_2.setRowCount(0)
					print("####################################################################")
					np.random.seed(None)

					self.ValuateSilver2()
					break
				weights_diamond=np.random.dirichlet(np.ones(qty))*diamond_wt
				weights_silver=np.random.dirichlet(np.ones(qty))*silver_wt
				weights=[]
				l=[]
				self.tableWidget_2.setRowCount(0)
				for i in range(qty):
					a=(weights_silver[i],weights_diamond[i])
					weights.append(a)
				print("*************************************")
				print(weights)
				print("*************************************")

				format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Stone_Description='Diamond'AND Purity=80;'''
				sql_command=format_str.format(metal='Silver')
				print(sql_command)
				self.cursor.execute(sql_command)
				res=self.cursor.fetchall()
				# print(res)
				for i in weights:
					list1=[]
					print(len(res))
					print(i)
					for j in res:
						if(i[0]>j[4] and i[0]<j[5] and i[1]>j[10] and i[1]<j[11]):
							set=(j[0],abs(abs(i[0]-(j[4]+j[5])/2)-abs(i[1]-(j[10]+j[11])/2)))
							print(set)
							list1.append(set)
					list1.sort(key = lambda x: x[1])
					# print(list1)
					# print(list1[0][0])
					if(len(list1)>0):
						format_str='''SELECT *  FROM Items WHERE Item_id={id};'''
						sql_command=format_str.format(id=list1[0][0])
						self.cursor.execute(sql_command)
						result=self.cursor.fetchone()
						l.append(result)
						self.fillRowWithStone(result,i[0],i[1])
						res.remove(result)
					else:
						break
		self.lineEdit_63.setText("Calculation Complete..")


	def ValuatePlatinum2(self):
		self.lineEdit_63.setText("Calculating...")
		noise=random.uniform(-500,500)
		if(self.radioButton_5.isChecked()):
			if(self.checkBox_2.isChecked()==0):
				Amount=int(self.lineEdit_54.text())+noise
				percent=int(self.lineEdit_57.text())
				qty=int(self.lineEdit_61.text())
				platinum_rate=float(self.lineEdit_50.text())

				platinum_amount=(Amount*percent)/100
				platinum_wt=(platinum_amount*24)/(19.2*platinum_rate/1000)
				l=[]
				# t1=time.time()
				timeout=time.time()+3
				while(len(l)!=qty):
					if(time.time()>timeout):
						self.tableWidget_2.setRowCount(0)
						print("####################################################################")
						np.random.seed(None)

						self.ValuatePlatinum2()
						break
					# weights_diamond=np.random.dirichlet(np.ones(qty))*diamond_wt
					weights_platinum=np.random.dirichlet(np.ones(qty))*platinum_wt
					# weights=[]
					l=[]
					self.tableWidget_2.setRowCount(0)
					# for i in range(qty):
					# 	a=(weights_gold[i],weights_diamond[i])
					# 	weights.append(a)
					print("*************************************")
					print(weights_platinum)
					print("*************************************")

					format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Stone_Description='...' AND Purity=19.2;'''
					sql_command=format_str.format(metal='Platinum')
					print(sql_command)
					self.cursor.execute(sql_command)
					res=self.cursor.fetchall()
					# print(res)
					for i in weights_platinum:
						list1=[]
						print(len(res))
						print(i)
						for j in res:
							if(i>j[4] and i<j[5]):
								set=(j[0],abs(i-(j[4]+j[5])/2))
								print(set)
								list1.append(set)
						list1.sort(key = lambda x: x[1])
						# print(list1)
						# print(list1[0][0])
						if(len(list1)>0):
							format_str='''SELECT *  FROM Items WHERE Item_id={id};'''
							sql_command=format_str.format(id=list1[0][0])
							self.cursor.execute(sql_command)
							result=self.cursor.fetchone()
							l.append(result)
							self.fillRowWithoutStone(result,i)
							res.remove(result)
						else:
							break
			else:
				Amount=int(self.lineEdit_54.text())
				percent=int(self.lineEdit_57.text())
				qty=int(self.lineEdit_61.text())
				platinum_rate=float(self.lineEdit_50.text())
				diamond_rate=float(self.lineEdit_51.text())

				platinum_amount=(Amount*percent*20)/100
				platinum_wt=(platinum_amount*24)/(18*platinum_rate/1000)
				diamond_amount=(Amount*percent*80)/100
				diamond_wt=diamond_amount/diamond_rate

				l=[]
				# t1=time.time()
				timeout=time.time()+3
				while(len(l)!=qty):
					if(time.time()>timeout):
						self.tableWidget_2.setRowCount(0)
						print("####################################################################")
						np.random.seed(None)

						self.ValuatePlatinum2()
						break
					weights_diamond=np.random.dirichlet(np.ones(qty))*diamond_wt
					weights_platinum=np.random.dirichlet(np.ones(qty))*platinum_wt
					weights=[]
					l=[]
					self.tableWidget_2.setRowCount(0)
					for i in range(qty):
						a=(weights_platinum[i],weights_diamond[i])
						weights.append(a)
					print("*************************************")
					print(weights)
					print("*************************************")

					format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Stone_Description='Diamond'AND Purity=18;'''
					sql_command=format_str.format(metal='Platinum')
					print(sql_command)
					self.cursor.execute(sql_command)
					res=self.cursor.fetchall()
					# print(res)
					for i in weights:
						list1=[]
						print(len(res))
						print(i)
						for j in res:
							if(i[0]>j[4] and i[0]<j[5] and i[1]>j[10] and i[1]<j[11]):
								set=(j[0],abs(abs(i[0]-(j[4]+j[5])/2)-abs(i[1]-(j[10]+j[11])/2)))
								print(set)
								list1.append(set)
						list1.sort(key = lambda x: x[1])
						# print(list1)
						# print(list1[0][0])
						if(len(list1)>0):
							format_str='''SELECT *  FROM Items WHERE Item_id={id};'''
							sql_command=format_str.format(id=list1[0][0])
							self.cursor.execute(sql_command)
							result=self.cursor.fetchone()
							l.append(result)
							self.fillRowWithStone(result,i[0],i[1])
							res.remove(result)
						else:
							break
		elif(self.radioButton_6.isChecked()):
			if(int(self.lineEdit_56.text())==0.0):
				platinum_wt=float(self.lineEdit_58.text())
				qty=int(self.lineEdit_62.text())
				l=[]
				# t1=time.time()
				timeout=time.time()+3
				while(len(l)!=qty):
					if(time.time()>timeout):
						self.tableWidget_2.setRowCount(0)
						print("####################################################################")
						np.random.seed(None)

						self.ValuatePlatinum2()
						break
					# weights_diamond=np.random.dirichlet(np.ones(qty))*diamond_wt
					weights_platinum=np.random.dirichlet(np.ones(qty))*platinum_wt
					# weights=[]
					l=[]
					self.tableWidget_2.setRowCount(0)
					# for i in range(qty):
					# 	a=(weights_gold[i],weights_diamond[i])
					# 	weights.append(a)
					print("*************************************")
					# print(weights_gold)
					print("*************************************")

					format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Stone_Description='...';'''
					sql_command=format_str.format(metal='Platinum')
					print(sql_command)
					self.cursor.execute(sql_command)
					res=self.cursor.fetchall()
					# print(res)
					for i in weights_platinum:
						list1=[]
						print(len(res))
						print(i)
						for j in res:
							if(i>j[4] and i<j[5]):
								set=(j[0],abs(i-(j[4]+j[5])/2))
								print(set)
								list1.append(set)
						list1.sort(key = lambda x: x[1])
						# print(list1)
						# print(list1[0][0])
						if(len(list1)>0):
							format_str='''SELECT *  FROM Items WHERE Item_id={id};'''
							sql_command=format_str.format(id=list1[0][0])
							self.cursor.execute(sql_command)
							result=self.cursor.fetchone()
							l.append(result)
							self.fillRowWithoutStone(result,i)
							res.remove(result)
						else:
							break
			else:
				platinum_wt=float(self.lineEdit_58.text())
				diamond_wt=float(self.lineEdit_56.text())
				qty=int(self.lineEdit_62.text())

				l=[]
				# t1=time.time()
				timeout=time.time()+3
				while(len(l)!=qty):
					if(time.time()>timeout):
						self.tableWidget_2.setRowCount(0)
						np.random.seed(None)

						self.ValuatePlatinum2()
						break
					weights_diamond=np.random.dirichlet(np.ones(qty))*diamond_wt
					weights_platinum=np.random.dirichlet(np.ones(qty))*platinum_wt
					weights=[]
					l=[]
					self.tableWidget_2.setRowCount(0)
					for i in range(qty):
						a=(weights_platinum[i],weights_diamond[i])
						weights.append(a)

					format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Stone_Description='Diamond' AND Purity=18;'''
					sql_command=format_str.format(metal='PLatinum')
					print(sql_command)
					self.cursor.execute(sql_command)
					res=self.cursor.fetchall()
					# print(res)
					for i in weights:
						list1=[]
						print(len(res))
						print(i)
						for j in res:
							if(i[0]>j[4] and i[0]<j[5] and i[1]>j[10] and i[1]<j[11]):
								set=(j[0],abs(abs(i[0]-(j[4]+j[5])/2)-abs(i[1]-(j[10]+j[11])/2)))
								print(set)
								list1.append(set)
						list1.sort(key = lambda x: x[1])
						# print(list1)
						# print(list1[0][0])
						if(len(list1)>0):
							format_str='''SELECT *  FROM Items WHERE Item_id={id};'''
							sql_command=format_str.format(id=list1[0][0])
							self.cursor.execute(sql_command)
							result=self.cursor.fetchone()
							l.append(result)
							self.fillRowWithStone(result,i[0],i[1])
							res.remove(result)
						else:
							break

		else:
			qty=int(self.lineEdit_62.text())
			platinum_percent=float(self.lineEdit_58.text())
			diamond_percent=float(self.lineEdit_56.text())
			platinum_rate=float(self.lineEdit_50.text())
			diamond_rate=float(self.lineEdit_51.text())
			Amount=int(self.lineEdit_54.text())+noise

			platinum_amount=(Amount*platinum_percent)/100
			platinum_wt=(platinum_amount*24)/(18*(platinum_rate/10))
			diamond_amount=(Amount*diamond_percent)/100
			diamond_wt=diamond_amount/diamond_rate
			l=[]
			# t1=time.time()
			timeout=time.time()+3
			while(len(l)!=qty):
				if(time.time()>timeout):
					self.tableWidget_2.setRowCount(0)
					print("####################################################################")
					np.random.seed(None)

					self.ValuatePlatinum2()
					break
				weights_diamond=np.random.dirichlet(np.ones(qty))*diamond_wt
				weights_platinum=np.random.dirichlet(np.ones(qty))*platinum_wt
				weights=[]
				l=[]
				self.tableWidget_2.setRowCount(0)
				for i in range(qty):
					a=(weights_platinum[i],weights_diamond[i])
					weights.append(a)
				print("*************************************")
				print(weights)
				print("*************************************")

				format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Stone_Description='Diamond'AND Purity=18;'''
				sql_command=format_str.format(metal='Platinum')
				print(sql_command)
				self.cursor.execute(sql_command)
				res=self.cursor.fetchall()
				# print(res)
				for i in weights:
					list1=[]
					print(len(res))
					print(i)
					for j in res:
						if(i[0]>j[4] and i[0]<j[5] and i[1]>j[10] and i[1]<j[11]):
							set=(j[0],abs(abs(i[0]-(j[4]+j[5])/2)-abs(i[1]-(j[10]+j[11])/2)))
							print(set)
							list1.append(set)
					list1.sort(key = lambda x: x[1])
					# print(list1)
					# print(list1[0][0])
					if(len(list1)>0):
						format_str='''SELECT *  FROM Items WHERE Item_id={id};'''
						sql_command=format_str.format(id=list1[0][0])
						self.cursor.execute(sql_command)
						result=self.cursor.fetchone()
						l.append(result)
						self.fillRowWithStone(result,i[0],i[1])
						res.remove(result)
					else:
						break
		self.lineEdit_63.setText("Calculation Complete..")
	



	def ValuateWhiteMetal2(self):
		if(self.radioButton_5.isChecked()):
			if(self.checkBox.isChecked()):
				Amount=int(self.lineEdit_54.text())
				percent=int(self.lineEdit_58.text())
				qty=int(self.lineEdit_62.text())
				# platinum_rate=float(self.lineEdit_50.text())
				diamond_rate=float(self.lineEdit_51.text())

				# platinum_amount=(Amount*percent*20)/100
				# platinum_wt=(platinum_amount*24)/(18*platinum_rate/1000)
				diamond_amount=(Amount*percent*80)/100
				diamond_wt=diamond_amount/diamond_rate

				l=[]
				# t1=time.time()
				timeout=time.time()+3
				while(len(l)!=qty):
					if(time.time()>timeout):
						self.tableWidget_2.setRowCount(0)
						print("####################################################################")
						np.random.seed(None)

						self.ValuateWhiteMetal2()
						break
					weights=np.random.dirichlet(np.ones(qty))*diamond_wt
					# weights_platinum=np.random.dirichlet(np.ones(qty))*platinum_wt
					# weights=[]
					l=[]
					self.tableWidget_2.setRowCount(0)
					# for i in range(qty):
					# 	a=(weights_platinum[i],weights_diamond[i])
					# 	weights.append(a)
					print("*************************************")
					print(weights)
					print("*************************************")

					format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Stone_Description='Diamond';'''
					sql_command=format_str.format(metal='White Metal')
					print(sql_command)
					self.cursor.execute(sql_command)
					res=self.cursor.fetchall()
					# print(res)
					for i in weights:
						list1=[]
						print(len(res))
						print(i)
						for j in res:
							if(i>j[10] and i<j[11]):
								set=(j[0],abs(i-(j[10]+j[11])/2))
								print(set)
								list1.append(set)
						list1.sort(key = lambda x: x[1])
						# print(list1)
						# print(list1[0][0])
						if(len(list1)>0):
							format_str='''SELECT *  FROM Items WHERE Item_id={id};'''
							sql_command=format_str.format(id=list1[0][0])
							self.cursor.execute(sql_command)
							result=self.cursor.fetchone()
							l.append(result)
							self.fillRowWithStone(result,0,i[1])
							res.remove(result)
						else:
							break
			else:
				QtWidgets.QMessageBox.warning(self, 'Error', 'Diamond Not Selected')					
		elif(self.radioButton_6.isChecked()):
			if(self.checkBox.isChecked()):
				# Amount=int(self.lineEdit_54.text())
				diamond_wt=int(self.lineEdit_58.text())
				qty=int(self.lineEdit_62.text())
				# platinum_rate=float(self.lineEdit_50.text())
				diamond_rate=float(self.lineEdit_51.text())

				# platinum_amount=((diamond_wt*diamond_rate)*0.25)

				# gold_amount=(Amount*percent*20)/100
				# platinum_wt=(platinum_amount*24)/(18*platinum_rate/1000)
				# diamond_amount=(Amount*percent*80)/100
				# diamond_wt=diamond_amount/diamond_rate

				l=[]
				# t1=time.time()
				timeout=time.time()+3
				while(len(l)!=qty):
					if(time.time()>timeout):
						self.tableWidget_2.setRowCount(0)
						np.random.seed(None)

						self.ValuateWhiteMetal2()
						break
					weights=np.random.dirichlet(np.ones(qty))*diamond_wt
					# weights_platinum=np.random.dirichlet(np.ones(qty))*platinum_wt
					# weights=[]
					l=[]
					# self.tableWidget_2.setRowCount(0)
					# for i in range(qty):
					# 	a=(weights_platinum[i],weights_diamond[i])
					# 	weights.append(a)

					format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Stone_Description='Diamond';'''
					sql_command=format_str.format(metal='White Metal')
					print(sql_command)
					self.cursor.execute(sql_command)
					res=self.cursor.fetchall()
					# print(res)
					for i in weights:
						list1=[]
						print(len(res))
						print(i)
						for j in res:
							if(i>j[10] and i<j[11]):
								set=(j[0],abs(i-(j[10]+j[11])/2))
								print(set)
								list1.append(set)
						list1.sort(key = lambda x: x[1])
						# print(list1)
						# print(list1[0][0])
						if(len(list1)>0):
							format_str='''SELECT *  FROM Items WHERE Item_id={id};'''
							sql_command=format_str.format(id=list1[0][0])
							self.cursor.execute(sql_command)
							result=self.cursor.fetchone()
							l.append(result)
							self.fillRowWithStone(result,0,i[1])
							res.remove(result)
						else:
							break
			else:
				QtWidgets.QMessageBox.warning(self, 'Error', 'Diamond Not Selected')

		else:
			if(self.checkBox.isChecked()):
				Amount=int(self.lineEdit_54.text())
				percent=int(self.lineEdit_58.text())
				qty=int(self.lineEdit_62.text())
				# platinum_rate=float(self.lineEdit_50.text())
				diamond_rate=float(self.lineEdit_51.text())

				# platinum_amount=(Amount*percent*20)/100
				# platinum_wt=(platinum_amount*24)/(18*platinum_rate/1000)
				diamond_amount=(Amount*percent*80)/100
				diamond_wt=diamond_amount/diamond_rate

				l=[]
				# t1=time.time()
				timeout=time.time()+3
				while(len(l)!=qty):
					if(time.time()>timeout):
						self.tableWidget_2.setRowCount(0)
						print("####################################################################")
						np.random.seed(None)

						self.ValuateWhiteMetal2()
						break
					weights=np.random.dirichlet(np.ones(qty))*diamond_wt
					# weights_platinum=np.random.dirichlet(np.ones(qty))*platinum_wt
					# weights=[]
					l=[]
					self.tableWidget_2.setRowCount(0)
					# for i in range(qty):
					# 	a=(weights_platinum[i],weights_diamond[i])
					# 	weights.append(a)
					print("*************************************")
					print(weights)
					print("*************************************")

					format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Stone_Description='Diamond';'''
					sql_command=format_str.format(metal='White Metal')
					print(sql_command)
					self.cursor.execute(sql_command)
					res=self.cursor.fetchall()
					# print(res)
					for i in weights:
						list1=[]
						print(len(res))
						print(i)
						for j in res:
							if(i>j[10] and i<j[11]):
								set=(j[0],abs(i-(j[10]+j[11])/2))
								print(set)
								list1.append(set)
						list1.sort(key = lambda x: x[1])
						# print(list1)
						# print(list1[0][0])
						if(len(list1)>0):
							format_str='''SELECT *  FROM Items WHERE Item_id={id};'''
							sql_command=format_str.format(id=list1[0][0])
							self.cursor.execute(sql_command)
							result=self.cursor.fetchone()
							l.append(result)
							self.fillRowWithStone(result,0,i[1])
							res.remove(result)
						else:
							break
			else:
				QtWidgets.QMessageBox.warning(self, 'Error', 'Diamond Not Selected')
	

	def clear_btn_1(self):
		self.lineEdit_55.setText("")
		self.lineEdit_59.setText("")

	def clear_btn_2(self):
		self.lineEdit_56.setText("")
		self.lineEdit_60.setText("")
	
	def clear_btn_3(self):
		self.lineEdit_57.setText("")
		self.lineEdit_61.setText("")
	
	def clear_btn_4(self):
		self.lineEdit_58.setText("")
		self.lineEdit_62.setText("")




							
					



					


					






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
		self.curr_row=self.tableWidget_2.currentRow()
		name=self.tableWidget_2.cellWidget(self.curr_row,0).text()
		format_str='''SELECT Metal FROM Items WHERE Item_Description='{name}';'''
		sql_command=format_str.format(name=name)
		self.cursor.execute(sql_command)
		res=self.cursor.fetchone()
		print(res)

		if(res is None):
			self.tableWidget_2.cellWidget(self.curr_row,1).setText(self.lineEdit_48.text())
			self.tableWidget_2.cellWidget(self.curr_row,12).lineEdit().setText('Gold')
		else:
			if(res[0]=='Platinum'):
				self.tableWidget_2.cellWidget(self.curr_row,1).setText(self.lineEdit_50.text())
				self.tableWidget_2.cellWidget(self.curr_row,12).lineEdit().setText(res[0])
			elif(res[0]=='Silver'):
				self.tableWidget_2.cellWidget(self.curr_row,1).setText(self.lineEdit_49.text())
				self.tableWidget_2.cellWidget(self.curr_row,12).lineEdit().setText(res[0])
			else:
				self.tableWidget_2.cellWidget(self.curr_row,1).setText(self.lineEdit_48.text())
				self.tableWidget_2.cellWidget(self.curr_row,12).lineEdit().setText(res[0])
		print(name)
		self.autoUpdateTotals()

	def autoMetalWt(self):
		self.curr_row=self.tableWidget_2.currentRow()
		self.tableWidget_2.cellWidget(self.curr_row,5).setText(str(format(float(self.tableWidget_2.cellWidget(self.curr_row,4).text()),'.2f')))
			# self.tableWidget_2.cellWidget.
		self.autoUpdateTotals()

		
	def autoChangeOnStoneEntered(self):
		self.curr_row=self.tableWidget_2.currentRow()
		gross=float(self.tableWidget_2.cellWidget(self.curr_row,4).text())
		# metal=float(self.tableWidget_2.cellWidget(self.curr_row,5).text())
		stone=float(self.tableWidget_2.cellWidget(self.curr_row,8).text())
		self.tableWidget_2.cellWidget(self.curr_row,5).setText(str(format(gross-stone,'.2f')))
		self.autoValue()
		self.autoUpdateTotals()

	def autoValue(self):
		# self.autoRate()
		# self.autoStoneWeight()
		self.curr_row=self.tableWidget_2.currentRow()
		rate=float(self.tableWidget_2.cellWidget(self.curr_row,1).text())
		purity=float(self.tableWidget_2.cellWidget(self.curr_row,2).text())
		wt=float(self.tableWidget_2.cellWidget(self.curr_row,5).text())
		metal=self.tableWidget_2.cellWidget(self.curr_row,12).lineEdit().text()
		if(metal=='Gold' or metal=='Platinum'):
			value=(purity*rate*wt)/240
		else:
			value=(purity*rate*wt)/100000
		self.tableWidget_2.cellWidget(self.curr_row,6).setText(str(format(round(value),'.2f')))
		self.autoTotal()
		self.autoUpdateTotals()


	def autoStoneRate(self):
		self.curr_row=self.tableWidget_2.currentRow()
		s_name=self.tableWidget_2.cellWidget(self.curr_row,7).text()
		if(s_name in 'Diamond' or s_name in 'diamond'):
			self.tableWidget_2.cellWidget(self.curr_row,7).setText("Diamond")
			self.tableWidget_2.cellWidget(self.curr_row,9).setText(self.lineEdit_51.text())
			self.tableWidget_2.cellWidget(self.curr_row,14).lineEdit().setText("Carats")
		self.autoUpdateTotals()

	def autoStoneValue(self):
		self.curr_row=self.tableWidget_2.currentRow()
		wt=float(self.tableWidget_2.cellWidget(self.curr_row,8).text())
		rate=float(self.tableWidget_2.cellWidget(self.curr_row,9).text())
		value=wt*rate
		self.tableWidget_2.cellWidget(self.curr_row,10).setText(str(format(round(value),'.2f')))
		self.autoUpdateTotals()

	def autoTotal(self):
		self.curr_row=self.tableWidget_2.currentRow()
		metal_total=float(self.tableWidget_2.cellWidget(self.curr_row,6).text())
		stone_total=float(self.tableWidget_2.cellWidget(self.curr_row,10).text())
		total=metal_total+stone_total
		self.tableWidget_2.cellWidget(self.curr_row,11).setText(str(format(round(total),'.2f')))
		self.autoUpdateTotals()

	def autoItemRateWise(self,a):
		self.curr_row=self.tableWidget_2.currentRow()
		# a=self.tableWidget_2.cellWidget(self.curr_row,13).lineEdit().text()
		if(a=='Quantitywise'):
			quantity=int(self.tableWidget_2.cellWidget(self.curr_row,3).text())
			self.autoValue()
			metal_value=float(self.tableWidget_2.cellWidget(self.curr_row,6).text())
			self.tableWidget_2.cellWidget(self.curr_row,6).setText(str(format(round(metal_value*quantity),'.2f')))
			self.autoTotal()
			self.autoUpdateTotals()
		else:
			self.autoValue()
			self.autoTotal()
			self.autoUpdateTotals()


	def autoStoneWeightwise(self,a):
		self.curr_row=self.tableWidget_2.currentRow()
		if(a=='Carats'):
			self.autoStoneValue()
			self.autoTotal()
			pass
		else:
			self.curr_row=self.tableWidget_2.currentRow()
			wt=float(self.tableWidget_2.cellWidget(self.curr_row,8).text())/5
			rate=float(self.tableWidget_2.cellWidget(self.curr_row,9).text())*5
			value=wt*rate
			self.tableWidget_2.cellWidget(self.curr_row,10).setText(str(format(round(value),'.2f')))
			self.autoTotal()
		self.autoUpdateTotals()



	def autoChangeMetal(self,a):
		self.curr_row=self.tableWidget_2.currentRow()
		if(a=='Gold' or a=='Platinum'):
			if(a=='Gold'):
				self.tableWidget_2.cellWidget(self.curr_row,1).setText(self.lineEdit_48.text())
				rate=float(self.tableWidget_2.cellWidget(self.curr_row,1).text())/10
			else:
				self.tableWidget_2.cellWidget(self.curr_row,1).setText(self.lineEdit_50.text())
				rate=float(self.tableWidget_2.cellWidget(self.curr_row,1).text())
		
			purity=float(self.tableWidget_2.cellWidget(self.curr_row,2).text())
			wt=float(self.tableWidget_2.cellWidget(self.curr_row,5).text())
			value=(purity*rate*wt)/24
			self.tableWidget_2.cellWidget(self.curr_row,6).setText(str(format(round(value),'.2f')))
			stone=float(self.tableWidget_2.cellWidget(self.curr_row,10).text())
			self.tableWidget_2.cellWidget(self.curr_row,11).setText(str(format(round(stone+value),'.2f')))

		else:
			self.tableWidget_2.cellWidget(self.curr_row,1).setText(self.lineEdit_49.text())
			rate=float(self.tableWidget_2.cellWidget(self.curr_row,1).text())/1000
			purity=float(self.tableWidget_2.cellWidget(self.curr_row,2).text())
			wt=float(self.tableWidget_2.cellWidget(self.curr_row,5).text())
			value=(purity*rate*wt)/100
			self.tableWidget_2.cellWidget(self.curr_row,6).setText(str(format(round(value),'.2f')))
			stone=float(self.tableWidget_2.cellWidget(self.curr_row,10).text())
			self.tableWidget_2.cellWidget(self.curr_row,11).setText(str(format(round(stone+value),'.2f')))
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
		for i in range(self.tableWidget_2.rowCount()):
			if(self.tableWidget_2.cellWidget(i,12).lineEdit().text()=='Gold'):

				gold_qt=gold_qt+int(self.tableWidget_2.cellWidget(i,3).text())
				gold_gross=gold_gross+float(self.tableWidget_2.cellWidget(i,4).text())
				gold_metal=gold_metal+float(self.tableWidget_2.cellWidget(i,5).text())
				gold_value=gold_value+float(self.tableWidget_2.cellWidget(i,6).text())
			
			if(self.tableWidget_2.cellWidget(i,12).lineEdit().text()=='Silver'):
				silver_qt=silver_qt+int(self.tableWidget_2.cellWidget(i,3).text())
				silver_gross=silver_gross+float(self.tableWidget_2.cellWidget(i,4).text())
				silver_metal=silver_metal+float(self.tableWidget_2.cellWidget(i,5).text())
				silver_value=silver_value+float(self.tableWidget_2.cellWidget(i,6).text())

			if(self.tableWidget_2.cellWidget(i,7).text()=='Diamond'):
				stone_qt=stone_qt+int(self.tableWidget_2.cellWidget(i,3).text())
				stone_gross=stone_gross+float(self.tableWidget_2.cellWidget(i,8).text())
				# silver_metal=silver_metal+float(self.tableWidget_2.cellWidget(i,5).text())
				stone_value=stone_value+float(self.tableWidget_2.cellWidget(i,10).text())
			
			grand_total=grand_total+float(self.tableWidget_2.cellWidget(i,11).text())
			
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
		self.CheckPurityWise(1)
	
	def deleteRow(self):
		# row = self.tableWidget_2.indexAt(self.tableWidget_2.currentRow())
		print("sbjhbsjhbfwsec")
		print(self.tableWidget_2.currentRow())
		self.tableWidget_2.removeRow(self.tableWidget_2.currentRow())
		print(self.tableWidget_2.currentRow())
		# self.tableWidget_2.setRowCount(self.-1)

	def SetCursor(self):
		self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,0).setCursorPosition(0)

	def ColumnIncrementer(self):
		self.curr_row=self.tableWidget_2.currentRow()
		self.curr_col=self.tableWidget_2.currentColumn()
		self.tableWidget_2.setCurrentCell(self.curr_row,self.curr_col+1)


	def createRow(self):
		# self.save()
		print("A")
		self.tableWidget_2.insertRow(self.tableWidget_2.rowCount())
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
		self.tableWidget_2.setCellWidget(self.tableWidget_2.rowCount()-1,0,self.line)
		self.line=QLineEdit()
		self.line.setObjectName("LINE")
		self.line.setText(str(0))
		self.line.returnPressed.connect(self.ColumnIncrementer)
		self.validate=QtGui.QDoubleValidator()
		self.line.setValidator(self.validate)
		self.tableWidget_2.setCellWidget(self.tableWidget_2.rowCount()-1,1,self.line)
		self.line=QLineEdit()
		self.line.setObjectName("LINE")
		self.line.setText(str(19.20))
		self.line.editingFinished.connect(self.autoTotal)
		self.line.editingFinished.connect(self.autoUpdateTotals)
		self.line.returnPressed.connect(self.ColumnIncrementer)
		self.validate=QtGui.QDoubleValidator()
		self.line.setValidator(self.validate)
		self.tableWidget_2.setCellWidget(self.tableWidget_2.rowCount()-1,2,self.line)
		self.line=QLineEdit()
		self.line.setObjectName("LINE")
		self.line.setText(str(1))
		self.line.returnPressed.connect(self.ColumnIncrementer)
		self.validate=QtGui.QIntValidator()
		self.line.setValidator(self.validate)
		self.tableWidget_2.setCellWidget(self.tableWidget_2.rowCount()-1,3,self.line)
		self.line=MyLineEdit()
		self.line.setObjectName("LINE")
		self.line.setText(str(0.0))
		# self.line.mousePressEvent = lambda _ : self.line.selectAll()
		self.line.editingFinished.connect(self.autoMetalWt)
		self.line.returnPressed.connect(self.ColumnIncrementer)
		self.validate=QtGui.QDoubleValidator()
		self.line.setValidator(self.validate)
		self.tableWidget_2.setCellWidget(self.tableWidget_2.rowCount()-1,4,self.line)
		self.line=MyLineEdit()
		self.line.setObjectName("LINE")
		self.line.setText(str(0))
		# self.line.returnPressed.connect(self.autoValue)
		self.line.editingFinished.connect(self.autoValue)
		self.line.returnPressed.connect(self.ColumnIncrementer)
		self.validate=QtGui.QDoubleValidator()
		self.line.setValidator(self.validate)
		self.tableWidget_2.setCellWidget(self.tableWidget_2.rowCount()-1,5,self.line)
		self.line=QLineEdit()
		self.line.setObjectName("LINE")
		self.line.setText(str(0))
		self.line.returnPressed.connect(self.ColumnIncrementer)
		self.validate=QtGui.QDoubleValidator()
		self.line.setValidator(self.validate)
		self.tableWidget_2.setCellWidget(self.tableWidget_2.rowCount()-1,6,self.line)
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
		self.tableWidget_2.setCellWidget(self.tableWidget_2.rowCount()-1,7,self.line)
		self.line=MyLineEdit()
		self.line.setObjectName("LINE")
		self.line.setText(str(0))
		self.line.editingFinished.connect(self.autoStoneValue)
		self.line.editingFinished.connect(self.autoTotal)
		self.line.editingFinished.connect(self.autoChangeOnStoneEntered)
		self.line.returnPressed.connect(self.ColumnIncrementer)
		self.validate=QtGui.QDoubleValidator()
		self.line.setValidator(self.validate)
		self.tableWidget_2.setCellWidget(self.tableWidget_2.rowCount()-1,8,self.line)
		self.line=QLineEdit()
		self.line.setObjectName("LINE")
		self.line.setText(str(0))
		self.line.editingFinished.connect(self.autoStoneValue)
		self.line.editingFinished.connect(self.autoTotal)
		self.line.editingFinished.connect(self.autoChangeOnStoneEntered)
		self.line.returnPressed.connect(self.ColumnIncrementer)
		self.validate=QtGui.QDoubleValidator()
		self.line.setValidator(self.validate)
		self.tableWidget_2.setCellWidget(self.tableWidget_2.rowCount()-1,9,self.line)
		self.line=QLineEdit()
		self.line.setObjectName("LINE")
		self.line.setText(str(0))
		self.line.returnPressed.connect(self.ColumnIncrementer)
		self.validate=QtGui.QDoubleValidator()
		self.line.setValidator(self.validate)
		self.tableWidget_2.setCellWidget(self.tableWidget_2.rowCount()-1,10,self.line)
		self.line=QLineEdit()
		self.line.setObjectName("LINE")
		self.line.setText(str(0))
		self.line.returnPressed.connect(self.ColumnIncrementer)
		self.validate=QtGui.QDoubleValidator()
		self.line.setValidator(self.validate)
		self.tableWidget_2.setCellWidget(self.tableWidget_2.rowCount()-1,11,self.line)
		self.comboBox_3 = QComboBox()
		self.comboBox_3.setEditable(True)
		self.comboBox_3.setObjectName("comboBox_3")
		self.comboBox_3.addItem("Gold")
		self.comboBox_3.addItem("Silver")
		self.comboBox_3.addItem("Platinum")
		self.comboBox_3.lineEdit().setText("Gold")
		print("B")
		self.comboBox_3.activated[str].connect(self.autoChangeMetal)
		self.tableWidget_2.setCellWidget(self.tableWidget_2.rowCount()-1,12,self.comboBox_3)
		self.comboBox_4 = QtWidgets.QComboBox()
		self.comboBox_4.setEditable(True)
		self.comboBox_4.setObjectName("comboBox_4")
		self.comboBox_4.addItem("Weightwise")
		self.comboBox_4.addItem("Quantitywise")
		self.comboBox_4.lineEdit().setText("Weightwise")
		self.comboBox_4.activated[str].connect(self.autoItemRateWise)
		# self.comboBox_4.addItem("Platinum")
		self.tableWidget_2.setCellWidget(self.tableWidget_2.rowCount()-1,13,self.comboBox_4)
		self.comboBox_5 = QtWidgets.QComboBox()
		self.comboBox_5.setEditable(True)
		self.comboBox_5.setObjectName("comboBox_5")
		self.comboBox_5.addItem("Grams")
		self.comboBox_5.addItem("Carats")
		self.comboBox_5.lineEdit().setText("Grams")
		self.comboBox_5.activated[str].connect(self.autoStoneWeightwise)
		# self.comboBox_5.addItem("Platinum")
		self.tableWidget_2.setCellWidget(self.tableWidget_2.rowCount()-1,14,self.comboBox_5)
		self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBox.setObjectName("checkBox")
		self.tableWidget_2.setCellWidget(self.tableWidget_2.rowCount()-1,15,self.checkBox)
		# self.tableWidget_2.cellChanged.connect(self.print)
	

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
		self.lineEdit_48.setText(str(res[3]))
		self.lineEdit_49.setText(str(res[4]))
		self.lineEdit_50.setText(str(res[5]))
		self.lineEdit_51.setText(str(res[6]))
		self.lineEdit_52.setText(str(res[7]))
		self.lineEdit_53.setText(str(res[8]))

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
		self.lineEdit_70.setText(res[1])
		self.lineEdit_71.setText(res[2])

	def CustomerPopup(self):
		self.popup=testselection.Ui_Selection(self,'Auto_Valuation',1)
		self.popup.show()

	def ReturnCustomer(self):
		format_str='''SELECT Row FROM Popup;'''
		self.cursor.execute(format_str)
		res=self.cursor.fetchone()
		print(res[0])
		format_str='''SELECT * FROM Auto_Valuation WHERE V_Id={id};'''
		sql_command=format_str.format(id=res[0])
		self.cursor.execute(sql_command)
		res=self.cursor.fetchone()
		print(res[0])
		self.lineEdit_67.setText(res[27])
		self.lineEdit_68.setText(str(res[28]))
		self.lineEdit_69.setText(res[29])

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
		self.lineEdit_64.setText(res[1])
		self.lineEdit_65.setText(res[2])

	def ValuationPopup(self):
		self.popup=testselection.Ui_Selection(self,'Auto_Valuation')
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
		format_str='''SELECT * FROM Auto_Valuation WHERE V_Id={id};'''
		sql_command=format_str.format(id=res[0])
		self.cursor.execute(sql_command)
		res=self.cursor.fetchone()
		print(res[0])
		Ui_Valuation_Expert.val_id=res[0]
		self.dateEdit_2.lineEdit().setText(str(res[1]))
		self.dateEdit.lineEdit().setText(str(res[2]))
		self.lineEdit_48.setText(str(res[3]))
		self.lineEdit_49.setText(str(res[4]))
		self.lineEdit_50.setText(str(res[5]))
		self.lineEdit_51.setText(str(res[6]))
		self.lineEdit_52.setText(str(res[7]))
		self.lineEdit_53.setText(str(res[8]))
		self.lineEdit_54.setText(str(res[9]))
		if(res[10]=='Amount'):
			self.radioButton_5.setChecked(True)
		elif(res[10]=='Weight'):
			self.radioButton_6.setChecked(True)
		else:
			self.radioButton.setChecked(True)
		
		if(res[11]==1):
			self.checkBox_4.setChecked(True)
		self.lineEdit_55.setText(str(res[12]))
		self.lineEdit_59.setText(str(res[13]))
		if(res[14]==1):
			self.checkBox_3.setChecked(True)
		self.lineEdit_56.setText(str(res[15]))
		self.lineEdit_60.setText(str(res[16]))
		if(res[17]==1):
			self.checkBox_2.setChecked(True)
		self.lineEdit_57.setText(str(res[18]))
		self.lineEdit_61.setText(str(res[19]))
		if(res[20]==1):
			self.checkBox.setChecked(True)
		self.lineEdit_25.setText(str(res[21]))
		self.lineEdit_22.setText(str(res[22]))
		self.comboBox_7.lineEdit().setText(str(res[23]))
		self.lineEdit_64.setText(str(res[24]))
		self.lineEdit_65.setText(str(res[25]))
		self.lineEdit_66.setText(str(res[26]))
		self.lineEdit_67.setText(str(res[27]))
		self.lineEdit_68.setText(str(res[28]))
		self.lineEdit_69.setText(str(res[29]))
		self.lineEdit_70.setText(str(res[30]))
		self.lineEdit_71.setText(str(res[31]))
		self.lineEdit_72.setText(str(res[32]))
		self.lineEdit_17.setText(str(res[33]))
		self.lineEdit_19.setText(str(res[34]))
		self.lineEdit_25.setText(str(res[35]))
		self.lineEdit_22.setText(str(res[36]))
		self.lineEdit_18.setText(str(res[37]))
		self.lineEdit_20.setText(str(res[38]))
		self.lineEdit_26.setText(str(res[39]))
		self.lineEdit_23.setText(str(res[40]))
		self.lineEdit_16.setText(str(res[41]))
		self.lineEdit_21.setText(str(res[42]))
		self.lineEdit_24.setText(str(res[43]))
		self.lineEdit_27.setText(str(res[44]))
		self.lineEdit_73.setText(str(res[45]))
		self.lineEdit_74.setText(str(res[46]))


		format_str='''SELECT * FROM Auto_Products WHERE Valuation_id ='{id}';'''
		sql_command=format_str.format(id=Ui_Valuation_Expert.val_id)
		self.cursor.execute(sql_command)
		res=self.cursor.fetchall()
		print("AAA")
		print(res)
		# self.tableWidget_2clearContents()
		# for i in range(self.tableWidget_2rowCount()+5):
		#     self.tableWidget_2removeRow(i)
		self.tableWidget_2.setRowCount(0)
		# self.tableWidget_2setColumnCount(0)
		c=0
		print(self.tableWidget_2.rowCount())
		for i in res:
			print(i[2])
			print("JNWD")
			self.createRow()
			print("JNadwdWD")
			print(self.tableWidget_2.rowCount())
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,0).setText(i[2])
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,1).setText(str(i[3]))
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,2).setText(str(i[4]))
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,3).setText(str(i[5]))
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,4).setText(str(i[6]))
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,5).setText(str(i[7]))
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,6).setText(str(i[8]))
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,7).setText(str(i[9]))
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,8).setText(str(i[10]))
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,9).setText(str(i[11]))
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,10).setText(str(i[12]))
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,11).setText(str(i[13]))
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,12).lineEdit().setText(str(i[14]))
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,13).lineEdit().setText(str(i[15]))
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,14).lineEdit().setText(str(i[16]))
			if(i[17]==1):
				self.tableWidget_2.cellWidget(c,15).setChecked(True)
			else:
				pass
			c=c+1
		self.autoUpdateTotals()


	def fillRates(self):
		date=self.dateEdit.lineEdit().text()
		print(date)
		try:
			format_str='''SELECT * FROM Rates WHERE From_Date='{date}';'''
			sql_command=format_str.format(date=date)
			print(sql_command)
			self.cursor.execute(sql_command)
			res=self.cursor.fetchone()
			self.lineEdit_48.setText(str(res[3]))
			self.lineEdit_49.setText(str(res[4]))
			self.lineEdit_50.setText(str(res[5]))
			self.lineEdit_51.setText(str(res[6]))
			self.lineEdit_52.setText(str(res[7]))
		except:
			QtWidgets.QMessageBox.warning(self, 'Error', 'Rates Does Not Exist')

	def MultipleValuation(self):
		date=self.dateEdit_2.lineEdit().text()
		format_str='''SELECT COUNT(*) FROM Auto_Valuation WHERE V_Date='{date}';'''
		sql_command=format_str.format(date=date)
		self.cursor.execute(sql_command)
		res=self.cursor.fetchall()
		if(res[0][0]>1):
			self.popup1=testselection.Ui_Selection(self,'Auto_Valuation',0,[],'V_Date',date)
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
		format_str='''SELECT * FROM Auto_Valuation WHERE V_Date='{date}';'''
		sql_command=format_str.format(date=date)
		self.cursor.execute(sql_command)
		res=self.cursor.fetchone()
		print(res[0])
		Ui_Valuation_Expert.val_id=res[0]
		self.dateEdit_2.lineEdit().setText(str(res[1]))
		self.dateEdit.lineEdit().setText(str(res[2]))
		self.lineEdit_48.setText(str(res[3]))
		self.lineEdit_49.setText(str(res[4]))
		self.lineEdit_50.setText(str(res[5]))
		self.lineEdit_51.setText(str(res[6]))
		self.lineEdit_52.setText(str(res[7]))
		self.lineEdit_53.setText(str(res[8]))
		self.lineEdit_54.setText(str(res[9]))
		if(res[10]=='Amount'):
			self.radioButton_5.setChecked(True)
		elif(res[10]=='Weight'):
			self.radioButton_6.setChecked(True)
		else:
			self.radioButton.setChecked(True)
		
		if(res[11]==1):
			self.checkBox_4.setChecked(True)
		self.lineEdit_55.setText(str(res[12]))
		self.lineEdit_59.setText(str(res[13]))
		if(res[14]==1):
			self.checkBox_3.setChecked(True)
		self.lineEdit_56.setText(str(res[15]))
		self.lineEdit_60.setText(str(res[16]))
		if(res[17]==1):
			self.checkBox_2.setChecked(True)
		self.lineEdit_57.setText(str(res[18]))
		self.lineEdit_61.setText(str(res[19]))
		if(res[20]==1):
			self.checkBox.setChecked(True)
		self.lineEdit_25.setText(str(res[21]))
		self.lineEdit_22.setText(str(res[22]))
		self.comboBox_7.lineEdit().setText(str(res[23]))
		self.lineEdit_64.setText(str(res[24]))
		self.lineEdit_65.setText(str(res[25]))
		self.lineEdit_66.setText(str(res[26]))
		self.lineEdit_67.setText(str(res[27]))
		self.lineEdit_68.setText(str(res[28]))
		self.lineEdit_69.setText(str(res[29]))
		self.lineEdit_70.setText(str(res[30]))
		self.lineEdit_71.setText(str(res[31]))
		self.lineEdit_72.setText(str(res[32]))
		self.lineEdit_17.setText(str(res[33]))
		self.lineEdit_19.setText(str(res[34]))
		self.lineEdit_25.setText(str(res[35]))
		self.lineEdit_22.setText(str(res[36]))
		self.lineEdit_18.setText(str(res[37]))
		self.lineEdit_20.setText(str(res[38]))
		self.lineEdit_26.setText(str(res[39]))
		self.lineEdit_23.setText(str(res[40]))
		self.lineEdit_16.setText(str(res[41]))
		self.lineEdit_21.setText(str(res[42]))
		self.lineEdit_24.setText(str(res[43]))
		self.lineEdit_27.setText(str(res[44]))
		self.lineEdit_73.setText(str(res[45]))
		self.lineEdit_74.setText(str(res[46]))


		format_str='''SELECT * FROM Auto_Products WHERE Valuation_id ='{id}';'''
		sql_command=format_str.format(id=Ui_Valuation_Expert.val_id)
		self.cursor.execute(sql_command)
		res=self.cursor.fetchall()
		print("AAA")
		print(res)
		# self.tableWidget_2clearContents()
		# for i in range(self.tableWidget_2rowCount()+5):
		#     self.tableWidget_2removeRow(i)
		self.tableWidget_2.setRowCount(0)
		# self.tableWidget_2setColumnCount(0)
		c=0
		print(self.tableWidget_2.rowCount())
		for i in res:
			print(i[2])
			print("JNWD")
			self.createRow()
			print("JNadwdWD")
			print(self.tableWidget_2.rowCount())
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,0).setText(i[2])
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,1).setText(str(i[3]))
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,2).setText(str(i[4]))
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,3).setText(str(i[5]))
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,4).setText(str(i[6]))
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,5).setText(str(i[7]))
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,6).setText(str(i[8]))
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,7).setText(str(i[9]))
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,8).setText(str(i[10]))
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,9).setText(str(i[11]))
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,10).setText(str(i[12]))
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,11).setText(str(i[13]))
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,12).lineEdit().setText(str(i[14]))
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,13).lineEdit().setText(str(i[15]))
			self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,14).lineEdit().setText(str(i[16]))
			if(i[17]==1):
				self.tableWidget_2.cellWidget(c,15).setChecked(True)
			else:
				pass
			c=c+1
		self.autoUpdateTotals()


	def new_btn(self):
		sql_command='''SELECT id FROM Last_Auto_id;'''
		self.cursor.execute(sql_command)
		res=self.cursor.fetchone()
		id=res[0]+1
		rate_date=self.dateEdit.lineEdit().text()
		valuation_date=self.dateEdit_2.lineEdit().text()
		G_rate=float(self.lineEdit_48.text())
		S_rate=float(self.lineEdit_49.text())
		P_rate=float(self.lineEdit_50.text())
		D_rate=float(self.lineEdit_51.text())
		Soverign_rate=float(self.lineEdit_52.text())
		Coin_rate=float(self.lineEdit_53.text())
		Amount=float(self.lineEdit_54.text())
		if(self.radioButton_5.isChecked()):
			mode='Amount'
		elif(self.radioButton_6.isChecked()):
			mode='Weight'
		else:
			mode='Percent'
		if(self.checkBox_4.isChecked()):
			G_Diamond=1
		else:
			G_Diamond=0
		G_precent=float(self.lineEdit_55.text())
		G_Qty=float(self.lineEdit_59.text())
		if(self.checkBox_3.isChecked()):
			S_Diamond=1
		else:
			S_Diamond=0
		S_precent=float(self.lineEdit_56.text())
		S_Qty=float(self.lineEdit_60.text())
		if(self.checkBox_2.isChecked()):
			P_Diamond=1
		else:
			P_Diamond=0
		P_precent=float(self.lineEdit_57.text())
		P_Qty=float(self.lineEdit_61.text())
		if(self.checkBox.isChecked()):
			W_Diamond=1
		else:
			W_Diamond=0
		W_precent=float(self.lineEdit_58.text())
		W_Qty=float(self.lineEdit_62.text())
		group=self.comboBox_7.lineEdit().text()
		V_Name=self.lineEdit_64.text()
		V_Reg_No=self.lineEdit_65.text()
		Purpose=self.lineEdit_66.text()
		Customer_name=self.lineEdit_67.text()
		Customer_Pan=self.lineEdit_68.text()
		customer_address=self.lineEdit_69.text()
		F_Name=self.lineEdit_70.text()
		F_Address=self.lineEdit_71.text()
		OS_With=self.lineEdit_72.text()
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
		# G_metal=float(self.lineEdit_25.text())
		Diamond_value=float(self.lineEdit_24.text())
		Grand_Total=float(self.lineEdit_27.text())
		G_Purity=float(self.lineEdit_73.text())
		S_Purity=float(self.lineEdit_74.text())
		

		format_str='''INSERT INTO `Auto_Valuation`(`V_Id`,`V_Date`,`Rate_Date`,`Gold_Rate`,`Silver_Rate`,`Platinum_Rate`,`Diamond_Rate`,`Soverign_Rate`,`Coin_Date`,`Valuation_Amount`,`Valuation_Mode`,`G_Diamond`,`G_Percent`,`G_Qty`,`S_Diamond`,`S_Percent`,`S_Qty`,`P_Diamond`,`P_Percent`,`P_Qty`,`W_Diamond`,`W_Percent`,`W_Qty`,`Exclude_Group`,`Valuer_Name`,`Valuer_Reg_No`,`Purpose`,`Customer_name`,`Customer_Pan`,`customer_address`,`F_Name`,`F_Address`,`OS_With`,`G_Total`,`G_Gross`,`G_Metal`,`G_Value`,`S_Total`,`S_Gross`,`S_Metal`,`S_Value`,`Stone_Total`,`Stone_Gross`,`Stone_Value`,`Grand_Total`,`G_Purity`,`S_Purity`) VALUES ({id},'{valuation_date}','{rate_date}',{G_rate},{S_rate},{P_rate},{D_rate},{Soverign_rate},{Coin_rate},{Amount},'{mode}',{G_Diamond},{G_precent},{G_Qty},{S_Diamond},{S_precent},{S_Qty},{P_Diamond},{P_precent},{P_Qty},{W_Diamond},{W_precent},{W_Qty},'{group}','{V_Name}','{V_Reg_No}','{V_Purpose}','{Customer_name}','{Customer_Pan}','{customer_address}','{F_Name}','{F_Address}','{OS_With}',{Gold_total},{Gold_gross},{Gold_metal},{Gold_value},{Silver_total},{Silver_gross},{Silver_metal},{Silver_value},{Diamond_total},{Diamond_gross},{Diamond_value},{Grand_Total},{G_Purity},{S_Purity});'''
		sql_command=format_str.format(id=id,valuation_date=valuation_date,rate_date=rate_date,G_rate=G_rate,S_rate=S_rate,P_rate=P_rate,D_rate=D_rate,Soverign_rate=Soverign_rate,Coin_rate=Coin_rate,Amount=Amount,mode=mode,G_Diamond=G_Diamond,G_precent=G_precent,G_Qty=G_Qty,S_Diamond=S_Diamond,S_precent=S_precent,S_Qty=S_Qty,P_Diamond=P_Diamond,P_precent=P_precent,P_Qty=P_Qty,W_Diamond=W_Diamond,W_precent=W_precent,W_Qty=W_Qty,group=group,V_Name=V_Name,V_Reg_No=V_Reg_No,V_Purpose=Purpose,Customer_name=Customer_name,Customer_Pan=Customer_Pan,customer_address=customer_address,F_Name=F_Name,F_Address=F_Address,OS_With=OS_With,Gold_total=Gold_total,Gold_gross=Gold_gross,Gold_metal=Gold_metal,Gold_value=Gold_value,Silver_total=Silver_total,Silver_gross=Silver_gross,Silver_metal=Silver_metal,Silver_value=Silver_value,Diamond_total=Diamond_total,Diamond_gross=Diamond_gross,Diamond_value=Diamond_value,Grand_Total=Grand_Total,G_Purity=G_Purity,S_Purity=S_Purity)
		self.cursor.execute(sql_command)

		for i in range(self.tableWidget_2.rowCount()):
			# for j in range(self.tableWidget_2.colorCount()):
			description=self.tableWidget_2.cellWidget(i,0).text()
			metal_rate=float(self.tableWidget_2.cellWidget(i,1).text())
			purity=float(self.tableWidget_2.cellWidget(i,2).text())
			qty=float(self.tableWidget_2.cellWidget(i,3).text())
			gross_wt=float(self.tableWidget_2.cellWidget(i,4).text())
			metal_wt=float(self.tableWidget_2.cellWidget(i,5).text())
			metal_value=float(self.tableWidget_2.cellWidget(i,6).text())
			s_description=self.tableWidget_2.cellWidget(i,7).text()
			s_wt=float(self.tableWidget_2.cellWidget(i,8).text())
			s_rate=float(self.tableWidget_2.cellWidget(i,9).text())
			s_value=float(self.tableWidget_2.cellWidget(i,10).text())
			total=float(self.tableWidget_2.cellWidget(i,11).text())
			metal=self.tableWidget_2.cellWidget(i,12).lineEdit().text()
			item_ratewise=self.tableWidget_2.cellWidget(i,13).lineEdit().text()
			stone_weightwise=self.tableWidget_2.cellWidget(i,14).lineEdit().text()
			if(self.tableWidget_2.cellWidget(i,15).isChecked()):
				is_soverign=1
			else:
				is_soverign=0
			
			format_str='''INSERT INTO Auto_Products(Valuation_id,Description,Rate,Purity,Quantity,Gross_Wt,Metal_Wt,Metal_Value,Stone_Description,Stone_Wt,Stone_Rate,Stone_Value,Total_Value,Metal,Item_Ratewise,Stone_Weightwise,Is_Soverign) VALUES ({id},'{item_description}',{rate},{purity},{quantity},{gross_wt},{metal_weight},{metal_value},'{stone_description}',{stone_wt},{stone_rate},{stone_value},{total_value},'{metal}','{item_ratewise}','{stone_weightwise}',{is_soverign});'''
			sql_command=format_str.format(id=id,item_description=description,rate=metal_rate,purity=purity,quantity=qty,gross_wt=gross_wt,metal_weight=metal_wt,metal_value=metal_value,stone_description=s_description,stone_wt=s_wt,stone_rate=s_rate,stone_value=s_value,total_value=total,metal=metal,item_ratewise=item_ratewise,stone_weightwise=stone_weightwise,is_soverign=is_soverign)
			self.cursor.execute(sql_command)
		
		format_str='''UPDATE Last_Auto_id SET id={id};'''
		sql_command=format_str.format(id=id)
		self.cursor.execute(sql_command)
		QtWidgets.QMessageBox.information(self, 'Success', 'New Valuation Created')
		self.connection.commit()
		self.default()


	def save_btn(self):
		rate_date=self.dateEdit.lineEdit().text()
		valuation_date=self.dateEdit_2.lineEdit().text()
		G_rate=float(self.lineEdit_48.text())
		S_rate=float(self.lineEdit_49.text())
		P_rate=float(self.lineEdit_50.text())
		D_rate=float(self.lineEdit_51.text())
		Soverign_rate=float(self.lineEdit_52.text())
		Coin_rate=float(self.lineEdit_53.text())
		Amount=float(self.lineEdit_54.text())
		if(self.radioButton_5.isChecked()):
			mode='Amount'
		elif(self.radioButton_6.isChecked()):
			mode='Weight'
		else:
			mode='Percent'
		if(self.checkBox_4.isChecked()):
			G_Diamond=1
		else:
			G_Diamond=0
		G_precent=float(self.lineEdit_55.text())
		G_Qty=float(self.lineEdit_59.text())
		if(self.checkBox_3.isChecked()):
			S_Diamond=1
		else:
			S_Diamond=0
		S_precent=float(self.lineEdit_56.text())
		S_Qty=float(self.lineEdit_60.text())
		if(self.checkBox_2.isChecked()):
			P_Diamond=1
		else:
			P_Diamond=0
		P_precent=float(self.lineEdit_57.text())
		P_Qty=float(self.lineEdit_61.text())
		if(self.checkBox.isChecked()):
			W_Diamond=1
		else:
			W_Diamond=0
		W_precent=float(self.lineEdit_58.text())
		W_Qty=float(self.lineEdit_62.text())
		group=self.comboBox_7.lineEdit().text()
		V_Name=self.lineEdit_64.text()
		V_Reg_No=self.lineEdit_65.text()
		Purpose=self.lineEdit_66.text()
		Customer_name=self.lineEdit_67.text()
		Customer_Pan=self.lineEdit_68.text()
		customer_address=self.lineEdit_69.text()
		F_Name=self.lineEdit_70.text()
		F_Address=self.lineEdit_71.text()
		OS_With=self.lineEdit_72.text()
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
		# G_metal=float(self.lineEdit_25.text())
		Diamond_value=float(self.lineEdit_24.text())
		Grand_Total=float(self.lineEdit_27.text())
		G_Purity=float(self.lineEdit_73.text())
		S_Purity=float(self.lineEdit_74.text())

		format_str='''UPDATE `Auto_Valuation` SET `V_Date`='{valuation_date}',`Rate_Date`='{rate_date}',`Gold_Rate`={G_rate},`Silver_Rate`={S_rate},`Platinum_Rate`={P_rate},`Diamond_Rate`={D_rate},`Soverign_Rate`={Soverign_rate},`Coin_Date`={Coin_rate},`Valuation_Amount`={Amount},`Valuation_Mode`='{mode}',`G_Diamond`={G_Diamond},`G_Percent`={G_precent},`G_Qty`={G_Qty},`S_Diamond`={S_Diamond},`S_Percent`={S_precent},`S_Qty`={S_Qty},`P_Diamond`={P_Diamond},`P_Percent`={P_precent},`P_Qty`={P_Qty},`W_Diamond`={W_Diamond},`W_Percent`={W_precent},`W_Qty`={W_Qty},`Exclude_Group`='{group}',`Valuer_Name`='{V_Name}',`Valuer_Reg_No`='{V_Reg_No}',`Purpose`='{V_Purpose}',`Customer_name`='{Customer_name}',`Customer_Pan`='{Customer_Pan}',`customer_address`='{customer_address}',`F_Name`='{F_Name}',`F_Address`='{F_Address}',`OS_With`='{OS_With}',`G_Total`={Gold_total},`G_Gross`={Gold_gross},`G_Metal`={Gold_metal},`G_Value`={Gold_value},`S_Total`={Silver_total},`S_Gross`={Silver_gross},`S_Metal`={Silver_metal},`S_Value`={Silver_value},`Stone_Total`={Diamond_total},`Stone_Gross`={Diamond_gross},`Stone_Value`={Diamond_value},`Grand_Total`={Grand_Total},`G_Purity`={G_Purity},`S_Purity`={S_Purity} WHERE `V_Id`={id} ;'''
		sql_command=format_str.format(id=Ui_Valuation_Expert.val_id,valuation_date=valuation_date,rate_date=rate_date,G_rate=G_rate,S_rate=S_rate,P_rate=P_rate,D_rate=D_rate,Soverign_rate=Soverign_rate,Coin_rate=Coin_rate,Amount=Amount,mode=mode,G_Diamond=G_Diamond,G_precent=G_precent,G_Qty=G_Qty,S_Diamond=S_Diamond,S_precent=S_precent,S_Qty=S_Qty,P_Diamond=P_Diamond,P_precent=P_precent,P_Qty=P_Qty,W_Diamond=W_Diamond,W_precent=W_precent,W_Qty=W_Qty,group=group,V_Name=V_Name,V_Reg_No=V_Reg_No,V_Purpose=Purpose,Customer_name=Customer_name,Customer_Pan=Customer_Pan,customer_address=customer_address,F_Name=F_Name,F_Address=F_Address,OS_With=OS_With,Gold_total=Gold_total,Gold_gross=Gold_gross,Gold_metal=Gold_metal,Gold_value=Gold_value,Silver_total=Silver_total,Silver_gross=Silver_gross,Silver_metal=Silver_metal,Silver_value=Silver_value,Diamond_total=Diamond_total,Diamond_gross=Diamond_gross,Diamond_value=Diamond_value,Grand_Total=Grand_Total,G_Purity=G_Purity,S_Purity=S_Purity)
		self.cursor.execute(sql_command)

		format_str='''DELETE FROM Auto_Products WHERE Valuation_id={id};'''
		sql_command=format_str.format(id=Ui_Valuation_Expert.val_id)
		self.cursor.execute(sql_command)

		for i in range(self.tableWidget_2.rowCount()):
			# for j in range(self.tableWidget_2.colorCount()):
			description=self.tableWidget_2.cellWidget(i,0).text()
			metal_rate=float(self.tableWidget_2.cellWidget(i,1).text())
			purity=float(self.tableWidget_2.cellWidget(i,2).text())
			qty=float(self.tableWidget_2.cellWidget(i,3).text())
			gross_wt=float(self.tableWidget_2.cellWidget(i,4).text())
			metal_wt=float(self.tableWidget_2.cellWidget(i,5).text())
			metal_value=float(self.tableWidget_2.cellWidget(i,6).text())
			s_description=self.tableWidget_2.cellWidget(i,7).text()
			s_wt=float(self.tableWidget_2.cellWidget(i,8).text())
			s_rate=float(self.tableWidget_2.cellWidget(i,9).text())
			s_value=float(self.tableWidget_2.cellWidget(i,10).text())
			total=float(self.tableWidget_2.cellWidget(i,11).text())
			metal=self.tableWidget_2.cellWidget(i,12).lineEdit().text()
			item_ratewise=self.tableWidget_2.cellWidget(i,13).lineEdit().text()
			stone_weightwise=self.tableWidget_2.cellWidget(i,14).lineEdit().text()
			if(self.tableWidget_2.cellWidget(i,15).isChecked()):
				is_soverign=1
			else:
				is_soverign=0
			
				format_str='''INSERT INTO Auto_Products(Valuation_id,Description,Rate,Purity,Quantity,Gross_Wt,Metal_Wt,Metal_Value,Stone_Description,Stone_Wt,Stone_Rate,Stone_Value,Total_Value,Metal,Item_Ratewise,Stone_Weightwise,Is_Soverign) VALUES ({id},'{item_description}',{rate},{purity},{quantity},{gross_wt},{metal_weight},{metal_value},'{stone_description}',{stone_wt},{stone_rate},{stone_value},{total_value},'{metal}','{item_ratewise}','{stone_weightwise}',{is_soverign});'''
				sql_command=format_str.format(id=Ui_Valuation_Expert.val_id,item_description=description,rate=metal_rate,purity=purity,quantity=qty,gross_wt=gross_wt,metal_weight=metal_wt,metal_value=metal_value,stone_description=s_description,stone_wt=s_wt,stone_rate=s_rate,stone_value=s_value,total_value=total,metal=metal,item_ratewise=item_ratewise,stone_weightwise=stone_weightwise,is_soverign=is_soverign)
				self.cursor.execute(sql_command)
		self.connection.commit()
		QtWidgets.QMessageBox.information(self, 'Success', 'Valuation Updated')

	def cancel_btn(self):
		self.close()

	def Document(self):
		# date=self.comboBox.lineEdit().text()
		# try:
		#     a,valuation_date=self.comboBox_2.lineEdit().text().split("   ")
		# except:
		#     valuation_date=self.comboBox_2.lineEdit().text()
		V_Date=self.dateEdit_2.lineEdit().text()
		print(V_Date)
		format_str='''SELECT * FROM Auto_Valuation WHERE V_Id={id};'''
		sql_command=format_str.format(id=Ui_Valuation_Expert.val_id)
		self.cursor.execute(sql_command)
		res=self.cursor.fetchone()
		if(res is None):
			QtWidgets.QMessageBox.warning(self,"Error","Please Save The Valuation First")
		else:
			print(res)
			id=res[0]
			context={}
			context={'Name':res[24],'Company':res[30],'Address':res[31],'Reg_No':res[25],'Date':res[1],'Customer_name':res[27],'customer_address':res[29],'OS_With':res[32],'Pupose':res[26],'rate_date':res[2]}

			format_str='''SELECT * FROM Auto_Products WHERE Valuation_id={id};'''
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
			filename="generated_doc(Auto) "+str(id)+".docx"
			doc.save(filename)
			print('SUCCESS')
			buttonReply = QMessageBox.question(self, 'Success', "Report Generated \n Do you want to open the Report?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
			if(buttonReply==QMessageBox.Yes):
				if(sys.platform=='linux'):
					command='xdg open ' + filename
					os.system(command)
				elif(sys.platform=='darwin'):
					command='open ' + filename
					os.system(command)
				else:
					command='lowriter ' + filename
					os.system(command)
			else:
				pass

	def ExitTool(self):
		self.a=1
		self.close()

	def AboutTool(self):
		About=""
		self.a=1
		QtWidgets.QMessageBox.information(self, 'About', About)

	def ChangePasswordTool(self):
		self.a=1
		self.change=Change_Password.Ui_ChangePassword()
		self.change.show()

	def ValuationTool(self):
		self.close()
		self.valuation=Valuation.Ui_Valuation()
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
	
	def SplitTool(self):
		self.close()
		self.split=SplitValuation.Ui_Split_Valuation()
		self.split.show()

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

	def SortTable(self):
		data={}
		data['Gold']=[]
		data['Gold+Stone']=[]
		data['Silver']=[]
		data['Silver+Stone']=[]
		data['Platinum']=[]
		data['Platinum+Stone']=[]
		for i in range(self.tableWidget_2.rowCount()):
			row=[]
			for j in range(self.tableWidget_2.columnCount()):
				#DROPBOX
				if(j==12 or j==13 or j==14):
					row.append(self.tableWidget_2.cellWidget(i,j).lineEdit().text())
				#CheckBox
				elif(j==15):
					if(self.tableWidget_2.cellWidget(i,j).isChecked()):
						row.append(1)
					else:
						row.append(0)
				#STRINGS
				elif(j==0 or j==7):
					row.append(self.tableWidget_2.cellWidget(i,j).text())
				elif(j==3):
					row.append(int(self.tableWidget_2.cellWidget(i,j).text()))
				elif(j==16):
					pass
				else:
					row.append(float(self.tableWidget_2.cellWidget(i,j).text()))
			if(self.tableWidget_2.cellWidget(i,12).lineEdit().text()=='Gold' and self.tableWidget_2.cellWidget(i,7).text()=='...'):
				index='Gold'
			elif(self.tableWidget_2.cellWidget(i,12).lineEdit().text()=='Gold'):
				index='Gold+Stone'
			elif(self.tableWidget_2.cellWidget(i,12).lineEdit().text()=='Silver' and self.tableWidget_2.cellWidget(i,7).text()=='...'):
				index='Silver'
			elif(self.tableWidget_2.cellWidget(i,12).lineEdit().text()=='Silver'):
				index='Silver+Stone'
			elif(self.tableWidget_2.cellWidget(i,12).lineEdit().text()=='Platinum' and self.tableWidget_2.cellWidget(i,7).text()=='...'):
				index='Platinum'
			elif(self.tableWidget_2.cellWidget(i,12).lineEdit().text()=='PLatinum'):
				index='Platinum+Stone'
			data[index].append(row)
		print(data)

		for j in data:
			for i in data[j]:
				self.createRow()
				self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,0).setText(i[2])
				self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,1).setText(str(i[3]))
				self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,2).setText(str(i[4]))
				self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,3).setText(str(i[5]))
				self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,4).setText(str(i[6]))
				self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,5).setText(str(i[7]))
				self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,6).setText(str(i[8]))
				self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,7).setText(str(i[9]))
				self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,8).setText(str(i[10]))
				self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,9).setText(str(i[11]))
				self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,10).setText(str(i[12]))
				self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,11).setText(str(i[13]))
				self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,12).lineEdit().setText(str(i[14]))
				self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,13).lineEdit().setText(str(i[15]))
				self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,14).lineEdit().setText(str(i[16]))
				if(i[17]==1):
					self.tableWidget_2.cellWidget(c,15).setChecked(True)
				else:
					pass
				c=c+1


				
				


	def minPurity(self,data):
		if(data==[]):
			return 0
		return min(data)

	def count(self,data):
		return len(data)

	def CheckPurityWise(self,c=0):
		gold=[]
		silver=[]
		platinum=[]
		for i in range(self.tableWidget_2.rowCount()):
			if(self.tableWidget_2.cellWidget(i,12).lineEdit().text()=='Gold'):
				gold.append(float(self.tableWidget_2.cellWidget(i,2).text()))
			elif(self.tableWidget_2.cellWidget(i,12).lineEdit().text()=='Silver'):
				silver.append(float(self.tableWidget_2.cellWidget(i,2).text()))
			else:    
				platinum.append(float(self.tableWidget_2.lineEdit.cellWidget(i,2).text()))
		if(c==0):
			purity='Gold-'+ str(self.minPurity(gold)) + ' || ' + str(self.count(gold)) +'\n' + 'Silver-'+ str(self.minPurity(silver)) + ' || ' + str(self.count(silver)) +"\n" + 'Platinum-'+ str(self.minPurity(platinum)) + ' || ' + str(self.count(platinum)) 
			QtWidgets.QMessageBox.information(self, 'Purity Wise', purity, QMessageBox.Ok, QMessageBox.Ok)
		else:
			self.lineEdit_73.setText(str(self.minPurity(gold)))
			self.lineEdit_74.setText(str(self.minPurity(silver)))





		# self.default()
	#**********************************************************************************************    
	#**********************************************************************************************
	#This is more accurate but without diamond
	# def ValuateGold1(self):
	#     if(self.radioButton_5.isChecked()):
	#         if(self.checkBox_4.isChecked()==0):
	#             Amount=int(self.lineEdit_54.text())
	#             percent=int(self.lineEdit_55.text())
	#             qty=int(self.lineEdit_59.text())
	#             gold_rate=float(self.lineEdit_48.text())

	#             gold_amount=(Amount*percent)/100
	#             gold_wt=(gold_amount*24)/(19.2*(gold_rate/10))
	#             weights=np.random.dirichlet(np.ones(qty))*gold_wt
	#             weights_ptr=0
				
	#             format_str='''SELECT MIN(Min_Wt),MAX(Max_Wt) FROM ITEMS WHERE Metal='{metal}' AND Groups<>'{group}' AND Stone_Description='...';'''
	#             sql_command=format_str.format(metal='Gold',group='Sets')
	#             self.cursor.execute(sql_command)
	#             res=self.cursor.fetchone()
	#             print(res)
	#             while(all(i >= res[0] and i<=res[1] for i in weights)==0):
	#                 weights=np.random.dirichlet(np.ones(qty))*gold_wt

	#             # # label: before
	#             # for i in weights:
	#             #     if(i<res[0] or i>res[1]):
	#             #         weights=np.random.dirichlet(np.ones(qty))*gold_wt
	#             #         # i=weights[0]
	#             #         # goto before
				
	#             print(weights)


	#             format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Groups<>'{group}' AND Stone_Description='...';'''
	#             sql_command=format_str.format(metal='Gold',group='Sets')
	#             print(sql_command)
	#             self.cursor.execute(sql_command)
	#             res=self.cursor.fetchall()
	#             print(res)
	#             # random_weights=[]
	#             i=1
	#             selected=[]
	#             checked=[]
	#             while(i<=qty):
	#                 a=random.randint(1,len(res)-1)
	#                 print(a)
	#                 if(a in selected):
	#                     pass
	#                 else:
	#                     # i=i+1
	#                     print(weights[weights_ptr])
	#                     print("BWYHFCMSFBBHC")
	#                     if(weights[weights_ptr]>res[a][4] and weights[weights_ptr]<res[a][5] and a not in checked):
	#                         print(res[a])
	#                         print(weights[weights_ptr])
	#                         self.fillRowWithoutStone(res[a],weights[weights_ptr])
	#                         selected.append(i)
	#                         # weights.pop(weights_ptr)
	#                         res.pop(a)
	#                         i=i+1
	#                         weights_ptr=weights_ptr+1
	#                         checked.append(a)

	#             self.autoUpdateTotals()
	#     elif(self.radioButton_6.isChecked()):
	#         if(self.checkBox_4.isChecked()==0):
	#             # Amount=int(self.lineEdit_54.text())
	#             gold_wt=int(self.lineEdit_55.text())
	#             qty=int(self.lineEdit_59.text())
	#             gold_rate=float(self.lineEdit_48.text())

	#             # gold_amount=(Amount*percent)/100
	#             # gold_wt=gold_amount/(gold_rate/10)
	#             weights=np.random.dirichlet(np.ones(qty))*gold_wt
	#             weights_ptr=0
	#             format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Groups<>'{group}' AND Stone_Description='...';'''
	#             sql_command=format_str.format(metal='Gold',group='Sets')
	#             self.cursor.execute(sql_command)
	#             res=self.cursor.fetchall()
	#             # random_weights=[]
	#             i=1
	#             selected=[]
	#             while(i<=qty):
	#                 a=random.randint(1,len(res))
	#                 if(a in selected):
	#                     pass
	#                 else:
	#                     # i=i+1
	#                     print(weights[weights_ptr])
	#                     if(weights[weights_ptr]>res[a][4] and weights[weights_ptr]<res[a][5]):
	#                         self.fillRowWithoutStone(res[a],weights[weights_ptr])
	#                         selected.append(i)
	#                         # weights.pop(weights_ptr)
	#                         res.pop(a)
	#                         i=i+1
	#                         weights_ptr=weights_ptr+1
	#             self.autoUpdateTotals()
	#     else:
	#         if(self.checkBox_4.isChecked()==0):
	#             Amount=int(self.lineEdit_54.text())
	#             percent=int(self.lineEdit_55.text())
	#             qty=int(self.lineEdit_59.text())
	#             gold_rate=float(self.lineEdit_48.text())

	#             gold_amount=(Amount*percent)/100
	#             gold_wt=gold_amount/(gold_rate/10)
	#             weights=np.random.dirichlet(np.ones(qty))*gold_wt
	#             weights_ptr=0
	#             format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Groups<>'{group}' AND Stone_Description='.%';'''
	#             sql_command=format_str.format(metal='Gold',group=self.comboBox_7.lineEdit().text())
	#             self.cursor.execute(sql_command)
	#             res=self.cursor.fetchall()
	#             # random_weights=[]
	#             i=1
	#             selected=[]
	#             while(i<=qty):
	#                 a=random.randint(1,len(res))
	#                 if(a in selected):
	#                     pass
	#                 else:
	#                     # i=i+1
	#                     if(weights[weights_ptr]>res[a][4] and weights[weights_ptr]<res[a][5]):
	#                         self.fillRowWithoutStone(res[a],weights[weights_ptr])
	#                         selected.append(i)
	#                         weights.pop(weights_ptr)
	#                         res.pop(a)
	#                         i=i+1
	#                         weights_ptr=weights_ptr+1


	# def ValuateSilver1(self):
	#     if(self.radioButton_5.isChecked()):
	#         if(self.checkBox_3.isChecked()==0):
	#             Amount=int(self.lineEdit_54.text())
	#             percent=int(self.lineEdit_56.text())
	#             qty=int(self.lineEdit_60.text())
	#             silver_rate=float(self.lineEdit_49.text())

	#             silver_amount=(Amount*percent)/100
	#             silver_wt=silver_amount/(silver_rate/1000)
	#             weights=np.random.dirichlet(np.ones(qty))*silver_wt
	#             weights_ptr=0
	#             format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Groups<>'{group}' AND Stone_Description='...';'''
	#             sql_command=format_str.format(metal='Silver',group='Sets')
	#             print(sql_command)
	#             self.cursor.execute(sql_command)
	#             res=self.cursor.fetchall()
	#             print(res)
	#             # random_weights=[]
	#             i=1
	#             selected=[]
	#             while(i<=qty):
	#                 a=random.randint(1,len(res)-1)
	#                 if(a in selected):
	#                     pass
	#                 else:
	#                     # i=i+1
	#                     if(weights[weights_ptr]>res[a][4] and weights[weights_ptr]<res[a][5]):
	#                         self.fillRowWithoutStone(res[a],weights[weights_ptr])
	#                         selected.append(i)
	#                         # weights.pop(weights_ptr)
	#                         res.pop(a)
	#                         i=i+1
	#                         weights_ptr=weights_ptr+1
	#     elif(self.radioButton_6.isChecked()):
	#         if(self.checkBox_3.isChecked()==0):
	#             # Amount=int(self.lineEdit_54.text())
	#             silver_wt=int(self.lineEdit_56.text())
	#             qty=int(self.lineEdit_60.text())
	#             silver_rate=float(self.lineEdit_49.text())

	#             # gold_amount=(Amount*percent)/100
	#             # gold_wt=gold_amount/(gold_rate/10)
	#             weights=np.random.dirichlet(np.ones(qty))*silver_wt
	#             weights_ptr=0
	#             format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Groups<>'{group}' AND Stone_Description='.%';'''
	#             sql_command=format_str.format(metal='Silver',group=self.comboBox_7.lineEdit().text())
	#             self.cursor.execute(sql_command)
	#             res=self.cursor.fetchall()
	#             # random_weights=[]
	#             i=1
	#             selected=[]
	#             while(i<=qty):
	#                 a=random.randint(1,len(res))
	#                 if(a in selected):
	#                     pass
	#                 else:
	#                     # i=i+1
	#                     if(weights[weights_ptr]>res[a][4] and weights[weights_ptr]<res[a][5]):
	#                         self.fillRowWithoutStone(res[a],weights[weights_ptr])
	#                         selected.append(i)
	#                         weights.pop(weights_ptr)
	#                         res.pop(a)
	#                         i=i+1
	#                         weights_ptr=weights_ptr+1
	#     else:
	#         if(self.checkBox_3.isChecked()==0):
	#             Amount=int(self.lineEdit_54.text())
	#             percent=int(self.lineEdit_56.text())
	#             qty=int(self.lineEdit_60.text())
	#             silver_rate=float(self.lineEdit_49.text())

	#             silver_amount=(Amount*percent)/100
	#             silver_wt=silver_amount/(silver_rate/1000)
	#             weights=np.random.dirichlet(np.ones(qty))*silver_wt
	#             weights_ptr=0
	#             format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Groups<>'{group}' AND Stone_Description='.%';'''
	#             sql_command=format_str.format(metal='Silver',group=self.comboBox_7.lineEdit().text())
	#             self.cursor.execute(sql_command)
	#             res=self.cursor.fetchall()
	#             # random_weights=[]
	#             i=1
	#             selected=[]
	#             while(i<=qty):
	#                 a=random.randint(1,len(res))
	#                 if(a in selected):
	#                     pass
	#                 else:
	#                     # i=i+1
	#                     if(weights[weights_ptr]>res[a][4] and weights[weights_ptr]<res[a][5]):
	#                         self.fillRowWithoutStone(res[a],weights[weights_ptr])
	#                         selected.append(i)
	#                         weights.pop(weights_ptr)
	#                         res.pop(a)
	#                         i=i+1
	#                         weights_ptr=weights_ptr+1

	# def ValuatePlatinum1(self):
	#     if(self.radioButton_5.isChecked()):
	#         if(self.checkBox_2.isChecked()==0):
	#             Amount=int(self.lineEdit_54.text())
	#             percent=int(self.lineEdit_57.text())
	#             qty=int(self.lineEdit_61.text())
	#             platinum_rate=float(self.lineEdit_50.text())

	#             platinum_amount=(Amount*percent)/100
	#             platinum_wt=platinum_amount/(platinum_rate/10)
	#             weights=np.random.dirichlet(np.ones(qty))*platinum_wt
	#             weights_ptr=0
	#             format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Groups<>'{group}' AND Stone_Description='.%';'''
	#             sql_command=format_str.format(metal='Platinum',group=self.comboBox_7.lineEdit().text())
	#             self.cursor.execute(sql_command)
	#             res=self.cursor.fetchall()
	#             # random_weights=[]
	#             i=1
	#             selected=[]
	#             while(i<=qty):
	#                 a=random.randint(1,len(res))
	#                 if(a in selected):
	#                     pass
	#                 else:
	#                     # i=i+1
	#                     if(weights[weights_ptr]>res[a][4] and weights[weights_ptr]<res[a][5]):
	#                         self.fillRowWithoutStone(res[a],weights[weights_ptr])
	#                         selected.append(i)
	#                         weights.pop(weights_ptr)
	#                         res.pop(a)
	#                         i=i+1
	#                         weights_ptr=weights_ptr+1
	#     elif(self.radioButton_6.isChecked()):
	#         if(self.checkBox_2.isChecked()==0):
	#             # Amount=int(self.lineEdit_54.text())
	#             platinum_wt=int(self.lineEdit_57.text())
	#             qty=int(self.lineEdit_61.text())
	#             platinum_rate=float(self.lineEdit_50.text())

	#             # gold_amount=(Amount*percent)/100
	#             # gold_wt=gold_amount/(gold_rate/10)
	#             weights=np.random.dirichlet(np.ones(qty))*platinum_wt
	#             weights_ptr=0
	#             format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Groups<>'{group}' AND Stone_Description='.%';'''
	#             sql_command=format_str.format(metal='Platinum',group=self.comboBox_7.lineEdit().text())
	#             self.cursor.execute(sql_command)
	#             res=self.cursor.fetchall()
	#             # random_weights=[]
	#             i=1
	#             selected=[]
	#             while(i<=qty):
	#                 a=random.randint(1,len(res))
	#                 if(a in selected):
	#                     pass
	#                 else:
	#                     # i=i+1
	#                     if(weights[weights_ptr]>res[a][4] and weights[weights_ptr]<res[a][5]):
	#                         self.fillRowWithoutStone(res[a],weights[weights_ptr])
	#                         selected.append(i)
	#                         weights.pop(weights_ptr)
	#                         res.pop(a)
	#                         i=i+1
	#                         weights_ptr=weights_ptr+1
	#     else:
	#         if(self.checkBox_2.isChecked()==0):
	#             Amount=int(self.lineEdit_54.text())
	#             percent=int(self.lineEdit_57.text())
	#             qty=int(self.lineEdit_61.text())
	#             platinum_rate=float(self.lineEdit_50.text())

	#             platinum_amount=(Amount*percent)/100
	#             platinum_wt=platinum_amount/(platinum_rate/10)
	#             weights=np.random.dirichlet(np.ones(qty))*platinum_wt
	#             weights_ptr=0
	#             format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Groups<>'{group}' AND Stone_Description='.%';'''
	#             sql_command=format_str.format(metal='Platinum',group=self.comboBox_7.lineEdit().text())
	#             self.cursor.execute(sql_command)
	#             res=self.cursor.fetchall()
	#             # random_weights=[]
	#             i=1
	#             selected=[]
	#             while(i<=qty):
	#                 a=random.randint(1,len(res))
	#                 if(a in selected):
	#                     pass
	#                 else:
	#                     # i=i+1
	#                     if(weights[weights_ptr]>res[a][4] and weights[weights_ptr]<res[a][5]):
	#                         self.fillRowWithoutStone(res[a],weights[weights_ptr])
	#                         selected.append(i)
	#                         weights.pop(weights_ptr)
	#                         res.pop(a)
	#                         i=i+1
	#                         weights_ptr=weights_ptr+1


	# def ValuateWhiteMetal1(self):
	#     if(self.radioButton_5.isChecked()):
	#         if(self.checkBox.isChecked()):
	#             Amount=int(self.lineEdit_54.text())
	#             percent=int(self.lineEdit_57.text())
	#             qty=int(self.lineEdit_61.text())
	#             white_metal_rate=float(self.lineEdit_50.text())

	#             platinum_amount=(Amount*percent)/100
	#             platinum_wt=platinum_amount/(white_metal_rate/10)
	#             weights=np.random.dirichlet(np.ones(qty))*platinum_wt
	#             weights_ptr=0
	#             format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Groups<>'{group}' AND Stone_Description='.%';'''
	#             sql_command=format_str.format(metal='Platinum',group=self.comboBox_7.lineEdit().text())
	#             self.cursor.execute(sql_command)
	#             res=self.cursor.fetchall()
	#             # random_weights=[]
	#             i=1
	#             selected=[]
	#             while(i<=qty):
	#                 a=random.randint(1,len(res))
	#                 if(a in selected):
	#                     pass
	#                 else:
	#                     # i=i+1
	#                     if(weights[weights_ptr]>res[a][4] and weights[weights_ptr]<res[a][5]):
	#                         self.fillRowWithoutStone(res[a],weights[weights_ptr])
	#                         selected.append(i)
	#                         weights.pop(weights_ptr)
	#                         res.pop(a)
	#                         i=i+1
	#                         weights_ptr=weights_ptr+1
	#     elif(self.radioButton_6.isChecked()):
	#         if(self.checkBox_2.isChecked()==0):
	#             # Amount=int(self.lineEdit_54.text())
	#             platinum_wt=int(self.lineEdit_57.text())
	#             qty=int(self.lineEdit_61.text())
	#             platinum_rate=float(self.lineEdit_50.text())

	#             # gold_amount=(Amount*percent)/100
	#             # gold_wt=gold_amount/(gold_rate/10)
	#             weights=np.random.dirichlet(np.ones(qty))*platinum_wt
	#             weights_ptr=0
	#             format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Groups<>'{group}' AND Stone_Description='.%';'''
	#             sql_command=format_str.format(metal='Platinum',group=self.comboBox_7.lineEdit().text())
	#             self.cursor.execute(sql_command)
	#             res=self.cursor.fetchall()
	#             # random_weights=[]
	#             i=1
	#             selected=[]
	#             while(i<=qty):
	#                 a=random.randint(1,len(res))
	#                 if(a in selected):
	#                     pass
	#                 else:
	#                     # i=i+1
	#                     if(weights[weights_ptr]>res[a][4] and weights[weights_ptr]<res[a][5]):
	#                         self.fillRowWithoutStone(res[a],weights[weights_ptr])
	#                         selected.append(i)
	#                         weights.pop(weights_ptr)
	#                         res.pop(a)
	#                         i=i+1
	#                         weights_ptr=weights_ptr+1
	#     else:
	#         if(self.checkBox_2.isChecked()==0):
	#             Amount=int(self.lineEdit_54.text())
	#             percent=int(self.lineEdit_57.text())
	#             qty=int(self.lineEdit_61.text())
	#             platinum_rate=float(self.lineEdit_50.text())

	#             platinum_amount=(Amount*percent)/100
	#             platinum_wt=platinum_amount/(platinum_rate/10)
	#             weights=np.random.dirichlet(np.ones(qty))*platinum_wt
	#             weights_ptr=0
	#             format_str='''SELECT * FROM Items WHERE Metal='{metal}' AND Groups<>'{group}' AND Stone_Description='.%';'''
	#             sql_command=format_str.format(metal='Platinum',group=self.comboBox_7.lineEdit().text())
	#             self.cursor.execute(sql_command)
	#             res=self.cursor.fetchall()
	#             # random_weights=[]
	#             i=1
	#             selected=[]
	#             while(i<=qty):
	#                 a=random.randint(1,len(res))
	#                 if(a in selected):
	#                     pass
	#                 else:
	#                     # i=i+1
	#                     if(weights[weights_ptr]>res[a][4] and weights[weights_ptr]<res[a][5]):
	#                         self.fillRowWithoutStone(res[a],weights[weights_ptr])
	#                         selected.append(i)
	#                         weights.pop(weights_ptr)
	#                         res.pop(a)
	#                         i=i+1
	#                         weights_ptr=weights_ptr+1












	#********************************************************************************************    
	#********************************************************************************************  

	# def ValuateSilver(self):
	#     if(self.radioButton_5.isChecked()):
	#         if(self.checkBox_3.isChecked()==0):

	#             Amount=int(self.lineEdit_54.text())
	#             percent=int(self.lineEdit_56.text())
	#             qty=int(self.lineEdit_60.text())
	#             silver_rate=float(self.lineEdit_49.text())

	#             silver_amount=(Amount*percent)/100
	#             silver_wt=gold_amount/(gold_rate/1000)
	#             a=np.random.dirichlet(np.ones(qty))*silver_wt
	#             list1=[]

	#             for i in a:
	#                 format_str='''SELECT TOP 1 * FROM Items WHERE Metal='Silver' AND Groups<>'{group}' AND Stone_Description='.%' AND IsActive=1 ORDER BY ABS((Min_Wt+Max_wt)/2-{input});'''
	#                 sql_command=format_str.format(group=self.comboBox_7.lineEdit().text(),input=i)
	#                 self.cursor.execute(sql_command)
	#                 res=self.cursor.fetchone()
	#                 if(res[0] in list1):
	#                     pass
	#                 else:
	#                     list1.append(res[0])
	#                     self.createRow()
	#                     self.tableWidget_2_2.cellWidget(self.tableWidget_2_2.rowCount()-1,0).setText(res[1])
	#                     self.tableWidget_2_2.cellWidget(self.tableWidget_2_2.rowCount()-1,1).setText(silver_rate)
						
	#                     self.tableWidget_2_2.cellWidget(self.tableWidget_2_2.rowCount()-1,2).setText(str(res[7]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,3).setText(str(1))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,4).setText(str((res[4]+res[5])/2))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,5).setText(str((res[4]+res[5])/2))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,6).setText(str((silver_rate*res[7]*(res[4]+res[5])/2)/24))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,7).setText(str(res[8]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,8).setText(str(0.0))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,9).setText(str(0.0))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,10).setText(str(0.0))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,11).setText(str(silver_rate*res[7]*(res[4]+res[5])/2)/24))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,12).lineEdit().setText(res[6])
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,13).lineEdit().setText(str(res[3]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,14).lineEdit().setText(str(res[10]))
	#                     self.autoTotal()
				

	#         else:

	#             Amount=int(self.lineEdit_54.text())
	#             percent=int(self.lineEdit_55.text())
	#             qty=int(self.lineEdit_59.text())
	#             silver_rate=float(self.lineEdit_49.text())

	#             silver_amount=(Amount*percent)/100
	#             silver_wt=gold_amount/(gold_rate/1000)
	#             a=np.random.dirichlet(np.ones(qty))*silver_wt
	#             list1=[]

	#             for i in a:
	#                 format_str='''SELECT TOP 1 * FROM Items WHERE Metal='Silver' AND Groups<>'{group}' AND IsActive=1 ORDER BY ABS((Min_Wt+Max_wt)/2-{input});'''
	#                 sql_command=format_str.format(group=self.comboBox_7.lineEdit().text(),input=i)
	#                 self.cursor.execute(sql_command)
	#                 res=self.cursor.fetchone()
	#                 if(res[0] in list1):
	#                     pass
	#                 else:
	#                     list1.append(res[0])
	#                     self.createRow()
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,0).setText(res[1])
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,1).setText(str(silver_rate))
						
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,2).setText(str(res[7]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,3).setText(str(1))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,4).setText(str((res[4]+res[5])/2))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,5).setText(str((res[4]+res[5])/2))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,6).setText(str((int(self.lineEdit_48.text())*res[7]*(res[4]+res[5])/2)/24))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,7).setText(str(res[8]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,8).setText(str((res[9]+res[10])/2))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,9).setText(str(self.lineEdit_51.text()))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,10).setText(str(int(self.lineEdit_51.text()*(res[9]+res[10])/2)))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,11).setText(str((int(self.lineEdit_48.text())*res[7]*(res[4]+res[5])/2)/24))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,12).lineEdit().setText(res[6])
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,13).lineEdit().setText(str(res[3]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,14).lineEdit().setText(str(res[10]))
	#                     self.autoTotal()

	#     elif(self.radioButton_6.isChecked()):
	#         if(self.checkBox_4.isChecked()==0):

	#             # Amount=int(self.lineEdit_54.text())
	#             wt=int(self.lineEdit_55.text())
	#             qty=int(self.lineEdit_59.text())
	#             gold_rate=float(self.lineEdit_48.text())

	#             # gold_amount=(Amount*percent)/100
	#             # gold_wt=gold_amount/(gold_rate/10)
	#             a=np.random.dirichlet(np.ones(qty))*gold_wt
	#             list1=[]

	#             for i in a:
	#                 format_str='''SELECT TOP 1 * FROM Items WHERE Metal='Gold' AND Groups<>'{group}' AND Stone_Description='.%' AND IsActive=1 ORDER BY ABS((Min_Wt+Max_wt)/2-{input});'''
	#                 sql_command=format_str.format(group=self.comboBox_7.lineEdit().text(),input=i)
	#                 self.cursor.execute(sql_command)
	#                 res=self.cursor.fetchone()
	#                 if(res[0] in list1):
	#                     pass
	#                 else:
	#                     list1.append(res[0])
	#                     self.createRow()
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,0).setText(res[1])
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,1).setText(self.lineEdit_48.text())
						
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,2).setText(str(res[7]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,3).setText(str(1))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,4).setText(str((res[4]+res[5])/2))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,5).setText(str((res[4]+res[5])/2))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,6).setText(str((int(self.lineEdit_48.text())*res[7]*(res[4]+res[5])/2)/24))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,7).setText(str(res[8]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,8).setText(str(0.0))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,9).setText(str(0.0))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,10).setText(str(0.0))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,11).setText(str((int(self.lineEdit_48.text())*res[7]*(res[4]+res[5])/2)/24))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,12).lineEdit().setText(res[6])
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,13).lineEdit().setText(str(res[3]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,14).lineEdit().setText(str(res[10]))
	#                     self.autoTotal()
	#         else:

	#             # Amount=int(self.lineEdit_54.text())
	#             wt=int(self.lineEdit_55.text())
	#             qty=int(self.lineEdit_59.text())
	#             gold_rate=float(self.lineEdit_48.text())

	#             # gold_amount=(Amount*percent)/100
	#             # gold_wt=gold_amount/(gold_rate/10)
	#             a=np.random.dirichlet(np.ones(qty))*gold_wt
	#             list1=[]

	#             for i in a:
	#                 format_str='''SELECT TOP 1 * FROM Items WHERE Metal='Gold' AND Groups<>'{group}' AND IsActive=1 ORDER BY ABS((Min_Wt+Max_wt)/2-{input});'''
	#                 sql_command=format_str.format(group=self.comboBox_7.lineEdit().text(),input=i)
	#                 self.cursor.execute(sql_command)
	#                 res=self.cursor.fetchone()
	#                 if(res[0] in list1):
	#                     pass
	#                 else:
	#                     list1.append(res[0])
	#                     self.createRow()
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,0).setText(res[1])
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,1).setText(self.lineEdit_48.text())
						
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,2).setText(str(res[7]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,3).setText(str(1))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,4).setText(str((res[4]+res[5])/2))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,5).setText(str((res[4]+res[5])/2))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,6).setText(str((int(self.lineEdit_48.text())*res[7]*(res[4]+res[5])/2)/24))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,7).setText(str(res[8]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,8).setText(str((res[9]+res[10])/2))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,9).setText(str(self.lineEdit_51.text()))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,10).setText(str(int(self.lineEdit_51.text()*(res[9]+res[10])/2)))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,11).setText(str((int(self.lineEdit_48.text())*res[7]*(res[4]+res[5])/2)/24))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,12).lineEdit().setText(res[6])
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,13).lineEdit().setText(str(res[3]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,14).lineEdit().setText(str(res[10]))
	#                     self.autoTotal()

	#     elif(self.radioButton.isChecked()):
	#         if(self.checkBox_4.isChecked()==0):

	#         Amount=int(self.lineEdit_54.text())
	#         percent=int(self.lineEdit_55.text())
	#         qty=int(self.lineEdit_59.text())
	#         gold_rate=float(self.lineEdit_48.text())

	#         gold_amount=(Amount*percent)/100
	#         gold_wt=gold_amount/(gold_rate/10)
	#         a=np.random.dirichlet(np.ones(qty))*gold_wt
	#         list1=[]

	#         for i in a:
	#             format_str='''SELECT TOP 1 * FROM Items WHERE Metal='Gold' AND Groups<>'{group}' AND Stone_Description='.%' AND IsActive=1 ORDER BY ABS((Min_Wt+Max_wt)/2-{input});'''
	#             sql_command=format_str.format(group=self.comboBox_7.lineEdit().text(),input=i)
	#             self.cursor.execute(sql_command)
	#             res=self.cursor.fetchone()
	#             if(res[0] is in list1):
	#                 pass
	#             else:
	#                 list1.append(res[0])
	#                 self.createRow()
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,0).setText(res[1])
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,1).setText(self.lineEdit_48.text())
					
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,2).setText(str(res[7]))
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,3).setText(str(1))
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,4).setText(str((res[4]+res[5])/2)
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,5).setText(str((res[4]+res[5])/2))
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,6).setText(str((int(self.lineEdit_48.text())*res[7]*(res[4]+res[5])/2)/24)
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,7).setText(str(res[8]))
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,8).setText(str(0.0))
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,9).setText(str(0.0))
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,10).setText(str(0.0))
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,11).setText(str((int(self.lineEdit_48.text())*res[7]*(res[4]+res[5])/2)/24)
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,12).lineEdit().setText(res[6])
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,13).lineEdit().setText(str(res[3]))
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,14).lineEdit().setText(str(res[10]))
	#                 self.autoTotal()
	#         else:

	#             Amount=int(self.lineEdit_54.text())
	#             percent=int(self.lineEdit_55.text())
	#             qty=int(self.lineEdit_59.text())
	#             gold_rate=float(self.lineEdit_48.text())

	#             gold_amount=(Amount*percent)/100
	#             gold_wt=gold_amount/(gold_rate/10)
	#             a=np.random.dirichlet(np.ones(qty))*gold_wt
	#             list1=[]

	#             for i in a:

	#                 format_str='''SELECT TOP 1 * FROM Items WHERE Metal='Gold' AND Groups<>'{group}' AND IsActive=1 ORDER BY ABS((Min_Wt+Max_wt)/2-{input});'''
	#                 sql_command=format_str.format(group=self.comboBox_7.lineEdit().text(),input=i)
	#                 self.cursor.execute(sql_command)
	#                 res=self.cursor.fetchone()
	#                 if(res[0] is in list1):
	#                     pass
	#                     # goto a
	#                 else:
	#                     list1.append(res[0])
	#                     self.createRow()
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,0).setText(res[1])
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,1).setText(self.lineEdit_48.text())
						
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,2).setText(str(res[7]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,3).setText(str(1))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,4).setText(str((res[4]+res[5])/2)
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,5).setText(str((res[4]+res[5])/2))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,6).setText(str((int(self.lineEdit_48.text())*res[7]*(res[4]+res[5])/2)/24)
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,7).setText(str(res[8]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,8).setText(str((res[9]+res[10])/2))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,9).setText(str(self.lineEdit_51.text()))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,10).setText(str(int(self.lineEdit_51.text()*(res[9]+res[10])/2)))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,11).setText(str((int(self.lineEdit_48.text())*res[7]*(res[4]+res[5])/2)/24)
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,12).lineEdit().setText(res[6])
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,13).lineEdit().setText(str(res[3]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,14).lineEdit().setText(str(res[10]))
	#                     self.autoTotal()

	#     else:
	#         pass

	# def ValuateGold(self):
		# if(self.radioButton_5.isChecked()):
		#     if(self.checkBox_4.isChecked()==0):

		#         Amount=int(self.lineEdit_54.text())
		#         percent=int(self.lineEdit_55.text())
		#         qty=int(self.lineEdit_59.text())
		#         gold_rate=float(self.lineEdit_48.text())

		#         gold_amount=(Amount*percent)/100
		#         gold_wt=gold_amount/(gold_rate/10)
		#         a=np.random.dirichlet(np.ones(qty))*gold_wt
	#             list1=[]

	#             for i in a:
	#                 format_str='''SELECT TOP 1 * FROM Items WHERE Metal='Gold' AND Groups<>'{group}' AND Stone_Description='.%' AND IsActive=1 ORDER BY ABS((Min_Wt+Max_wt)/2-{input});'''
	#                 sql_command=format_str.format(group=self.comboBox_7.lineEdit().text(),input=i)
	#                 self.cursor.execute(sql_command)
	#                 res=self.cursor.fetchone()
	#                 if(res[0] is in list1):
	#                     pass
	#                 else:
	#                     list1.append(res[0])
	#                     self.createRow()
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,0).setText(res[1])
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,1).setText(self.lineEdit_48.text())
						
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,2).setText(str(res[7]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,3).setText(str(1))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,4).setText(str((res[4]+res[5])/2)
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,5).setText(str((res[4]+res[5])/2))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,6).setText(str((int(self.lineEdit_48.text())*res[7]*(res[4]+res[5])/2)/24)
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,7).setText(str(res[8]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,8).setText(str(0.0))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,9).setText(str(0.0))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,10).setText(str(0.0))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,11).setText(str((int(self.lineEdit_48.text())*res[7]*(res[4]+res[5])/2)/24)
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,12).lineEdit().setText(res[6])
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,13).lineEdit().setText(str(res[3]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,14).lineEdit().setText(str(res[10]))
	#                     self.autoTotal()
				


	#         else:

	#             Amount=int(self.lineEdit_54.text())
	#             percent=int(self.lineEdit_55.text())
	#             qty=int(self.lineEdit_59.text())
	#             gold_rate=float(self.lineEdit_48.text())

	#             gold_amount=(Amount*percent)/100
	#             gold_wt=gold_amount/(gold_rate/10)
	#             a=np.random.dirichlet(np.ones(qty))*gold_wt
	#             list1=[]

	#             for i in a:
	#                 format_str='''SELECT TOP 1 * FROM Items WHERE Metal='Gold' AND Groups<>'{group}' AND IsActive=1 ORDER BY ABS((Min_Wt+Max_wt)/2-{input});'''
	#                 sql_command=format_str.format(group=self.comboBox_7.lineEdit().text(),input=i)
	#                 self.cursor.execute(sql_command)
	#                 res=self.cursor.fetchone()
	#                 if(res[0] is in list1):
	#                     pass
	#                 else:
	#                     list1.append(res[0])
	#                     self.createRow()
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,0).setText(res[1])
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,1).setText(self.lineEdit_48.text())
						
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,2).setText(str(res[7]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,3).setText(str(1))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,4).setText(str((res[4]+res[5])/2)
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,5).setText(str((res[4]+res[5])/2))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,6).setText(str((int(self.lineEdit_48.text())*res[7]*(res[4]+res[5])/2)/24)
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,7).setText(str(res[8]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,8).setText(str((res[9]+res[10])/2))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,9).setText(str(self.lineEdit_51.text()))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,10).setText(str(int(self.lineEdit_51.text()*(res[9]+res[10])/2)))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,11).setText(str((int(self.lineEdit_48.text())*res[7]*(res[4]+res[5])/2)/24)
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,12).lineEdit().setText(res[6])
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,13).lineEdit().setText(str(res[3]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,14).lineEdit().setText(str(res[10]))
	#                     self.autoTotal()

	#     elif(self.radioButton_6.isChecked()):
	#         if(self.checkBox_4.isChecked()==0):

	#             # Amount=int(self.lineEdit_54.text())
	#             wt=int(self.lineEdit_55.text())
	#             qty=int(self.lineEdit_59.text())
	#             gold_rate=float(self.lineEdit_48.text())

	#             # gold_amount=(Amount*percent)/100
	#             # gold_wt=gold_amount/(gold_rate/10)
	#             a=np.random.dirichlet(np.ones(qty))*gold_wt
	#             list1=[]

	#             for i in a:
	#                 format_str='''SELECT TOP 1 * FROM Items WHERE Metal='Gold' AND Groups<>'{group}' AND Stone_Description='.%' AND IsActive=1 ORDER BY ABS((Min_Wt+Max_wt)/2-{input});'''
	#                 sql_command=format_str.format(group=self.comboBox_7.lineEdit().text(),input=i)
	#                 self.cursor.execute(sql_command)
	#                 res=self.cursor.fetchone()
	#                 if(res[0] is in list1):
	#                     pass
	#                 else:
	#                     list1.append(res[0])
	#                     self.createRow()
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,0).setText(res[1])
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,1).setText(self.lineEdit_48.text())
						
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,2).setText(str(res[7]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,3).setText(str(1))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,4).setText(str((res[4]+res[5])/2)
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,5).setText(str((res[4]+res[5])/2))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,6).setText(str((int(self.lineEdit_48.text())*res[7]*(res[4]+res[5])/2)/24)
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,7).setText(str(res[8]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,8).setText(str(0.0))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,9).setText(str(0.0))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,10).setText(str(0.0))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,11).setText(str((int(self.lineEdit_48.text())*res[7]*(res[4]+res[5])/2)/24)
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,12).lineEdit().setText(res[6])
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,13).lineEdit().setText(str(res[3]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,14).lineEdit().setText(str(res[10]))
	#                     self.autoTotal()
	#         else:

	#             # Amount=int(self.lineEdit_54.text())
	#             wt=int(self.lineEdit_55.text())
	#             qty=int(self.lineEdit_59.text())
	#             gold_rate=float(self.lineEdit_48.text())

	#             # gold_amount=(Amount*percent)/100
	#             # gold_wt=gold_amount/(gold_rate/10)
	#             a=np.random.dirichlet(np.ones(qty))*gold_wt
	#             list1=[]

	#             for i in a:
	#                 format_str='''SELECT TOP 1 * FROM Items WHERE Metal='Gold' AND Groups<>'{group}' AND IsActive=1 ORDER BY ABS((Min_Wt+Max_wt)/2-{input});'''
	#                 sql_command=format_str.format(group=self.comboBox_7.lineEdit().text(),input=i)
	#                 self.cursor.execute(sql_command)
	#                 res=self.cursor.fetchone()
	#                 if(res[0] is in list1):
	#                     pass
	#                 else:
	#                     list1.append(res[0])
	#                     self.createRow()
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,0).setText(res[1])
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,1).setText(self.lineEdit_48.text())
						
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,2).setText(str(res[7]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,3).setText(str(1))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,4).setText(str((res[4]+res[5])/2)
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,5).setText(str((res[4]+res[5])/2))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,6).setText(str((int(self.lineEdit_48.text())*res[7]*(res[4]+res[5])/2)/24)
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,7).setText(str(res[8]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,8).setText(str((res[9]+res[10])/2))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,9).setText(str(self.lineEdit_51.text()))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,10).setText(str(int(self.lineEdit_51.text()*(res[9]+res[10])/2)))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,11).setText(str((int(self.lineEdit_48.text())*res[7]*(res[4]+res[5])/2)/24)
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,12).lineEdit().setText(res[6])
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,13).lineEdit().setText(str(res[3]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,14).lineEdit().setText(str(res[10]))
	#                     self.autoTotal()

	#     elif(self.radioButton.isChecked()):
	#         if(self.checkBox_4.isChecked()==0):

	#         Amount=int(self.lineEdit_54.text())
	#         percent=int(self.lineEdit_55.text())
	#         qty=int(self.lineEdit_59.text())
	#         gold_rate=float(self.lineEdit_48.text())

	#         gold_amount=(Amount*percent)/100
	#         gold_wt=gold_amount/(gold_rate/10)
	#         a=np.random.dirichlet(np.ones(qty))*gold_wt
	#         list1=[]

	#         for i in a:
	#             format_str='''SELECT TOP 1 * FROM Items WHERE Metal='Gold' AND Groups<>'{group}' AND Stone_Description='.%' AND IsActive=1 ORDER BY ABS((Min_Wt+Max_wt)/2-{input});'''
	#             sql_command=format_str.format(group=self.comboBox_7.lineEdit().text(),input=i)
	#             self.cursor.execute(sql_command)
	#             res=self.cursor.fetchone()
	#             if(res[0] is in list1):
	#                 pass
	#             else:
	#                 list1.append(res[0])
	#                 self.createRow()
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,0).setText(res[1])
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,1).setText(self.lineEdit_48.text())
					
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,2).setText(str(res[7]))
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,3).setText(str(1))
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,4).setText(str((res[4]+res[5])/2)
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,5).setText(str((res[4]+res[5])/2))
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,6).setText(str((int(self.lineEdit_48.text())*res[7]*(res[4]+res[5])/2)/24)
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,7).setText(str(res[8]))
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,8).setText(str(0.0))
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,9).setText(str(0.0))
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,10).setText(str(0.0))
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,11).setText(str((int(self.lineEdit_48.text())*res[7]*(res[4]+res[5])/2)/24)
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,12).lineEdit().setText(res[6])
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,13).lineEdit().setText(str(res[3]))
	#                 self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,14).lineEdit().setText(str(res[10]))
	#                 self.autoTotal()
	#         else:

	#             Amount=int(self.lineEdit_54.text())
	#             percent=int(self.lineEdit_55.text())
	#             qty=int(self.lineEdit_59.text())
	#             gold_rate=float(self.lineEdit_48.text())

	#             gold_amount=(Amount*percent)/100
	#             gold_wt=gold_amount/(gold_rate/10)
	#             a=np.random.dirichlet(np.ones(qty))*gold_wt
	#             list1=[]

	#             for i in a:

	#                 format_str='''SELECT TOP 1 * FROM Items WHERE Metal='Gold' AND Groups<>'{group}' AND IsActive=1 ORDER BY ABS((Min_Wt+Max_wt)/2-{input});'''
	#                 sql_command=format_str.format(group=self.comboBox_7.lineEdit().text(),input=i)
	#                 self.cursor.execute(sql_command)
	#                 res=self.cursor.fetchone()
	#                 if(res[0] is in list1):
	#                     pass
	#                     # goto a
	#                 else:
	#                     list1.append(res[0])
	#                     self.createRow()
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,0).setText(res[1])
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,1).setText(self.lineEdit_48.text())
						
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,2).setText(str(res[7]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,3).setText(str(1))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,4).setText(str((res[4]+res[5])/2)
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,5).setText(str((res[4]+res[5])/2))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,6).setText(str((int(self.lineEdit_48.text())*res[7]*(res[4]+res[5])/2)/24)
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,7).setText(str(res[8]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,8).setText(str((res[9]+res[10])/2))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,9).setText(str(self.lineEdit_51.text()))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,10).setText(str(int(self.lineEdit_51.text()*(res[9]+res[10])/2)))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,11).setText(str((int(self.lineEdit_48.text())*res[7]*(res[4]+res[5])/2)/24)
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,12).lineEdit().setText(res[6])
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,13).lineEdit().setText(str(res[3]))
	#                     self.tableWidget_2.cellWidget(self.tableWidget_2.rowCount()-1,14).lineEdit().setText(str(res[10]))
	#                     self.autoTotal()
						
	#     else:
	#         pass



	# def save_btn(self):
	#     rate_date=self.comboBox.lineEdit().text()
	#     try:
	#         a,valuation_date=self.comboBox_2.lineEdit().text().split("   ")
	#     except:
	#         valuation_date=self.comboBox_2.lineEdit().text()
	#     G_rate=float(self.lineEdit_48.text())
	#     S_rate=float(self.lineEdit_49.text())
	#     P_rate=float(self.lineEdit_50.text())
	#     D_rate=float(self.lineEdit_51.text())
	#     Soverign_rate=float(self.lineEdit_52.text())
	#     Coin_rate=float(self.lineEdit_53.text())
	#     Amount=float(self.lineEdit_54.text())
	#     if(self.radioButton_5.isChecked()):
	#         mode='Amount'
	#     elif(self.radioButton_6.isChecked()):
	#         mode='Weight'
	#     else:
	#         mode='Percent'
	#     if(self.checkBox_4.isChecked()):
	#         G_Diamond=1
	#     else:
	#         G_Diamond=0
	#     G_precent=float(self.lineEdit_55.text())
	#     G_Qty=float(self.lineEdit_59.text())
	#     if(self.checkBox_3.isChecked()):
	#         S_Diamond=1
	#     else:
	#         S_Diamond=0
	#     S_precent=float(self.lineEdit_56.text())
	#     S_Qty=float(self.lineEdit_60.text())
	#     if(self.checkBox_2.isChecked()):
	#         P_Diamond=1
	#     else:
	#         P_Diamond=0
	#     P_precent=float(self.lineEdit_57.text())
	#     P_Qty=float(self.lineEdit_61.text())
	#     if(self.checkBox.isChecked()):
	#         W_Diamond=1
	#     else:
	#         W_Diamond=0
	#     W_precent=float(self.lineEdit_58.text())
	#     W_Qty=float(self.lineEdit_62.text())
	#     group=self.comboBox_7.lineEdit().text()
	#     V_Name=self.lineEdit_64.text()
	#     V_Reg_No=self.lineEdit_65.text()
	#     Purpose=self.lineEdit_66.text()
	#     Customer_name=self.lineEdit_67.text()
	#     Customer_Pan=self.lineEdit_68.text()
	#     customer_address=self.lineEdit_69.text()
	#     F_Name=self.lineEdit_70.text()
	#     F_Address=self.lineEdit_71.text()
	#     OS_With=self.lineEdit_72.text()
	#     Gold_total=float(self.lineEdit_17.text())
	#     Gold_gross=float(self.lineEdit_19.text())
	#     Gold_metal=float(self.lineEdit_25.text())
	#     Gold_value=float(self.lineEdit_22.text())
	#     Silver_total=float(self.lineEdit_18.text())
	#     Silver_gross=float(self.lineEdit_20.text())
	#     Silver_metal=float(self.lineEdit_26.text())
	#     Silver_value=float(self.lineEdit_23.text())
	#     Diamond_total=float(self.lineEdit_16.text())
	#     Diamond_gross=float(self.lineEdit_21.text())
	#     # G_metal=float(self.lineEdit_25.text())
	#     Diamond_value=float(self.lineEdit_24.text())
	#     Grand_Total=float(self.lineEdit_27.text())
	#     G_Purity=float(self.lineEdit_73.text())
	#     S_Purity=float(self.lineEdit_74.text())

	#     format_str='''UPDATE Valuation SET Valuation_date='{valuation_date}',Rate_date='{rate_date}',Gold_rate={gold},Silver_rate={silver},Platinum_rate={platinum},Soverign_rate={soverign},Coin_rate={coin},Diamond_rate={diamond},Valuer_name='{V_Name}',Valuer_reg_no={V_Reg_No},Purpose='{V_Purpose}',Customer_name='{Customer_name}',Customer_Pan={Customer_Pan},customer_address='{customer_address}',Firm_name='{F_Name}',Firm_address='{F_Address}',OS='{OS_With}',Gold_total={Gold_total},Gold_gross={Gold_gross},Gold_metal={Gold_metal},Gold_value={Gold_value},Silver_total={Silver_total},Silver_gross={Silver_gross},Silver_metal={Silver_metal},Silver_value={Silver_value},Stone_total={Diamond_total},Stone_gross={Diamond_gross},Stone_value={Diamond_value},Grand_Total={Grand_Total} WHERE Valuation_id={id};'''
	#     sql_command=format_str.format(id=Ui_Valuation.val_id,valuation_date=valuation_date,rate_date=rate_date,gold=gold,silver=silver,platinum=platinum,diamond=diamond,soverign=soverign,coin=coin,V_Name=V_Name,V_Reg_No=V_Reg_No,V_Purpose=V_Purpose,Customer_name=Customer_name,Customer_Pan=Customer_Pan,customer_address=customer_address,F_Name=F_Name,F_Address=F_Address,OS_With=OS_With,Gold_total=Gold_total,Gold_gross=Gold_gross,Gold_metal=Gold_metal,Gold_value=Gold_value,Silver_total=Silver_total,Silver_gross=Silver_gross,Silver_metal=Silver_metal,Silver_value=Silver_value,Diamond_total=Diamond_total,Diamond_gross=Diamond_gross,Diamond_value=Diamond_value,Grand_Total=Grand_Total)
	#     self.connection.commit()
	#     self.cursor.execute(sql_command)

	#     format_str='''DELETE FROM Products WHERE Valuation_id={id};'''
	#     sql_command=format_str.format(id=Ui_Valuation.val_id)
	#     self.cursor.execute(sql_command)

	#     for i in range(self.tableWidget_2.rowCount()):
	#         # for j in range(self.tableWidget_2.colorCount()):
	#         description=self.tableWidget_2.cellWidget(i,0).text()
	#         metal_rate=float(self.tableWidget_2.cellWidget(i,1).text())
	#         purity=float(self.tableWidget_2.cellWidget(i,2).text())
	#         qty=float(self.tableWidget_2.cellWidget(i,3).text())
	#         gross_wt=float(self.tableWidget_2.cellWidget(i,4).text())
	#         metal_wt=float(self.tableWidget_2.cellWidget(i,5).text())
	#         metal_value=float(self.tableWidget_2.cellWidget(i,6).text())
	#         s_description=self.tableWidget_2.cellWidget(i,7).text()
	#         s_wt=float(self.tableWidget_2.cellWidget(i,8).text())
	#         s_rate=float(self.tableWidget_2.cellWidget(i,9).text())
	#         s_value=float(self.tableWidget_2.cellWidget(i,10).text())
	#         total=float(self.tableWidget_2.cellWidget(i,11).text())
	#         metal=self.tableWidget_2.cellWidget(i,12).lineEdit().text()
	#         item_ratewise=self.tableWidget_2.cellWidget(i,13).lineEdit().text()
	#         stone_weightwise=self.tableWidget_2.cellWidget(i,14).lineEdit().text()
	#         if(self.tableWidget_2.cellWidget(i,15).isChecked()):
	#             is_soverign=1
	#         else:
	#             is_soverign=0
			
	#         format_str='''INSERT INTO Products(Valuation_Id,Description,Rate,Purity,Quantity,Gross_Wt,Metal_Wt,Metal_Value,Stone_Description,Stone_Wt,Stone_Rate,Stone_Value,Total_Value,Metal,Item_Ratewise,Stone_Weightwise,Is_Soverign) VALUES ({id},'{item_description}',{rate},{purity},{quantity},{gross_wt},{metal_weight},{metal_value},'{stone_description}',{stone_wt},{stone_rate},{stone_value},{total_value},'{metal}','{item_ratewise}','{stone_weightwise}',{is_soverign});'''
	#         sql_command=format_str.format(id=Ui_Valuation.val_id,item_description=description,rate=metal_rate,purity=purity,quantity=qty,gross_wt=gross_wt,metal_weight=metal_wt,metal_value=metal_value,stone_description=s_description,stone_wt=s_wt,stone_rate=s_rate,stone_value=s_value,total_value=total,metal=metal,item_ratewise=item_ratewise,stone_weightwise=stone_weightwise,is_soverign=is_soverign)
	#         self.cursor.execute(sql_command)

	#     QtWidgets.QMessageBox.information(self, 'Success', 'Valuation Updated')
	#     # self.default()

				
	# def closeEvent(self, event):
	# 	if(self.a==1):
	# 		self.close
	# 	# if not self.authenticated:
	# 	buttonReply = QMessageBox.question(self, 'PyQt5 message', "Do you want to close the window?", QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
	# 	print(int(buttonReply))
	# 	if buttonReply == QMessageBox.Yes:
	# 		self.close()
	# 	if buttonReply == QMessageBox.No:
	# 		event.ignore()

	# def keyPressEvent(self, event):
	# 	if not event.key() == QtCore.Qt.Key_Escape:
	# 		super(Ui_Valuation_Expert, self).keyPressEvent(event)

	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1241, 625)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.horizontalLayout_43 = QtWidgets.QHBoxLayout(self.centralwidget)
		self.horizontalLayout_43.setObjectName("horizontalLayout_43")
		self.verticalLayout_58 = QtWidgets.QVBoxLayout()
		self.verticalLayout_58.setObjectName("verticalLayout_58")
		self.verticalLayout_38 = QtWidgets.QVBoxLayout()
		self.verticalLayout_38.setObjectName("verticalLayout_38")
		self.verticalLayout_39 = QtWidgets.QVBoxLayout()
		self.verticalLayout_39.setObjectName("verticalLayout_39")
		self.verticalLayout_40 = QtWidgets.QVBoxLayout()
		self.verticalLayout_40.setObjectName("verticalLayout_40")
		self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_25.setObjectName("horizontalLayout_25")
		self.verticalLayout_41 = QtWidgets.QVBoxLayout()
		self.verticalLayout_41.setObjectName("verticalLayout_41")
		self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_26.setObjectName("horizontalLayout_26")
		self.label_46 = QtWidgets.QLabel(self.centralwidget)
		self.label_46.setObjectName("label_46")
		self.horizontalLayout_26.addWidget(self.label_46)
		self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
		self.dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
		self.dateEdit.setCalendarPopup(True)
		self.dateEdit.setDate(QtCore.QDate(2019, 8, 6))
		self.dateEdit.setObjectName("dateEdit")
		self.horizontalLayout_26.addWidget(self.dateEdit)
		self.toolButton = QtWidgets.QToolButton(self.centralwidget)
		self.toolButton.setObjectName("toolButton")
		self.horizontalLayout_26.addWidget(self.toolButton)
		self.verticalLayout_41.addLayout(self.horizontalLayout_26)
		self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_27.setObjectName("horizontalLayout_27")
		self.label_47 = QtWidgets.QLabel(self.centralwidget)
		self.label_47.setObjectName("label_47")
		self.horizontalLayout_27.addWidget(self.label_47)
		self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
		self.dateEdit_2.setCalendarPopup(True)
		self.dateEdit_2.setDate(QtCore.QDate(2019, 8, 6))
		self.dateEdit_2.setObjectName("dateEdit_2")
		self.horizontalLayout_27.addWidget(self.dateEdit_2)
		self.toolButton_3 = QtWidgets.QToolButton(self.centralwidget)
		self.toolButton_3.setObjectName("toolButton_3")
		self.horizontalLayout_27.addWidget(self.toolButton_3)
		self.verticalLayout_41.addLayout(self.horizontalLayout_27)
		self.horizontalLayout_25.addLayout(self.verticalLayout_41)
		self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_28.setObjectName("horizontalLayout_28")
		self.verticalLayout_42 = QtWidgets.QVBoxLayout()
		self.verticalLayout_42.setObjectName("verticalLayout_42")
		self.label_48 = QtWidgets.QLabel(self.centralwidget)
		self.label_48.setObjectName("label_48")
		self.verticalLayout_42.addWidget(self.label_48)
		self.lineEdit_48 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_48.setObjectName("lineEdit_48")
		self.verticalLayout_42.addWidget(self.lineEdit_48)
		self.horizontalLayout_28.addLayout(self.verticalLayout_42)
		self.verticalLayout_43 = QtWidgets.QVBoxLayout()
		self.verticalLayout_43.setObjectName("verticalLayout_43")
		self.label_49 = QtWidgets.QLabel(self.centralwidget)
		self.label_49.setObjectName("label_49")
		self.verticalLayout_43.addWidget(self.label_49)
		self.lineEdit_49 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_49.setObjectName("lineEdit_49")
		self.verticalLayout_43.addWidget(self.lineEdit_49)
		self.horizontalLayout_28.addLayout(self.verticalLayout_43)
		self.verticalLayout_44 = QtWidgets.QVBoxLayout()
		self.verticalLayout_44.setObjectName("verticalLayout_44")
		self.label_50 = QtWidgets.QLabel(self.centralwidget)
		self.label_50.setObjectName("label_50")
		self.verticalLayout_44.addWidget(self.label_50)
		self.lineEdit_50 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_50.setObjectName("lineEdit_50")
		self.verticalLayout_44.addWidget(self.lineEdit_50)
		self.horizontalLayout_28.addLayout(self.verticalLayout_44)
		self.verticalLayout_45 = QtWidgets.QVBoxLayout()
		self.verticalLayout_45.setObjectName("verticalLayout_45")
		self.label_51 = QtWidgets.QLabel(self.centralwidget)
		self.label_51.setObjectName("label_51")
		self.verticalLayout_45.addWidget(self.label_51)
		self.lineEdit_51 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_51.setObjectName("lineEdit_51")
		self.verticalLayout_45.addWidget(self.lineEdit_51)
		self.horizontalLayout_28.addLayout(self.verticalLayout_45)
		self.verticalLayout_46 = QtWidgets.QVBoxLayout()
		self.verticalLayout_46.setObjectName("verticalLayout_46")
		self.label_52 = QtWidgets.QLabel(self.centralwidget)
		self.label_52.setObjectName("label_52")
		self.verticalLayout_46.addWidget(self.label_52)
		self.lineEdit_52 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_52.setObjectName("lineEdit_52")
		self.verticalLayout_46.addWidget(self.lineEdit_52)
		self.horizontalLayout_28.addLayout(self.verticalLayout_46)
		self.verticalLayout_47 = QtWidgets.QVBoxLayout()
		self.verticalLayout_47.setObjectName("verticalLayout_47")
		self.label_53 = QtWidgets.QLabel(self.centralwidget)
		self.label_53.setObjectName("label_53")
		self.verticalLayout_47.addWidget(self.label_53)
		self.lineEdit_53 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_53.setObjectName("lineEdit_53")
		self.verticalLayout_47.addWidget(self.lineEdit_53)
		self.horizontalLayout_28.addLayout(self.verticalLayout_47)
		self.horizontalLayout_25.addLayout(self.horizontalLayout_28)
		spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_25.addItem(spacerItem)
		self.verticalLayout_40.addLayout(self.horizontalLayout_25)
		self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_29.setObjectName("horizontalLayout_29")
		self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_30.setObjectName("horizontalLayout_30")
		self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_31.setObjectName("horizontalLayout_31")
		self.verticalLayout_48 = QtWidgets.QVBoxLayout()
		self.verticalLayout_48.setObjectName("verticalLayout_48")
		spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_48.addItem(spacerItem1)
		self.label_54 = QtWidgets.QLabel(self.centralwidget)
		self.label_54.setObjectName("label_54")
		self.verticalLayout_48.addWidget(self.label_54)
		self.lineEdit_54 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_54.setObjectName("lineEdit_54")
		self.verticalLayout_48.addWidget(self.lineEdit_54)
		self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
		self.radioButton_5.setObjectName("radioButton_5")
		self.verticalLayout_48.addWidget(self.radioButton_5)
		self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
		self.radioButton_6.setObjectName("radioButton_6")
		self.verticalLayout_48.addWidget(self.radioButton_6)
		self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
		self.radioButton.setObjectName("radioButton")
		self.verticalLayout_48.addWidget(self.radioButton)
		self.horizontalLayout_31.addLayout(self.verticalLayout_48)
		self.verticalLayout_49 = QtWidgets.QVBoxLayout()
		self.verticalLayout_49.setObjectName("verticalLayout_49")
		spacerItem2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.verticalLayout_49.addItem(spacerItem2)
		self.label_55 = QtWidgets.QLabel(self.centralwidget)
		self.label_55.setObjectName("label_55")
		self.verticalLayout_49.addWidget(self.label_55)
		self.label_56 = QtWidgets.QLabel(self.centralwidget)
		self.label_56.setObjectName("label_56")
		self.verticalLayout_49.addWidget(self.label_56)
		self.label_57 = QtWidgets.QLabel(self.centralwidget)
		self.label_57.setObjectName("label_57")
		self.verticalLayout_49.addWidget(self.label_57)
		self.label_58 = QtWidgets.QLabel(self.centralwidget)
		self.label_58.setObjectName("label_58")
		self.verticalLayout_49.addWidget(self.label_58)
		self.horizontalLayout_31.addLayout(self.verticalLayout_49)
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")
		spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout.addItem(spacerItem3)
		self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBox_4.setObjectName("checkBox_4")
		self.verticalLayout.addWidget(self.checkBox_4)
		self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBox_3.setObjectName("checkBox_3")
		self.verticalLayout.addWidget(self.checkBox_3)
		self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBox_2.setObjectName("checkBox_2")
		self.verticalLayout.addWidget(self.checkBox_2)
		self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBox.setObjectName("checkBox")
		self.verticalLayout.addWidget(self.checkBox)
		self.horizontalLayout_31.addLayout(self.verticalLayout)
		self.verticalLayout_50 = QtWidgets.QVBoxLayout()
		self.verticalLayout_50.setObjectName("verticalLayout_50")
		self.label_59 = QtWidgets.QLabel(self.centralwidget)
		self.label_59.setObjectName("label_59")
		self.verticalLayout_50.addWidget(self.label_59)
		self.lineEdit_55 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_55.setObjectName("lineEdit_55")
		self.verticalLayout_50.addWidget(self.lineEdit_55)
		self.lineEdit_56 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_56.setObjectName("lineEdit_56")
		self.verticalLayout_50.addWidget(self.lineEdit_56)
		self.lineEdit_57 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_57.setObjectName("lineEdit_57")
		self.verticalLayout_50.addWidget(self.lineEdit_57)
		self.lineEdit_58 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_58.setObjectName("lineEdit_58")
		self.verticalLayout_50.addWidget(self.lineEdit_58)
		self.horizontalLayout_31.addLayout(self.verticalLayout_50)
		self.verticalLayout_51 = QtWidgets.QVBoxLayout()
		self.verticalLayout_51.setObjectName("verticalLayout_51")
		self.label_60 = QtWidgets.QLabel(self.centralwidget)
		self.label_60.setObjectName("label_60")
		self.verticalLayout_51.addWidget(self.label_60)
		self.lineEdit_59 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_59.setObjectName("lineEdit_59")
		self.verticalLayout_51.addWidget(self.lineEdit_59)
		self.lineEdit_60 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_60.setObjectName("lineEdit_60")
		self.verticalLayout_51.addWidget(self.lineEdit_60)
		self.lineEdit_61 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_61.setObjectName("lineEdit_61")
		self.verticalLayout_51.addWidget(self.lineEdit_61)
		self.lineEdit_62 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_62.setObjectName("lineEdit_62")
		self.verticalLayout_51.addWidget(self.lineEdit_62)
		self.horizontalLayout_31.addLayout(self.verticalLayout_51)
		self.verticalLayout_52 = QtWidgets.QVBoxLayout()
		self.verticalLayout_52.setObjectName("verticalLayout_52")
		spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_52.addItem(spacerItem4)
		self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_22.setObjectName("pushButton_22")
		self.verticalLayout_52.addWidget(self.pushButton_22)
		self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_23.setObjectName("pushButton_23")
		self.verticalLayout_52.addWidget(self.pushButton_23)
		self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_24.setObjectName("pushButton_24")
		self.verticalLayout_52.addWidget(self.pushButton_24)
		self.pushButton_25 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_25.setObjectName("pushButton_25")
		self.verticalLayout_52.addWidget(self.pushButton_25)
		self.horizontalLayout_31.addLayout(self.verticalLayout_52)
		self.horizontalLayout_30.addLayout(self.horizontalLayout_31)
		self.verticalLayout_53 = QtWidgets.QVBoxLayout()
		self.verticalLayout_53.setObjectName("verticalLayout_53")
		spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_53.addItem(spacerItem5)
		self.pushButton_26 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_26.setObjectName("pushButton_26")
		self.verticalLayout_53.addWidget(self.pushButton_26)
		self.pushButton_27 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_27.setObjectName("pushButton_27")
		self.verticalLayout_53.addWidget(self.pushButton_27)
		self.pushButton_28 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_28.setObjectName("pushButton_28")
		self.verticalLayout_53.addWidget(self.pushButton_28)
		self.pushButton_29 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_29.setObjectName("pushButton_29")
		self.verticalLayout_53.addWidget(self.pushButton_29)
		self.horizontalLayout_30.addLayout(self.verticalLayout_53)
		self.horizontalLayout_29.addLayout(self.horizontalLayout_30)
		self.verticalLayout_54 = QtWidgets.QVBoxLayout()
		self.verticalLayout_54.setObjectName("verticalLayout_54")
		self.label_61 = QtWidgets.QLabel(self.centralwidget)
		self.label_61.setObjectName("label_61")
		self.verticalLayout_54.addWidget(self.label_61)
		self.lineEdit_63 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_63.setObjectName("lineEdit_63")
		self.verticalLayout_54.addWidget(self.lineEdit_63)
		spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.verticalLayout_54.addItem(spacerItem6)
		self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_32.setObjectName("horizontalLayout_32")
		self.label_62 = QtWidgets.QLabel(self.centralwidget)
		self.label_62.setObjectName("label_62")
		self.horizontalLayout_32.addWidget(self.label_62)
		self.comboBox_7 = QtWidgets.QComboBox(self.centralwidget)
		self.comboBox_7.setEditable(True)
		self.comboBox_7.setObjectName("comboBox_7")
		self.horizontalLayout_32.addWidget(self.comboBox_7)
		self.verticalLayout_54.addLayout(self.horizontalLayout_32)
		self.horizontalLayout_29.addLayout(self.verticalLayout_54)
		spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_29.addItem(spacerItem7)
		self.verticalLayout_40.addLayout(self.horizontalLayout_29)
		self.verticalLayout_39.addLayout(self.verticalLayout_40)
		self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_33.setObjectName("horizontalLayout_33")
		self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox.setObjectName("groupBox")
		self.formLayout = QtWidgets.QFormLayout(self.groupBox)
		self.formLayout.setObjectName("formLayout")
		self.lineEdit_65 = QtWidgets.QLineEdit(self.groupBox)
		self.lineEdit_65.setObjectName("lineEdit_65")
		self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_65)
		self.label_66 = QtWidgets.QLabel(self.groupBox)
		self.label_66.setObjectName("label_66")
		self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_66)
		self.lineEdit_66 = QtWidgets.QLineEdit(self.groupBox)
		self.lineEdit_66.setObjectName("lineEdit_66")
		self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_66)
		self.label_64 = QtWidgets.QLabel(self.groupBox)
		self.label_64.setObjectName("label_64")
		self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_64)
		self.label_65 = QtWidgets.QLabel(self.groupBox)
		self.label_65.setObjectName("label_65")
		self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_65)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.lineEdit_64 = QtWidgets.QLineEdit(self.groupBox)
		self.lineEdit_64.setObjectName("lineEdit_64")
		self.horizontalLayout.addWidget(self.lineEdit_64)
		self.toolButton_2 = QtWidgets.QToolButton(self.groupBox)
		self.toolButton_2.setObjectName("toolButton_2")
		self.horizontalLayout.addWidget(self.toolButton_2)
		self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
		self.horizontalLayout_33.addWidget(self.groupBox)
		self.groupBox1 = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox1.setObjectName("groupBox1")
		self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox1)
		self.formLayout_2.setObjectName("formLayout_2")
		self.label_68 = QtWidgets.QLabel(self.groupBox1)
		self.label_68.setObjectName("label_68")
		self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_68)
		self.label_69 = QtWidgets.QLabel(self.groupBox1)
		self.label_69.setObjectName("label_69")
		self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_69)
		self.lineEdit_68 = QtWidgets.QLineEdit(self.groupBox1)
		self.lineEdit_68.setObjectName("lineEdit_68")
		self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_68)
		self.label_70 = QtWidgets.QLabel(self.groupBox1)
		self.label_70.setObjectName("label_70")
		self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_70)
		self.lineEdit_69 = QtWidgets.QLineEdit(self.groupBox1)
		self.lineEdit_69.setObjectName("lineEdit_69")
		self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_69)
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.lineEdit_67 = QtWidgets.QLineEdit(self.groupBox1)
		self.lineEdit_67.setObjectName("lineEdit_67")
		self.horizontalLayout_2.addWidget(self.lineEdit_67)
		self.toolButton_4 = QtWidgets.QToolButton(self.groupBox1)
		self.toolButton_4.setObjectName("toolButton_4")
		self.horizontalLayout_2.addWidget(self.toolButton_4)
		self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
		self.horizontalLayout_33.addWidget(self.groupBox1)
		self.groupBox2 = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox2.setObjectName("groupBox2")
		self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox2)
		self.formLayout_3.setObjectName("formLayout_3")
		self.label_72 = QtWidgets.QLabel(self.groupBox2)
		self.label_72.setObjectName("label_72")
		self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_72)
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.lineEdit_70 = QtWidgets.QLineEdit(self.groupBox2)
		self.lineEdit_70.setObjectName("lineEdit_70")
		self.horizontalLayout_3.addWidget(self.lineEdit_70)
		self.toolButton_5 = QtWidgets.QToolButton(self.groupBox2)
		self.toolButton_5.setObjectName("toolButton_5")
		self.horizontalLayout_3.addWidget(self.toolButton_5)
		self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
		self.label_73 = QtWidgets.QLabel(self.groupBox2)
		self.label_73.setObjectName("label_73")
		self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_73)
		self.lineEdit_71 = QtWidgets.QLineEdit(self.groupBox2)
		self.lineEdit_71.setObjectName("lineEdit_71")
		self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_71)
		self.label_74 = QtWidgets.QLabel(self.groupBox2)
		self.label_74.setObjectName("label_74")
		self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_74)
		self.lineEdit_72 = QtWidgets.QLineEdit(self.groupBox2)
		self.lineEdit_72.setObjectName("lineEdit_72")
		self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_72)
		self.horizontalLayout_33.addWidget(self.groupBox2)
		spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_33.addItem(spacerItem8)
		self.verticalLayout_39.addLayout(self.horizontalLayout_33)
		self.verticalLayout_38.addLayout(self.verticalLayout_39)
		self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
		self.tableWidget_2.setObjectName("tableWidget_2")
		self.tableWidget_2.setColumnCount(16)
		self.tableWidget_2.setRowCount(0)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget_2.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget_2.setHorizontalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget_2.setHorizontalHeaderItem(2, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget_2.setHorizontalHeaderItem(3, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget_2.setHorizontalHeaderItem(4, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget_2.setHorizontalHeaderItem(5, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget_2.setHorizontalHeaderItem(6, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget_2.setHorizontalHeaderItem(7, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget_2.setHorizontalHeaderItem(8, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget_2.setHorizontalHeaderItem(9, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget_2.setHorizontalHeaderItem(10, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget_2.setHorizontalHeaderItem(11, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget_2.setHorizontalHeaderItem(12, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget_2.setHorizontalHeaderItem(13, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget_2.setHorizontalHeaderItem(14, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget_2.setHorizontalHeaderItem(15, item)
		self.verticalLayout_38.addWidget(self.tableWidget_2)
		self.verticalLayout_58.addLayout(self.verticalLayout_38)
		self.verticalLayout_37 = QtWidgets.QVBoxLayout()
		self.verticalLayout_37.setObjectName("verticalLayout_37")
		self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_15.setObjectName("horizontalLayout_15")
		self.verticalLayout_17 = QtWidgets.QVBoxLayout()
		self.verticalLayout_17.setObjectName("verticalLayout_17")
		spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_17.addItem(spacerItem9)
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
		spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_11.addItem(spacerItem10)
		spacerItem11 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_11.addItem(spacerItem11)
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
		spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_12.addItem(spacerItem12)
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
		spacerItem13 = QtWidgets.QSpacerItem(13, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.verticalLayout_16.addItem(spacerItem13)
		self.label_21 = QtWidgets.QLabel(self.centralwidget)
		self.label_21.setObjectName("label_21")
		self.verticalLayout_16.addWidget(self.label_21)
		self.lineEdit_25 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_25.setObjectName("lineEdit_25")
		self.verticalLayout_16.addWidget(self.lineEdit_25)
		self.lineEdit_26 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_26.setObjectName("lineEdit_26")
		self.verticalLayout_16.addWidget(self.lineEdit_26)
		spacerItem14 = QtWidgets.QSpacerItem(20, 27, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.verticalLayout_16.addItem(spacerItem14)
		self.horizontalLayout_15.addLayout(self.verticalLayout_16)
		self.verticalLayout_14 = QtWidgets.QVBoxLayout()
		self.verticalLayout_14.setObjectName("verticalLayout_14")
		spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_14.addItem(spacerItem15)
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
		spacerItem16 = QtWidgets.QSpacerItem(20, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.verticalLayout_18.addItem(spacerItem16)
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setObjectName("pushButton")
		self.verticalLayout_18.addWidget(self.pushButton)
		self.lineEdit_27 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_27.setObjectName("lineEdit_27")
		self.verticalLayout_18.addWidget(self.lineEdit_27)
		self.horizontalLayout_15.addLayout(self.verticalLayout_18)
		self.horizontalLayout_44 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_44.setObjectName("horizontalLayout_44")
		self.verticalLayout_59 = QtWidgets.QVBoxLayout()
		self.verticalLayout_59.setObjectName("verticalLayout_59")
		spacerItem17 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.verticalLayout_59.addItem(spacerItem17)
		self.label_75 = QtWidgets.QLabel(self.centralwidget)
		self.label_75.setObjectName("label_75")
		self.verticalLayout_59.addWidget(self.label_75)
		self.label_76 = QtWidgets.QLabel(self.centralwidget)
		self.label_76.setObjectName("label_76")
		self.verticalLayout_59.addWidget(self.label_76)
		self.horizontalLayout_44.addLayout(self.verticalLayout_59)
		self.verticalLayout_60 = QtWidgets.QVBoxLayout()
		self.verticalLayout_60.setObjectName("verticalLayout_60")
		spacerItem18 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.verticalLayout_60.addItem(spacerItem18)
		self.label_77 = QtWidgets.QLabel(self.centralwidget)
		self.label_77.setObjectName("label_77")
		self.verticalLayout_60.addWidget(self.label_77)
		self.horizontalLayout_45 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_45.setObjectName("horizontalLayout_45")
		self.lineEdit_73 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_73.setObjectName("lineEdit_73")
		self.horizontalLayout_45.addWidget(self.lineEdit_73)
		self.label_78 = QtWidgets.QLabel(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
		self.label_78.setSizePolicy(sizePolicy)
		self.label_78.setObjectName("label_78")
		self.horizontalLayout_45.addWidget(self.label_78)
		spacerItem19 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_45.addItem(spacerItem19)
		self.verticalLayout_60.addLayout(self.horizontalLayout_45)
		self.horizontalLayout_46 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_46.setObjectName("horizontalLayout_46")
		self.lineEdit_74 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_74.setObjectName("lineEdit_74")
		self.horizontalLayout_46.addWidget(self.lineEdit_74)
		self.label_79 = QtWidgets.QLabel(self.centralwidget)
		self.label_79.setObjectName("label_79")
		self.horizontalLayout_46.addWidget(self.label_79)
		spacerItem20 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_46.addItem(spacerItem20)
		self.verticalLayout_60.addLayout(self.horizontalLayout_46)
		self.horizontalLayout_44.addLayout(self.verticalLayout_60)
		self.horizontalLayout_15.addLayout(self.horizontalLayout_44)
		spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_15.addItem(spacerItem21)
		self.verticalLayout_37.addLayout(self.horizontalLayout_15)
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
		spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_16.addItem(spacerItem22)
		self.verticalLayout_37.addLayout(self.horizontalLayout_16)
		self.verticalLayout_58.addLayout(self.verticalLayout_37)
		self.horizontalLayout_43.addLayout(self.verticalLayout_58)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 961, 22))
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
		self.shortcut = QShortcut(QKeySequence("Insert"), self)
		self.shortcut.activated.connect(self.createRow)
		self.shortcut = QShortcut(QKeySequence("Delete"), self)
		self.shortcut.activated.connect(self.deleteRow)
		self.toolBar.actionTriggered[QAction].connect(self.toolbtnpressed)
		self.radioButton_6.toggled.connect(self.weightClicked)
		self.radioButton_5.toggled.connect(self.weightClicked)
		self.radioButton.toggled.connect(self.weightClicked)
		self.pushButton.clicked.connect(self.CheckPurityWise)
		self.pushButton_22.clicked.connect(self.ValuateGold2)
		self.pushButton_23.clicked.connect(self.ValuateSilver2)
		self.pushButton_24.clicked.connect(self.ValuatePlatinum2)
		self.pushButton_25.clicked.connect(self.ValuateWhiteMetal2)
		self.pushButton_2.clicked.connect(self.new_btn)
		self.pushButton_3.clicked.connect(self.Document)
		self.pushButton_4.clicked.connect(self.save_btn)
		self.pushButton_5.clicked.connect(self.cancel_btn)
		self.toolButton_2.clicked.connect(self.ValuerPopup)
		self.toolButton_4.clicked.connect(self.CustomerPopup)
		self.toolButton_5.clicked.connect(self.FirmPopup)
		self.toolButton.clicked.connect(self.RatePopup)
		self.toolButton_3.clicked.connect(self.ValuationPopup)
		self.calender1=QCalendarWidget()
		self.calender1.clicked.connect(self.fillRates)
		self.dateEdit.setCalendarWidget(self.calender1)
		self.calender2=QCalendarWidget()
		self.calender2.clicked.connect(self.MultipleValuation)
		self.dateEdit_2.setCalendarWidget(self.calender2)
		self.pushButton_26.clicked.connect(self.clear_btn_1)
		self.pushButton_27.clicked.connect(self.clear_btn_2)
		self.pushButton_28.clicked.connect(self.clear_btn_3)
		self.pushButton_29.clicked.connect(self.clear_btn_4)
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.label_46.setText(_translate("MainWindow", "Rate Date:"))
		self.toolButton.setText(_translate("MainWindow", "..."))
		self.label_47.setText(_translate("MainWindow", "Valuation Date:"))
		self.toolButton_3.setText(_translate("MainWindow", "..."))
		self.label_48.setText(_translate("MainWindow", "Gold(10 g)"))
		self.label_49.setText(_translate("MainWindow", "Silver(1 kg)"))
		self.label_50.setText(_translate("MainWindow", "Platinum"))
		self.label_51.setText(_translate("MainWindow", "Diamond"))
		self.label_52.setText(_translate("MainWindow", "Soverign"))
		self.label_53.setText(_translate("MainWindow", "Coin"))
		self.label_54.setText(_translate("MainWindow", "Valuation Amount"))
		self.radioButton_5.setText(_translate("MainWindow", "Amount"))
		self.radioButton_6.setText(_translate("MainWindow", "Weight"))
		self.radioButton.setText(_translate("MainWindow", "Percentage"))
		self.label_55.setText(_translate("MainWindow", "Gold"))
		self.label_56.setText(_translate("MainWindow", "Silver"))
		self.label_57.setText(_translate("MainWindow", "Platinum"))
		self.label_58.setText(_translate("MainWindow", "White Metal"))
		self.checkBox_4.setText(_translate("MainWindow", "Diamond"))
		self.checkBox_3.setText(_translate("MainWindow", "Diamond"))
		self.checkBox_2.setText(_translate("MainWindow", "Diamond"))
		self.checkBox.setText(_translate("MainWindow", "Diamond"))
		self.label_59.setText(_translate("MainWindow", "%"))
		self.label_60.setText(_translate("MainWindow", "Qty."))
		self.pushButton_22.setText(_translate("MainWindow", "Valuate Gold"))
		self.pushButton_23.setText(_translate("MainWindow", "Valuate Silver"))
		self.pushButton_24.setText(_translate("MainWindow", "Valuate Platinum"))
		self.pushButton_25.setText(_translate("MainWindow", "Valuate White Metal"))
		self.pushButton_26.setText(_translate("MainWindow", "Clear"))
		self.pushButton_27.setText(_translate("MainWindow", "Clear"))
		self.pushButton_28.setText(_translate("MainWindow", "Clear"))
		self.pushButton_29.setText(_translate("MainWindow", "Clear"))
		self.label_61.setText(_translate("MainWindow", "Calculation Status"))
		self.label_62.setText(_translate("MainWindow", "Exclude Group"))
		self.groupBox.setTitle(_translate("MainWindow", "Valuers"))
		self.label_66.setText(_translate("MainWindow", "Purpose"))
		self.label_64.setText(_translate("MainWindow", "Name"))
		self.label_65.setText(_translate("MainWindow", "R.No."))
		self.toolButton_2.setText(_translate("MainWindow", "..."))
		self.groupBox1.setTitle(_translate("MainWindow", "Customer"))
		self.label_68.setText(_translate("MainWindow", "Name"))
		self.label_69.setText(_translate("MainWindow", "Address 1"))
		self.label_70.setText(_translate("MainWindow", "Address 2"))
		self.toolButton_4.setText(_translate("MainWindow", "..."))
		self.groupBox2.setTitle(_translate("MainWindow", "Firm"))
		self.label_72.setText(_translate("MainWindow", "Name"))
		self.toolButton_5.setText(_translate("MainWindow", "..."))
		self.label_73.setText(_translate("MainWindow", "Address"))
		self.label_74.setText(_translate("MainWindow", "Under O/S with"))
		item = self.tableWidget_2.horizontalHeaderItem(0)
		item.setText(_translate("MainWindow", "Description"))
		item = self.tableWidget_2.horizontalHeaderItem(1)
		item.setText(_translate("MainWindow", "Rate"))
		item = self.tableWidget_2.horizontalHeaderItem(2)
		item.setText(_translate("MainWindow", "Purity"))
		item = self.tableWidget_2.horizontalHeaderItem(3)
		item.setText(_translate("MainWindow", "Qty."))
		item = self.tableWidget_2.horizontalHeaderItem(4)
		item.setText(_translate("MainWindow", "Gross Wt."))
		item = self.tableWidget_2.horizontalHeaderItem(5)
		item.setText(_translate("MainWindow", "Metal Wt."))
		item = self.tableWidget_2.horizontalHeaderItem(6)
		item.setText(_translate("MainWindow", "Value(Metal)"))
		item = self.tableWidget_2.horizontalHeaderItem(7)
		item.setText(_translate("MainWindow", "Stone"))
		item = self.tableWidget_2.horizontalHeaderItem(8)
		item.setText(_translate("MainWindow", "Wt (Stone)"))
		item = self.tableWidget_2.horizontalHeaderItem(9)
		item.setText(_translate("MainWindow", "Rate(Stone)"))
		item = self.tableWidget_2.horizontalHeaderItem(10)
		item.setText(_translate("MainWindow", "Value(Stone)"))
		item = self.tableWidget_2.horizontalHeaderItem(11)
		item.setText(_translate("MainWindow", "Total Value"))
		item = self.tableWidget_2.horizontalHeaderItem(12)
		item.setText(_translate("MainWindow", "Metal"))
		item = self.tableWidget_2.horizontalHeaderItem(13)
		item.setText(_translate("MainWindow", "Item Ratewise"))
		item = self.tableWidget_2.horizontalHeaderItem(14)
		item.setText(_translate("MainWindow", "Stone Weightwise"))
		item = self.tableWidget_2.horizontalHeaderItem(15)
		item.setText(_translate("MainWindow", "Is_Soverign"))
		self.label_22.setText(_translate("MainWindow", "Gold"))
		self.label_24.setText(_translate("MainWindow", "Silver"))
		self.label_23.setText(_translate("MainWindow", "Diamond"))
		self.label_18.setText(_translate("MainWindow", "Total Qty."))
		self.label_19.setText(_translate("MainWindow", "Gross Wt."))
		self.label_21.setText(_translate("MainWindow", "Metal Wt."))
		self.label_20.setText(_translate("MainWindow", "Value"))
		self.pushButton.setText(_translate("MainWindow", "Check Purity Wise Total"))
		self.label_75.setText(_translate("MainWindow", "Gold"))
		self.label_76.setText(_translate("MainWindow", "Silver/Pt."))
		self.label_77.setText(_translate("MainWindow", "Min Purity"))
		self.label_78.setText(_translate("MainWindow", "Ct"))
		self.label_79.setText(_translate("MainWindow", "%"))
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





if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	ex = Ui_Valuation_Expert()
	# w = QtWidgets.QMainWindow()
	ex.show()
	# w.show()
	sys.exit(app.exec_())