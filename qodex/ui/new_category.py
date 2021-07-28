# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_category.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_NewCategoryDialog(object):
    def setupUi(self, NewCategoryDialog):
        if not NewCategoryDialog.objectName():
            NewCategoryDialog.setObjectName(u"NewCategoryDialog")
        NewCategoryDialog.resize(400, 133)
        self.formLayout = QFormLayout(NewCategoryDialog)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(NewCategoryDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.name = QLineEdit(NewCategoryDialog)
        self.name.setObjectName(u"name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.name)

        self.label_2 = QLabel(NewCategoryDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.parent_category = QComboBox(NewCategoryDialog)
        self.parent_category.setObjectName(u"parent_category")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.parent_category)

        self.buttonBox = QDialogButtonBox(NewCategoryDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.buttonBox)


        self.retranslateUi(NewCategoryDialog)
        self.buttonBox.accepted.connect(NewCategoryDialog.accept)
        self.buttonBox.rejected.connect(NewCategoryDialog.reject)

        QMetaObject.connectSlotsByName(NewCategoryDialog)
    # setupUi

    def retranslateUi(self, NewCategoryDialog):
        NewCategoryDialog.setWindowTitle(QCoreApplication.translate("NewCategoryDialog", u"New category", None))
        self.label.setText(QCoreApplication.translate("NewCategoryDialog", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("NewCategoryDialog", u"Parent", None))
    # retranslateUi

