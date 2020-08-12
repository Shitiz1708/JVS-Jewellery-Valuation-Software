import sys
from PyQt5 import QtWidgets,QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, pyqtSlot
import sqlite3
import Firm
import Groups
import Items
import Rates
import Valuers
import Change_Password
import Valuation
import SplitValuation

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
        self.connection = sqlite3.connect("MAINDB.db")
        self.cursor=self.connection.cursor()

    def default(self):
        sql_command='''SELECT * FROM Valuers;'''
        self.cursor.execute(sql_command)
        res = self.cursor.fetchall()
        self.tableWidget.setRowCount(0)
        c=0
        for i in res:
            self.tableWidget.insertRow(c)
            self.tableWidget.setItem(c,0,QTableWidgetItem(i[1]))
            c=c+1
        self.label_9.setText("")
    
    def tableClicked(self):
        name=self.tableWidget.currentItem().text()
        format_str='''SELECT * FROM Valuers WHERE Valuer_Name="{name}";'''
        sql_command=format_str.format(name=name)
        self.cursor.execute(sql_command)
        res = self.cursor.fetchone()
        self.lineEdit.setText(str(res[1]))
        self.lineEdit_2.setText(str(res[2]))
        self.label_9.setText(str(res[1]))
    
    # def closeEvent(self, event):
    #     # if not self.authenticated:
    #     buttonReply = QMessageBox.question(self, 'PyQt5 message', "Do you want to close the window?", QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
    #     print(int(buttonReply))
    #     if buttonReply == QMessageBox.Yes:
    #         self.close()
    #     if buttonReply == QMessageBox.No:
    #         event.ignore()

    # def keyPressEvent(self, event):
    #     if not event.key() == QtCore.Qt.Key_Escape:
    #         super(Ui_Valuation, self).keyPressEvent(event)
    
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1241, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_9.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font: 75 11pt \"URW Bookman L\";    \n""color: rgb(46, 52, 54);\n""font-size: 25px;")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        spacerItem = QtWidgets.QSpacerItem(20, 450, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_16.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_16.addWidget(self.pushButton_2)
        self.pushButton_1 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout_16.addWidget(self.pushButton_1)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_16.addWidget(self.pushButton_4)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.horizontalLayout_9.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addLayout(self.horizontalLayout_9)
        spacerItem2 = QtWidgets.QSpacerItem(11, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 708, 22))
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
        self.actionSplit_Valuation = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons8-separate-document-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSplit_Valuation.setIcon(icon9)
        self.actionSplit_Valuation.setObjectName("actionSplit_Valuation")
        self.toolBar.addAction(self.actionFirm)
        self.toolBar.addAction(self.actionValuer)
        self.toolBar.addAction(self.actionGroups)
        self.toolBar.addAction(self.actionItems)
        self.toolBar.addAction(self.actionMarket_Rates)
        self.toolBar.addAction(self.actionValuation)
        self.toolBar.addAction(self.actionSplit_Valuation)
        self.toolBar.addAction(self.actionChange_Password)
        self.toolBar.addAction(self.actionAbout)
        self.toolBar.addAction(self.actionExit)
        self.pushButton_3.clicked.connect(self.new_btn)
        self.pushButton_2.clicked.connect(self.delete_btn)
        self.pushButton_1.clicked.connect(self.save_btn)
        self.pushButton_4.clicked.connect(self.cancel_btn)
        self.pushButton_5.clicked.connect(self.search_btn)
        self.lineEdit_3.cursorPositionChanged.connect(self.search_btn)
        self.tableWidget.itemPressed.connect(self.tableClicked)
        self.toolBar.actionTriggered[QAction].connect(self.toolbtnpressed)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Search:"))
        self.pushButton_5.setText(_translate("MainWindow", "Search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Valuers"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "Registration No."))
        self.pushButton_3.setText(_translate("MainWindow", "New"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete"))
        self.pushButton_1.setText(_translate("MainWindow", "Save"))
        self.pushButton_4.setText(_translate("MainWindow", "Close"))
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
        self.actionSplit_Valuation.setText(_translate("MainWindow", "Split Valuation"))


    
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
                format_str='''INSERT INTO Valuers (Valuer_Name,Valuer_Registration_No) VALUES("{name}",'{registration_no}');'''
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
            format_str='''UPDATE Valuers SET Valuer_Registration_No="{registration_no}" WHERE Valuer_Name="{name}";'''
            sql_command=format_str.format(name=name,registration_no=registration_no)
            self.cursor.execute(sql_command)
            QtWidgets.QMessageBox.information(self, 'Success', 'Valuer Updated Successfully')
            self.default()
            self.clear()
            return
    
    def search_btn(self):
        print("A")
        name=self.lineEdit_3.text()
        format_str='''SELECT * FROM Valuers WHERE Valuer_Name LIKE "{name}%";'''
        sql_command=format_str.format(name=name)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchall()
        self.tableWidget.setRowCount(0)
        c=0
        for i in res:
            self.tableWidget.insertRow(c)
            self.tableWidget.setItem(c,0,QTableWidgetItem(i[1]))
            c=c+1

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





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Valuer_setup()
    # w = QtWidgets.QMainWindow()
    ex.show()
    # w.show()
    sys.exit(app.exec_())
