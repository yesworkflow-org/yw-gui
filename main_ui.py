import sys
from PyQt4 import QtGui, QtCore
from update_ui import Ui_MainWindow
import time, Queue
import shlex
import logging
import subprocess
import os
import re
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import threading

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

messageQueue = Queue.Queue()

files = sorted([f for f in os.listdir('.') if os.path.isfile(f)])

class Watch_Thread(QtCore.QThread):
	updated = QtCore.pyqtSignal(str)
	class MyHandler(PatternMatchingEventHandler):
		patterns = ["*.py", "*.png", "*.svg"]

		def __init__(self, eventThread, patterns=None, ignore_patterns=None,
	             ignore_directories=False, case_sensitive=False):
			super(PatternMatchingEventHandler, self).__init__()
			self.eventThread = eventThread
			self._patterns = patterns
			self._ignore_patterns = ignore_patterns
			self._ignore_directories = ignore_directories
			self._case_sensitive = case_sensitive

		def process(self, event):
			"""
			event.event_type
				'modified' | 'created' | 'moved' | 'deleted'
			event.is_directory
				True | False
			event.src_path
				path/to/observed/file
			"""
			# the file will be processed here
			#print event.src_path, event.event_type #print now for debug
			event_string = str(event.src_path) + ' ' + str(event.event_type) + ' ' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())) + '\n'
			#print event_string
			self.eventThread.updated.emit(event_string)			

		def on_modified(self, event):
			self.process(event)

		def on_created(self, event):
			self.process(event)

	def run(self):
		observer = Observer()
		observer.schedule(self.MyHandler(self), path='.')
		observer.start()
		observer.join()

