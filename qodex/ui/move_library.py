# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'move_library.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MoveLibrary(object):
    def setupUi(self, MoveLibrary):
        if not MoveLibrary.objectName():
            MoveLibrary.setObjectName(u"MoveLibrary")
        MoveLibrary.resize(667, 279)
        self.verticalLayout = QVBoxLayout(MoveLibrary)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(MoveLibrary)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setTextFormat(Qt.AutoText)

        self.horizontalLayout.addWidget(self.label)

        self.library_path = QLabel(MoveLibrary)
        self.library_path.setObjectName(u"library_path")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.library_path.sizePolicy().hasHeightForWidth())
        self.library_path.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.library_path)

        self.select_folder = QPushButton(MoveLibrary)
        self.select_folder.setObjectName(u"select_folder")
        sizePolicy.setHeightForWidth(self.select_folder.sizePolicy().hasHeightForWidth())
        self.select_folder.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.select_folder)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.groupBox = QGroupBox(MoveLibrary)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.method_copy = QRadioButton(self.groupBox)
        self.method_copy.setObjectName(u"method_copy")
        self.method_copy.setGeometry(QRect(10, 30, 104, 21))
        self.method_copy.setChecked(True)
        self.method_move = QRadioButton(self.groupBox)
        self.method_move.setObjectName(u"method_move")
        self.method_move.setGeometry(QRect(110, 30, 104, 21))

        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.create_category_folders = QCheckBox(MoveLibrary)
        self.create_category_folders.setObjectName(u"create_category_folders")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.create_category_folders.sizePolicy().hasHeightForWidth())
        self.create_category_folders.setSizePolicy(sizePolicy3)
        self.create_category_folders.setChecked(True)

        self.gridLayout.addWidget(self.create_category_folders, 2, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(MoveLibrary)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(MoveLibrary)
        self.buttonBox.accepted.connect(MoveLibrary.accept)
        self.buttonBox.rejected.connect(MoveLibrary.reject)

        QMetaObject.connectSlotsByName(MoveLibrary)
    # setupUi

    def retranslateUi(self, MoveLibrary):
        MoveLibrary.setWindowTitle(QCoreApplication.translate("MoveLibrary", u"Move library", None))
        self.label.setText(QCoreApplication.translate("MoveLibrary", u"Location: ", None))
        self.library_path.setText("")
        self.select_folder.setText(QCoreApplication.translate("MoveLibrary", u"Select folder", None))
        self.groupBox.setTitle(QCoreApplication.translate("MoveLibrary", u"Collection method", None))
        self.method_copy.setText(QCoreApplication.translate("MoveLibrary", u"Copy", None))
        self.method_move.setText(QCoreApplication.translate("MoveLibrary", u"Move", None))
        self.create_category_folders.setText(QCoreApplication.translate("MoveLibrary", u"Create category folders", None))
    # retranslateUi

