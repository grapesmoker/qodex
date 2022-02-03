import logging
from pathlib import Path
from logging import getLogger
from PySide6 import QtWidgets, QtCore, QtGui, Qt
from PySide6.QtUiTools import QUiLoader
from pprint import pprint
from ui.mainwindow import Ui_QodexMain

from qodex.common import UpdateMode
from qodex.db import models
from qodex.db.utils import get_or_create
from qodex.db.settings import get_session
from qodex.dialogs import (
    NewShelfDialog, NewAuthorDialog, NewCategoryDialog,
    EditShelfView, EditAuthorView, EditCategoryView,
    EditDocumentView, MoveLibraryDialog
)
from qodex.item_models import ShelfItem, AuthorItem, CategoryItem, DocumentItem
from qodex.doctools.pdf import extract_meta
from qodex.doctools.meta import MetaUpdater
from qodex.doctools.batch import RenameController, BulkMoveController


logger = getLogger(__name__)
logger.setLevel(logging.DEBUG)


class MainWindow(QtWidgets.QMainWindow, Ui_QodexMain):

    author_added = QtCore.Signal(models.Author)
    document_added = QtCore.Signal(models.Document)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loader = QUiLoader()
        self._setup_models()

        self.thread_pool = QtCore.QThreadPool()

        self.action_add_shelf.triggered.connect(self.new_shelf)
        self.action_add_author.triggered.connect(self.new_author)
        self.action_add_category.triggered.connect(self.new_category)
        self.action_add_document.triggered.connect(self.new_document)

        self.rename_selection.triggered.connect(self._bulk_rename_selection)
        self.rename_all.triggered.connect(self._bulk_rename_all)
        self.action_move_library.triggered.connect(self._move_library)
        self.splitter.setSizes([10000, 10000])

    def _setup_models(self):

        self.tree_model = QtGui.QStandardItemModel()
        self.tree_root = self.tree_model.invisibleRootItem()
        self.tree_model.setHorizontalHeaderLabels(['Library'])

        self.shelf_model = QtGui.QStandardItemModel()
        self.shelf_model.setHorizontalHeaderLabels(ShelfItem.labels)

        self.documents_model = QtGui.QStandardItemModel()
        self.documents_model.setHorizontalHeaderLabels(DocumentItem.labels)

        self.authors_model = QtGui.QStandardItemModel()
        self.authors_model.setHorizontalHeaderLabels(AuthorItem.labels)

        self.categories_model = QtGui.QStandardItemModel()
        self.categories_root = self.categories_model.invisibleRootItem()
        self.categories_model.setHorizontalHeaderLabels(['Categories'])

        self.shelf_view.setModel(self.shelf_model)
        self.shelf_view.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.shelf_view.clicked.connect(self._shelf_selected)

        self.documents_view.setModel(self.documents_model)
        self.documents_view.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.documents_view.clicked.connect(self._document_selected)

        self.authors_view.setModel(self.authors_model)
        self.authors_view.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.authors_view.clicked.connect(self._author_selected)

        self.categories_view.setModel(self.categories_model)
        self.categories_view.clicked.connect(self._category_selected)

        self._load_data(models.Shelf, ShelfItem, self.shelf_model)
        self._load_data(models.Author, AuthorItem, self.authors_model)
        self._load_data(models.Document, DocumentItem, self.documents_model)
        self._load_categories()

    @staticmethod
    def _load_data(model, item_model, root):

        s = get_session()
        data_items = s.query(model).all()
        for i, data_item in enumerate(data_items):
            item = item_model(data_item)
            children = []
            for col, display_field in enumerate(item_model.display_fields):
                children.append(QtGui.QStandardItem(str(getattr(item.model, display_field))))
            root.appendRow(children)
            root.setData(root.index(i, 0), data_item, QtCore.Qt.UserRole)

    def _load_categories(self):

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

    def _shelf_selected(self, index: QtCore.QModelIndex):

        row_idx = self.shelf_model.index(index.row(), 0)
        data_item = self.shelf_model.itemData(row_idx)[QtCore.Qt.UserRole]

        widget = EditShelfView(data_item, index)
        widget.update.connect(self._refresh_shelves)
        self.properties_scroll.setWidget(widget)
        widget.show()

    def _document_selected(self, index: QtCore.QModelIndex):

        row_idx = self.documents_model.index(index.row(), 0)
        data_item = self.documents_model.itemData(row_idx)[QtCore.Qt.UserRole]

        widget = EditDocumentView(data_item, row_idx)
        widget.update.connect(self._refresh_documents)
        widget.new_author.connect(self.new_author)
        self.author_added.connect(widget.update_author_list)
        self.properties_scroll.setWidget(widget)
        widget.show()

    def _author_selected(self, index: QtCore.QModelIndex):

        row_idx = self.authors_model.index(index.row(), 0)
        data_item = self.authors_model.itemData(row_idx)[QtCore.Qt.UserRole]

        widget = EditAuthorView(data_item, row_idx)
        widget.update.connect(self._refresh_authors)
        self.properties_scroll.setWidget(widget)
        widget.show()

    def _category_selected(self, index: QtCore.QModelIndex, *args):

        data_item = self.categories_model.itemFromIndex(index).category

        widget = EditCategoryView(data_item, index)
        widget.update.connect(self._refresh_categories)
        self.properties_scroll.setWidget(widget)
        widget.show()

    def _refresh_authors(self, instance: models.Author, index: QtCore.QModelIndex):

        for col, display_field in enumerate(AuthorItem.display_fields):
            self.authors_model.setItem(index.row(), col, QtGui.QStandardItem(getattr(instance, display_field)))

        self.authors_model.setData(self.authors_model.index(index.row(), 0), instance, QtCore.Qt.UserRole)

    def _refresh_shelves(self, instance: models.Shelf, index: QtCore.QModelIndex):

        for col, display_field in enumerate(ShelfItem.display_fields):
            self.shelf_model.setItem(index.row(), col, QtGui.QStandardItem(getattr(instance, display_field)))

        self.shelf_model.setData(self.shelf_model.index(index.row(), 0), instance, QtCore.Qt.UserRole)

    def _refresh_documents(self, instance: models.Document, index: QtCore.QModelIndex, mode=UpdateMode.UPDATE):

        if mode == UpdateMode.UPDATE:
            for col, display_field in enumerate(DocumentItem.display_fields):
                print(index.row(), col)
                self.documents_model.setItem(index.row(), col, QtGui.QStandardItem(getattr(instance, display_field)))

            self.documents_model.setData(self.documents_model.index(index.row(), 0), instance, QtCore.Qt.UserRole)
        elif mode == UpdateMode.DELETE:
            self.documents_model.removeRow(index.row())
            widget = self.properties_scroll.takeWidget()
            widget.deleteLater()

    def _refresh_categories(self, *_):

        # this isn't efficient in general, but it accounts for the fact that the category hierarchy
        # can change and there's no good way of doing surgery on the tree to account for that. and
        # there aren't going to be that many categories anyway probably
        # FIXME: do this correctly
        self.categories_model.clear()
        self._load_categories()

    def _refresh_all_docs(self):
        self.documents_model.clear()
        self._load_data(models.Document, DocumentItem, self.documents_model)

    def _find_parent_category(self, category: models.Category):

        s = get_session()
        parent = s.query(models.Category).get(category.parent_id)
        categories = self.categories_model.findItems(str(parent), QtCore.Qt.MatchRecursive)
        for candidate in categories:  # type: CategoryItem
            if parent.id == candidate.category.id:
                return candidate
        return self.categories_root

    def new_shelf(self, *_):

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
                idx = self.shelf_model.createIndex(self.shelf_model.rowCount(), 0)
                self._refresh_shelves(shelf, idx)
            else:
                msg = QtWidgets.QMessageBox(self)
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setWindowTitle('Shelf exists')
                msg.setText(f'A shelf named "{shelf.name}" already exists.')
                msg.exec_()

    def new_author(self, *_):

        dlg = NewAuthorDialog()
        if dlg.exec_():
            s = get_session()
            author, created = get_or_create(models.Author,
                                            session=s,
                                            first_name=dlg.first_name.text(),
                                            middle_name=dlg.middle_name.text(),
                                            last_name=dlg.last_name.text())
            if created:
                idx = self.authors_model.createIndex(self.authors_model.rowCount(), 0)
                self._refresh_authors(author, idx)
                self.author_added.emit(author)
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
            # don't repeat work we've already done
            if created:
                update_worker = MetaUpdater(doc.id, parent=self)
                update_worker.finished.connect(update_worker.deleteLater)
                update_worker.ready.connect(
                    lambda: self._refresh_documents(
                        doc,
                        self.documents_model.createIndex(self.documents_model.rowCount(), 0)
                    )
                )
                update_worker.start()

        self._load_data(models.Author, AuthorItem, self.authors_model)
        self._load_data(models.Document, DocumentItem, self.documents_model)

    def _bulk_rename_all(self):

        s = get_session()
        doc_ids = [doc.id for doc in s.query(models.Document).all()]
        self._bulk_rename(doc_ids)

    def _bulk_rename_selection(self):

        selection = self.documents_view.selectedIndexes()
        doc_items = [self.documents_model.itemData(idx) for idx in selection]
        doc_ids = []
        for item in doc_items:
            doc = item.get(QtCore.Qt.UserRole, None)
            if doc:
                doc_ids.append(doc.id)
        self._bulk_rename(doc_ids)

    def _bulk_rename(self, doc_ids):

        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(len(doc_ids))

        title = 'Rename files'
        msg = """Enter the format string for renaming the document. Allowed field values are:\n\n""" \

        default = '{title} - {authors}.pdf'
        pattern, ok = QtWidgets.QInputDialog.getText(self, title, msg, QtWidgets.QLineEdit.Normal, default)

        if ok:
            rename_worker = RenameController(doc_ids, pattern)
            rename_worker.signals.progress.connect(lambda i: self.progress_bar.setValue(i))
            rename_worker.signals.ready.connect(self._refresh_all_docs)
            self.thread_pool.start(rename_worker)

    def _move_library(self):

        s = get_session()
        dlg = MoveLibraryDialog()

        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(s.query(models.Document).count())

        if dlg.exec_():
            base_path = dlg.library_path.text()
            if str(base_path).strip() == '':
                msg = QtWidgets.QMessageBox(self)
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setWindowTitle('Invalid directory!')
                msg.setText(f'You have selected an invalid directory: {base_path}. Please choose a valid '
                            f'directory into which you want to put your files.')
                msg.exec_()
            else:
                if dlg.method_copy.isChecked():
                    method = 'copy'
                elif dlg.method_move.isChecked():
                    method = 'move'
                else:
                    raise ValueError('Unknown method state!')
                create_category_folders = dlg.create_category_folders.isChecked()
                move_worker = BulkMoveController(base_path, method, create_category_folders)
                move_worker.signals.progress.connect(lambda i: self.progress_bar.setValue(i))
                move_worker.signals.ready.connect(self._refresh_all_docs)
                self.thread_pool.start(move_worker)
