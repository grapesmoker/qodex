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
        EditDocument.resize(692, 905)
        self.formLayout_2 = QFormLayout(EditDocument)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetNoConstraint)
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

        self.label_4 = QLabel(EditDocument)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.document_type = QComboBox(EditDocument)
        self.document_type.setObjectName(u"document_type")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.document_type)

        self.label_14 = QLabel(EditDocument)
        self.label_14.setObjectName(u"label_14")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_14)

        self.doi = QLineEdit(EditDocument)
        self.doi.setObjectName(u"doi")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.doi)

        self.label_15 = QLabel(EditDocument)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_15)

        self.isbn = QLineEdit(EditDocument)
        self.isbn.setObjectName(u"isbn")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.isbn)

        self.label_16 = QLabel(EditDocument)
        self.label_16.setObjectName(u"label_16")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_16)

        self.url = QLineEdit(EditDocument)
        self.url.setObjectName(u"url")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.url)

        self.label_5 = QLabel(EditDocument)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_5)

        self.doc_abstract = QTextEdit(EditDocument)
        self.doc_abstract.setObjectName(u"doc_abstract")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.doc_abstract)

        self.label_6 = QLabel(EditDocument)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_6)

        self.publication = QLineEdit(EditDocument)
        self.publication.setObjectName(u"publication")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.publication)

        self.label_7 = QLabel(EditDocument)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_7)

        self.edition = QLineEdit(EditDocument)
        self.edition.setObjectName(u"edition")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.edition)

        self.label_8 = QLabel(EditDocument)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_8)

        self.volume = QLineEdit(EditDocument)
        self.volume.setObjectName(u"volume")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.volume)

        self.label_9 = QLabel(EditDocument)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_9)

        self.issue = QLineEdit(EditDocument)
        self.issue.setObjectName(u"issue")

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.issue)

        self.label_10 = QLabel(EditDocument)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_10)

        self.pages = QLineEdit(EditDocument)
        self.pages.setObjectName(u"pages")

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.pages)

        self.label_11 = QLabel(EditDocument)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.label_11)

        self.date = QDateEdit(EditDocument)
        self.date.setObjectName(u"date")

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.date)

        self.label_12 = QLabel(EditDocument)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(14, QFormLayout.LabelRole, self.label_12)

        self.series = QLineEdit(EditDocument)
        self.series.setObjectName(u"series")

        self.formLayout.setWidget(14, QFormLayout.FieldRole, self.series)

        self.label_13 = QLabel(EditDocument)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.label_13)

        self.language = QLineEdit(EditDocument)
        self.language.setObjectName(u"language")

        self.formLayout.setWidget(15, QFormLayout.FieldRole, self.language)

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


        self.formLayout.setLayout(16, QFormLayout.FieldRole, self.horizontalLayout)


        self.formLayout_2.setLayout(0, QFormLayout.SpanningRole, self.formLayout)


        self.retranslateUi(EditDocument)

        QMetaObject.connectSlotsByName(EditDocument)
    # setupUi

    def retranslateUi(self, EditDocument):
        EditDocument.setWindowTitle(QCoreApplication.translate("EditDocument", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("EditDocument", u"Path", None))
        self.path.setText("")
        self.label.setText(QCoreApplication.translate("EditDocument", u"Title", None))
        self.label_3.setText(QCoreApplication.translate("EditDocument", u"Authors", None))
        self.label_4.setText(QCoreApplication.translate("EditDocument", u"Type", None))
        self.label_14.setText(QCoreApplication.translate("EditDocument", u"DOI", None))
        self.label_15.setText(QCoreApplication.translate("EditDocument", u"ISBN", None))
        self.label_16.setText(QCoreApplication.translate("EditDocument", u"URL", None))
        self.label_5.setText(QCoreApplication.translate("EditDocument", u"Abstract", None))
        self.label_6.setText(QCoreApplication.translate("EditDocument", u"Publication", None))
        self.label_7.setText(QCoreApplication.translate("EditDocument", u"Edition", None))
        self.label_8.setText(QCoreApplication.translate("EditDocument", u"Volume", None))
        self.label_9.setText(QCoreApplication.translate("EditDocument", u"Issue", None))
        self.label_10.setText(QCoreApplication.translate("EditDocument", u"Pages", None))
        self.label_11.setText(QCoreApplication.translate("EditDocument", u"Date", None))
        self.label_12.setText(QCoreApplication.translate("EditDocument", u"Series", None))
        self.label_13.setText(QCoreApplication.translate("EditDocument", u"Language", None))
        self.save_button.setText(QCoreApplication.translate("EditDocument", u"Save", None))
        self.delete_button.setText(QCoreApplication.translate("EditDocument", u"Delete", None))
        self.view_button.setText(QCoreApplication.translate("EditDocument", u"View PDF", None))
    # retranslateUi

