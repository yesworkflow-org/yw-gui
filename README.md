# yw-gui
Graphical interface for rending graphs produced by YesWorkflow

Overview
--------

The GUI's purpose is to provide users an interactive ability to customize their own scripts as well as view a graphical representation of their script.

Currently the GUI allows the user to view what files are in the current working directory that the main_ui file is located in. From here, the user can indicate a file for a yw command to be run upon. 
The current supported yw commands from the GUI are the graph, extract, and the help (-h) function.

Installation (Windows)
------------

- Python 2.7
- Watchdog
- PyQt

### 1. Check installed version of Python

Ensure that Python 2.7 is installed on your computer. Find the correct version of Python to install at [https://www.python.org/download/releases/2.7/](https://www.python.org/download/releases/2.7/). To make any changes to the GUI, ensure that you have Python installed. Make sure that 'python' 

### 2. Install PyQt Library

PyQt is an library extension to Python that allows developers to create GUI's that are customizable to their own functionality. Ensure that you have PyQt4, the correct version for Yes Workflow. Find instructions for installation and download the libraries at [http://www.riverbankcomputing.com/software/pyqt/download](http://www.riverbankcomputing.com/software/pyqt/download). Follow instructions to install PyQt on the link.

### 3. Include Watchdog library. 

The Watchdog API is an open source library for Python that monitors directories for files specified by the developer. Yes Workflow utilizes Watchdog to carefully watch scripts that are rendered to the GUI for any changes, in which case the rendering of the script will be updated in the GUI. To install Watchdog and download, follow the instructions at [https://github.com/gorakhargosh/watchdog](https://github.com/gorakhargosh/watchdog)

### 4. Install Yes Workflow

Yes Workflow is the tool that yw-gui utilizes to render the scripts into workflow graphs. To install Yes Workflow follow the installation instructions at [https://github.com/yesworkflow-org/yw-prototypes](https://github.com/yesworkflow-org/yw-prototypes)

### 5. Ensure the Yes Workflow jar file is part of your path variables

The GUI references the jar file, yesworkflow-0.2-SNAPSHOT-jar-with-dependencies.jar, as YW_JAR_PATH. Add these to your environment variables on Windows by opening Control Panel, Navigating to System and Security, System, and Advanced system settings. From here open your Environment Variables and add a new variable under the name 'YW_JAR_PATH' and make the Value the path to your jar file. For example, '{Working Directory}/yesworkflow-0.2-SNAPSHOT-jar-with-dependencies.jar'.


Running (Windows supported right now)
-------

### Preparing your scripts

After marking up your scripts with Yes Workflow comments, include the main_ui.py and update_ui.py files in the same working directory as your scripts. Run your scripts using python and then start the GUI by running 'python main_ui.py'. This should bring up a window for the Yes Workflow User Interface.

### Rendering your scripts

Inside of the GUI, click on the button 'YW Graph' and then a file dialog should show up. With properly commented scripts, you can select your scripts to render and then a new tab should be created with the new graph.

### Controlling the Tabs

Inside of the tabs that contain images you can zoom in and out of the images by using 'Ctrl' + '+' or 'Ctrl' + '-'. Click any of the buttons on the left side of the panel to change any of the graph view settings. In addition, if there are any URI labels visible, you can click on them to either open the directory or the files themselves. 

### Editing your scripts

The GUI will detect any changes to python scripts in the current directory. If you go inside of yoru scripts and change the Yes Workflow mark up comments and then save your file, the GUI should detect this and attempt to re-render your script into a workflow graph.