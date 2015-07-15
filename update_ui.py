# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_ui.ui'
#
# Created: Wed Jul 08 11:56:45 2015
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
        MainWindow.resize(658, 646)
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
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnShowAllFiles = QtGui.QPushButton(self.tab_2)
        self.btnShowAllFiles.setObjectName(_fromUtf8("btnShowAllFiles"))
        self.horizontalLayout.addWidget(self.btnShowAllFiles)
        self.btnSortPy = QtGui.QPushButton(self.tab_2)
        self.btnSortPy.setObjectName(_fromUtf8("btnSortPy"))
        self.horizontalLayout.addWidget(self.btnSortPy)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.txtYWGraph = QtGui.QListWidget(self.tab_2)
        self.txtYWGraph.setObjectName(_fromUtf8("txtYWGraph"))
        self.verticalLayout.addWidget(self.txtYWGraph)
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
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.WatchText = QtGui.QTextBrowser(self.tab_2)
        self.WatchText.setObjectName(_fromUtf8("WatchText"))
        self.verticalLayout_2.addWidget(self.WatchText)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem)
        self.btnRunYW = QtGui.QPushButton(self.tab_2)
        self.btnRunYW.setObjectName(_fromUtf8("btnRunYW"))
        self.horizontalLayout_18.addWidget(self.btnRunYW)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem1)
        self.btnClearWatchText = QtGui.QPushButton(self.tab_2)
        self.btnClearWatchText.setObjectName(_fromUtf8("btnClearWatchText"))
        self.horizontalLayout_18.addWidget(self.btnClearWatchText)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_18)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.tabData.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayout_9.addWidget(self.tabData)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 658, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuYW_Commands = QtGui.QMenu(self.menubar)
        self.menuYW_Commands.setObjectName(_fromUtf8("menuYW_Commands"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuYW_Commands.menuAction())

        self.retranslateUi(MainWindow)
        self.tabData.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_4.setText(_translate("MainWindow", "Files in Current Directory", None))
        self.btnShowAllFiles.setText(_translate("MainWindow", "Show all files", None))
        self.btnSortPy.setText(_translate("MainWindow", "Show .py files", None))
        self.btnYWExtract.setText(_translate("MainWindow", "YW Extract", None))
        self.btnModel.setText(_translate("MainWindow", "YW Model", None))
        self.label.setText(_translate("MainWindow", "Message Box", None))
        self.btnYWGraph.setText(_translate("MainWindow", "YW Graph", None))
        self.label_3.setText(_translate("MainWindow", "Message Box", None))
        self.btnRunYW.setText(_translate("MainWindow", "Help", None))
        self.btnClearWatchText.setText(_translate("MainWindow", "Clear", None))
        self.tabData.setTabText(self.tabData.indexOf(self.tab_2), _translate("MainWindow", "YW Tools", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuYW_Commands.setTitle(_translate("MainWindow", "View", None))

