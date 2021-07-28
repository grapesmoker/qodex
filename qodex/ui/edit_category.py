# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_category.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_EditCategory(object):
    def setupUi(self, EditCategory):
        if not EditCategory.objectName():
            EditCategory.setObjectName(u"EditCategory")
        EditCategory.resize(400, 115)
        self.formLayout = QFormLayout(EditCategory)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(EditCategory)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.name = QLineEdit(EditCategory)
        self.name.setObjectName(u"name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.name)

        self.label_2 = QLabel(EditCategory)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.parent_category = QComboBox(EditCategory)
        self.parent_category.setObjectName(u"parent_category")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.parent_category)

        self.save_button = QPushButton(EditCategory)
        self.save_button.setObjectName(u"save_button")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.save_button)


        self.retranslateUi(EditCategory)

        QMetaObject.connectSlotsByName(EditCategory)
    # setupUi

    def retranslateUi(self, EditCategory):
        EditCategory.setWindowTitle(QCoreApplication.translate("EditCategory", u"Form", None))
        self.label.setText(QCoreApplication.translate("EditCategory", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("EditCategory", u"Parent", None))
        self.save_button.setText(QCoreApplication.translate("EditCategory", u"Save", None))
    # retranslateUi

