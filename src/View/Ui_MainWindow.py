# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View/Ui_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(659, 517)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.tamelID = QtWidgets.QLineEdit(self.centralwidget)
        self.tamelID.setObjectName("tamelID")
        self.horizontalLayout.addWidget(self.tamelID)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.tamelPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.tamelPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.tamelPassword.setObjectName("tamelPassword")
        self.horizontalLayout_2.addWidget(self.tamelPassword)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.aipoID = QtWidgets.QLineEdit(self.centralwidget)
        self.aipoID.setObjectName("aipoID")
        self.horizontalLayout_3.addWidget(self.aipoID)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.aipoPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.aipoPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.aipoPassword.setObjectName("aipoPassword")
        self.horizontalLayout_4.addWidget(self.aipoPassword)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.myPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.myPushButton.setObjectName("myPushButton")
        self.verticalLayout.addWidget(self.myPushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 659, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "tamel ID"))
        self.label_3.setText(_translate("MainWindow", "tamel password"))
        self.label.setText(_translate("MainWindow", "aipo ID"))
        self.label_5.setText(_translate("MainWindow", "aipo password"))
        self.myPushButton.setText(_translate("MainWindow", "Get morning memo"))

