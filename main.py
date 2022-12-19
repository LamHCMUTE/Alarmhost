import sys
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from time import sleep

import cv2
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.uic.properties import QtGui, QtCore

from test import Ui_Main

class ThreadStreamVideo(QThread):
    changePixmap = pyqtSignal(QImage)
    stopVideo = pyqtSignal()
    errorOpenCamera = pyqtSignal()
    def __init__(self,):
        super(ThreadStreamVideo, self,).__init__()
        self.cap = None
        self.rtsp = 'rtsp://client:User@view2022@113.160.97.99:1554/cam/realmonitor?channel=1&subtype=1'
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
        self.th1 = ThreadStreamVideo()
        self.th1.rtsp = 'rtsp://client:User@view2022@113.160.97.99:1554/cam/realmonitor?channel=1&subtype=1'
        self.th1.changePixmap.connect(self.setImage)

        self.th1.threadactive = True
        self.count=0
        # self.th1.start()

        self.StartButton.clicked.connect(self.starton)
    def starton(self):
        if self.count == 0:
            self.th1.start()
            self.count = 1
            self.StartButton.setIcon(QIcon(QPixmap('res\icon\pause.png')))
        else:
            self.th1.stop()
            self.count = 0
            self.StartButton.setIcon(QIcon(QPixmap('res\icon\stop.png')))

    def setImage(self, image):
        self.lbCam.setPixmap(QPixmap.fromImage(image))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())