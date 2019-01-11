# -*- coding: utf-8 -*-

import sys
import os

from PyQt5.QtWidgets import *
from PyQt5 import uic
from Model.Webdriver import Webdriver
from Tasks.Aipo import Aipo
from Constants.Paths import Paths
from View.Ui_MainWindow import Ui_MainWindow

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, chromeDriver):
        super().__init__()
        self.Aipo = Aipo(chromeDriver)

        self.setupUi(self)
        self.myPushButton.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        someValue = self.Aipo.start(self.aipoID.text(), self.aipoPassword.text())
        self.label.setText(someValue)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow(Webdriver().chromeDriver())
    myWindow.show()
    app.exec_()
