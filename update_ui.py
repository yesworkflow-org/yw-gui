# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_ui.ui'
#
# Created: Fri Jun 05 13:42:14 2015
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
        MainWindow.resize(830, 612)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.TabWindow = QtGui.QTabWidget(self.centralwidget)
        self.TabWindow.setObjectName(_fromUtf8("TabWindow"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.WatchText = QtGui.QTextBrowser(self.tab)
        self.WatchText.setObjectName(_fromUtf8("WatchText"))
        self.horizontalLayout_4.addWidget(self.WatchText)
        self.btnRunYW = QtGui.QPushButton(self.tab)
        self.btnRunYW.setObjectName(_fromUtf8("btnRunYW"))
        self.horizontalLayout_4.addWidget(self.btnRunYW)
        self.TabWindow.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.btnSortPy = QtGui.QPushButton(self.tab_2)
        self.btnSortPy.setObjectName(_fromUtf8("btnSortPy"))
        self.verticalLayout.addWidget(self.btnSortPy)
        self.btnShowAllFiles = QtGui.QPushButton(self.tab_2)
        self.btnShowAllFiles.setObjectName(_fromUtf8("btnShowAllFiles"))
        self.verticalLayout.addWidget(self.btnShowAllFiles)
        self.txtYWGraph = QtGui.QListWidget(self.tab_2)
        self.txtYWGraph.setObjectName(_fromUtf8("txtYWGraph"))
        self.verticalLayout.addWidget(self.txtYWGraph)
        self.btnYWExtract = QtGui.QPushButton(self.tab_2)
        self.btnYWExtract.setObjectName(_fromUtf8("btnYWExtract"))
        self.verticalLayout.addWidget(self.btnYWExtract)
        self.btnYWGraph = QtGui.QPushButton(self.tab_2)
        self.btnYWGraph.setObjectName(_fromUtf8("btnYWGraph"))
        self.verticalLayout.addWidget(self.btnYWGraph)
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.txtErrorBox = QtGui.QTextBrowser(self.tab_2)
        self.txtErrorBox.setObjectName(_fromUtf8("txtErrorBox"))
        self.verticalLayout.addWidget(self.txtErrorBox)
        self.TabWindow.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.TabWindow.addTab(self.tab_3, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.TabWindow)
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 346, 551))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.txtFiles = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.txtFiles.setObjectName(_fromUtf8("txtFiles"))
        self.verticalLayout_2.addWidget(self.txtFiles)
        self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 830, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dock1 = QtGui.QDockWidget(MainWindow)
        self.dock1.setObjectName(_fromUtf8("dock1"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.ClearButton = QtGui.QPushButton(self.dockWidgetContents)
        self.ClearButton.setObjectName(_fromUtf8("ClearButton"))
        self.horizontalLayout_2.addWidget(self.ClearButton)
        self.dock1.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dock1)
        self.dock2 = QtGui.QDockWidget(MainWindow)
        self.dock2.setObjectName(_fromUtf8("dock2"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.dockWidgetContents_2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.WatchButton = QtGui.QPushButton(self.dockWidgetContents_2)
        self.WatchButton.setObjectName(_fromUtf8("WatchButton"))
        self.horizontalLayout_3.addWidget(self.WatchButton)
        self.dock2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dock2)

        self.retranslateUi(MainWindow)
        self.TabWindow.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btnRunYW.setText(_translate("MainWindow", "Run YW", None))
        self.TabWindow.setTabText(self.TabWindow.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.label_4.setText(_translate("MainWindow", "Files in Current Directory", None))
        self.btnSortPy.setText(_translate("MainWindow", "Show .py files", None))
        self.btnShowAllFiles.setText(_translate("MainWindow", "Show all files", None))
        self.btnYWExtract.setText(_translate("MainWindow", "YW Extract", None))
        self.btnYWGraph.setText(_translate("MainWindow", "YW Graph", None))
        self.label.setText(_translate("MainWindow", "Error Message Box:", None))
        self.TabWindow.setTabText(self.TabWindow.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))
        self.TabWindow.setTabText(self.TabWindow.indexOf(self.tab_3), _translate("MainWindow", "Page", None))
        self.label_2.setText(_translate("MainWindow", "Files in Current Directory", None))
        self.ClearButton.setText(_translate("MainWindow", "PushButton", None))
        self.WatchButton.setText(_translate("MainWindow", "Watch", None))

