from pathlib import Path
from typing import List

from PySide6 import QtWidgets, QtCore, QtGui, Qt

from ui.new_shelf import Ui_NewShelfDialog
from ui.new_author import Ui_NewAuthorDialog
from ui.edit_shelf import Ui_EditShelf
from ui.edit_author import Ui_EditAuthor
from ui.new_category import Ui_NewCategoryDialog
from ui.edit_category import Ui_EditCategory
from ui.edit_document import Ui_EditDocument
from ui.select_author import Ui_SelectAuthorDialog
from ui.select_shelves import Ui_SelectShelvesDialog
from ui.move_library import Ui_MoveLibrary

from qodex.common import UpdateMode
from qodex.db.settings import get_session
from qodex.db import models
from qodex.item_models import AuthorItem, CategoryItem, ShelfItem, DocumentItem
from qodex.doctools.batch import ImportController
from qodex.doctools.utils import rename


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


class SelectAuthorDialog(QtWidgets.QDialog, Ui_SelectAuthorDialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.authors_model = QtGui.QStandardItemModel()
        self.authors_view.setModel(self.authors_model)

        s = get_session()

        all_authors = s.query(models.Author).order_by(models.Author.last_name).all()

        for author in all_authors:
            self.authors_model.appendRow(AuthorItem(author))


class SelectShelvesDialog(QtWidgets.QDialog, Ui_SelectShelvesDialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.shelf_model = QtGui.QStandardItemModel()
        self.shelf_view.setModel(self.shelf_model)

        s = get_session()

        all_authors = s.query(models.Shelf).all()

        for author in all_authors:
            self.shelf_model.appendRow(ShelfItem(author))


class EditShelfView(QtWidgets.QWidget, Ui_EditShelf):

    update = QtCore.Signal(models.Shelf, QtCore.QModelIndex)

    def __init__(self, shelf: models.Shelf, index=None, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.shelf = shelf
        self.index = index

        self.shelf_name.setText(shelf.name)
        self.shelf_description.setText(shelf.description)
        self.save_button.clicked.connect(self._save_shelf)

        self.documents_model = QtGui.QStandardItemModel()
        self.documents.setModel(self.documents_model)
        self.documents.customContextMenuRequested.connect(self._docs_context_menu)
        for doc in self.shelf.documents:
            doc_item = DocumentItem(doc)
            self.documents_model.appendRow(doc_item)

    def _save_shelf(self, *args):

        s = get_session()
        self.shelf.name = self.shelf_name.text()
        self.shelf.description = self.shelf_description.toPlainText()
        s.add(self.shelf)
        s.commit()

        self.update.emit(self.shelf, self.index)

    def _docs_context_menu(self, coords: QtCore.QPoint):

        selection = self.documents.selectedIndexes()
        menu = QtWidgets.QMenu(self)
        add_to_shelf = QtGui.QAction('Add documents')
        # add_to_shelf.triggered.connect(self._add_shelf)
        menu.addAction(add_to_shelf)
        if len(selection) > 0:
            remove_from_shelf = QtGui.QAction('Remove from shelf')
            remove_from_shelf.triggered.connect(lambda _: self._remove_documents(selection))
            menu.addAction(remove_from_shelf)

        result = menu.exec_(self.documents.viewport().mapToGlobal(coords))

    def _remove_documents(self, selection: List[QtCore.QModelIndex]):

        s = get_session()
        for idx in sorted(selection, key=lambda index: index.row(), reverse=True):
            doc_item = self.documents_model.itemFromIndex(idx)
            self.shelf.documents.remove(doc_item.document)
            self.documents_model.removeRow(idx.row())
        s.commit()


class EditAuthorView(QtWidgets.QWidget, Ui_EditAuthor):

    update = QtCore.Signal(models.Author, QtCore.QModelIndex)

    def __init__(self, author: models.Author, index=None, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.author = author
        self.index = index

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

        self.update.emit(self.author, self.index)


class EditCategoryView(QtWidgets.QWidget, Ui_EditCategory):

    update = QtCore.Signal(models.Category, QtCore.QModelIndex)

    def __init__(self, category: models.Category, index=None, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.category = category
        self.index = index
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

        self.update.emit(self.category, self.index)

    def _find_parent_category(self, category: models.Category):

        for row in range(1, self.combo_root.rowCount()):
            item: CategoryItem = self.combo_root.child(row, 0)
            if category.parent_id == item.category.id:
                return item, row

        return None, 0


class EditDocumentView(QtWidgets.QWidget, Ui_EditDocument):

    update = QtCore.Signal(models.Document, QtCore.QModelIndex, UpdateMode)
    new_author = QtCore.Signal()

    RENAME_FIELDS =  ['author', 'title', 'edition', 'volume', 'pages', 'series', 'date']

    def __init__(self, document: models.Document, index=None, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.doc = document
        self.index = index
        self.authors_model = QtGui.QStandardItemModel()
        self.categories_model = QtGui.QStandardItemModel()
        self.shelf_model = QtGui.QStandardItemModel()
        self.categories_root = self.categories_model.invisibleRootItem()
        self.category.setModel(self.categories_model)
        self.authors.setModel(self.authors_model)
        self.shelves.setModel(self.shelf_model)
        self._show_data()
        self._set_up_signals()
        self._set_up_categories()
        self._thread_pool = QtCore.QThreadPool()

    def _show_data(self):

        s = get_session()
        s.refresh(self.doc)

        self.path.setText(self.doc.path)
        self.title.setText(self.doc.title)
        self._populate_types()
        self.doi.setText(self.doc.doi)
        self.isbn.setText(self.doc.isbn)
        self.url.setText(self.doc.url)
        self.doc_abstract.setText(self.doc.abstract)
        self.publication.setText(self.doc.publication)
        self.edition.setText(self.doc.edition)
        self.volume.setText(self.doc.volume)
        self.issue.setText(self.doc.issue)
        self.pages.setText(self.doc.pages)
        self.date.setDate(self.doc.date)
        self.series.setText(self.doc.series)
        self.language.setText(self.doc.language)

        self.authors_model.clear()
        for author in self.doc.authors:
            author_item = AuthorItem(author)
            self.authors_model.appendRow(author_item)

        self.shelf_model.clear()
        for shelf in self.doc.shelves:
            shelf_item = ShelfItem(shelf)
            self.shelf_model.appendRow(shelf_item)

    def _set_up_categories(self):

        s = get_session()
        top_level_categories = s.query(models.Category).filter(
            models.Category.parent_id == None
        ).all()

        def recursive_add_category(root, category: models.Category):
            item = CategoryItem(category)
            item.setText(str(category))
            root.appendRow(item)
            for category in category.subcategories:
                recursive_add_category(item, category)

        for category in top_level_categories:
            recursive_add_category(self.categories_root, category)

        for category in self.doc.categories:
            category_item = self._find_category(category)
            self.category.selectionModel().select(category_item.index(), QtCore.QItemSelectionModel.Select)

        self.category.expandAll()

    def _find_category(self, category: models.Category):

        categories = self.categories_model.findItems(str(category), QtCore.Qt.MatchRecursive)
        for candidate in categories:  # type: CategoryItem
            if category.id == candidate.category.id:
                return candidate
        return None

    def _find_parent_category(self, category: models.Category):

        s = get_session()
        parent = s.query(models.Category).get(category.parent_id)
        categories = self.categories_model.findItems(str(parent), QtCore.Qt.MatchRecursive)
        for candidate in categories:  # type: CategoryItem
            if parent.id == candidate.category.id:
                return candidate
        return self.categories_root

    def _set_up_signals(self):

        self.document_type.activated.connect(lambda x: print(x))
        self.save_button.clicked.connect(self._save_document)
        self.update_meta_button.clicked.connect(self._refresh_metadata)
        self.rename_file_button.clicked.connect(self._rename_document_file)
        self.delete_button.clicked.connect(self._remove_document)
        self.view_button.clicked.connect(self._view_document)
        self.authors.customContextMenuRequested.connect(self._author_context_menu)
        self.shelves.customContextMenuRequested.connect(self._shelf_context_menu)

    def _populate_types(self):

        s = get_session()
        self.document_type.insertItem(0, 'None', userData=None)
        current_index = 0
        for i, document_type in enumerate(s.query(models.DocumentType).all()):
            self.document_type.insertItem(i + 1, document_type.display_title, userData=document_type)
            if self.doc.document_type is not None and self.doc.document_type.id == document_type.id:
                current_index = i + 1
        self.document_type.setCurrentIndex(current_index)

    def _save_document(self, *args):

        s = get_session()
        self.doc.title = self.title.text()
        self.doc.doi = self.doi.text()
        self.doc.isbn = self.isbn.text()
        self.doc.url = self.url.text()
        self.doc.abstract = self.doc_abstract.toPlainText()
        self.doc.publication = self.publication.text()
        self.doc.edition = self.edition.text()
        self.doc.volume = self.volume.text()
        self.doc.issue = self.issue.text()
        self.doc.pages = self.pages.text()
        self.doc.date = self.date.date().toPython()
        self.doc.series = self.series.text()
        self.doc.language = self.language.text()

        document_type = self.document_type.itemData(self.document_type.currentIndex())
        self.doc.document_type = document_type
        for category_index in self.category.selectionModel().selectedIndexes():
            category_item = self.categories_model.itemFromIndex(category_index)
            # category_item = self.categories_root.child(self.category.currentIndex(), 0)
            self.doc.categories.append(category_item.category)

        s.add(self.doc)
        s.commit()

        self.update.emit(self.doc, self.index, UpdateMode.UPDATE)

    def _remove_document(self, *args):

        msg = 'Really remove this document from the library? This operation cannot be undone, but your file ' \
              'will not be deleted.'
        really_delete = QtWidgets.QMessageBox.question(
            self, 'Delete?', msg, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if really_delete == QtWidgets.QMessageBox.Yes:
            s = get_session()
            s.delete(self.doc)
            s.commit()
            self.update.emit(self.doc, self.index, UpdateMode.DELETE)

    def _view_document(self, *args):

        QtGui.QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile(self.doc.path))

    def _refresh_metadata(self, *args):

        # title = 'Refresh metadata?'
        # msg = 'Metadata will be replaced by any data that is obtained from metadata servers. Continue?'
        # really_refresh = QtWidgets.QMessageBox.question(
        #     self, title, msg, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        really_refresh = QtWidgets.QMessageBox.Yes

        if really_refresh == QtWidgets.QMessageBox.Yes:
            update_worker = ImportController([self.doc.id], get_meta_from_file=False, parent=self)
            update_worker.signals.ready.connect(self._show_data)
            update_worker.signals.ready.connect(lambda: self.update.emit(self.doc, self.index, UpdateMode.UPDATE))
            self._thread_pool.start(update_worker)

    def _author_context_menu(self, coords: QtCore.QPoint):

        selection = self.authors.selectedIndexes()
        menu = QtWidgets.QMenu(self)
        add_new_author = QtGui.QAction('Add new author')
        add_new_author.triggered.connect(lambda _: self.new_author.emit())
        menu.addAction(add_new_author)
        add_existing_author = QtGui.QAction('Add existing author')
        add_existing_author.triggered.connect(self._add_existing_author)
        menu.addAction(add_existing_author)

        if len(selection) > 0:
            remove_authors = QtGui.QAction('Remove author(s)')
            remove_authors.triggered.connect(lambda _: self._remove_authors(selection))
            menu.addAction(remove_authors)

        result = menu.exec_(self.authors.viewport().mapToGlobal(coords))

    def _shelf_context_menu(self, coords: QtCore.QPoint):

        selection = self.shelves.selectedIndexes()
        menu = QtWidgets.QMenu(self)
        add_to_shelf = QtGui.QAction('Add to shelf')
        add_to_shelf.triggered.connect(self._add_shelf)
        menu.addAction(add_to_shelf)
        if len(selection) > 0:
            remove_from_shelf = QtGui.QAction('Remove from shelf')
            remove_from_shelf.triggered.connect(lambda _: self._remove_shelves(selection))
            menu.addAction(remove_from_shelf)

        result = menu.exec_(self.shelves.viewport().mapToGlobal(coords))

    @QtCore.Slot(models.Author)
    def update_author_list(self, author: models.Author):

        print(f'added {author}')
        self.authors_model.appendRow(AuthorItem(author))
        s = get_session()
        author.documents.append(self.doc)
        s.commit()

    def _remove_authors(self, selection: List[QtCore.QModelIndex]):

        s = get_session()
        for idx in sorted(selection, key=lambda index: index.row(), reverse=True):
            author_item = self.authors_model.itemFromIndex(idx)
            self.doc.authors.remove(author_item.author)
            self.authors_model.removeRow(idx.row())
        s.commit()

    def _remove_shelves(self, selection: List[QtCore.QModelIndex]):

        s = get_session()
        for idx in sorted(selection, key=lambda index: index.row(), reverse=True):
            shelf_item = self.shelf_model.itemFromIndex(idx)
            self.doc.shelves.remove(shelf_item.shelf)
            self.shelf_model.removeRow(idx.row())
        s.commit()

    def _add_existing_author(self):

        dlg = SelectAuthorDialog()
        if dlg.exec_():
            selected_indexes = dlg.authors_view.selectedIndexes()
            selected_authors = [dlg.authors_model.itemFromIndex(index).author for index in selected_indexes]
            s = get_session()
            for author in selected_authors:
                self.doc.authors.append(author)
                self.authors_model.appendRow(AuthorItem(author))
            s.commit()
            self.update.emit(self.doc, self.index, UpdateMode.UPDATE)

    def _add_shelf(self):

        dlg = SelectShelvesDialog()
        if dlg.exec_():
            selected_indexes = dlg.shelf_view.selectedIndexes()
            selected_shelves = [dlg.shelf_model.itemFromIndex(index).shelf for index in selected_indexes]
            s = get_session()
            for shelf in selected_shelves:
                self.doc.shelves.append(shelf)
                self.shelf_model.appendRow(ShelfItem(shelf))
            s.commit()
            self.update.emit(self.doc, self.index, UpdateMode.UPDATE)

    def _rename_document_file(self):

        title = 'Rename file'
        msg = """Enter the format string for renaming the document. Allowed field values are:
            {last_name}, {first_name}, {author}, {authors_last_names}, {authors}, {title}, {categories}
           """
        default = '{title} - {authors}.pdf'
        pattern, ok = QtWidgets.QInputDialog.getText(self, title, msg, QtWidgets.QLineEdit.Normal, default)

        if ok:
            new_name = rename(pattern, self.doc)
            msg = f'Renaming {self.doc.path} -> {new_name}'
            really_rename = QtWidgets.QMessageBox.question(
                self, 'Rename?', msg, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if really_rename == QtWidgets.QMessageBox.Yes:
                Path(self.doc.path).rename(new_name)
                self.doc.path = str(new_name)
                s = get_session()
                s.add(self.doc)
                s.commit()
                self.path.setText(str(new_name))
                self.update.emit(self.doc, self.index, UpdateMode.UPDATE)


class MoveLibraryDialog(QtWidgets.QDialog, Ui_MoveLibrary):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.select_folder.clicked.connect(self._select_folder)

    def _select_folder(self):

        directory = QtWidgets.QFileDialog.getExistingDirectory(self)
        self.library_path.setText(directory)
