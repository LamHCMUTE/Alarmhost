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
        self.rtsp = 'rtsp://client:User@view2022@113.160.97.99:5554/cam/realmonitor?channel=1&subtype=1'
        #self.rtsp_2 = 'rtsp://client:User@view2022@113.160.97.99:2554/cam/realmonitor?channel=1&subtype=1'
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
        super(MainWindow,self).__init__()
        self.setupUi(self)

        self.Cld.hide()
        self.Btlich.clicked.connect(self.Bt_lich)
        self.Cld.clicked[QtCore.QDate].connect(self.get_Date)

        self.Cld_1.hide()
        self.Btlich_1.clicked.connect(self.Bt_lich1)
        self.Cld_1.clicked[QtCore.QDate].connect(self.get_Date1)
        list=['Tất cả','Cam 1','Cam 2','Cam 3']
        for x in list:
            self.BxCam.addItem(x)
        self.BxCam.currentIndexChanged.connect(self.cam)
        # self.th1 = ThreadStreamVideo()
        # self.th1.rtsp = 'rtsp://client:User@view2022@113.160.97.99:1554/cam/realmonitor?channel=1&subtype=1'
        # self.th1.changePixmap.connect(self.setImage)
        # self.th1.threadactive = True
        # self.th1.start()
        # self.count = 0
        # self.StartButton.clicked.connect(self.starton)
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
    def cam(self):
        self.th1 = ThreadStreamVideo()
        self.th1.rtsp = 'rtsp://client:User@view2022@113.160.97.99:5554/cam/realmonitor?channel=1&subtype=1'
        self.th1.changePixmap.connect(self.setImage1)
        self.th1.threadactive = True
        self.th1.start()
        self.count = 0
        self.StartButton.clicked.connect(self.starton)
    def setImage1(self, image):
        self.lbCam.setPixmap(QPixmap.fromImage(image))
    def starton(self):
        if self.count == 0:
            self.th1.stop()
            self.count = 1
            self.StartButton.setIcon(QIcon(QPixmap('res\icon\stop.png')))
        else:
            self.th1.start()
            self.count = 0
            self.StartButton.setIcon(QIcon(QPixmap('res\icon\pause.png')))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())