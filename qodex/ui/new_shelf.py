# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_shelf.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_NewShelfDialog(object):
    def setupUi(self, NewShelfDialog):
        if not NewShelfDialog.objectName():
            NewShelfDialog.setObjectName(u"NewShelfDialog")
        NewShelfDialog.resize(400, 300)
        self.buttonBox = QDialogButtonBox(NewShelfDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.widget = QWidget(NewShelfDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 10, 324, 225))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.shelf_name = QLineEdit(self.widget)
        self.shelf_name.setObjectName(u"shelf_name")

        self.gridLayout.addWidget(self.shelf_name, 0, 1, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.shelf_description = QTextEdit(self.widget)
        self.shelf_description.setObjectName(u"shelf_description")

        self.gridLayout.addWidget(self.shelf_description, 1, 1, 1, 1)


        self.retranslateUi(NewShelfDialog)
        self.buttonBox.accepted.connect(NewShelfDialog.accept)
        self.buttonBox.rejected.connect(NewShelfDialog.reject)

        QMetaObject.connectSlotsByName(NewShelfDialog)
    # setupUi

    def retranslateUi(self, NewShelfDialog):
        NewShelfDialog.setWindowTitle(QCoreApplication.translate("NewShelfDialog", u"New Shelf", None))
        self.label.setText(QCoreApplication.translate("NewShelfDialog", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("NewShelfDialog", u"Description", None))
    # retranslateUi

