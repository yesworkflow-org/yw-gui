import sys
from PyQt4 import QtGui, QtCore
from update_ui import Ui_MainWindow
import time
import shlex
import logging
import subprocess
import os
import re
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import threading

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

files = sorted([f for f in os.listdir('.') if os.path.isfile(f)])

"""def fileWatcher():
	logging.basicConfig(level=logging.INFO,
						format='%(asctime)s - %(message)s',
						datefmt='%Y-%m-%d %H:%M:%S')
	#path = sys.argv[1] if len(sys.argv) > 1 else '.'
	path = '.'
	event_handler = LoggingEventHandler()
	observer = Observer()
	observer.schedule(event_handler, path, recursive=True)
	observer.start()
	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		observer.stop()
	observer.daemon = True
	observer.join()"""

class Main(QtGui.QMainWindow):

	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.writefiles()
		self.ui.btnRunYW.clicked.connect(self.btnStartYW)
		self.ui.btnYWExtract.clicked.connect(self.btnYWExtract)
		self.ui.btnYWGraph.clicked.connect(self.btnYWGraph)
		self.ui.btnSortPy.clicked.connect(self.btnSortPy)
		self.ui.btnShowAllFiles.clicked.connect(self.btnShowAllFiles)
		self.test()
		self.dirWatcher=threading.Thread(target=self.watchdog)
		self.dirWatcher.daemon = True
		self.dirWatcher.start()
		self.ui.tabData.tabCloseRequested.connect(self.ui.tabData.removeTab)

	def watchdog(self): # function does not work properly
		#watch = subprocess.Popen('python monitor.py', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		watch = subprocess.Popen('python monitor.py')
		"""while True:
			line = watch.stdout.readline()
			if not line:
				continue
			else:
				print line
				self.ui.txtWatch.insertPlainText(line)"""

	def test(self):
		test_command = 'dir'
		p = subprocess.check_output(test_command, shell=True)
		self.ui.txtOutput.insertPlainText(p)
		print p


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
		ywcommand = ['java', '-jar', 'yesworkflow-jar.jar', '-h']
		p = subprocess.Popen(ywcommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		(p_err, p_out) = p.communicate()
		self.ui.WatchText.insertPlainText(p_out)

	def btnYWExtract(self):
		self.ui.txtErrorBox.clear()
		ywcommand = 'java -jar ' + os.environ['YW_JAR_PATH'] + ' extract'
		ywinput = str(self.ui.txtYWGraph.currentItem().text())
		if ywinput in files:
			ywcommand += ' ' + ywinput + ' -c extract.listfile'
			os.system(ywcommand)
		else:
			error_message = "The file, " + ywinput + " is not located in the current directory"
			self.ui.txtErrorBox.insertPlainText(error_message)

	def writefiles(self):
		for f in files:
			self.ui.txtFiles.insertPlainText(f + '\n')
			"""item = QListWidgetItem(f)
												item.setCheckable(True)
												self.ui.txtYWGraph.addItem(item)"""
			self.ui.txtYWGraph.addItem(f)

	def btnYWGraph(self):
		self.ui.txtErrorBox.clear()
		ywcommand = 'java -jar ' + os.environ['YW_JAR_PATH'] + ' graph '
		ywinput = ''
		if self.ui.txtYWGraph.currentItem():
			ywinput = str(self.ui.txtYWGraph.currentItem().text())
		print ywinput
		if ywinput in files:
			ywcommand += ywinput + ' | dot -Tsvg -o '
			ywinput = re.sub('\.py$', '', ywinput)
			ywinput += '.svg'
			ywcommand += ywinput
			os.system(ywcommand)
			self.NewTab = QtGui.QWidget()
			self.lbl_1 = QtGui.QLabel('')
			self.layout = QtGui.QVBoxLayout(self.NewTab)
			self.layout.addWidget(self.lbl_1)
			self.ui.tabData.addTab(self.NewTab, ywinput)
			pixmap = QtGui.QPixmap(ywinput)
			self.lbl_1.setPixmap(pixmap)
		else:
			error_message = "The file, " + ywinput + " is not located in the current directory"
			self.ui.txtErrorBox.insertPlainText(error_message)

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = Main()
	window.show()
	sys.exit(app.exec_())
	