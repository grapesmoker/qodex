# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'text_analyzer.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_TextAnalyzer(object):
    def setupUi(self, TextAnalyzer):
        if not TextAnalyzer.objectName():
            TextAnalyzer.setObjectName(u"TextAnalyzer")
        TextAnalyzer.resize(400, 478)
        self.verticalLayout = QVBoxLayout(TextAnalyzer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.text = QPlainTextEdit(TextAnalyzer)
        self.text.setObjectName(u"text")
        self.text.setReadOnly(True)

        self.verticalLayout.addWidget(self.text)

        self.text_type = QGroupBox(TextAnalyzer)
        self.text_type.setObjectName(u"text_type")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_type.sizePolicy().hasHeightForWidth())
        self.text_type.setSizePolicy(sizePolicy)
        self.radio_title = QRadioButton(self.text_type)
        self.radio_title.setObjectName(u"radio_title")
        self.radio_title.setGeometry(QRect(10, 30, 104, 21))
        self.radio_subtitle = QRadioButton(self.text_type)
        self.radio_subtitle.setObjectName(u"radio_subtitle")
        self.radio_subtitle.setGeometry(QRect(10, 60, 104, 21))
        self.radio_author_first_middle_last = QRadioButton(self.text_type)
        self.radio_author_first_middle_last.setObjectName(u"radio_author_first_middle_last")
        self.radio_author_first_middle_last.setGeometry(QRect(10, 90, 211, 21))
        self.radio_author_last_first = QRadioButton(self.text_type)
        self.radio_author_last_first.setObjectName(u"radio_author_last_first")
        self.radio_author_last_first.setGeometry(QRect(10, 120, 104, 21))

        self.verticalLayout.addWidget(self.text_type)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_next_text = QPushButton(TextAnalyzer)
        self.button_next_text.setObjectName(u"button_next_text")

        self.horizontalLayout.addWidget(self.button_next_text)

        self.button_next_doc = QPushButton(TextAnalyzer)
        self.button_next_doc.setObjectName(u"button_next_doc")

        self.horizontalLayout.addWidget(self.button_next_doc)

        self.button_stop = QPushButton(TextAnalyzer)
        self.button_stop.setObjectName(u"button_stop")

        self.horizontalLayout.addWidget(self.button_stop)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(TextAnalyzer)

        QMetaObject.connectSlotsByName(TextAnalyzer)
    # setupUi

    def retranslateUi(self, TextAnalyzer):
        TextAnalyzer.setWindowTitle(QCoreApplication.translate("TextAnalyzer", u"Form", None))
        self.text_type.setTitle(QCoreApplication.translate("TextAnalyzer", u"Text type", None))
        self.radio_title.setText(QCoreApplication.translate("TextAnalyzer", u"Title", None))
        self.radio_subtitle.setText(QCoreApplication.translate("TextAnalyzer", u"Subtitle", None))
        self.radio_author_first_middle_last.setText(QCoreApplication.translate("TextAnalyzer", u"Author: First, middle, last", None))
        self.radio_author_last_first.setText(QCoreApplication.translate("TextAnalyzer", u"Author: Last, first", None))
        self.button_next_text.setText(QCoreApplication.translate("TextAnalyzer", u"Next text", None))
        self.button_next_doc.setText(QCoreApplication.translate("TextAnalyzer", u"Next document", None))
        self.button_stop.setText(QCoreApplication.translate("TextAnalyzer", u"Stop", None))
    # retranslateUi

