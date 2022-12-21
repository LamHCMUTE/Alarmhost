import sys
from email.mime import image
from PyQt5 import QtWidgets, QtCore
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from time import sleep
import cv2
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QImage, QPixmap, QIcon
from test import Ui_Main
class ThreadStreamVideo(QThread):
    changePixmap = pyqtSignal(QImage)
    stopVideo = pyqtSignal()
    errorOpenCamera = pyqtSignal()
    def __init__(self,):
        super(ThreadStreamVideo, self,).__init__()
        self.cap = None
        self.rtsp = 'rtsp://client:User@view2022@113.160.97.99:4554/cam/realmonitor?channel=1&subtype=1'
        self.rtsp = 'rtsp://client:User@view2022@113.160.97.99:2554/cam/realmonitor?channel=1&subtype=1'
        self.rtsp = 'rtsp://client:User@view2022@113.160.97.99:1554/cam/realmonitor?channel=1&subtype=1'
        self.rtsp = 'rtsp://client:User@view2022@113.160.97.99:5554/cam/realmonitor?channel=1&subtype=1'
        self.threadactive = None
        self.frame = None
    def run(self):
        self.threadactive = True
        # print("Luồng 1: ", len(self.data))
        # print("self.threadactive: ", self.threadactive)
        if len(self.rtsp) != 0:
            self.cap = cv2.VideoCapture(str(self.rtsp))
            if self.cap.isOpened():
                while self.threadactive:
                    fontret, fontframe = self.cap.read()
                    #set width and height
                    if fontret:
                        fontframe = cv2.resize(fontframe, (640, 480))
                        self.frame = fontframe
                        rgbImage = cv2.cvtColor(fontframe, cv2.COLOR_BGR2RGB)
                        h, w, ch = rgbImage.shape
                        bytesPerLine = ch * w
                        convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                        p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                        self.changePixmap.emit(p)
                self.stopVideo.emit()
                self.cap.release()
            else:
                self.errorOpenCamera.emit()
    def stop(self):
        self.threadactive = False
        self.quit()
class MainWindow(QMainWindow, Ui_Main):
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
        people = [{"Thời gian": " ", "Loại cảnh báo": 'Phát hiện di chuyển', "Thiết bị cảnh báo": "Camera Văn Phòng","Độ ưu tiên":"Bình thường","Trạng thái xử lí":"Chưa xử lí"},
                  {"Thời gian": " ", "Loại cảnh báo": 'Kích hoạt thủ công', "Thiết bị cảnh báo": "Obox alarm 01","Độ ưu tiên":"Khẩn cấp","Trạng thái xử lí":"Chưa xử lí"}]
        row = 0
        self.tableWidget.setRowCount(len(people))
        for person in people:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person["Thời gian"]))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(person["Loại cảnh báo"])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(person["Thiết bị cảnh báo"]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(person["Độ ưu tiên"]))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(person["Trạng thái xử lí"]))
            row = row + 1
    def showtable(self):
        self.tableWidget.show()
        #self.home.hover()
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
    # self.th1 = ThreadStreamVideo()
    # self.th1.rtsp = 'rtsp://client:User@view2022@113.160.97.99:1554/cam/realmonitor?channel=1&subtype=1'
    # self.th1.changePixmap.connect(self.setImage)
    # self.th1.threadactive = True
    # self.th1.start()
    # self.count = 0
    # self.StartButton.clicked.connect(self.starton)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())