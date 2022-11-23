from PyQt5 import QtCore, QtGui, QtWidgets


class Screen(object):
    def __init__(self):
        self.actionNew = None
        self.actionAbout_2 = None
        self.label_2 = None
        self.horizontalSlider = None
        self.actionPaste_2 = None
        self.actionCopy_2 = None
        self.actionCut_2 = None
        self.actionCopy = None
        self.actionCut = None
        self.menuHelp = None
        self.actionSave_2 = None
        self.actionPaste = None
        self.actionOpen_2 = None
        self.actionAbout = None
        self.menubar = None
        self.menuFile = None
        self.statusbar = None
        self.actionSave = None
        self.actionOpen = None
        self.menuEdit = None
        self.label = None
        self.pushButton = None
        self.textEdit = None
        self.radioButton_2 = None
        self.radioButton = None
        self.verticalLayout = None
        self.verticalLayoutWidget = None
        self.centralwidget = None

    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(828, 718)
        Window.setFixedSize(828, 718)
        Window.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: black;")
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(630, 230, 81, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton.setStyleSheet("QRadioButton::indicator {width: 13px; height: 13px; border-radius: 8px;} "
                                       "QRadioButton::indicator:checked {background-color: white; width: 9px; "
                                       "height: 9px; border: 4px solid rgb(232, 0, 0);} "
                                       "QRadioButton::indicator:checked:hover {border: 4px solid rgb(255, 0, 0);} "
                                       "QRadioButton::indicator:unchecked {background-color: rgb(240, 240, 240); "
                                       "border: 2px solid rgb(100, 100, 100);} QRadioButton::indicator:unchecked:hover "
                                       "{border: 2px solid rgb(232, 0, 0);}")
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_2.setStyleSheet("QRadioButton::indicator {width: 13px; height: 13px; border-radius: 8px;} "
                                         "QRadioButton::indicator:checked {background-color: white; width: 9px;\n"
                                         "height: 9px; border: 4px solid rgb(232, 0, 0);} "
                                         "QRadioButton::indicator:checked:hover {border: 4px solid rgb(255, 0, 0);} "
                                         "QRadioButton::indicator:unchecked {background-color: rgb(240, 240, 240);"
                                         "border: 2px solid rgb(100, 100, 100);} "
                                         "QRadioButton::indicator:unchecked:hover {border: 2px solid rgb(232, 0, 0);}")
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(110, 410, 601, 181))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textEdit.setStyleSheet("border: 1px solid rgb(232, 232, 232);")
        self.textEdit.setMarkdown("")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 610, 601, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {border: 1px solid rgb(232, 232, 232); border-radius: 6px;\n"
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, "
                                      "stop:0 rgba(255, 255, 255, 255), stop:1 rgba(245, 245, 245, 255));}\n"
                                      "QPushButton:hover {background-color: qlineargradient(spread:pad, "
                                      "x1:0, y1:1, x2:0, y2:0, stop:0 rgba(245, 245, 245, 255), "
                                      "stop:1 rgba(255, 255, 255, 255)); border: 1px solid rgb(232, 0, 0);}")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 30, 481, 341))
        self.label.setStyleSheet("image: url(:/newPrefix/enigma.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(630, 380, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(169, 380, 431, 22))
        self.horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider.setStyleSheet("QSlider:handle {\n"
                                            "background-color: rgb(232, 0, 0);\n"
                                            "border-radius: 6px;\n"
                                            "}\n"
                                            "QSlider:handle:hover {\n"
                                            "background-color: rgb(255, 0, 0);\n"
                                            "border-radius: 6px;\n}")
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSliderPosition(10)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setObjectName("horizontalSlider")
        Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 828, 26))
        self.menubar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menuFile.setStyleSheet("QMenu::item:selected {background-color: rgb(230, 230, 230);}")
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setStyleSheet("QMenu::item:selected {background-color: rgb(230, 230, 230);}")
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setStyleSheet("QMenu::item:selected {background-color: rgb(230, 230, 230);}")
        self.menuHelp.setObjectName("menuHelp")
        Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Window)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        Window.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(Window)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(Window)
        self.actionSave.setObjectName("actionSave")
        self.actionCopy = QtWidgets.QAction(Window)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCut = QtWidgets.QAction(Window)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(Window)
        self.actionPaste.setObjectName("actionPaste")
        self.actionAbout = QtWidgets.QAction(Window)
        self.actionAbout.setObjectName("actionAbout")
        self.actionOpen_2 = QtWidgets.QAction(Window)
        self.actionOpen_2.setObjectName("actionOpen_2")
        self.actionSave_2 = QtWidgets.QAction(Window)
        self.actionSave_2.setObjectName("actionSave_2")
        self.actionCopy_2 = QtWidgets.QAction(Window)
        self.actionCopy_2.setObjectName("actionCopy_2")
        self.actionCut_2 = QtWidgets.QAction(Window)
        self.actionCut_2.setObjectName("actionCut_2")
        self.actionPaste_2 = QtWidgets.QAction(Window)
        self.actionPaste_2.setObjectName("actionPaste_2")
        self.actionAbout_2 = QtWidgets.QAction(Window)
        self.actionAbout_2.setObjectName("actionAbout_2")
        self.actionNew = QtWidgets.QAction(Window)
        self.actionNew.setObjectName("actionNew")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen_2)
        self.menuFile.addAction(self.actionSave_2)
        self.menuEdit.addAction(self.actionCopy_2)
        self.menuEdit.addAction(self.actionCut_2)
        self.menuEdit.addAction(self.actionPaste_2)
        self.menuHelp.addAction(self.actionAbout_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Caesar\'s Cipher"))
        self.radioButton.setText(_translate("Window", "Encode"))
        self.radioButton_2.setText(_translate("Window", "Decode"))
        self.textEdit.setHtml(_translate("Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                         "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" />"
                                                   "<style type=\"text/css\">"
                                         "\np, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; "
                                                   "font-weight:400; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
                                                   "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                                   "text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("Window", "Encode"))
        self.label_2.setText(_translate("Window", "10"))
        self.menuFile.setTitle(_translate("Window", "File"))
        self.menuEdit.setTitle(_translate("Window", "Edit"))
        self.menuHelp.setTitle(_translate("Window", "Help"))
        self.actionOpen.setText(_translate("Window", "Open"))
        self.actionSave.setText(_translate("Window", "Save"))
        self.actionCopy.setText(_translate("Window", "Copy"))
        self.actionCut.setText(_translate("Window", "Cut"))
        self.actionPaste.setText(_translate("Window", "Paste"))
        self.actionAbout.setText(_translate("Window", "About"))
        self.actionOpen_2.setText(_translate("Window", "Open"))
        self.actionSave_2.setText(_translate("Window", "Save"))
        self.actionCopy_2.setText(_translate("Window", "Copy"))
        self.actionCut_2.setText(_translate("Window", "Cut"))
        self.actionPaste_2.setText(_translate("Window", "Paste"))
        self.actionAbout_2.setText(_translate("Window", "About"))
        self.actionNew.setText(_translate("Window", "New"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = Screen()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())
