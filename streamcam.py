
import sys
from email.mime import image
from PyQt5 import QtWidgets, QtCore
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from time import sleep
import cv2
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QImage, QPixmap, QIcon
class ThreadStreamVideo(QThread):
    changePixmap = pyqtSignal(QImage)
    stopVideo = pyqtSignal()
    errorOpenCamera = pyqtSignal()
    def __init__(self,):
        super(ThreadStreamVideo, self,).__init__()
        self.cap = None
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