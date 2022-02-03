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
        EditDocument.resize(745, 938)
        self.verticalLayout = QVBoxLayout(EditDocument)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(EditDocument)
        self.tabWidget.setObjectName(u"tabWidget")
        self.primary_data_tab = QWidget()
        self.primary_data_tab.setObjectName(u"primary_data_tab")
        self.horizontalLayout_2 = QHBoxLayout(self.primary_data_tab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_2 = QLabel(self.primary_data_tab)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.path = QLabel(self.primary_data_tab)
        self.path.setObjectName(u"path")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.path)

        self.label = QLabel(self.primary_data_tab)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label)

        self.title = QLineEdit(self.primary_data_tab)
        self.title.setObjectName(u"title")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.title)

        self.label_3 = QLabel(self.primary_data_tab)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.authors = QListView(self.primary_data_tab)
        self.authors.setObjectName(u"authors")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.authors.sizePolicy().hasHeightForWidth())
        self.authors.setSizePolicy(sizePolicy)
        self.authors.setContextMenuPolicy(Qt.CustomContextMenu)
        self.authors.setSelectionMode(QAbstractItemView.MultiSelection)
        self.authors.setResizeMode(QListView.Adjust)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.authors)

        self.label_4 = QLabel(self.primary_data_tab)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.document_type = QComboBox(self.primary_data_tab)
        self.document_type.setObjectName(u"document_type")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.document_type)

        self.label_17 = QLabel(self.primary_data_tab)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_17)

        self.category = QTreeView(self.primary_data_tab)
        self.category.setObjectName(u"category")
        self.category.setSelectionMode(QAbstractItemView.MultiSelection)
        self.category.header().setVisible(False)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.category)

        self.label_18 = QLabel(self.primary_data_tab)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_18)

        self.shelves = QListView(self.primary_data_tab)
        self.shelves.setObjectName(u"shelves")
        self.shelves.setContextMenuPolicy(Qt.CustomContextMenu)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.shelves)

        self.label_14 = QLabel(self.primary_data_tab)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_14)

        self.doi = QLineEdit(self.primary_data_tab)
        self.doi.setObjectName(u"doi")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.doi)

        self.label_15 = QLabel(self.primary_data_tab)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.label_15)

        self.isbn = QLineEdit(self.primary_data_tab)
        self.isbn.setObjectName(u"isbn")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.isbn)

        self.label_16 = QLabel(self.primary_data_tab)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.label_16)

        self.url = QLineEdit(self.primary_data_tab)
        self.url.setObjectName(u"url")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.url)


        self.horizontalLayout_2.addLayout(self.formLayout_2)

        self.tabWidget.addTab(self.primary_data_tab, "")
        self.additional_meta_tab = QWidget()
        self.additional_meta_tab.setObjectName(u"additional_meta_tab")
        self.widget = QWidget(self.additional_meta_tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 431, 871))
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.publication = QLineEdit(self.widget)
        self.publication.setObjectName(u"publication")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.publication)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.edition = QLineEdit(self.widget)
        self.edition.setObjectName(u"edition")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.edition)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_8)

        self.volume = QLineEdit(self.widget)
        self.volume.setObjectName(u"volume")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.volume)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_9)

        self.issue = QLineEdit(self.widget)
        self.issue.setObjectName(u"issue")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.issue)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_10)

        self.pages = QLineEdit(self.widget)
        self.pages.setObjectName(u"pages")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.pages)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_11)

        self.date = QDateEdit(self.widget)
        self.date.setObjectName(u"date")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.date)

        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_12)

        self.series = QLineEdit(self.widget)
        self.series.setObjectName(u"series")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.series)

        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_13)

        self.language = QLineEdit(self.widget)
        self.language.setObjectName(u"language")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.language)

        self.doc_abstract = QTextEdit(self.widget)
        self.doc_abstract.setObjectName(u"doc_abstract")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.doc_abstract)

        self.tabWidget.addTab(self.additional_meta_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.save_button = QPushButton(EditDocument)
        self.save_button.setObjectName(u"save_button")

        self.horizontalLayout.addWidget(self.save_button)

        self.update_meta_button = QPushButton(EditDocument)
        self.update_meta_button.setObjectName(u"update_meta_button")

        self.horizontalLayout.addWidget(self.update_meta_button)

        self.rename_file_button = QPushButton(EditDocument)
        self.rename_file_button.setObjectName(u"rename_file_button")

        self.horizontalLayout.addWidget(self.rename_file_button)

        self.delete_button = QPushButton(EditDocument)
        self.delete_button.setObjectName(u"delete_button")

        self.horizontalLayout.addWidget(self.delete_button)

        self.view_button = QPushButton(EditDocument)
        self.view_button.setObjectName(u"view_button")

        self.horizontalLayout.addWidget(self.view_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(EditDocument)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(EditDocument)
    # setupUi

    def retranslateUi(self, EditDocument):
        EditDocument.setWindowTitle(QCoreApplication.translate("EditDocument", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("EditDocument", u"Path", None))
        self.path.setText("")
        self.label.setText(QCoreApplication.translate("EditDocument", u"Title", None))
        self.label_3.setText(QCoreApplication.translate("EditDocument", u"Authors", None))
        self.label_4.setText(QCoreApplication.translate("EditDocument", u"Type", None))
        self.label_17.setText(QCoreApplication.translate("EditDocument", u"Category", None))
        self.label_18.setText(QCoreApplication.translate("EditDocument", u"Shelves", None))
        self.label_14.setText(QCoreApplication.translate("EditDocument", u"DOI", None))
        self.label_15.setText(QCoreApplication.translate("EditDocument", u"ISBN", None))
        self.label_16.setText(QCoreApplication.translate("EditDocument", u"URL", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.primary_data_tab), QCoreApplication.translate("EditDocument", u"Primary data", None))
        self.label_5.setText(QCoreApplication.translate("EditDocument", u"Abstract", None))
        self.label_6.setText(QCoreApplication.translate("EditDocument", u"Publication", None))
        self.label_7.setText(QCoreApplication.translate("EditDocument", u"Edition", None))
        self.label_8.setText(QCoreApplication.translate("EditDocument", u"Volume", None))
        self.label_9.setText(QCoreApplication.translate("EditDocument", u"Issue", None))
        self.label_10.setText(QCoreApplication.translate("EditDocument", u"Pages", None))
        self.label_11.setText(QCoreApplication.translate("EditDocument", u"Date", None))
        self.label_12.setText(QCoreApplication.translate("EditDocument", u"Series", None))
        self.label_13.setText(QCoreApplication.translate("EditDocument", u"Language", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.additional_meta_tab), QCoreApplication.translate("EditDocument", u"Additional metadata", None))
        self.save_button.setText(QCoreApplication.translate("EditDocument", u"Save", None))
        self.update_meta_button.setText(QCoreApplication.translate("EditDocument", u"Refresh Meta", None))
        self.rename_file_button.setText(QCoreApplication.translate("EditDocument", u"Rename file", None))
        self.delete_button.setText(QCoreApplication.translate("EditDocument", u"Delete", None))
        self.view_button.setText(QCoreApplication.translate("EditDocument", u"View PDF", None))
    # retranslateUi

