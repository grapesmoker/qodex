# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_shelf.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_EditShelf(object):
    def setupUi(self, EditShelf):
        if not EditShelf.objectName():
            EditShelf.setObjectName(u"EditShelf")
        EditShelf.resize(400, 300)
        self.formLayout = QFormLayout(EditShelf)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(EditShelf)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.shelf_name = QLineEdit(EditShelf)
        self.shelf_name.setObjectName(u"shelf_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.shelf_name)

        self.label_2 = QLabel(EditShelf)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.shelf_description = QTextEdit(EditShelf)
        self.shelf_description.setObjectName(u"shelf_description")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.shelf_description)

        self.save_button = QPushButton(EditShelf)
        self.save_button.setObjectName(u"save_button")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.save_button)


        self.retranslateUi(EditShelf)

        QMetaObject.connectSlotsByName(EditShelf)
    # setupUi

    def retranslateUi(self, EditShelf):
        EditShelf.setWindowTitle(QCoreApplication.translate("EditShelf", u"Form", None))
        self.label.setText(QCoreApplication.translate("EditShelf", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("EditShelf", u"Description", None))
        self.save_button.setText(QCoreApplication.translate("EditShelf", u"Save", None))
    # retranslateUi

