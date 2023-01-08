import sys
from email.mime import image
from PyQt5 import QtWidgets, QtCore
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from time import sleep
import cv2
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QImage, QPixmap, QIcon
from boxalarm import Ui_BoxAlarm
from streamcam import ThreadStreamVideo

class MainWindow(QMainWindow, Ui_BoxAlarm):
    def __init__(self):
        super(MainWindow,self,).__init__()
        self.setupUi(self)
        #show calendar start
        self.Cld.hide()
        self.Btlich.clicked.connect(self.Bt_lich)
        self.Cld.clicked[QtCore.QDate].connect(self.get_Date)
        # show calendar finish
        self.Cld_1.hide()
        self.Btlich_1.clicked.connect(self.Bt_lich1)
        self.Cld_1.clicked[QtCore.QDate].connect(self.get_Date1)
        # show data table
        self.tableWidget.hide()
        self.tableWidget.setColumnWidth(0,233)
        self.tableWidget.setColumnWidth(1,233)
        self.tableWidget.setColumnWidth(2,234)
        self.tableWidget.setColumnWidth(3,234)
        self.tableWidget.setColumnWidth(4,234)
        self.tableWidget.setRowHeight(0, 50)
        self.tableWidget.setRowHeight(1, 50)
        self.loaddata()

        self.home.clicked.connect(self.showtable)
        self.clock.clicked.connect(self.showtime)
        #stream 4 cam
        self.th = None
        self.list=[{'name':'Tất cả','rtsp':''}
            ,{'name':'Cam 1','rtsp':'rtsp://client:User@view2022@113.160.97.99:4554/cam/realmonitor?channel=1&subtype=1'}
            ,{'name':'Cam 2','rtsp':'rtsp://client:User@view2022@113.160.97.99:1554/cam/realmonitor?channel=1&subtype=1'}
            ,{'name':'Cam 3','rtsp':'rtsp://client:User@view2022@113.160.97.99:2554/cam/realmonitor?channel=1&subtype=1'}
            ,{'name':'Cam 4','rtsp':'rtsp://client:User@view2022@113.160.97.99:5554/cam/realmonitor?channel=1&subtype=1'}]
        for x in self.list:
            self.bxCam.addItem(x['name'])
        self.bxCam.currentIndexChanged.connect(lambda : self.switchCam())
    def loaddata(self):
        titletable = [{"Thời gian": " ", "Loại cảnh báo": 'Phát hiện di chuyển', "Thiết bị cảnh báo": "Camera Văn Phòng","Độ ưu tiên":"Bình thường","Trạng thái xử lí":"Chưa xử lí"},
                  {"Thời gian": " ", "Loại cảnh báo": 'Kích hoạt thủ công', "Thiết bị cảnh báo": "Obox alarm 01","Độ ưu tiên":"Khẩn cấp","Trạng thái xử lí":"Chưa xử lí"}]
        row = 0
        self.tableWidget.setRowCount(len(titletable))
        for title in titletable:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title["Thời gian"]))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(title["Loại cảnh báo"])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(title["Thiết bị cảnh báo"]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(title["Độ ưu tiên"]))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(title["Trạng thái xử lí"]))
            row = row + 1
    def showtable(self):
        self.tableWidget.show()

    def showtime(self):
        self.tableWidget.hide()
    def switchCam(self):
        cam = self.list[self.bxCam.currentIndex()]
        if cam is not None and cam['rtsp'] != '':
            self.cam(cam['rtsp'])
        # elif cam['name':'Tất cả']:
        #     self.lbCam.disconnect()
    def cam(self,rtsp):
        if self.th !=None and self.th.isRunning():
            self.th.stop()
        self.th = ThreadStreamVideo()
        print(self.th.isRunning())
        self.th.rtsp =rtsp
        self.th.changePixmap.connect(self.setImage1)
        self.th.threadactive = True
        self.th.start()
        print(self.th.isRunning())
        self.count = 0
        self.StartButton.clicked.connect(self.starton)
    def setImage1(self, image):
        self.lbCam.setPixmap(QPixmap.fromImage(image))
    def starton(self):
        if self.count == 0:
            self.th.stop()
            self.count = 1
            self.StartButton.setIcon(QIcon(QPixmap('res\icon\stop.png')))
        else:
            self.th.start()
            self.count = 0
            self.StartButton.setIcon(QIcon(QPixmap('res\icon\pause.png')))
    def Bt_lich(self):
        if self.Cld.isHidden():
            self.Cld.show()
        else:
            self.Cld.hide()
    def get_Date(self, date):
        self.dateEdit.setDate(date)
        self.Cld.hide()
    def Bt_lich1(self):
        if self.Cld_1.isHidden():
            self.Cld_1.show()
        else:
            self.Cld_1.hide()
    def get_Date1(self, date):
        self.dateEdit_1.setDate(date)
        self.Cld_1.hide()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())