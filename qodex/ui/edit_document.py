# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_document.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_EditDocument(object):
    def setupUi(self, EditDocument):
        if not EditDocument.objectName():
            EditDocument.setObjectName(u"EditDocument")
        EditDocument.resize(692, 361)
        self.formLayout = QFormLayout(EditDocument)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(EditDocument)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.path = QLabel(EditDocument)
        self.path.setObjectName(u"path")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.path)

        self.label = QLabel(EditDocument)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.title = QLineEdit(EditDocument)
        self.title.setObjectName(u"title")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.title)

        self.label_3 = QLabel(EditDocument)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.authors = QListView(EditDocument)
        self.authors.setObjectName(u"authors")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.authors.sizePolicy().hasHeightForWidth())
        self.authors.setSizePolicy(sizePolicy)
        self.authors.setContextMenuPolicy(Qt.CustomContextMenu)
        self.authors.setSelectionMode(QAbstractItemView.MultiSelection)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.authors)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.save_button = QPushButton(EditDocument)
        self.save_button.setObjectName(u"save_button")

        self.horizontalLayout.addWidget(self.save_button)

        self.delete_button = QPushButton(EditDocument)
        self.delete_button.setObjectName(u"delete_button")

        self.horizontalLayout.addWidget(self.delete_button)

        self.view_button = QPushButton(EditDocument)
        self.view_button.setObjectName(u"view_button")

        self.horizontalLayout.addWidget(self.view_button)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout)


        self.retranslateUi(EditDocument)

        QMetaObject.connectSlotsByName(EditDocument)
    # setupUi

    def retranslateUi(self, EditDocument):
        EditDocument.setWindowTitle(QCoreApplication.translate("EditDocument", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("EditDocument", u"Path", None))
        self.path.setText("")
        self.label.setText(QCoreApplication.translate("EditDocument", u"Title", None))
        self.label_3.setText(QCoreApplication.translate("EditDocument", u"Authors", None))
        self.save_button.setText(QCoreApplication.translate("EditDocument", u"Save", None))
        self.delete_button.setText(QCoreApplication.translate("EditDocument", u"Delete", None))
        self.view_button.setText(QCoreApplication.translate("EditDocument", u"View PDF", None))
    # retranslateUi

