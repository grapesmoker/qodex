from PySide6 import QtWidgets, QtCore, QtGui, Qt

from qodex.db import models


class ShelfItem(QtGui.QStandardItem):

    def __init__(self, shelf: models.Shelf, *args, **kwargs):

        super().__init__(shelf.name)
        self.shelf = shelf


class AuthorItem(QtGui.QStandardItem):

    def __init__(self, author: models.Author, *args, **kwargs):

        super().__init__(str(author))
        self.author = author

    def type(self) -> int:

        return QtGui.QStandardItem.UserType


class DocumentItem(QtGui.QStandardItem):

    def __init__(self, doc: models.Document, *args, **kwargs):

        super().__init__(str(doc))
        self.document = doc


class CategoryItem(QtGui.QStandardItem):

    def __init__(self, category: models.Category, *args, **kwargs):

        super().__init__(str(category))
        self.category = category
