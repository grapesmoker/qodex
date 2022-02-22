# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_author.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_NewAuthorDialog(object):
    def setupUi(self, NewAuthorDialog):
        if not NewAuthorDialog.objectName():
            NewAuthorDialog.setObjectName(u"NewAuthorDialog")
        NewAuthorDialog.resize(400, 178)
        self.buttonBox = QDialogButtonBox(NewAuthorDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(40, 130, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.last_name = QLineEdit(NewAuthorDialog)
        self.last_name.setObjectName(u"last_name")
        self.last_name.setGeometry(QRect(98, 81, 288, 21))
        self.middle_name = QLineEdit(NewAuthorDialog)
        self.middle_name.setObjectName(u"middle_name")
        self.middle_name.setGeometry(QRect(98, 50, 288, 21))
        self.label = QLabel(NewAuthorDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(24, 19, 66, 21))
        self.first_name = QLineEdit(NewAuthorDialog)
        self.first_name.setObjectName(u"first_name")
        self.first_name.setGeometry(QRect(98, 19, 288, 21))
        self.first_name.setFocusPolicy(Qt.WheelFocus)
        self.first_name.setLayoutDirection(Qt.LeftToRight)
        self.label_2 = QLabel(NewAuthorDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(25, 81, 65, 21))
        self.label_3 = QLabel(NewAuthorDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 50, 80, 21))
        QWidget.setTabOrder(self.first_name, self.middle_name)
        QWidget.setTabOrder(self.middle_name, self.last_name)

        self.retranslateUi(NewAuthorDialog)
        self.buttonBox.accepted.connect(NewAuthorDialog.accept)
        self.buttonBox.rejected.connect(NewAuthorDialog.reject)

        QMetaObject.connectSlotsByName(NewAuthorDialog)
    # setupUi

    def retranslateUi(self, NewAuthorDialog):
        NewAuthorDialog.setWindowTitle(QCoreApplication.translate("NewAuthorDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("NewAuthorDialog", u"First Name", None))
        self.label_2.setText(QCoreApplication.translate("NewAuthorDialog", u"Last Name", None))
        self.label_3.setText(QCoreApplication.translate("NewAuthorDialog", u"Middle Name", None))
    # retranslateUi

