# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_author.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_EditAuthor(object):
    def setupUi(self, EditAuthor):
        if not EditAuthor.objectName():
            EditAuthor.setObjectName(u"EditAuthor")
        EditAuthor.resize(400, 163)
        self.formLayout = QFormLayout(EditAuthor)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(EditAuthor)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.first_name = QLineEdit(EditAuthor)
        self.first_name.setObjectName(u"first_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.first_name)

        self.label_3 = QLabel(EditAuthor)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.middle_name = QLineEdit(EditAuthor)
        self.middle_name.setObjectName(u"middle_name")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.middle_name)

        self.label_2 = QLabel(EditAuthor)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.last_name = QLineEdit(EditAuthor)
        self.last_name.setObjectName(u"last_name")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.last_name)

        self.save_button = QPushButton(EditAuthor)
        self.save_button.setObjectName(u"save_button")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.save_button)


        self.retranslateUi(EditAuthor)

        QMetaObject.connectSlotsByName(EditAuthor)
    # setupUi

    def retranslateUi(self, EditAuthor):
        EditAuthor.setWindowTitle(QCoreApplication.translate("EditAuthor", u"Form", None))
        self.label.setText(QCoreApplication.translate("EditAuthor", u"First Name", None))
        self.label_3.setText(QCoreApplication.translate("EditAuthor", u"Middle Name", None))
        self.label_2.setText(QCoreApplication.translate("EditAuthor", u"Last Name", None))
        self.save_button.setText(QCoreApplication.translate("EditAuthor", u"Save", None))
    # retranslateUi

