import datetime
import logging
import isbnlib
import crossref_commons.retrieval
import threading

from pprint import pprint
from typing import List
from pathlib import Path
from logging import getLogger
from PySide6 import QtWidgets, QtCore, QtGui, Qt
from PySide6.QtUiTools import QUiLoader

from ui.mainwindow import Ui_Qodex

from qodex.db import models
from qodex.db.utils import get_or_create
from qodex.db.settings import get_session
from qodex.dialogs import (
    NewShelfDialog, NewAuthorDialog, NewCategoryDialog,
    EditShelfView, EditAuthorView, EditCategoryView,
    EditDocumentView, EditFooView
)
from qodex.item_models import ShelfItem, AuthorItem, CategoryItem, DocumentItem
from qodex.doctools.pdf import extract_meta
from qodex.doctools.meta import MetaUpdater


logger = getLogger(__name__)
logger.setLevel(logging.DEBUG)


class MainWindow(QtWidgets.QMainWindow, Ui_Qodex):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loader = QUiLoader()
        self._setup_models()

        self.action_add_shelf.triggered.connect(self.new_shelf)
        self.action_add_author.triggered.connect(self.new_author)
        self.action_add_category.triggered.connect(self.new_category)
        self.action_add_document.triggered.connect(self.new_document)

    def _setup_models(self):

        self.tree_model = QtGui.QStandardItemModel()
        self.tree_root = self.tree_model.invisibleRootItem()
        self.tree_model.setHorizontalHeaderLabels(['Library'])

        self.docs_root = QtGui.QStandardItem('Documents')
        self.authors_root = QtGui.QStandardItem('Authors')
        self.categories_root = QtGui.QStandardItem('Categories')
        self.shelves_root = QtGui.QStandardItem('Shelves')

        self.tree_root.appendRows([self.docs_root, self.authors_root, self.categories_root, self.shelves_root])

        self.treeView.setModel(self.tree_model)
        self.treeView.clicked.connect(self._tree_item_selected)

        self._load_data(models.Shelf, ShelfItem, self.shelves_root)
        self._load_data(models.Author, AuthorItem, self.authors_root)
        self._load_data(models.Document, DocumentItem, self.docs_root)
        self._load_catetories()

    @staticmethod
    def _load_data(model, item_model, root):

        s = get_session()
        data_items = s.query(model).all()
        for data_item in data_items:
            item = item_model(data_item)
            root.appendRow(item)

    def _load_catetories(self):

        s = get_session()
        parent_categories = s.query(models.Category).filter(
            models.Category.parent_id == None
        ).all()

        self.categories_root.removeRows(0, self.categories_root.rowCount())

        def recursive_add_category(root, category: models.Category):
            item = CategoryItem(category)
            item.setText(str(category))
            root.appendRow(item)
            for category in category.subcategories:
                recursive_add_category(item, category)

        for category in parent_categories:
            recursive_add_category(self.categories_root, category)

    def _tree_item_selected(self, index: QtCore.QModelIndex):

        logger.debug(index)
        item = self.tree_model.itemFromIndex(index)
        logger.debug(item)

        for child in self.frame.children():
            child.deleteLater()

        if isinstance(item, ShelfItem):
            widget = EditShelfView(item.shelf, parent=self.frame)
            widget.update.connect(self._refresh_tree)
            widget.show()
        elif isinstance(item, AuthorItem):
            widget = EditAuthorView(item.author, parent=self.frame)
            widget.update.connect(self._refresh_tree)
            widget.show()
        elif isinstance(item, CategoryItem):
            widget = EditCategoryView(item.category, parent=self.frame)
            widget.update.connect(self._load_catetories)
            widget.show()
        elif isinstance(item, DocumentItem):
            widget = EditDocumentView(item.document, parent=self.frame)
            widget.update.connect(self._refresh_tree)
            widget.show()
        else:
            logger.debug('unknown type')

    # @QtCore.Slot(models.Author, str, str)
    def _refresh_tree(self, instance, root: str, item_model: str):

        tree_root = getattr(self, root)
        for row in range(tree_root.rowCount()):
            item = tree_root.child(row, 0)
            if getattr(item, item_model).id == instance.id:
                setattr(item, item_model, instance)
                item.setText(str(instance))

    def _find_parent_category(self, category: models.Category):

        for row in range(self.categories_root.rowCount()):
            item: CategoryItem = self.categories_root.child(row, 0)
            if category.parent_id == item.category.id:
                return item

    def new_shelf(self, s):

        logger.debug(f'adding shelf {s}')
        dlg = NewShelfDialog()
        if dlg.exec_():
            s = get_session()
            shelf, created = get_or_create(models.Shelf,
                                           session=s,
                                           name=dlg.shelf_name.text())
            if created:
                shelf.description = dlg.shelf_description.toPlainText()
                s.add(shelf)
                s.commit()
                shelf_item = ShelfItem(shelf)
                self.shelves_root.appendRow(shelf_item)
            else:
                msg = QtWidgets.QMessageBox(self)
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setWindowTitle('Shelf exists')
                msg.setText(f'A shelf named "{shelf.name}" already exists.')
                msg.exec_()

    def new_author(self, s):

        print('adding author', s)
        dlg = NewAuthorDialog()
        if dlg.exec_():
            s = get_session()
            author, created = get_or_create(models.Author,
                                            session=s,
                                            first_name=dlg.first_name.text(),
                                            middle_name=dlg.middle_name.text(),
                                            last_name=dlg.last_name.text())
            if created:
                author_item = AuthorItem(author)
                self.authors_root.appendRow(author_item)
            else:
                msg = QtWidgets.QMessageBox(self)
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setWindowTitle('Author exists')
                msg.setText(f'An author named "{author}" already exists.')
                msg.exec_()

    def new_category(self):

        s = get_session()
        top_level_categories = s.query(models.Category).filter(
            models.Category.parent_id == None
        ).all()

        dlg = NewCategoryDialog(top_level_categories)
        if dlg.exec_():
            category, created = get_or_create(models.Category,
                                              session=s,
                                              name=dlg.name.text())
            parent_category_idx = dlg.parent_category.currentIndex()
            if parent_category_idx > 0:
                parent_category_item = dlg.combo_model.item(parent_category_idx)
                category.parent_id = parent_category_item.category.id
                s.add(category)
                s.commit()
            if created:
                category_item = CategoryItem(category)
                parent_category_item = self._find_parent_category(category)
                parent_category_item.appendRow(category_item)
            else:
                msg = QtWidgets.QMessageBox(self)
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setWindowTitle('Category exists')
                msg.setText(f'A category named "{category}" already exists.')
                msg.exec_()

    def new_document(self):

        home = Path.home()
        filenames, filters = QtWidgets.QFileDialog.getOpenFileNames(
            self, 'Select file', str(home), '*.pdf')

        for file in filenames:
            doc, created = get_or_create(models.Document, path=file)

            update_worker = MetaUpdater(doc.id, parent=self)
            update_worker.finished.connect(update_worker.deleteLater)
            if not created:
                update_worker.ready.connect(
                    lambda: self._refresh_tree(doc, 'docs_root', 'document')
                )
            else:
                update_worker.ready.connect(
                    lambda: self.docs_root.appendRow(DocumentItem(doc))
                )

            update_worker.start()
