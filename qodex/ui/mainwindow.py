# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Qodex(object):
    def setupUi(self, Qodex):
        if not Qodex.objectName():
            Qodex.setObjectName(u"Qodex")
        Qodex.resize(1046, 635)
        self.action_add_shelf = QAction(Qodex)
        self.action_add_shelf.setObjectName(u"action_add_shelf")
        self.action_add_document = QAction(Qodex)
        self.action_add_document.setObjectName(u"action_add_document")
        self.action_add_author = QAction(Qodex)
        self.action_add_author.setObjectName(u"action_add_author")
        self.action_add_category = QAction(Qodex)
        self.action_add_category.setObjectName(u"action_add_category")
        self.centralwidget = QWidget(Qodex)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.treeView = QTreeView(self.centralwidget)
        self.treeView.setObjectName(u"treeView")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.treeView, 0, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 2, 1, 1)

        Qodex.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Qodex)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1046, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuNew_3 = QMenu(self.menuFile)
        self.menuNew_3.setObjectName(u"menuNew_3")
        Qodex.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Qodex)
        self.statusbar.setObjectName(u"statusbar")
        Qodex.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.menuNew_3.menuAction())
        self.menuNew_3.addAction(self.action_add_shelf)
        self.menuNew_3.addAction(self.action_add_document)
        self.menuNew_3.addAction(self.action_add_author)
        self.menuNew_3.addAction(self.action_add_category)

        self.retranslateUi(Qodex)

        QMetaObject.connectSlotsByName(Qodex)
    # setupUi

    def retranslateUi(self, Qodex):
        Qodex.setWindowTitle(QCoreApplication.translate("Qodex", u"Qodex", None))
        self.action_add_shelf.setText(QCoreApplication.translate("Qodex", u"Shelf", None))
        self.action_add_document.setText(QCoreApplication.translate("Qodex", u"Document", None))
        self.action_add_author.setText(QCoreApplication.translate("Qodex", u"Author", None))
        self.action_add_category.setText(QCoreApplication.translate("Qodex", u"Category", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Qodex", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Qodex", u"Tab 2", None))
        self.menuFile.setTitle(QCoreApplication.translate("Qodex", u"File", None))
        self.menuNew_3.setTitle(QCoreApplication.translate("Qodex", u"New", None))
    # retranslateUi

