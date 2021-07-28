from typing import List

from PySide6 import QtWidgets, QtCore, QtGui, Qt

from ui.new_shelf import Ui_NewShelfDialog
from ui.new_author import Ui_NewAuthorDialog
from ui.edit_shelf import Ui_EditShelf
from ui.edit_author import Ui_EditAuthor
from ui.new_category import Ui_NewCategoryDialog
from ui.edit_category import Ui_EditCategory
from ui.edit_document import Ui_EditDocument

from qodex.db.settings import get_session
from qodex.db import models
from qodex.item_models import AuthorItem, CategoryItem


class NewShelfDialog(QtWidgets.QDialog, Ui_NewShelfDialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


class NewAuthorDialog(QtWidgets.QDialog, Ui_NewAuthorDialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


class NewCategoryDialog(QtWidgets.QDialog, Ui_NewCategoryDialog):

    def __init__(self, top_level_categories: List[models.Category]):
        super().__init__()
        self.setupUi(self)
        self.combo_model = QtGui.QStandardItemModel()
        self.combo_root = self.combo_model.invisibleRootItem()
        self.parent_category.setModel(self.combo_model)

        def recursive_add_category(root, category: models.Category, level: int):
            item = CategoryItem(category)
            item.setText(('-' * level) + str(category))
            root.appendRow(item)
            for category in category.subcategories:
                recursive_add_category(root, category, level + 1)

        none_item = QtGui.QStandardItem('None')
        self.combo_root.appendRow(none_item)

        for category in top_level_categories:
            recursive_add_category(self.combo_root, category, 0)


class EditShelfView(QtWidgets.QWidget, Ui_EditShelf):

    update = QtCore.Signal(models.Shelf, str, str)

    def __init__(self, shelf: models.Shelf, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.shelf = shelf

        self.shelf_name.setText(shelf.name)
        self.shelf_description.setText(shelf.description)
        self.save_button.clicked.connect(self._save_shelf)

    def _save_shelf(self, *args):

        s = get_session()
        self.shelf.name = self.shelf_name.text()
        self.shelf.description = self.shelf_description.toPlainText()
        s.add(self.shelf)
        s.commit()

        self.update.emit(self.shelf, 'shelves_root', 'shelf')


class EditAuthorView(QtWidgets.QWidget, Ui_EditAuthor):

    update = QtCore.Signal(models.Author, str, str)

    def __init__(self, author: models.Author, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.author = author

        self.first_name.setText(author.first_name)
        self.middle_name.setText(author.middle_name)
        self.last_name.setText(author.last_name)

        self.save_button.clicked.connect(self._save_author)

    def _save_author(self, *args):

        s = get_session()
        self.author.first_name = self.first_name.text()
        self.author.middle_name = self.middle_name.text()
        self.author.last_name = self.last_name.text()
        s.add(self.author)
        s.commit()

        self.update.emit(self.author, 'authors_root', 'author')


class EditCategoryView(QtWidgets.QWidget, Ui_EditCategory):

    update = QtCore.Signal()

    def __init__(self, category: models.Category, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.category = category
        self.name.setText(str(category))
        self.save_button.clicked.connect(self._save_category)

        s = get_session()
        top_level_categories = s.query(models.Category).filter(
            models.Category.parent_id == None
        ).all()

        self.combo_model = QtGui.QStandardItemModel()
        self.combo_root = self.combo_model.invisibleRootItem()
        self.parent_category.setModel(self.combo_model)

        def recursive_add_category(root, category: models.Category, level: int):
            if category.id != self.category.id:
                item = CategoryItem(category)
                item.setText(('-' * level) + str(category))
                root.appendRow(item)
                for category in category.subcategories:
                    recursive_add_category(root, category, level + 1)

        none_item = QtGui.QStandardItem('None')
        self.combo_root.appendRow(none_item)

        for category in top_level_categories:
            recursive_add_category(self.combo_root, category, 0)

        parent_category, idx = self._find_parent_category(self.category)
        self.parent_category.setCurrentIndex(idx)

    def _save_category(self, *args):

        s = get_session()
        self.category.name = self.name.text()
        parent_idx = self.parent_category.currentIndex()
        if parent_idx > 0:
            item: CategoryItem = self.combo_model.item(parent_idx)
            self.category.parent_id = item.category.id
        else:
            self.category.parent_id = None
        s.add(self.category)
        s.commit()

        self.update.emit()

    def _find_parent_category(self, category: models.Category):

        for row in range(1, self.combo_root.rowCount()):
            item: CategoryItem = self.combo_root.child(row, 0)
            if category.parent_id == item.category.id:
                return item, row

        return None, 0


class EditFooView(QtWidgets.QWidget, Ui_EditDocument):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)


class EditDocumentView(QtWidgets.QWidget, Ui_EditDocument):

    update = QtCore.Signal()

    def __init__(self, document: models.Document, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.doc = document

        self.path.setText(self.doc.path)
        self.title.setText(self.doc.title)

        self.authors_model = QtGui.QStandardItemModel()
        self.authors.setModel(self.authors_model)

        for author in self.doc.authors:
            author_item = AuthorItem(author)
            self.authors_model.appendRow(author_item)

        self.save_button.clicked.connect(self._save_document)

    def _save_document(self, *args):

        s = get_session()
        self.doc.title = self.title.text()
        s.add(self.doc)
        s.commit()

        self.update.emit(self.doc, 'docs_root', 'document')
