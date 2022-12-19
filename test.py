# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1227, 831)
        Main.setWindowOpacity(1.0)
        Main.setStyleSheet("")
        Main.setDockNestingEnabled(True)
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"    border-image: url(:/imgs/img/2.png) stretch, stretch;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalFrame = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame.setMaximumSize(QtCore.QSize(60, 16777215))
        self.verticalFrame.setStyleSheet("background-color: rgb(44, 62, 76);\n"
"\n"
"")
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalFrame)
        self.label.setMaximumSize(QtCore.QSize(52, 20))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("res/img/lo1.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_27 = QtWidgets.QLabel(self.verticalFrame)
        self.label_27.setMaximumSize(QtCore.QSize(50, 50))
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap("res/icon/home.png"))
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName("label_27")
        self.verticalLayout.addWidget(self.label_27)
        self.label_33 = QtWidgets.QLabel(self.verticalFrame)
        self.label_33.setMaximumSize(QtCore.QSize(50, 50))
        self.label_33.setText("")
        self.label_33.setPixmap(QtGui.QPixmap("res/icon/1.png"))
        self.label_33.setScaledContents(True)
        self.label_33.setObjectName("label_33")
        self.verticalLayout.addWidget(self.label_33)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_35 = QtWidgets.QLabel(self.verticalFrame)
        self.label_35.setMaximumSize(QtCore.QSize(40, 40))
        self.label_35.setText("")
        self.label_35.setPixmap(QtGui.QPixmap("res/icon/3.png"))
        self.label_35.setScaledContents(True)
        self.label_35.setObjectName("label_35")
        self.verticalLayout.addWidget(self.label_35)
        self.label_36 = QtWidgets.QLabel(self.verticalFrame)
        self.label_36.setMaximumSize(QtCore.QSize(40, 40))
        self.label_36.setText("")
        self.label_36.setPixmap(QtGui.QPixmap("res/icon/4.png"))
        self.label_36.setScaledContents(True)
        self.label_36.setObjectName("label_36")
        self.verticalLayout.addWidget(self.label_36)
        self.label_34 = QtWidgets.QLabel(self.verticalFrame)
        self.label_34.setMaximumSize(QtCore.QSize(40, 40))
        self.label_34.setText("")
        self.label_34.setPixmap(QtGui.QPixmap("res/icon/5.png"))
        self.label_34.setScaledContents(True)
        self.label_34.setObjectName("label_34")
        self.verticalLayout.addWidget(self.label_34)
        self.horizontalLayout_2.addWidget(self.verticalFrame)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalFrame_2 = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.horizontalFrame_2.setStyleSheet("background-color: rgb(3, 14, 22);")
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalFrame_2)
        self.pushButton_7.setAutoFillBackground(False)
        self.pushButton_7.setStyleSheet("\n"
"\n"
"font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font: 13px;\n"
"line-height: 16px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 1;\n"
"flex-grow: 0;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/icon/6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setIconSize(QtCore.QSize(29, 20))
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        self.pushButton = QtWidgets.QPushButton(self.horizontalFrame_2)
        self.pushButton.setStyleSheet("font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font: 13px;\n"
"line-height: 16px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 1;\n"
"flex-grow: 0;")
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(29, 20))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.comboBox = QtWidgets.QComboBox(self.horizontalFrame_2)
        self.comboBox.setMaximumSize(QtCore.QSize(119, 16777215))
        self.comboBox.setStyleSheet("font-family: \'Inte\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font: 12px;\n"
"line-height: 15px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;\n"
"box-sizing: border-box;\n"
"\n"
"position: absolute;\n"
"width: 119.7px;\n"
"height: 25.31px;\n"
"left: 314.41px;\n"
"top: 15.42px;\n"
"\n"
"border: 1px solid rgba(255, 255, 255, 0.5);\n"
"border-radius: 3px;")
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.horizontalFrame_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Layouttime = QtWidgets.QFrame(self.centralwidget)
        self.Layouttime.setStyleSheet("#Layouttime{\n"
"background: rgba(85, 89, 93, 0.5);\n"
"border-right: 1px solid #000000;\n"
"}")
        self.Layouttime.setObjectName("Layouttime")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Layouttime)
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Title = QtWidgets.QFrame(self.Layouttime)
        self.Title.setStyleSheet("Title{\n"
"background: rgba(85, 89, 93, 0.5);\n"
"border-right: 1px solid #000000;\n"
"}")
        self.Title.setObjectName("Title")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Title)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.Title)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMaximumSize(QtCore.QSize(122, 16777215))
        self.label_7.setStyleSheet("position: absolute;\n"
"width: 57px;\n"
"height: 16px;\n"
"left: 77.33px;\n"
"top: 69.58px;\n"
"\n"
"font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 13px;\n"
"line-height: 16px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;\n"
"")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_6 = QtWidgets.QLabel(self.Title)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setStyleSheet("position: absolute;\n"
"width: 57px;\n"
"height: 16px;\n"
"left: 77.33px;\n"
"top: 69.58px;\n"
"\n"
"font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 13px;\n"
"line-height: 16px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;\n"
"")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label_5 = QtWidgets.QLabel(self.Title)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet("position: absolute;\n"
"width: 57px;\n"
"height: 16px;\n"
"left: 77.33px;\n"
"top: 69.58px;\n"
"\n"
"font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 13px;\n"
"line-height: 16px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;\n"
"")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.label_4 = QtWidgets.QLabel(self.Title)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet("position: absolute;\n"
"width: 57px;\n"
"height: 16px;\n"
"left: 77.33px;\n"
"top: 69.58px;\n"
"\n"
"font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 13px;\n"
"line-height: 16px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;\n"
"")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.label_3 = QtWidgets.QLabel(self.Title)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("position: absolute;\n"
"width: 57px;\n"
"height: 16px;\n"
"left: 77.33px;\n"
"top: 69.58px;\n"
"\n"
"font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 13px;\n"
"line-height: 16px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;\n"
"")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout_4.addWidget(self.Title)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.line = QtWidgets.QFrame(self.Layouttime)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_6.addWidget(self.line)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalFrame_21 = QtWidgets.QFrame(self.Layouttime)
        self.horizontalFrame_21.setStyleSheet("background: rgba(217, 217, 217, 0.2);\n"
"border-radius: 5px;\n"
"\n"
"position: absolute;\n"
"width: 122px;\n"
"height: 16px;\n"
"left: 78.33px;\n"
"top: 197.42px;\n"
"\n"
"font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 13px;\n"
"line-height: 16px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;")
        self.horizontalFrame_21.setObjectName("horizontalFrame_21")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalFrame_21)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_12 = QtWidgets.QLabel(self.horizontalFrame_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMaximumSize(QtCore.QSize(122, 16777215))
        self.label_12.setStyleSheet("width: 57px;")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_7.addWidget(self.label_12)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.label_11 = QtWidgets.QLabel(self.horizontalFrame_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMaximumSize(QtCore.QSize(117, 16777215))
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.label_10 = QtWidgets.QLabel(self.horizontalFrame_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.label_9 = QtWidgets.QLabel(self.horizontalFrame_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.label_2 = QtWidgets.QLabel(self.horizontalFrame_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("background: rgba(217, 217, 217, 0.2);\n"
"border-radius: 5px;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.verticalLayout_4.addWidget(self.horizontalFrame_21)
        self.horizontalFrame = QtWidgets.QFrame(self.Layouttime)
        self.horizontalFrame.setStyleSheet("position: absolute;\n"
"width: 122px;\n"
"height: 16px;\n"
"left: 78.33px;\n"
"top: 197.42px;\n"
"\n"
"font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 13px;\n"
"line-height: 16px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;")
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_15 = QtWidgets.QLabel(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMaximumSize(QtCore.QSize(122, 16777215))
        self.label_15.setStyleSheet("")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_4.addWidget(self.label_15)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.label_17 = QtWidgets.QLabel(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_4.addWidget(self.label_17)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.label_16 = QtWidgets.QLabel(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_4.addWidget(self.label_16)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem12)
        self.label_14 = QtWidgets.QLabel(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem13)
        self.label_13 = QtWidgets.QLabel(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_4.addWidget(self.label_13)
        self.verticalLayout_4.addWidget(self.horizontalFrame)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem14)
        self.horizontalLayout_5.addWidget(self.Layouttime)
        self.a = QtWidgets.QFrame(self.centralwidget)
        self.a.setMaximumSize(QtCore.QSize(678, 16777215))
        self.a.setStyleSheet("#a{\n"
"background: rgba(85, 89, 93, 0.5);\n"
"}")
        self.a.setObjectName("a")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.a)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lbCam = QtWidgets.QLabel(self.a)
        self.lbCam.setMaximumSize(QtCore.QSize(680, 428))
        self.lbCam.setStyleSheet("")
        self.lbCam.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbCam.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lbCam.setText("")
        self.lbCam.setScaledContents(True)
        self.lbCam.setObjectName("lbCam")
        self.verticalLayout_6.addWidget(self.lbCam)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_19 = QtWidgets.QLabel(self.a)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setMaximumSize(QtCore.QSize(9, 12))
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("res/icon/left.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_8.addWidget(self.label_19)
        self.StartButton = QtWidgets.QPushButton(self.a)
        self.StartButton.setMaximumSize(QtCore.QSize(9, 12))
        self.StartButton.setStyleSheet("background: rgba(85, 89, 93, 0.5);\n"
"border-right: 1px solid #000000;")
        self.StartButton.setText("")
        self.StartButton.setObjectName("StartButton")
        self.horizontalLayout_8.addWidget(self.StartButton)
        self.n = QtWidgets.QLabel(self.a)
        self.n.setMaximumSize(QtCore.QSize(9, 12))
        self.n.setText("")
        self.n.setPixmap(QtGui.QPixmap("res/icon/right.png"))
        self.n.setScaledContents(True)
        self.n.setObjectName("n")
        self.horizontalLayout_8.addWidget(self.n)
        self.line_2 = QtWidgets.QFrame(self.a)
        self.line_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_8.addWidget(self.line_2)
        self.label_23 = QtWidgets.QLabel(self.a)
        self.label_23.setMaximumSize(QtCore.QSize(26, 12))
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap("res/icon/time.png"))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_8.addWidget(self.label_23)
        self.label_22 = QtWidgets.QLabel(self.a)
        self.label_22.setMaximumSize(QtCore.QSize(18, 14))
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap("res/icon/sound.png"))
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_8.addWidget(self.label_22)
        self.label_21 = QtWidgets.QLabel(self.a)
        self.label_21.setMaximumSize(QtCore.QSize(14, 14))
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("res/icon/zoom.png"))
        self.label_21.setScaledContents(True)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_8.addWidget(self.label_21)
        self.label_24 = QtWidgets.QLabel(self.a)
        self.label_24.setMaximumSize(QtCore.QSize(15, 15))
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap("res/icon/down.png"))
        self.label_24.setScaledContents(True)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_8.addWidget(self.label_24)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.label_25 = QtWidgets.QLabel(self.a)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setStyleSheet("width: 114px;\n"
"height: 17px;\n"
"\n"
"font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 14px;\n"
"line-height: 17px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;")
        self.label_25.setObjectName("label_25")
        self.verticalLayout_6.addWidget(self.label_25)
        self.label_26 = QtWidgets.QLabel(self.a)
        self.label_26.setText("")
        self.label_26.setPixmap(QtGui.QPixmap("res/icon/line.png"))
        self.label_26.setObjectName("label_26")
        self.verticalLayout_6.addWidget(self.label_26)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_38 = QtWidgets.QLabel(self.a)
        self.label_38.setStyleSheet("width: 61px;\n"
"height: 16px;\n"
"\n"
"font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 13px;\n"
"line-height: 16px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: rgba(255, 255, 255, 0.5);\n"
"\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;")
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_12.addWidget(self.label_38)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem15)
        self.label_37 = QtWidgets.QLabel(self.a)
        self.label_37.setStyleSheet("width: 127px;\n"
"height: 16px;\n"
"\n"
"font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 13px;\n"
"line-height: 16px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 1;\n"
"flex-grow: 0;")
        self.label_37.setObjectName("label_37")
        self.horizontalLayout_12.addWidget(self.label_37)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_41 = QtWidgets.QLabel(self.a)
        self.label_41.setStyleSheet("width: 112px;\n"
"height: 16px;\n"
"\n"
"font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 13px;\n"
"line-height: 16px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: rgba(255, 255, 255, 0.5);\n"
"\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;")
        self.label_41.setObjectName("label_41")
        self.horizontalLayout_13.addWidget(self.label_41)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem16)
        self.label_39 = QtWidgets.QLabel(self.a)
        self.label_39.setStyleSheet("width: 116px;\n"
"height: 16px;\n"
"\n"
"font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 13px;\n"
"line-height: 16px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 1;\n"
"flex-grow: 0;")
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_13.addWidget(self.label_39)
        self.verticalLayout_6.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_42 = QtWidgets.QLabel(self.a)
        self.label_42.setStyleSheet("width: 90px;\n"
"height: 16px;\n"
"\n"
"font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 13px;\n"
"line-height: 16px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: rgba(255, 255, 255, 0.5);\n"
"\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;")
        self.label_42.setObjectName("label_42")
        self.horizontalLayout_14.addWidget(self.label_42)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem17)
        self.label_40 = QtWidgets.QLabel(self.a)
        self.label_40.setStyleSheet("width: 121px;\n"
"height: 16px;\n"
"\n"
"font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 13px;\n"
"line-height: 16px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 1;\n"
"flex-grow: 0;")
        self.label_40.setObjectName("label_40")
        self.horizontalLayout_14.addWidget(self.label_40)
        self.verticalLayout_6.addLayout(self.horizontalLayout_14)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem18)
        self.label_28 = QtWidgets.QLabel(self.a)
        self.label_28.setStyleSheet("width: 114px;\n"
"height: 17px;\n"
"\n"
"font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 14px;\n"
"line-height: 17px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"/* Inside auto layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;")
        self.label_28.setObjectName("label_28")
        self.verticalLayout_6.addWidget(self.label_28)
        self.label_29 = QtWidgets.QLabel(self.a)
        self.label_29.setText("")
        self.label_29.setPixmap(QtGui.QPixmap("res/icon/line.png"))
        self.label_29.setObjectName("label_29")
        self.verticalLayout_6.addWidget(self.label_29)
        self.label_32 = QtWidgets.QLabel(self.a)
        self.label_32.setText("")
        self.label_32.setObjectName("label_32")
        self.verticalLayout_6.addWidget(self.label_32)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_31 = QtWidgets.QLabel(self.a)
        self.label_31.setStyleSheet("position: absolute;\n"
"width: 88px;\n"
"height: 15px;\n"
"left: 1065.04px;\n"
"top: 830.45px;\n"
"\n"
"font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 12px;\n"
"line-height: 15px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;")
        self.label_31.setTextFormat(QtCore.Qt.AutoText)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_7.addWidget(self.label_31)
        self.comboBox_3 = QtWidgets.QComboBox(self.a)
        self.comboBox_3.setMaximumSize(QtCore.QSize(217, 16777215))
        self.comboBox_3.setStyleSheet("background: rgba(85, 89, 93, 0.5);\n"
"position: absolute;\n"
"width: 217px;\n"
"height: 15px;\n"
"left: 1070.6px;\n"
"top: 862.3px;\n"
"\n"
"font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 12px;\n"
"line-height: 15px;\n"
"/* identical to box height */\n"
"\n"
"border: 1px solid rgba(255, 255, 255, 0.5);\n"
"border-radius: 3px;\n"
"color: #FFFFFF;")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.verticalLayout_7.addWidget(self.comboBox_3)
        self.horizontalLayout_10.addLayout(self.verticalLayout_7)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_10)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem19)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_30 = QtWidgets.QLabel(self.a)
        self.label_30.setStyleSheet("position: absolute;\n"
"width: 88px;\n"
"height: 15px;\n"
"left: 1065.04px;\n"
"top: 830.45px;\n"
"\n"
"font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 12px;\n"
"line-height: 15px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;")
        self.label_30.setObjectName("label_30")
        self.verticalLayout_3.addWidget(self.label_30)
        self.comboBox_2 = QtWidgets.QComboBox(self.a)
        self.comboBox_2.setMaximumSize(QtCore.QSize(217, 16777215))
        self.comboBox_2.setStyleSheet("background: rgba(85, 89, 93, 0.5);\n"
"position: absolute;\n"
"width: 217px;\n"
"height: 15px;\n"
"left: 1070.6px;\n"
"top: 862.3px;\n"
"\n"
"font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 12px;\n"
"line-height: 15px;\n"
"/* identical to box height */\n"
"\n"
"border: 1px solid rgba(255, 255, 255, 0.5);\n"
"border-radius: 3px;\n"
"color: #FFFFFF;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_2)
        self.horizontalLayout_11.addLayout(self.verticalLayout_3)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_11)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem20)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem21)
        self.label_43 = QtWidgets.QLabel(self.a)
        self.label_43.setMaximumSize(QtCore.QSize(20, 18))
        self.label_43.setText("")
        self.label_43.setPixmap(QtGui.QPixmap("res/icon/bin.png"))
        self.label_43.setScaledContents(True)
        self.label_43.setObjectName("label_43")
        self.horizontalLayout_17.addWidget(self.label_43)
        self.verticalLayout_6.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_5.addWidget(self.a)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "MainWindow"))
        self.pushButton_7.setText(_translate("Main", "01/11/2022"))
        self.pushButton.setText(_translate("Main", "02/12/2022"))
        self.comboBox.setItemText(0, _translate("Main", "Tất cả"))
        self.comboBox.setItemText(1, _translate("Main", "l"))
        self.label_7.setText(_translate("Main", "Thời gian"))
        self.label_6.setText(_translate("Main", "Loại cảnh báo"))
        self.label_5.setText(_translate("Main", "Thiết bị cảnh báo"))
        self.label_4.setText(_translate("Main", "Độ ưu tiên"))
        self.label_3.setText(_translate("Main", "Trạng thái xử lí"))
        self.label_12.setText(_translate("Main", "02/12/2022"))
        self.label_11.setText(_translate("Main", "Phát hiện di chuyển"))
        self.label_10.setText(_translate("Main", "Cameara văn phòng"))
        self.label_9.setText(_translate("Main", "Bình thường"))
        self.label_2.setText(_translate("Main", "Chưa xử lí"))
        self.label_15.setText(_translate("Main", "17/11/2022 "))
        self.label_17.setText(_translate("Main", "Kích hoạt thủ công"))
        self.label_16.setText(_translate("Main", "Obox Alarm 01"))
        self.label_14.setText(_translate("Main", "Khẩn cấp"))
        self.label_13.setText(_translate("Main", "Chưa xử lí"))
        self.label_25.setText(_translate("Main", "Chi tiết báo động"))
        self.label_38.setText(_translate("Main", "Thời gian:"))
        self.label_37.setText(_translate("Main", "02/12/2022 10:03:12"))
        self.label_41.setText(_translate("Main", "Thiết bị cảnh báo:"))
        self.label_39.setText(_translate("Main", "Camera văn phòng"))
        self.label_42.setText(_translate("Main", "Loại cảnh báo:"))
        self.label_40.setText(_translate("Main", "Phát hiện di chuyển"))
        self.label_28.setText(_translate("Main", "Xử lí"))
        self.label_31.setText(_translate("Main", "Trạng thái xử lí"))
        self.comboBox_3.setItemText(0, _translate("Main", "Chưa xử lí           "))
        self.label_30.setText(_translate("Main", "Độ ưu tiên"))
        self.comboBox_2.setItemText(0, _translate("Main", "Bình thường"))
import res.resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())
