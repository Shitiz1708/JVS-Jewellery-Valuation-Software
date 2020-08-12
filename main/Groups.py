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
# import toolbar_rc

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
        self.connection = sqlite3.connect("MAINDB.db")
        self.cursor=self.connection.cursor()
    
    def default(self):
        sql_command='''SELECT * FROM Groups;'''
        self.cursor.execute(sql_command)
        res = self.cursor.fetchall()
        self.tableWidget.setRowCount(0)
        c=0
        for i in res:
            self.tableWidget.insertRow(c)
            self.tableWidget.setItem(c,0,QTableWidgetItem(i[1]))
            c=c+1
        sql_command='''SELECT DISTINCT Group_Type FROM Groups;'''
        self.cursor.execute(sql_command)
        res = self.cursor.fetchall()
        print(res)
        self.comboBox.clear()
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
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(QtCore.Qt.DotLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 41, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 450, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.verticalLayout_3.addWidget(self.groupBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 300, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.groupBox1 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox1.setObjectName("groupBox1")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox1)
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox1)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_5.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox1)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_5.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox1)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_5.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox1)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_5.addWidget(self.pushButton_8)
        self.verticalLayout_3.addWidget(self.groupBox1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 721, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(24, 24))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
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
        self.pushButton_5.clicked.connect(self.new_btn)
        self.pushButton_6.clicked.connect(self.delete_btn)
        self.pushButton_7.clicked.connect(self.save_btn)
        self.pushButton_8.clicked.connect(self.cancel_btn)
        self.pushButton.clicked.connect(self.search_btn)
        self.lineEdit.cursorPositionChanged.connect(self.search_btn)
        self.tableWidget.itemPressed.connect(self.tableClicked)
        self.toolBar.actionTriggered[QAction].connect(self.toolbtnpressed)

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
                # self.close()
    
    def delete_btn(self):
        group_name=self.lineEdit_2.text()
        group_type=self.comboBox.lineEdit().text()
        format_str='''SELECT * FROM Groups WHERE Group_Name="{name}";'''
        sql_command=format_str.format(name=group_name)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchone()
        if(res is None):
            QtWidgets.QMessageBox.warning(self, 'Error', 'Group Does Not Exists')
            # self.close()
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
        format_str='''SELECT * FROM Groups WHERE Group_Name= "{name}";'''
        sql_command=format_str.format(name=group_name)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchone()
        if(res is None):
            QtWidgets.QMessageBox.warning(self, 'Error', 'Group Does Not Exists')
            # self.close()
        else:
            format_str='''UPDATE Groups SET Group_Name="{name}",Group_Type="{type}" WHERE Group_Name="{name}";'''
            sql_command=format_str.format(name=group_name,type=group_type)
            self.cursor.execute(sql_command)
            QtWidgets.QMessageBox.information(self, 'Success', 'Group Updated Successfully')
            self.default()
            self.clear()
            return
    
    def search_btn(self):
        print("A")
        name=self.lineEdit.text()
        format_str='''SELECT * FROM Groups WHERE Group_Name LIKE "{name}%";'''
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
    
    def SplitTool(self):
        self.close()
        self.split=SplitValuation.Ui_Split_Valuation()
        self.split.show()

    def ItemTool(self):
        self.close()
        self.items=Items.Ui_Items()
        self.items.show()

    def GroupsTool(self):
        self.close()
        self.groups=Ui_Groups()
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

    







if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Groups()
    # w = QtWidgets.QMainWindow()
    ex.show()
    # w.show()
    sys.exit(app.exec_())
