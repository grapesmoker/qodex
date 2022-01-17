from PySide6 import QtWidgets, QtCore, QtGui, Qt

from qodex.db import models


class ShelfItem(QtGui.QStandardItem):

    labels = ['Shelf Name', 'Description']
    display_fields = ['name', 'description']

    def __init__(self, shelf: models.Shelf, *args, **kwargs):

        super().__init__(shelf.name)
        self.shelf = shelf
        self.model = shelf


class AuthorItem(QtGui.QStandardItem):

    labels = ['Last Name', 'First Name', 'Middle Name']
    display_fields = ['last_name', 'first_name', 'middle_name']

    def __init__(self, author: models.Author, *args, **kwargs):

        super().__init__(str(author))
        self.author = author
        self.model = author

    def type(self) -> int:

        return QtGui.QStandardItem.UserType


class DocumentItem(QtGui.QStandardItem):

    labels = ['Title', 'Author', 'Category']
    display_fields = ['title', 'display_authors', 'display_categories']

    def __init__(self, doc: models.Document, *args, **kwargs):

        super().__init__(str(doc))
        self.document = doc
        self.model = doc


class CategoryItem(QtGui.QStandardItem):

    def __init__(self, category: models.Category, *args, **kwargs):

        super().__init__(str(category))
        self.category = category
