import cv2
import self
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from IntelligentAnalysis.intelligentQT import Ui_Main
class Calendar(QMainWindow, Ui_Main):
    def __init__(self,parent=None):
        super(Calendar,self).__init__(parent)
        self.parent = parent
        self.showcal()
    def showcal(self):
        # show calendar start
        self.parent.Cld.hide()
        self.parent.Btlich.clicked.connect(self.Bt_lich)
        self.parent.Cld.clicked[QtCore.QDate].connect(self.get_Date)
        # show calendar finish
        self.parent.Cld_1.hide()
        self.parent.Btlich_1.clicked.connect(self.Bt_lich1)
        self.parent.Cld_1.clicked[QtCore.QDate].connect(self.get_Date1)
    def Bt_lich(self):
        if self.parent.Cld.isHidden():
            self.parent.Cld.show()
        else:
            self.parent.Cld.hide()
    def get_Date(self, date):
        self.parent.dateEdit.setDate(date)
        self.parent.Cld.hide()
    def Bt_lich1(self):
        if self.parent.Cld_1.isHidden():
            self.parent.Cld_1.show()
        else:
            self.parent.Cld_1.hide()
    def get_Date1(self, date):
        self.parent.dateEdit_1.setDate(date)
        self.parent.Cld_1.hide()
