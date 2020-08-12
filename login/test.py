import Login
import testItemMaster
import sys
from PyQt5 import QtWidgets,QtWidgets,QtCore
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

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Login.UiLogin()
    ex.show()
    #ex1=test_firm.Ui_Firm_setup()
    #ex1.show()
    ex1=testitemMaster.Ui_Items()
    ex1.show()
    sys.exit(app.exec_())
