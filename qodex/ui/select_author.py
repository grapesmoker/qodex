# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_author.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_SelectAuthorDialog(object):
    def setupUi(self, SelectAuthorDialog):
        if not SelectAuthorDialog.objectName():
            SelectAuthorDialog.setObjectName(u"SelectAuthorDialog")
        SelectAuthorDialog.resize(414, 359)
        self.verticalLayout = QVBoxLayout(SelectAuthorDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.authors_view = QListView(SelectAuthorDialog)
        self.authors_view.setObjectName(u"authors_view")
        self.authors_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.authors_view.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout.addWidget(self.authors_view)

        self.button_box = QDialogButtonBox(SelectAuthorDialog)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setOrientation(Qt.Horizontal)
        self.button_box.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.button_box)


        self.retranslateUi(SelectAuthorDialog)
        self.button_box.accepted.connect(SelectAuthorDialog.accept)
        self.button_box.rejected.connect(SelectAuthorDialog.reject)

        QMetaObject.connectSlotsByName(SelectAuthorDialog)
    # setupUi

    def retranslateUi(self, SelectAuthorDialog):
        SelectAuthorDialog.setWindowTitle(QCoreApplication.translate("SelectAuthorDialog", u"Select author", None))
    # retranslateUi

