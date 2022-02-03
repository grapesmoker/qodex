# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_shelf.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_NewShelfDialog(object):
    def setupUi(self, NewShelfDialog):
        if not NewShelfDialog.objectName():
            NewShelfDialog.setObjectName(u"NewShelfDialog")
        NewShelfDialog.resize(400, 300)
        self.formLayout = QFormLayout(NewShelfDialog)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(NewShelfDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.shelf_name = QLineEdit(NewShelfDialog)
        self.shelf_name.setObjectName(u"shelf_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.shelf_name)

        self.label_2 = QLabel(NewShelfDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.shelf_description = QTextEdit(NewShelfDialog)
        self.shelf_description.setObjectName(u"shelf_description")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.shelf_description)

        self.buttonBox = QDialogButtonBox(NewShelfDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.buttonBox)


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

