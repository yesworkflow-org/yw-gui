# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_ui.ui'
#
# Created: Thu Jul 23 15:11:50 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(354, 410)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.tabData = QtGui.QTabWidget(self.centralwidget)
        self.tabData.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tabData.setAutoFillBackground(True)
        self.tabData.setTabsClosable(True)
        self.tabData.setMovable(True)
        self.tabData.setObjectName(_fromUtf8("tabData"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btnYWExtract = QtGui.QPushButton(self.tab_2)
        self.btnYWExtract.setObjectName(_fromUtf8("btnYWExtract"))
        self.horizontalLayout_2.addWidget(self.btnYWExtract)
        self.btnModel = QtGui.QPushButton(self.tab_2)
        self.btnModel.setObjectName(_fromUtf8("btnModel"))
        self.horizontalLayout_2.addWidget(self.btnModel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.txtErrorBox = QtGui.QTextBrowser(self.tab_2)
        self.txtErrorBox.setObjectName(_fromUtf8("txtErrorBox"))
        self.verticalLayout.addWidget(self.txtErrorBox)
        self.btnYWGraph = QtGui.QPushButton(self.tab_2)
        self.btnYWGraph.setObjectName(_fromUtf8("btnYWGraph"))
        self.verticalLayout.addWidget(self.btnYWGraph)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.tabData.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayout_9.addWidget(self.tabData)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabData.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btnYWExtract.setText(_translate("MainWindow", "YW Extract", None))
        self.btnModel.setText(_translate("MainWindow", "YW Model", None))
        self.label.setText(_translate("MainWindow", "Message Box", None))
        self.btnYWGraph.setText(_translate("MainWindow", "YW Graph", None))
        self.tabData.setTabText(self.tabData.indexOf(self.tab_2), _translate("MainWindow", "YW Tools", None))

