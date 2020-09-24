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

class Ui_Items(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.databaseAccess()
        self.setupUi(self)
        self.default()
        # self.databaseAccess()
    
    def __del__(self):
        self.connection.commit()
        # self.connection_1.commit()
        self.connection.close()
        # self.connection_1.close()
    
    def databaseAccess(self):
        self.connection = sqlite3.connect("./dbs/MAINDB.db")
        self.cursor=self.connection.cursor()
    
    def default(self):
        sql_command='''SELECT * FROM Items;'''
        self.cursor.execute(sql_command)
        res = self.cursor.fetchall()
        self.tableWidget.setRowCount(0)
        c=0
        for i in res:
            self.tableWidget.insertRow(c)
            self.tableWidget.setItem(c,0,QTableWidgetItem(i[1]))
            c=c+1
        
        sql_command='''SELECT DISTINCT Group_Name FROM Groups;'''
        self.cursor.execute(sql_command)
        res = self.cursor.fetchall()
        for i in res:
            self.comboBox.addItem(i[0])



    def printDB(self):
        sql_command='''SELECT * FROM Items;'''
        self.cursor.execute(sql_command)
        res = self.cursor.fetchall()

    def clear(self):
        self.lineEdit_5.setText(str(""))
        self.comboBox.lineEdit().setText(str(""))
        self.radioButton_3.setChecked(False)
        self.radioButton_4.setChecked(False)
        self.radioButton_11.setChecked(False)
        self.radioButton_12.setChecked(False)
        self.radioButton_13.setChecked(False)
        self.radioButton_14.setChecked(False)
        self.lineEdit.setText(str(""))
        self.lineEdit_4.setText(str(""))
        self.radioButton_9.setChecked(False)
        self.radioButton_10.setChecked(False)
        self.lineEdit_11.setText(str(""))
        self.lineEdit_3.setText(str(""))
        self.lineEdit_9.setText(str(""))
        self.radioButton_7.setChecked(False)
        self.radioButton_8.setChecked(False)
        self.lineEdit_2.setText(str(""))
        self.lineEdit_7.setText(str(""))
        self.lineEdit_6.setText(str(""))
        self.checkBox.setChecked(False)

    def tableClicked(self):
        name=self.tableWidget.currentItem().text()
        format_str='''SELECT * FROM Items WHERE Item_Description="{name}";'''
        sql_command=format_str.format(name=name)
        self.cursor.execute(sql_command)
        res = self.cursor.fetchone()
        self.lineEdit_5.setText(str(res[1]))
        self.comboBox.lineEdit().setText(str(res[2]))
        rate=str(res[3])
        if(rate=='Weightwise'):
            self.radioButton_3.setChecked(True)
        else:
            self.radioButton_4.setChecked(True)
        self.lineEdit_3.setText(str(res[4]))
        self.lineEdit_9.setText(str(res[5]))
        metal=str(res[6])
        if(metal=='Gold'):
            self.radioButton_11.setChecked(True)
        elif(metal=='Silver'):
            self.radioButton_12.setChecked(True)
        elif(metal=='Platinum'):
            self.radioButton_13.setChecked(True)
        else:
            self.radioButton_14.setChecked(True)
            self.lineEdit.setText(metal)
        self.lineEdit_4.setText(str(res[7]))
        stone=str(res[8])
        if(stone=='Diamond'):
            self.radioButton_9.setChecked(True)
        else:
            self.radioButton_10.setChecked(True)
            self.lineEdit_11.setText(stone)
        rateAs=str(res[9])
        if(rateAs=='Grams'):
            self.radioButton_7.setChecked(True)
        else:
            self.radioButton_8.setChecked(True)
        self.lineEdit_2.setText(str(res[10]))
        self.lineEdit_7.setText(str(res[11]))
        self.lineEdit_6.setText(str(res[12]))
        Active=res[13]
        if(Active==1):
            self.checkBox.setChecked(True)
        

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1328, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_6.addWidget(self.lineEdit_10)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_6.addWidget(self.pushButton_5)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(QtCore.Qt.DotLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(220)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.verticalLayout_7.addWidget(self.tableWidget)
        self.horizontalLayout_9.addLayout(self.verticalLayout_7)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout.addWidget(self.lineEdit_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_3.addWidget(self.comboBox)
        spacerItem1 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_19.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_19.addWidget(self.radioButton_4)
        self.horizontalLayout_4.addWidget(self.frame_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_2.addWidget(self.lineEdit_9)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.radioButton_11 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_11.setObjectName("radioButton_11")
        self.horizontalLayout_16.addWidget(self.radioButton_11)
        self.radioButton_12 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_12.setObjectName("radioButton_12")
        self.horizontalLayout_16.addWidget(self.radioButton_12)
        self.radioButton_13 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_13.setObjectName("radioButton_13")
        self.horizontalLayout_16.addWidget(self.radioButton_13)
        self.radioButton_14 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_14.setObjectName("radioButton_14")
        self.horizontalLayout_16.addWidget(self.radioButton_14)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_16.addWidget(self.lineEdit)
        self.horizontalLayout_6.addWidget(self.frame)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_7.addWidget(self.lineEdit_4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_3.addWidget(self.label_15)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.radioButton_9 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_9.setObjectName("radioButton_9")
        self.horizontalLayout_17.addWidget(self.radioButton_9)
        self.radioButton_10 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_10.setObjectName("radioButton_10")
        self.horizontalLayout_17.addWidget(self.radioButton_10)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_17.addWidget(self.lineEdit_11)
        self.horizontalLayout_8.addWidget(self.frame_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.radioButton_7 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_7.setObjectName("radioButton_7")
        self.horizontalLayout_18.addWidget(self.radioButton_7)
        self.radioButton_8 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_8.setObjectName("radioButton_8")
        self.horizontalLayout_18.addWidget(self.radioButton_8)
        self.horizontalLayout_2.addWidget(self.frame_3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_12.addWidget(self.label_13)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_4.addWidget(self.label_12)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_4.addWidget(self.lineEdit_2)
        self.horizontalLayout_11.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_5.addWidget(self.label_16)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_5.addWidget(self.lineEdit_7)
        self.horizontalLayout_11.addLayout(self.verticalLayout_5)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_13.addWidget(self.label_14)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_13.addWidget(self.lineEdit_6)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_3.addWidget(self.checkBox)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_14.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_14.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_14.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_14.addWidget(self.pushButton_4)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_9.addLayout(self.verticalLayout_3)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem10)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem11)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 680, 22))
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
        icon.addPixmap(QtGui.QPixmap("./icons/icons8-organization-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFirm.setIcon(icon)
        self.actionFirm.setObjectName("actionFirm")
        self.actionValuer = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icons/icons8-user-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionValuer.setIcon(icon1)
        self.actionValuer.setObjectName("actionValuer")
        self.actionGroups = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./icons/icons8-list-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGroups.setIcon(icon2)
        self.actionGroups.setObjectName("actionGroups")
        self.actionItems = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./icons/icons8-ring-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionItems.setIcon(icon3)
        self.actionItems.setObjectName("actionItems")
        self.actionMarket_Rates = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./icons/icons8-us-dollar-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMarket_Rates.setIcon(icon4)
        self.actionMarket_Rates.setObjectName("actionMarket_Rates")
        self.actionValuation = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./icons/icons8-contract-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionValuation.setIcon(icon5)
        self.actionValuation.setObjectName("actionValuation")
        self.actionChange_Password = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./icons/icons8-password-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionChange_Password.setIcon(icon6)
        self.actionChange_Password.setObjectName("actionChange_Password")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("./icons/icons8-about-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon7)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("./icons/icons8-exit-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon8)
        self.actionExit.setObjectName("actionExit")
        self.actionSplit_Valuation = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("./icons/icons8-separate-document-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.pushButton.clicked.connect(self.new_btn)
        self.pushButton_2.clicked.connect(self.delete_btn)
        self.pushButton_3.clicked.connect(self.save_btn)
        self.pushButton_4.clicked.connect(self.cancel_btn)
        self.pushButton_5.clicked.connect(self.search_btn)
        self.lineEdit_10.cursorPositionChanged.connect(self.search_btn)
        self.tableWidget.itemPressed.connect(self.tableClicked)
        self.toolBar.actionTriggered[QAction].connect(self.toolbtnpressed)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", "Search:"))
        self.pushButton_5.setText(_translate("MainWindow", "Search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item"))
        self.label.setText(_translate("MainWindow", "Item Description"))
        self.label_10.setText(_translate("MainWindow", "Group"))
        self.label_2.setText(_translate("MainWindow", "Rates"))
        self.radioButton_3.setText(_translate("MainWindow", "Weightwise"))
        self.radioButton_4.setText(_translate("MainWindow", "QuantityWise"))
        self.label_4.setText(_translate("MainWindow", "Weight"))
        self.label_3.setText(_translate("MainWindow", "Min Weight"))
        self.label_11.setText(_translate("MainWindow", "Max Weight"))
        self.label_6.setText(_translate("MainWindow", "Metal"))
        self.radioButton_11.setText(_translate("MainWindow", "Gold"))
        self.radioButton_12.setText(_translate("MainWindow", "Silver"))
        self.radioButton_13.setText(_translate("MainWindow", "Platinum"))
        self.radioButton_14.setText(_translate("MainWindow", "Others"))
        self.label_5.setText(_translate("MainWindow", "Purity"))
        self.label_15.setText(_translate("MainWindow", "Stone Details"))
        self.label_8.setText(_translate("MainWindow", "Stone Description"))
        self.radioButton_9.setText(_translate("MainWindow", "Diamond"))
        self.radioButton_10.setText(_translate("MainWindow", "Others"))
        self.label_7.setText(_translate("MainWindow", "Rate As:"))
        self.radioButton_7.setText(_translate("MainWindow", "Grams"))
        self.radioButton_8.setText(_translate("MainWindow", "Carats"))
        self.label_13.setText(_translate("MainWindow", "Stone Weight"))
        self.label_12.setText(_translate("MainWindow", "Min Weight"))
        self.label_16.setText(_translate("MainWindow", "Max Weight"))
        self.label_14.setText(_translate("MainWindow", "Max Quantity Allowed To Increase"))
        self.checkBox.setText(_translate("MainWindow", "Active"))
        self.pushButton.setText(_translate("MainWindow", "New"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete"))
        self.pushButton_3.setText(_translate("MainWindow", "Save"))
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
    
    def cancel_btn(self):
        self.close()
    
    def new_btn(self):
        item_description = self.lineEdit_5.text()
        group=self.comboBox.lineEdit().text()
        min_wt=self.lineEdit_3.text()
        max_wt=self.lineEdit_9.text()
        purity=self.lineEdit_4.text()
        stone_min_weight=self.lineEdit_2.text()
        stone_max_weight=self.lineEdit_7.text()
        max_quantity=self.lineEdit_6.text()
        if(self.radioButton_3.isChecked()):
            rates=self.radioButton_3.text()
        else:
            rates=self.radioButton_4.text()
        if(self.radioButton_11.isChecked()):
            metal=self.radioButton_11.text()
        elif(self.radioButton_12.isChecked()):
            metal=self.radioButton_12.text()
        elif(self.radioButton_13.isChecked()):
            metal=self.radioButton_13.text()
        else:
            metal=self.lineEdit.text()
        if(self.radioButton_9.isChecked()):
            stone=self.radioButton_9.text()
        else:
            stone=self.lineEdit_11.text()
        
        if(self.radioButton_7.isChecked()):
            rate_as=self.radioButton_7.text()
        else:
            rate_as=self.radioButton_8.text()
        if(self.checkBox.isChecked()):
            isActive=1
        else:
            isActive=0

        format_str='''SELECT * FROM Items WHERE Item_Description="{name}";'''
        sql_command=format_str.format(name=item_description)
        self.cursor.execute(sql_command)
        res = self.cursor.fetchone()
        if(res is None):
            format_str='''INSERT INTO Items(Item_Description,Groups,Rates,Min_Wt,Max_Wt,Metal,Purity,Stone_Description,S_Rate,S_Min_Wt,S_Max_Wt,Max_Qty,IsActive) VALUES ('{item_description}','{group}','{rates}',{min_wt},{max_wt},'{metal}',{purity},'{stone}','{rate_as}',{stone_min_weight},{stone_max_weight},{max_quantity},{isActive});'''
            sql_command=format_str.format(item_description=item_description,group=group,rates=rates,min_wt=min_wt,max_wt=max_wt,metal=metal,purity=purity,stone=stone,rate_as=rate_as,stone_min_weight=stone_min_weight,stone_max_weight=stone_max_weight,max_quantity=max_quantity,isActive=isActive)
            self.cursor.execute(sql_command)
            QtWidgets.QMessageBox.information(self, 'Success', 'New Item Created')
            self.default()
            self.clear()
            format_str='''SELECT * FROM Groups WHERE Group_Name='{group}';'''
            sql_command=format_str.format(group=group)
            self.cursor.execute(sql_command)
            res = self.cursor.fetchone()
            if(res is None):
                format_str='''INSERT INTO Groups(Group_Name,Group_Type) VALUES ('{group}','COMMON');'''
                sql_command=format_str.format(group=group)
                self.cursor.execute(sql_command)
                return
        else:
                QtWidgets.QMessageBox.warning(self, 'Error', 'Item Already Exists')
                self.default()
                self.clear()
                # self.close()
    
    def delete_btn(self):
        item_description = self.lineEdit_5.text()
        group=self.comboBox.lineEdit.text()
        min_wt=self.lineEdit_3.text()
        max_wt=self.lineEdit_9.text()
        purity=self.lineEdit_4.text()
        stone_min_weight=self.lineEdit_2text()
        stone_max_weight=self.lineEdit_7.text()
        max_quantity=self.lineEdit_6.text()
        if(self.radioButton_3.isChecked()):
            rates=self.radioButton_3.text()
        else:
            rates=self.radioButton_4.text()

        if(self.radioButton_11.isChecked()):
            metal=self.radioButton_11.text()
        elif(self.radioButton_12.isChecked()):
            metal=self.radioButton_12.text()
        elif(self.radioButton_13.isChecked()):
            metal=self.radioButton_13.text()
        else:
            metal=self.lineEdit.text()
        
        if(self.radioButton_9.isChecked()):
            stone=self.radioButton_9.text()
        else:
            stone=self.lineEdit_11.text()
        
        if(self.radioButton_7.isChecked()):
            rate_as=self.radioButton_7.text()
        else:
            rate_as=self.radioButton_8.text()
        
        if(self.checkBox.isChecked()):
            isActive=1
        else:
            isActive=0
        format_str='''SELECT * FROM Items WHERE Item_Description=""{item_description}"";'''
        sql_command=format_str.format(item_description=item_description)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchone()
        if(res is None):
            QtWidgets.QMessageBox.warning(self, 'Error', 'Item Does Not Exists')
            # self.close()
        else:
            format_str='''DELETE FROM Items WHERE Item_Description=""{item_description}"";'''
            sql_command=format_str.format(item_description=item_description)
            self.cursor.execute(sql_command)
            QtWidgets.QMessageBox.information(self, 'Success', 'Item Updated Successfully')
            self.default()
            self.clear()
            return
    
    def save_btn(self):
        item_description = self.lineEdit_5.text()
        group=self.comboBox.lineEdit().text()
        min_wt=self.lineEdit_3.text()
        max_wt=self.lineEdit_9.text()
        purity=self.lineEdit_4.text()
        stone_min_weight=self.lineEdit_2.text()
        stone_max_weight=self.lineEdit_7.text()
        max_quantity=self.lineEdit_6.text()
        if(self.radioButton_3.isChecked()):
            rates=self.radioButton_3.text()
        else:
            rates=self.radioButton_4.text()

        if(self.radioButton_11.isChecked()):
            metal=self.radioButton_11.text()
        elif(self.radioButton_12.isChecked()):
            metal=self.radioButton_12.text()
        elif(self.radioButton_13.isChecked()):
            metal=self.radioButton_13.text()
        else:
            metal=self.lineEdit.text()
        
        if(self.radioButton_9.isChecked()):
            stone=self.radioButton_9.text()
        else:
            stone=self.lineEdit_11.text()
        
        if(self.radioButton_7.isChecked()):
            rate_as=self.radioButton_7.text()
        else:
            rate_as=self.radioButton_8.text()
        
        if(self.checkBox.isChecked()):
            isActive=1
        else:
            isActive=0
        format_str='''SELECT * FROM Items WHERE Item_Description="{item_description}";'''
        sql_command=format_str.format(item_description=item_description)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchone()
        if(res is None):
            QtWidgets.QMessageBox.warning(self, 'Error', 'Item Does Not Exists')
            # self.close()
        else:
            format_str='''UPDATE Items SET Item_Description='{item_description}',Groups='{group},Rates='{rates}',Min_Wt={min_wt},Max_Wt={max_wt},Metal='{metal}',Purity={purity},Stone_Description='{stone}',S_Rate='{rate_as}',S_Min_Wt={stone_min_weight},S_Max_Wt={stone_max_weight},Max_Qty={max_quantity},IsActive={isActive};'''
            sql_command=format_str.format(item_description=item_description,group=group,rates=rates,min_wt=min_wt,max_wt=max_wt,metal=metal,purity=purity,stone=stone,rate_as=rate_as,stone_min_weight=stone_min_weight,stone_max_weight=stone_max_weight,max_quantity=max_quantity,isActive=isActive)
            self.cursor.execute(sql_command)
            QtWidgets.QMessageBox.information(self, 'Success', 'Item Updated Successfully')
            self.default()
            self.clear()
            return
    
    def search_btn(self):
        name=self.lineEdit_10.text()
        format_str='''SELECT * FROM Items WHERE Item_Description LIKE "{name}%";'''
        sql_command=format_str.format(name=name)
        self.cursor.execute(sql_command)
        res=self.cursor.fetchall()
        self.tableWidget.setRowCount(0)
        c=0
        for i in res:
            self.tableWidget.insertRow(c)
            self.tableWidget.setItem(c,0,QTableWidgetItem(i[1]))
            c=c+1







if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Items()
    # w = QtWidgets.QMainWindow()
    ex.show()
    # w.show()
    sys.exit(app.exec_())