class Main(QtGui.QMainWindow):

	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.initfiles()
		self.watcher_Thread = Watch_Thread(self)
		self.watcher_Thread.updated.connect(self.update_WatchText)
		self.watcher_Thread.start()
		self.ui.btnRunYW.clicked.connect(self.btnStartYW)
		self.ui.btnYWExtract.clicked.connect(self.btnYWExtract)
		self.ui.btnYWGraph.clicked.connect(self.btnYWGraph)
		self.ui.btnSortPy.clicked.connect(self.btnSortPy)
		self.ui.btnShowAllFiles.clicked.connect(self.btnShowAllFiles)
		self.ui.btnSortPy_2.clicked.connect(self.btnSortPy_2)
		self.ui.btnShowAllFiles_2.clicked.connect(self.btnShowAllFiles_2)
		self.ui.btnClearWatchText.clicked.connect(self.btnClearWatchText)
		self.ui.tabData.tabCloseRequested.connect(self.ui.tabData.removeTab)
		#self.ui.tabData.tabBar.setTabsClosable(False)

	def initfiles(self):
		for f in files:
			if ".py" in f:
				self.ui.txtYWGraph_2.addItem(f)

	def btnClearWatchText(self):
		self.ui.WatchText.clear()

	def update_WatchText(self, text):
		self.ui.WatchText.insertPlainText(text)

	def btnSortPy_2(self):
		self.ui.txtYWGraph_2.clear()
		for f in files:
			if ".py" in f:
				self.ui.txtYWGraph_2.addItem(f)

	def btnShowAllFiles_2(self):
		self.ui.txtYWGraph_2.clear()
		for f in files:
			self.ui.txtYWGraph_2.addItem(f)

	def btnSortPy(self):
		self.ui.txtYWGraph.clear()
		for f in files:
			if ".py" in f:
				self.ui.txtYWGraph.addItem(f)

	def btnShowAllFiles(self):
		self.ui.txtYWGraph.clear()
		for f in files:
			self.ui.txtYWGraph.addItem(f)

	def dataWatcher(self):
		p = subprocess.Popen(command, )

	def btnStartYW(self):
		ywcommand = ['java', '-jar', 'yesworkflow-0.2-SNAPSHOT-jar-with-dependencies.jar', '-h']
		p = subprocess.Popen(ywcommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		(p_err, p_out) = p.communicate()
		self.ui.WatchText.insertPlainText(p_out)

	def btnYWExtract(self):
		self.ui.txtErrorBox.clear()
		ywcommand = ['java', '-jar', 'yesworkflow-0.2-SNAPSHOT-jar-with-dependencies.jar']
		ywinput = str(self.ui.txtYWGraph.currentItem().text())
		if ywinput in files:
			ywcommand.append('extract')
			ywcommand.append(ywinput)
			ywcommand.append('-c')
			ywcommand.append('extract.listfile')
			#print ywcommand
			p = subprocess.Popen(ywcommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
			(p_out, p_err) = p.communicate()
			self.ui.txtErrorBox.insertPlainText(p_out)
		else:
			error_message = "The file, " + ywinput + " is not located in the current directory"
			self.ui.txtErrorBox.insertPlainText(error_message)

	def checkBoxes(self, pyfile):
		returned = ''
		if self.ui.btnProcessView.isChecked():
			returned += ' -c ' + 'graph.view=PROCESS'
		elif self.ui.btnDataView.isChecked():
			returned += ' -c ' + 'graph.view=DATA'
		elif self.ui.btnCombinedView.isChecked():
			returned += ' -c ' + 'graph.view=COMBINED'
		if self.ui.chkNameLabel.isChecked():
			if self.ui.chkURILabel.isChecked():
				returned += ' -c ' + 'graph.datalabel=BOTH'
			else:
				returned += ' -c ' + 'graph.datalabel=NAME'
		elif self.ui.chkURILabel.isChecked():
			returned += ' -c graph.datalabel=URI'
		if self.ui.chkShowComments.isChecked():
			returned += ' -c graph.dotcomments=SHOW'
		if self.ui.btnLRLayout.isChecked():
			returned += ' -c graph.layout=LR'
		elif self.ui.btnRLLayout.isChecked():
			returned += ' -c graph.layout=RL'
		elif self.ui.btnTBLayout.isChecked():
			returned += ' -c graph.layout=TB'
		elif self.ui.btnBTLayout.isChecked():
			returned += ' -c graph.layout=BT'
		if self.ui.btnParamHide.isChecked():
			returned += ' -c graph.params=HIDE'
		elif self.ui.btnParamShow.isChecked():
			returned += ' -c graph.params=SHOW'
		elif self.ui.btnParamReduce.isChecked():
			returned += ' -c graph.params=REDUCE'
		if not self.ui.chkLabelShow.isChecked():
			returned += ' -c graph.edgelabels=HIDE'
		if not self.ui.chkWorkflowShow.isChecked():
			returned += ' -c graph.workflowbox=HIDE'
		if self.ui.btnPortGroup.isChecked():
			returned += ' -c graph.portlayout=GROUP'
		elif self.ui.btnPortHide.isChecked():
			returned += ' -c graph.portlayout=HIDE'
		elif self.ui.btnPortRelax.isChecked():
			returned += ' -c graph.portlayout=RELAX'
		if self.ui.btnRename.isChecked():
			if self.ui.btnRename.text():
				returned += ' -c graph.title='
				returned += pyfile
		if self.ui.btnTopTitle.isChecked():
			returned += ' -c graph.titleposition=TOP'
		elif self.ui.btnBottomTitle.isChecked():
			returned += ' -c graph.titleposition=BOTTOM'
		elif self.ui.btnHideTitle.isChecked():
			returned += ' -c graph.titleposition=HIDE'
		return returned

	def btnYWGraph(self):
		self.ui.txtErrorBox.clear()
		ywcommand = 'java -jar ' + os.environ['YW_JAR_PATH'] + ' graph'
		ywinput = ''
		if self.ui.txtYWGraph_2.currentItem():
			ywinput = str(self.ui.txtYWGraph_2.currentItem().text())
		if ywinput in files:
			ywextension = self.checkBoxes(ywinput)
			if self.ui.btnExport.isChecked():
				if not self.ui.txtExportDOT.text():
					filename = re.sub('\.py$', '', ywinput)
					filename += '.gv'
					returned += ' -c graph.dotfile=' + filename
				else:
					filename = str(self.ui.txtExportDOT.text())
					returned += ' -c graph.dotfile=' + filename
					returned += '.gv'
			ywcommand += ywextension + ' '
			ywcommand += ywinput + ' | dot -Tsvg -o '
			ywinput = re.sub('\.py$', '', ywinput)
			ywinput += '(' + str(self.ui.tabData.count()-1) + ')'
			ywinput += '.svg'
			ywcommand += ywinput
			#print ywcommand
			os.system(ywcommand)
			self.makeNewTab(ywcommand, ywinput)
		else:
			error_message = "The file, " + ywinput + " is not located in the current directory"
			self.ui.txtErrorBox.insertPlainText(error_message)

	def makeNewTab(self, ywcommand, ywinput):
		# adds a new tab to the tab widget
		self.NewTab = QtGui.QWidget()
		self.lbl_1 = QtGui.QLabel('')
		self.hlayout_1 = QtGui.QHBoxLayout(self.NewTab)
		self.graphoptions = QtGui.QVBoxLayout()
		# add two vertical layouts placed side-by-side horizontally
		self.lbl_2 = QtGui.QLabel('Graph Options')
		self.graphoptions.addWidget(self.lbl_2)
		# self.graphoptions are the graph options
		# self.vlayout_1 holds the label that displays the svg rendering
		self.vlayout_1 = QtGui.QVBoxLayout()
		# Add graph options

		### Workflow View
		self.workflowview = QtGui.QGroupBox('Workflow View')
		self.tabProcessView = QtGui.QRadioButton('Process')
		self.tabDataView = QtGui.QRadioButton('Data')
		self.tabCombinedView = QtGui.QRadioButton('Combined')
		self.templayout = QtGui.QHBoxLayout()
		self.templayout.addWidget(self.tabProcessView)
		self.templayout.addWidget(self.tabDataView)
		self.templayout.addWidget(self.tabCombinedView)
		self.tabProcessView.toggled.connect(self.update_graph_handler)
		self.tabDataView.toggled.connect(self.update_graph_handler)
		self.tabCombinedView.toggled.connect(self.update_graph_handler)
		self.workflowview.setLayout(self.templayout)
		self.graphoptions.addWidget(self.workflowview)

		### Show Workflow Box
		self.workflowbox = QtGui.QGroupBox('Workflow Box')
		self.tabShowWorkflowBox = QtGui.QCheckBox('Show')
		self.templayout = QtGui.QHBoxLayout()
		self.templayout.addWidget(self.tabShowWorkflowBox)
		self.tabShowWorkflowBox.toggled.connect(self.update_graph)
		self.workflowbox.setLayout(self.templayout)
		self.graphoptions.addWidget(self.workflowbox)

		### Data Labels
		self.datalabel = QtGui.QGroupBox('Data Label')
		self.tabNameLabel = QtGui.QCheckBox('Name')
		self.tabURILabel = QtGui.QCheckBox('URI')
		self.templayout = QtGui.QHBoxLayout()
		self.templayout.addWidget(self.tabNameLabel)
		self.templayout.addWidget(self.tabURILabel)
		self.tabNameLabel.toggled.connect(self.update_graph)
		self.tabURILabel.toggled.connect(self.update_graph)
		self.datalabel.setLayout(self.templayout)
		self.graphoptions.addWidget(self.datalabel)

		### Show Edge Labels
		self.ShowEdgeLabel = QtGui.QGroupBox('Edge Labels')
		self.tabShowEdgeLabels = QtGui.QCheckBox('Show')
		self.templayout = QtGui.QHBoxLayout()
		self.templayout.addWidget(self.tabShowEdgeLabels)
		self.tabShowEdgeLabels.toggled.connect(self.update_graph)
		self.ShowEdgeLabel.setLayout(self.templayout)
		self.graphoptions.addWidget(self.ShowEdgeLabel)

		### Layout
		self.LayoutBox = QtGui.QGroupBox('Layout')
		self.LR = QtGui.QRadioButton('Left-Right')
		self.RL = QtGui.QRadioButton('Right-Left')
		self.TB = QtGui.QRadioButton('Top-Bottom')
		self.BT = QtGui.QRadioButton('Bottom-Top')
		self.templayout = QtGui.QHBoxLayout()
		self.templayout.addWidget(self.LR)
		self.templayout.addWidget(self.RL)
		self.templayout.addWidget(self.TB)
		self.templayout.addWidget(self.BT)
		self.LR.toggled.connect(self.update_graph_handler)
		self.RL.toggled.connect(self.update_graph_handler)
		self.TB.toggled.connect(self.update_graph_handler)
		self.BT.toggled.connect(self.update_graph_handler)
		self.LayoutBox.setLayout(self.templayout)
		self.graphoptions.addWidget(self.LayoutBox)

		### Port Layout
		self.PortLayoutBox = QtGui.QGroupBox('Port Layout')
		self.portGroup = QtGui.QRadioButton('Group')
		self.portRelax = QtGui.QRadioButton('Relax')
		self.portHide = QtGui.QRadioButton('Hide')
		self.templayout = QtGui.QHBoxLayout()
		self.templayout.addWidget(self.portGroup)
		self.templayout.addWidget(self.portRelax)
		self.templayout.addWidget(self.portHide)
		self.portGroup.toggled.connect(self.update_graph_handler)
		self.portRelax.toggled.connect(self.update_graph_handler)
		self.portHide.toggled.connect(self.update_graph_handler)
		self.PortLayoutBox.setLayout(self.templayout)
		self.graphoptions.addWidget(self.PortLayoutBox)

		### Parameters
		self.ParameterBox = QtGui.QGroupBox('Parameters')
		self.paraShow = QtGui.QRadioButton('Show')
		self.paraReduce = QtGui.QRadioButton('Reduce')
		self.paraHide = QtGui.QRadioButton('Hide')
		self.templayout = QtGui.QHBoxLayout()
		self.templayout.addWidget(self.paraShow)
		self.templayout.addWidget(self.paraReduce)
		self.templayout.addWidget(self.paraHide)
		self.paraShow.toggled.connect(self.update_graph_handler)
		self.paraReduce.toggled.connect(self.update_graph_handler)
		self.paraHide.toggled.connect(self.update_graph_handler)
		self.ParameterBox.setLayout(self.templayout)
		self.graphoptions.addWidget(self.ParameterBox)

		### Graph Title Position
		self.titleBox = QtGui.QGroupBox('Title Position')
		self.titleTop = QtGui.QRadioButton('Top')
		self.titleBottom = QtGui.QRadioButton('Bottom')
		self.titleHide = QtGui.QRadioButton('Hide')
		self.templayout = QtGui.QHBoxLayout()
		self.templayout.addWidget(self.titleTop)
		self.templayout.addWidget(self.titleBottom)
		self.templayout.addWidget(self.titleHide)
		self.titleTop.toggled.connect(self.update_graph_handler)
		self.titleBottom.toggled.connect(self.update_graph_handler)
		self.titleHide.toggled.connect(self.update_graph_handler)
		self.titleBox.setLayout(self.templayout)
		self.graphoptions.addWidget(self.titleBox)

		# add widgets to the layouts
		self.vlayout_1.addWidget(self.lbl_1)
		self.hlayout_1.addLayout(self.graphoptions)
		self.hlayout_1.addLayout(self.vlayout_1)
		self.ui.tabData.addTab(self.NewTab, ywinput)
		pixmap = QtGui.QPixmap(ywinput)
		self.lbl_1.setPixmap(pixmap)

	def update_graph_handler(self, enabled):
		if enabled:
			self.update_graph()

	def update_graph(self):
		#print "graphing"
		ywcommand = 'java -jar ' + os.environ['YW_JAR_PATH'] + ' graph'
		i = self.ui.tabData.currentIndex()
		ywinput = str(self.ui.tabData.tabText(i))
		ywinput = ywinput.split('(')[0]
		#ywinput = re.sub('\.svg$', '', ywinput)
		ywinput += '.py'
		print ywinput
		ywcommand += ' ' + ywinput + ' | dot -Tsvg -o '
		ywinput = re.sub('\.py$', '', ywinput)
		ywinput += str(self.ui.tabData.currentIndex())
		ywinput += '.svg'
		ywcommand += ywinput
		os.system(ywcommand)
		pixmap = QtGui.QPixmap(ywinput)
		self.lbl_1.setPixmap(pixmap)

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	"""dirWatcher=threading.Thread(target=watchdog)
	dirWatcher.daemon = True
	dirWatcher.start()"""
	window = Main()
	window.show()
	sys.exit(app.exec_())