# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Split.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
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
        self.dateEdit_3 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_3.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit_3.setCalendarPopup(True)
        self.dateEdit_3.setDate(QtCore.QDate(2019, 8, 6))
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.horizontalLayout_5.addWidget(self.dateEdit_3)
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
        self.dateEdit_4 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_4.setCalendarPopup(True)
        self.dateEdit_4.setDate(QtCore.QDate(2019, 8, 6))
        self.dateEdit_4.setObjectName("dateEdit_4")
        self.horizontalLayout_6.addWidget(self.dateEdit_4)
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
        self.lineEdit_42 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_42.setReadOnly(True)
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.verticalLayout_29.addWidget(self.lineEdit_42)
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
        icon.addPixmap(QtGui.QPixmap(":/icons/icons8-organization-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFirm.setIcon(icon)
        self.actionFirm.setObjectName("actionFirm")
        self.actionValuer = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons8-user-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionValuer.setIcon(icon1)
        self.actionValuer.setObjectName("actionValuer")
        self.actionGroups = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons8-list-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGroups.setIcon(icon2)
        self.actionGroups.setObjectName("actionGroups")
        self.actionItems = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons8-ring-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionItems.setIcon(icon3)
        self.actionItems.setObjectName("actionItems")
        self.actionValuation = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons8-contract-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionValuation.setIcon(icon4)
        self.actionValuation.setObjectName("actionValuation")
        self.actionMarket_Rates = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons8-us-dollar-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMarket_Rates.setIcon(icon5)
        self.actionMarket_Rates.setObjectName("actionMarket_Rates")
        self.actionChange_Password = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons8-password-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionChange_Password.setIcon(icon6)
        self.actionChange_Password.setObjectName("actionChange_Password")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons8-about-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon7)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons8-exit-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon8)
        self.actionExit.setObjectName("actionExit")
        self.actionSplit_Valuation = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/icons8-separate-document-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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


import toolbar_rc
