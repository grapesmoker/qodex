# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_QodexMain(object):
    def setupUi(self, QodexMain):
        if not QodexMain.objectName():
            QodexMain.setObjectName(u"QodexMain")
        QodexMain.resize(1012, 947)
        self.actionAdd_shelf = QAction(QodexMain)
        self.actionAdd_shelf.setObjectName(u"actionAdd_shelf")
        self.actionAdd_document = QAction(QodexMain)
        self.actionAdd_document.setObjectName(u"actionAdd_document")
        self.action_add_shelf = QAction(QodexMain)
        self.action_add_shelf.setObjectName(u"action_add_shelf")
        self.action_add_document = QAction(QodexMain)
        self.action_add_document.setObjectName(u"action_add_document")
        self.action_add_author = QAction(QodexMain)
        self.action_add_author.setObjectName(u"action_add_author")
        self.action_add_category = QAction(QodexMain)
        self.action_add_category.setObjectName(u"action_add_category")
        self.centralwidget = QWidget(QodexMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.main_tab_view = QTabWidget(self.centralwidget)
        self.main_tab_view.setObjectName(u"main_tab_view")
        self.shelf_tab = QWidget()
        self.shelf_tab.setObjectName(u"shelf_tab")
        self.verticalLayout = QVBoxLayout(self.shelf_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.shelf_view = QTableView(self.shelf_tab)
        self.shelf_view.setObjectName(u"shelf_view")

        self.verticalLayout.addWidget(self.shelf_view)

        self.main_tab_view.addTab(self.shelf_tab, "")
        self.documents_tab = QWidget()
        self.documents_tab.setObjectName(u"documents_tab")
        self.horizontalLayout_2 = QHBoxLayout(self.documents_tab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.documents_view = QTableView(self.documents_tab)
        self.documents_view.setObjectName(u"documents_view")

        self.horizontalLayout_2.addWidget(self.documents_view)

        self.main_tab_view.addTab(self.documents_tab, "")
        self.authors_tab = QWidget()
        self.authors_tab.setObjectName(u"authors_tab")
        self.horizontalLayout_3 = QHBoxLayout(self.authors_tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.authors_view = QTableView(self.authors_tab)
        self.authors_view.setObjectName(u"authors_view")
        self.authors_view.horizontalHeader().setCascadingSectionResizes(False)
        self.authors_view.horizontalHeader().setStretchLastSection(False)

        self.horizontalLayout_3.addWidget(self.authors_view)

        self.main_tab_view.addTab(self.authors_tab, "")
        self.categories_tab = QWidget()
        self.categories_tab.setObjectName(u"categories_tab")
        self.horizontalLayout_4 = QHBoxLayout(self.categories_tab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.categories_view = QTreeView(self.categories_tab)
        self.categories_view.setObjectName(u"categories_view")

        self.horizontalLayout_4.addWidget(self.categories_view)

        self.main_tab_view.addTab(self.categories_tab, "")

        self.horizontalLayout.addWidget(self.main_tab_view)

        self.verticalSpacer = QSpacerItem(20, 880, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout.addItem(self.verticalSpacer)

        self.properties_scroll = QScrollArea(self.centralwidget)
        self.properties_scroll.setObjectName(u"properties_scroll")
        self.properties_scroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 477, 881))
        self.properties_scroll.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.properties_scroll)

        QodexMain.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(QodexMain)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1012, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuNew = QMenu(self.menuFile)
        self.menuNew.setObjectName(u"menuNew")
        QodexMain.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(QodexMain)
        self.statusbar.setObjectName(u"statusbar")
        QodexMain.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuNew.addAction(self.action_add_shelf)
        self.menuNew.addAction(self.action_add_document)
        self.menuNew.addAction(self.action_add_author)
        self.menuNew.addAction(self.action_add_category)

        self.retranslateUi(QodexMain)

        self.main_tab_view.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(QodexMain)
    # setupUi

    def retranslateUi(self, QodexMain):
        QodexMain.setWindowTitle(QCoreApplication.translate("QodexMain", u"MainWindow", None))
        self.actionAdd_shelf.setText(QCoreApplication.translate("QodexMain", u"Add shelf", None))
        self.actionAdd_document.setText(QCoreApplication.translate("QodexMain", u"Add document", None))
        self.action_add_shelf.setText(QCoreApplication.translate("QodexMain", u"Shelf", None))
        self.action_add_document.setText(QCoreApplication.translate("QodexMain", u"Document", None))
        self.action_add_author.setText(QCoreApplication.translate("QodexMain", u"Author", None))
        self.action_add_category.setText(QCoreApplication.translate("QodexMain", u"Category", None))
        self.main_tab_view.setTabText(self.main_tab_view.indexOf(self.shelf_tab), QCoreApplication.translate("QodexMain", u"Shelves", None))
        self.main_tab_view.setTabText(self.main_tab_view.indexOf(self.documents_tab), QCoreApplication.translate("QodexMain", u"Documents", None))
        self.main_tab_view.setTabText(self.main_tab_view.indexOf(self.authors_tab), QCoreApplication.translate("QodexMain", u"Authors", None))
        self.main_tab_view.setTabText(self.main_tab_view.indexOf(self.categories_tab), QCoreApplication.translate("QodexMain", u"Categories", None))
        self.menuFile.setTitle(QCoreApplication.translate("QodexMain", u"File", None))
        self.menuNew.setTitle(QCoreApplication.translate("QodexMain", u"New", None))
    # retranslateUi

