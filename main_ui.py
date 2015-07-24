import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtWebKit import *
from PyQt4.QtSvg import *
from update_ui import Ui_MainWindow
import time, Queue, shlex, logging, subprocess, os, re, shutil, threading
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

files = sorted([f for f in os.listdir('.') if os.path.isfile(f)])

class Watch_Thread(QtCore.QThread):
	updated = QtCore.pyqtSignal(str)
	class MyHandler(PatternMatchingEventHandler):
		patterns = ["*.py"]
		#patterns = []

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
			#print event.src_path, event.event_type
			#event_string = str(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())) + ' : '
			event_string = str(event.src_path) + ' ' + str(event.event_type)
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
		self.watcher_Thread = Watch_Thread(self)
		self.watcher_Thread.updated.connect(self.WatchdogReceiver)
		self.watcher_Thread.start()
		self.ui.btnYWExtract.clicked.connect(self.btnYWExtract)
		self.ui.btnYWGraph.clicked.connect(self.btnYWGraph)
		self.ui.tabData.tabCloseRequested.connect(self.closeTab)
		self.ui.tabData.connect(self.ui.tabData, QtCore.SIGNAL('currentChanged(int)'), self.update_tab_color)
		self.graphCount = dict()
		self.currentGraphs = dict()
		self.initTabKeys()
		self.initNewTabWidgets()

	@QtCore.pyqtSlot(str)
	def update_svg_window(self, input):
		themessage = input.split(' ')
		ywinput = str(themessage[1])
		message = str(themessage[0])
		self.nodedisplay[ywinput].setText(message)
		if '{' in message:
			newmessage = message.split('{')[0]
			if '/' in newmessage:
				newmessage = newmessage.rsplit('/', 1)[0]
				filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', newmessage)
				thepath = os.path.abspath(filename)
				os.startfile(thepath)
				self.nodedisplay[ywinput].setText(filename)
			else:
				filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
				self.nodedisplay[ywinput].setText(filename)
				thepath = os.path.abspath(filename)
				os.startfile(thepath)
		else:
			if '/' in message:
				cwd = os.getcwd()
				print cwd
				cwd += '/' + message
				os.startfile(cwd)
			else:
				thepath = os.path.abspath(message)
				os.startfile(thepath)

	def update_tab_color(self, tab_index):
		self.ui.tabData.tabBar().setTabTextColor(tab_index, QtCore.Qt.black)

	def closeTab(self, index):
		tabName = str(self.ui.tabData.tabText(index))
		tabName = tabName.split('(')
		tabName_temp = tabName[0]
		tabName = tabName[1].split(')')
		count = int(tabName[0])
		self.graphCount[tabName_temp].remove(count)
		self.currentGraphs[tabName_temp].remove(count)
		self.ui.tabData.removeTab(index)

	def initNewTabWidgets(self):
		self.NewTab = dict()
		self.lbl_1 = dict()
		self.graphoptions = dict()
		self.tabProcessView = dict()
		self.tabDataView = dict()
		self.tabCombinedView = dict()
		self.tabShowWorkflowBox = dict()
		self.tabNameLabel = dict()
		self.tabURILabel = dict()
		self.tabShowEdgeLabels = dict()
		self.LR = dict()
		self.RL = dict()
		self.TB = dict()
		self.BT = dict()
		self.portGroup = dict()
		self.portRelax = dict()
		self.portHide = dict()
		self.paraShow = dict()
		self.paraReduce = dict()
		self.paraHide = dict()
		self.titleTop = dict()
		self.titleBottom = dict()
		self.titleHide = dict()
		self.zoomIn = dict()
		self.zoomOut = dict()
		self.zoomNormal = dict()
		self.nodedisplay = dict()

	def initTabKeys(self):
		self.graphCount['YW Tools'] = 1
		self.graphCount['Graph'] = 1

	def btnClearWatchText(self):
		self.ui.WatchText.clear()

	def WatchdogReceiver(self, text):
		received = text.split(' ')
		change = str(received[1])
		changed_file = str(received[0].split("\\")[-1])
		changed_file = re.sub('\.py$', '', changed_file)
		if changed_file in self.graphCount:
			if change == "modified":
				self.tryUpdatingGraphs(changed_file)

	def tryUpdatingGraphs(self, ywinput):
		# ywinput is the name of the file that was changed/modified
		# function is called when a file that is graphed/rendered was modified
		for number in self.graphCount[ywinput]:
			graph = ywinput + '(' + str(number) + ').svg'
			self.update_graph(graph)
			i1 = self.ui.tabData.currentIndex()
			i2 = self.ui.tabData.indexOf(self.NewTab[graph])
			if i1 is not i2:
				self.ui.tabData.tabBar().setTabTextColor(self.ui.tabData.indexOf(self.NewTab[graph]), QtCore.Qt.blue)

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
		ywinput = str(QtGui.QFileDialog.getOpenFileName(self, 'Open file', '.'))
		#if ywinput in files:
		ywcommand.append('extract')
		ywcommand.append(ywinput)
		ywcommand.append('-c')
		ywcommand.append('extract.listfile')
		p = subprocess.Popen(ywcommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		(p_out, p_err) = p.communicate()
		self.ui.txtErrorBox.insertPlainText(p_out)
		"""else:
			error_message = "The file, " + ywinput + " is not located in the current directory"
			self.ui.txtErrorBox.insertPlainText(error_message)"""

	def btnYWGraph(self):
		fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '.')
		yw_fname = fname.split('/')[-1]
		ywcommand = 'java -jar ' + os.environ['YW_JAR_PATH'] + ' graph '
		ywinput = ''
		ywinput = str(yw_fname)
		if ywinput in files:
			ywfilename = ywinput.split('.py')[0]
			ywcommand += ywinput + ' -c graph.dotfile=' + ywfilename + '.gv'
			ywcommand += ' -c graph.view=PROCESS -c graph.datalabel=BOTH -c graph.edgelabels=HIDE'
			ywcommand += ' -c graph.layout=TB -c graph.portlayout=HIDE -c graph.params=REDUCE -c graph.titleposition=HIDE'
			ywcommand += ' -c graph.workflowbox=SHOW'
			ywaftercommand = 'dot -Tsvg ' + ywfilename + '.gv > '
			ywinput = re.sub('\.py$', '', ywinput)
			if ywinput not in self.graphCount:
				self.graphCount[ywinput] = []
				self.graphCount[ywinput].append(1)
				count = 1
				self.currentGraphs[ywinput] = []
				self.watcher_Thread.MyHandler.patterns.append(ywinput)
			else:
				count = self.findNextHigher(ywinput)
				self.graphCount[ywinput].append(count)
			self.currentGraphs[ywinput].append(count)
			ywinput += '('
			ywinput += str(count)
			ywinput += ')'
			ywinput += '.svg'
			os.system(ywcommand)
			ywaftercommand += ywinput
			os.system(ywaftercommand)
			self.makeNewTab(ywcommand, ywinput)
		else:
			error_message = "The file, " + ywinput + " is not located in the current directory"
			self.ui.txtErrorBox.insertPlainText(error_message)

	def findNextHigher(self, ywinput):
		i = 1
		while i in self.graphCount[ywinput]:
			i += 1
		return i

	def modifySVGFile(self, filename):
		filename = str(filename)
		file_w = os.path.abspath(filename)
		file_r = os.path.abspath(filename + '~')
		shutil.move(file_w, file_r)
		destination = open(file_w, "w")
		source = open(file_r, "r")
		for line in source:
			if 'file:' in line:
				newline = line
				arrayline = newline.split('<text ')
				insert = '<text ' + 'onclick="node_displayer.update_svg_window('
				nodename_temp = line.split('file:')
				nodename_temp = nodename_temp[1].split('</text>')[0]
				insert += "'" + nodename_temp
				insert += ' ' + filename + "'"
				insert += ')" '
				newline = insert + arrayline[1]
				destination.write(newline)
			else:
				destination.write(line)
		source.close()
		destination.close()
		temp_file = open(file_w, "r")
		html = temp_file.read()
		return html

	def makeNewTab(self, ywcommand, ywinput):
		# adds a new tab to the tab widget
		self.NewTab[ywinput] = QtGui.QTabWidget()
		self.hlayout_1 = QtGui.QHBoxLayout(self.NewTab[ywinput])
		self.graphoptions[ywinput] = QtGui.QVBoxLayout()
		# add two vertical layouts placed side-by-side horizontally
		self.lbl_2 = QtGui.QLabel('Graph Options')
		self.graphoptions[ywinput].addWidget(self.lbl_2)
		# self.graphoptions[ywinput] are the graph options
		# self.vlayout_1 holds the label that displays the svg rendering
		self.vlayout_1 = QtGui.QVBoxLayout()
		# Add graph options

		### Workflow View
		self.workflowview = QtGui.QGroupBox('Workflow View')
		self.tabProcessView[ywinput] = QtGui.QRadioButton('Process')
		self.tabDataView[ywinput] = QtGui.QRadioButton('Data')
		self.tabCombinedView[ywinput] = QtGui.QRadioButton('Combined')
		self.tabProcessView[ywinput].setChecked(True)
		self.templayout = QtGui.QHBoxLayout()
		self.templayout.addWidget(self.tabProcessView[ywinput])
		self.templayout.addWidget(self.tabDataView[ywinput])
		self.templayout.addWidget(self.tabCombinedView[ywinput])
		self.tabProcessView[ywinput].toggled.connect(lambda: self.update_graph_handler(self.tabProcessView[ywinput].isChecked, ywinput))
		self.tabDataView[ywinput].toggled.connect(lambda: self.update_graph_handler(self.tabDataView[ywinput].isChecked, ywinput))
		self.tabCombinedView[ywinput].toggled.connect(lambda: self.update_graph_handler(self.tabCombinedView[ywinput].isChecked, ywinput))
		self.workflowview.setLayout(self.templayout)
		self.graphoptions[ywinput].addWidget(self.workflowview)

		### Show Workflow Box
		self.workflowbox = QtGui.QGroupBox('Workflow Box')
		self.tabShowWorkflowBox[ywinput] = QtGui.QCheckBox('Show')
		self.tabShowWorkflowBox[ywinput].setChecked(True)
		self.templayout = QtGui.QHBoxLayout()
		self.templayout.addWidget(self.tabShowWorkflowBox[ywinput])
		self.tabShowWorkflowBox[ywinput].toggled.connect(lambda: self.update_graph(ywinput))
		self.workflowbox.setLayout(self.templayout)
		self.graphoptions[ywinput].addWidget(self.workflowbox)

		### Data Labels
		self.datalabel = QtGui.QGroupBox('Data Label')
		self.tabNameLabel[ywinput] = QtGui.QCheckBox('Name')
		self.tabURILabel[ywinput] = QtGui.QCheckBox('URI')
		self.tabNameLabel[ywinput].setChecked(True)
		self.tabURILabel[ywinput].setChecked(True)
		self.templayout = QtGui.QHBoxLayout()
		self.templayout.addWidget(self.tabNameLabel[ywinput])
		self.templayout.addWidget(self.tabURILabel[ywinput])
		self.tabNameLabel[ywinput].toggled.connect(lambda: self.update_graph(ywinput))
		self.tabURILabel[ywinput].toggled.connect(lambda: self.update_graph(ywinput))
		self.datalabel.setLayout(self.templayout)
		self.graphoptions[ywinput].addWidget(self.datalabel)

		### Show Edge Labels
		self.ShowEdgeLabel = QtGui.QGroupBox('Edge Labels')
		self.tabShowEdgeLabels[ywinput] = QtGui.QCheckBox('Show')
		self.tabShowEdgeLabels[ywinput].setChecked(False)
		self.templayout = QtGui.QHBoxLayout()
		self.templayout.addWidget(self.tabShowEdgeLabels[ywinput])
		self.tabShowEdgeLabels[ywinput].toggled.connect(lambda: self.update_graph(ywinput))
		self.ShowEdgeLabel.setLayout(self.templayout)
		self.graphoptions[ywinput].addWidget(self.ShowEdgeLabel)

		### Layout
		self.LayoutBox = QtGui.QGroupBox('Layout')
		self.LR[ywinput] = QtGui.QRadioButton('Left-Right')
		self.RL[ywinput] = QtGui.QRadioButton('Right-Left')
		self.TB[ywinput] = QtGui.QRadioButton('Top-Bottom')
		self.BT[ywinput] = QtGui.QRadioButton('Bottom-Top')
		self.TB[ywinput].setChecked(True)
		self.templayout = QtGui.QHBoxLayout()
		self.templayout.addWidget(self.LR[ywinput])
		self.templayout.addWidget(self.RL[ywinput])
		self.templayout.addWidget(self.TB[ywinput])
		self.templayout.addWidget(self.BT[ywinput])
		self.LR[ywinput].toggled.connect(lambda: self.update_graph_handler(self.LR[ywinput].isChecked, ywinput))
		self.RL[ywinput].toggled.connect(lambda: self.update_graph_handler(self.RL[ywinput].isChecked, ywinput))
		self.TB[ywinput].toggled.connect(lambda: self.update_graph_handler(self.TB[ywinput].isChecked, ywinput))
		self.BT[ywinput].toggled.connect(lambda: self.update_graph_handler(self.BT[ywinput].isChecked, ywinput))
		self.LayoutBox.setLayout(self.templayout)
		self.graphoptions[ywinput].addWidget(self.LayoutBox)

		### Port Layout
		self.PortLayoutBox = QtGui.QGroupBox('Port Layout')
		self.portGroup[ywinput] = QtGui.QRadioButton('Group')
		self.portRelax[ywinput] = QtGui.QRadioButton('Relax')
		self.portHide[ywinput] = QtGui.QRadioButton('Hide')
		self.portHide[ywinput].setChecked(True)
		self.templayout = QtGui.QHBoxLayout()
		self.templayout.addWidget(self.portGroup[ywinput])
		self.templayout.addWidget(self.portRelax[ywinput])
		self.templayout.addWidget(self.portHide[ywinput])
		self.portGroup[ywinput].toggled.connect(lambda: self.update_graph_handler(self.portGroup[ywinput].isChecked, ywinput))
		self.portRelax[ywinput].toggled.connect(lambda: self.update_graph_handler(self.portRelax[ywinput].isChecked, ywinput))
		self.portHide[ywinput].toggled.connect(lambda: self.update_graph_handler(self.portHide[ywinput].isChecked, ywinput))
		self.PortLayoutBox.setLayout(self.templayout)
		self.graphoptions[ywinput].addWidget(self.PortLayoutBox)

		### Parameters
		self.ParameterBox = QtGui.QGroupBox('Parameters')
		self.paraShow[ywinput] = QtGui.QRadioButton('Show')
		self.paraReduce[ywinput] = QtGui.QRadioButton('Reduce')
		self.paraHide[ywinput] = QtGui.QRadioButton('Hide')
		self.paraReduce[ywinput].setChecked(True)
		self.templayout = QtGui.QHBoxLayout()
		self.templayout.addWidget(self.paraShow[ywinput])
		self.templayout.addWidget(self.paraReduce[ywinput])
		self.templayout.addWidget(self.paraHide[ywinput])
		self.paraShow[ywinput].toggled.connect(lambda: self.update_graph_handler(self.paraShow[ywinput].isChecked, ywinput))
		self.paraReduce[ywinput].toggled.connect(lambda: self.update_graph_handler(self.paraReduce[ywinput].isChecked, ywinput))
		self.paraHide[ywinput].toggled.connect(lambda: self.update_graph_handler(self.paraHide[ywinput].isChecked, ywinput))
		self.ParameterBox.setLayout(self.templayout)
		self.graphoptions[ywinput].addWidget(self.ParameterBox)

		### Graph Title Position
		self.titleBox = QtGui.QGroupBox('Title Position')
		self.titleTop[ywinput] = QtGui.QRadioButton('Top')
		self.titleBottom[ywinput] = QtGui.QRadioButton('Bottom')
		self.titleHide[ywinput] = QtGui.QRadioButton('Hide')
		self.titleHide[ywinput].setChecked(True)
		self.templayout = QtGui.QHBoxLayout()
		self.templayout.addWidget(self.titleTop[ywinput])
		self.templayout.addWidget(self.titleBottom[ywinput])
		self.templayout.addWidget(self.titleHide[ywinput])
		self.titleTop[ywinput].toggled.connect(lambda: self.update_graph_handler(self.titleTop[ywinput].isChecked, ywinput))
		self.titleBottom[ywinput].toggled.connect(lambda: self.update_graph_handler(self.titleBottom[ywinput].isChecked, ywinput))
		self.titleHide[ywinput].toggled.connect(lambda: self.update_graph_handler(self.titleHide[ywinput].isChecked, ywinput))
		self.titleBox.setLayout(self.templayout)
		self.graphoptions[ywinput].addWidget(self.titleBox)

		#Node that is clicked
		self.nodedisplay[ywinput] = QtGui.QLabel('')
		self.graphoptions[ywinput].addWidget(self.nodedisplay[ywinput])

		# add widgets to the layouts
		self.scrollArea = QtGui.QScrollArea()
		self.scrollArea.setGeometry(QtCore.QRect(10, 10, 201, 121))
		self.scrollArea.setWidgetResizable(True)
		self.scrollAreaWidgetContents = QtGui.QWidget()
		self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 199, 119))
		self.lbl_1[ywinput] = QWebView(self.scrollAreaWidgetContents)
		
		# Zoom Functionality for the webview
		self.lbl_1[ywinput].zoomIn = QtGui.QShortcut(QtGui.QKeySequence("Ctrl+="), self.lbl_1[ywinput], activated = lambda: self.lbl_1[ywinput].setZoomFactor(self.lbl_1[ywinput].zoomFactor()+.05))
		self.zoomOut = QtGui.QShortcut(QtGui.QKeySequence("Ctrl+-"), self.lbl_1[ywinput], activated = lambda: self.lbl_1[ywinput].setZoomFactor(self.lbl_1[ywinput].zoomFactor()-.05))
		self.zoomNormal = QtGui.QShortcut(QtGui.QKeySequence("Ctrl+0"), self.lbl_1[ywinput], activated = lambda: self.lbl_1[ywinput].setZoomFactor(0.8))

		self.scrollArea.setWidget(self.lbl_1[ywinput])
		self.vlayout_1.addWidget(self.scrollArea)
		self.hlayout_1.addLayout(self.graphoptions[ywinput])
		self.hlayout_1.addLayout(self.vlayout_1)
		count = self.ui.tabData.count()
		self.ui.tabData.addTab(self.NewTab[ywinput], ywinput)
		self.ui.tabData.tabBar().setTabTextColor(count, QtCore.Qt.red)
		path = "file:///"
		path += os.path.abspath(ywinput)
		path = QtCore.QString(path)
		html_code = self.modifySVGFile(ywinput)
		self.lbl_1[ywinput].setHtml(html_code)
		frame = self.lbl_1[ywinput].page().mainFrame()
		frame.addToJavaScriptWindowObject('node_displayer', self)

	def update_graph_handler(self, enabled, ywinput):
		if enabled:
			self.update_graph(ywinput)

	def update_graph(self, ywinput):
		ywcommand = 'java -jar ' + os.environ['YW_JAR_PATH'] + ' graph'
		raw_ywinput = ywinput
		ywfilename = ywinput.split('(')[0]
		ywinput = ywinput.split('(')[0]
		ywinput += '.py'
		ywextension = self.retrieveArgs(raw_ywinput)
		ywcommand += ywextension
		ywcommand += ' ' + ywinput + ' -c graph.dotfile=' + ywfilename + '.gv'
		ywinput = re.sub('\.py$', '', ywinput)
		ywinput += str(self.ui.tabData.currentIndex())
		ywinput += '.svg'
		os.system(ywcommand)
		ywaftercommand = 'dot -Tsvg ' + ywfilename + '.gv > ' + raw_ywinput
		os.system(ywaftercommand)
		html_code = self.modifySVGFile(raw_ywinput)
		path = "file:///"
		path += os.path.abspath(raw_ywinput)
		self.lbl_1[raw_ywinput].setHtml(html_code)
		frame = self.lbl_1[raw_ywinput].page().mainFrame()
		frame.addToJavaScriptWindowObject('node_displayer', self)

	def retrieveArgs(self, ywinput):
		returned = ''
		if self.tabProcessView[ywinput].isChecked():
			returned += ' -c graph.view=PROCESS'
		elif self.tabDataView[ywinput].isChecked():
			returned += ' -c graph.view=DATA'
		elif self.tabCombinedView[ywinput].isChecked():
			returned += ' -c graph.view=COMBINED'
		if not self.tabShowWorkflowBox[ywinput].isChecked():
			returned += ' -c graph.workflowbox=HIDE'
		if self.tabNameLabel[ywinput].isChecked():
			if self.tabURILabel[ywinput].isChecked():
				returned += ' -c graph.datalabel=BOTH'
			else:
				returned += ' -c graph.datalabel=NAME'
		elif self.tabURILabel[ywinput].isChecked():
			returned += ' -c graph.datalabel=URI'
		if not self.tabShowEdgeLabels[ywinput].isChecked():
			returned += ' -c graph.edgelabels=HIDE'
		if self.LR[ywinput].isChecked():
			returned += ' -c graph.layout=LR'
		elif self.RL[ywinput].isChecked():
			returned += ' -c graph.layout=RL'
		elif self.TB[ywinput].isChecked():
			returned += ' -c graph.layout=TB'
		elif self.BT[ywinput].isChecked():
			returned += ' -c graph.layout=BT'
		if self.portGroup[ywinput].isChecked():
			returned += ' -c graph.portlayout=GROUP'
		elif self.portRelax[ywinput].isChecked():
			returned += ' -c graph.portlayout=RELAX'
		elif self.portHide[ywinput].isChecked():
			returned += ' -c graph.portlayout=HIDE'
		if self.paraShow[ywinput].isChecked():
			returned += ' -c graph.params=SHOW'
		elif self.paraReduce[ywinput].isChecked():
			returned += ' -c graph.params=REDUCE'
		elif self.paraHide[ywinput].isChecked():
			returned += ' -c graph.params=HIDE'
		if self.titleTop[ywinput].isChecked():
			returned += ' -c graph.titleposition=TOP'
		elif self.titleBottom[ywinput].isChecked():
			returned += ' -c graph.titleposition=BOTTOM'
		elif self.titleHide[ywinput].isChecked():
			returned += ' -c graph.titleposition=HIDE'
		returned += ' -c graph.dotfile=' + ywinput
		return returned


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = Main()
	window.show()
	sys.exit(app.exec_())