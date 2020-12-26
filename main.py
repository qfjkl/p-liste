# This Module load all sources in project 
# This file Also Content The MainWindow call's

import sys 
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QGridLayout,QLabel,QAction
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMenu, QToolBar
from Ressources import qrc_resources
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
        self._createActions()
        self._createMenuBar()
        self._createToolBars()
        # Display Main Windows 
        self.show()
    def _createMenuBar(self):
        menuBar = self.menuBar()
        # Creating menus using a QMenu object
        fileMenu = QMenu("&Fichier", self)
        menuBar.addMenu(fileMenu)
        fileNewMenu  = fileMenu.addMenu("Nouveau")
        fileNewMenu.addAction(self.newAccountAction)
        fileNewMenu.addAction(self.newWalletAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.quitAction)
      
        
        # helpMenu  = menuBar.addMenu(QIcon(":menu-dashboard.svg"), "&Dashboard")
        dashMenu = menuBar.addMenu("&Dashboard")
        dashMenu.addAction(self.dashMineAction)
        dashMenu.addAction(self.dashWalletAction)
        walletMenu = menuBar.addMenu("&Porte Feuille")
        walletMenu.addAction(self.walletAction)
        aproposMenu = menuBar.addMenu("&Apropos")
        aproposMenu.addAction(self.aproposAction)
        helpMenu = menuBar.addMenu("&Aide")
        helpMenu.addAction(self.helpAction)
        # helpMenu  = menuBar.addMenu(QIcon(":menu-dashboard.svg"), "&Help")
    def _createToolBars(self):
        # Using a title
        fileToolBar = self.addToolBar("File")
        # Using a QToolBar object
        dashToolBar = QToolBar("DashBoard", self)
        self.addToolBar(dashToolBar)
        dashToolBar.setMovable(False)
        dashToolBar.addAction(self.dashWalletAction)
        dashToolBar.addAction(self.dashMineAction)
        # Using a QToolBar object and a toolbar area
        helpToolBar = QToolBar("Help", self)
        self.addToolBar(Qt.LeftToolBarArea, helpToolBar)
    def _createActions(self):
        # Creating action using   constructor
        self.newAction = QAction(self)
        self.newAction.setText("&Mouveau")
        self.newAccountAction = QAction("&Compte...", self)
        self.newWalletAction = QAction("&Porte Feuill...", self)
        self.openAction = QAction("&Ouvrir...", self)
        self.dashMineAction = QAction(QIcon(":menu-dashboard.svg"), "&Minage...", self)
        self.dashWalletAction = QAction(QIcon(":menu--wallet-filled-money-tool.svg"), "&Porte Feuiille...", self)
        self.quitAction = QAction("&Quitter...", self)
        self.walletAction = QAction("&Porte Feuille...", self)
        self.aproposAction = QAction("&Apropos", self)
        self.helpAction = QAction("&Aide", self)
   
app = QApplication(sys.argv)
d = Main()
sys.exit(app.exec_())
