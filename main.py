# This Module load all sources in project 
# This file Also Content The MainWindow call's

import sys 
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QGridLayout,QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMenu
class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        main_grid  = QGridLayout()
        #Load Ui File 
        uic.loadUi('UIViews/main.ui', self)
        # Set The Name Of the Main Windows
        self.setWindowTitle("BitcoinTracker")
        
        
        # main_grid.addWidget(ribbon, 0 , 0)
   
        self.centralwidget.setLayout(main_grid)
        self._createMenuBar()
        # Display Main Windows 
        self.show()
    def _createMenuBar(self):
        menuBar = self.menuBar()
        # Creating menus using a QMenu object
        fileMenu = QMenu("&File", self)
        menuBar.addMenu(fileMenu)
        # Creating menus using a title
        editMenu = menuBar.addMenu("&DashBord")
        helpMenu = menuBar.addMenu("&Aide")
        helpMenu = menuBar.addMenu("&Apropos")
app = QApplication(sys.argv)
d = Main()
sys.exit(app.exec_())
