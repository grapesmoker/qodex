# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_shelves.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_SelectShelvesDialog(object):
    def setupUi(self, SelectShelvesDialog):
        if not SelectShelvesDialog.objectName():
            SelectShelvesDialog.setObjectName(u"SelectShelvesDialog")
        SelectShelvesDialog.resize(468, 386)
        self.buttonBox = QDialogButtonBox(SelectShelvesDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(120, 350, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.shelf_view = QListView(SelectShelvesDialog)
        self.shelf_view.setObjectName(u"shelf_view")
        self.shelf_view.setGeometry(QRect(10, 10, 451, 331))
        self.shelf_view.setSelectionMode(QAbstractItemView.MultiSelection)

        self.retranslateUi(SelectShelvesDialog)
        self.buttonBox.accepted.connect(SelectShelvesDialog.accept)
        self.buttonBox.rejected.connect(SelectShelvesDialog.reject)

        QMetaObject.connectSlotsByName(SelectShelvesDialog)
    # setupUi

    def retranslateUi(self, SelectShelvesDialog):
        SelectShelvesDialog.setWindowTitle(QCoreApplication.translate("SelectShelvesDialog", u"Select shelves", None))
    # retranslateUi

