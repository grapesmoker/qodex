import datetime
import time

import isbnlib
from PySide6.QtCore import QObject, QThread, QMutex, Slot, Signal, QRunnable
from crossref_commons.retrieval import get_publication_as_json

from qodex.db.models import Document, Category, Author
from qodex.db.settings import get_session
from qodex.db.utils import get_or_create
from qodex.doctools.pdf import extract_meta
from qodex.doctools.utils import rename
from qodex.common import WorkerSignals

from typing import List
from multiprocessing import Pool
from pathlib import Path
from logging import getLogger

import shutil


mutex = QMutex()
logger = getLogger(__name__)


class RenameController(QRunnable):

    def __init__(self, doc_ids: List[int], pattern: str, *args, **kwargs):
        super().__init__()
        s = get_session()
        self._document_ids = doc_ids
        self._pattern = pattern
        self.signals = WorkerSignals()

    @Slot()
    def run(self):

        with Pool() as pool:
            args = [(doc_id, self._pattern) for doc_id in self._document_ids]
            futures = pool.starmap_async(self._rename, args)
            for i, result in enumerate(futures.get()):
                self.signals.progress.emit(i + 1)
                print(result)
        self.signals.ready.emit()

    @staticmethod
    def _rename(doc_id: int, pattern: str):

        s = get_session()
        doc = s.query(Document).get(doc_id)
        new_filename = rename(pattern, doc)
        old_filename = Path(doc.path)
        try:
            print(f'{old_filename} -> {new_filename}')
            if not new_filename.exists():
                Path(doc.path).rename(new_filename)
                doc.path = str(new_filename)
                s.add(doc)
                s.commit()
        except Exception as ex:
            print(f'Something went wrong: {ex}')
            print('Reverting rename')
            if new_filename.exists():
                Path(new_filename).rename(old_filename)


class BulkMoveController(QRunnable):

    def __init__(self, base_path: str, collection_method: str, create_category_folders: bool):
        super().__init__()
        s = get_session()
        self._document_ids = [doc.id for doc in s.query(Document).all()]
        self._collection_method = collection_method
        self._create_category_folders = create_category_folders
        self._base_path = Path(base_path)
        self.signals = WorkerSignals()

    @Slot()
    def run(self) -> None:

        if self._create_category_folders:
            self._create_category_structure()

        with Pool() as pool:
            args = [(self._base_path, self._collection_method, doc_id) for doc_id in self._document_ids]
            futures = pool.starmap_async(self._stage_document, args)
            for i, result in enumerate(futures.get()):
                self.signals.progress.emit(i + 1)

    def _create_category_structure(self):

        s = get_session()
        all_categories = s.query(Category).all()

        for category in all_categories:
            ancestor_chain = map(str, category.get_ancestor_chain()[::-1])
            target_dir = self._base_path / '/'.join(ancestor_chain) / str(category)
            print(ancestor_chain, category)
            print(target_dir)
            if not target_dir.exists():
                target_dir.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def _stage_document(base_path: Path, collection_method: str, doc_id: int):

        s = get_session()
        doc = s.query(Document).get(doc_id)
        target_paths = BulkMoveController._determine_doc_path(base_path, doc)
        for path in target_paths:
            path.unlink(missing_ok=True)

        primary_path, other_paths = target_paths[0], target_paths[1:]

        if collection_method == 'copy':
            coll_func = shutil.copy2
        elif collection_method == 'move':
            coll_func = shutil.move
        else:
            raise ValueError('Unknown collection method.')

        try:
            coll_func(doc.path, primary_path)
        except shutil.SameFileError:
            pass
        for target in other_paths:
            try:
                target.symlink_to(primary_path)
            except shutil.SameFileError:
                pass
        if Path(doc.path) != primary_path and primary_path.exists():
            doc.path = str(primary_path)
            s.add(doc)
            s.commit()

        print(f'{doc.path} -> {primary_path}')

    @staticmethod
    def _determine_doc_path(base_path: Path, doc: Document) -> List[Path]:

        if len(doc.categories) == 0:
            paths = [base_path / Path(doc.path).name]
        else:
            paths = []
            for category in doc.categories:
                ancestor_chain = map(str, category.get_ancestor_chain()[::-1])
                paths.append(base_path / '/'.join(ancestor_chain) / str(category) / Path(doc.path).name)

        return paths


class ImportController(QRunnable):

    ready = Signal()

    def __init__(self, doc_ids: List[int], get_meta_from_file=True, *args, **kwargs):
        super().__init__()
        self._document_ids = doc_ids
        self._get_meta_from_file = get_meta_from_file
        self.signals = WorkerSignals()

    def run(self):

        with Pool() as pool:
            args = [(doc_id, self._get_meta_from_file) for doc_id in self._document_ids]
            futures = pool.starmap_async(self._update_doc_meta, args)
            for i, result in enumerate(futures.get()):
                self.signals.progress.emit(i + 1)
                print(result)
        self.signals.ready.emit()

    @staticmethod
    def fetch_meta(meta):

        try:
            if meta['isbn']:
                isbn_meta = isbnlib.meta(meta['isbn'])
            else:
                isbn_meta = {}
        except Exception as ex:
            logger.warning(f'Could not fetch ISBN data: {ex}')
            isbn_meta = {}

        print(isbn_meta)

        try:
            if meta['doi']:
                doi_meta = get_publication_as_json(meta['doi'])
            else:
                doi_meta = {}
        except Exception as ex:
            logger.warning(f'Could not fetch DOI data: {ex}')
            doi_meta = {}

        print(doi_meta)

        return isbn_meta, doi_meta

    @staticmethod
    def _process_author(doc: Document, author: List[str], session):

        if len(author) == 1:
            first_name = author[0]
            last_name = None
        else:
            first_name, last_name = author[0], author[-1]
        if len(author) > 2:
            middle_name = ' '.join(author[1:-1])
        else:
            middle_name = None
        mutex.lock()
        author, created = get_or_create(Author,
                                        first_name=first_name,
                                        last_name=last_name,
                                        middle_name=middle_name)
        if created:
            author.documents.append(doc)
            session.add(author)
            session.commit()
        mutex.unlock()

    @staticmethod
    def _update_doc_meta(doc_id: Document, get_meta_from_file: bool):

        session = get_session()
        doc = session.query(Document).get(doc_id)

        if get_meta_from_file:
            meta = extract_meta(Path(doc.path))
        else:
            meta = {'isbn': doc.isbn, 'doi': doc.doi}

        isbn_meta, doi_meta = ImportController.fetch_meta(meta)

        try:
            if isbn_meta:
                doc.isbn = isbn_meta.get('ISBN-13', None)
                for author in isbn_meta.get('Authors', []):
                    if author != '':
                        author = author.split()
                        ImportController._process_author(doc, author, session)
                doc.title = isbn_meta.get('Title', None)
                doc.publication = isbn_meta.get('Publisher', None)
                doc.date = datetime.date(year=int(isbn_meta['Year']), day=1, month=1) if 'Year' in isbn_meta else None
                doc.language = isbn_meta.get('Language', None)

        except Exception as ex:
            logger.error(f'Could not update ISBN metadata for {doc.path}: {ex}')

        try:
            if doi_meta:
                print('doi')
                doc.doi = doi_meta.get('DOI', None)
                date_created = doi_meta.get('created', None)
                if date_created:
                    date_parts = date_created.get('date_parts', None)
                    if date_parts and isinstance(date_parts, list):
                        doc.date = datetime.date(**date_parts[0])
                doc.title = doi_meta['title'][0]
                doc.doi = doi_meta['DOI']
                doc.issue = doi_meta.get('issue', None)
                doc.volume = doi_meta.get('volume', None)
                for author in doi_meta.get('author', []):
                    author = [author['given'], author['family']]
                    ImportController._process_author(doc, author, session)
                # TODO: handle this meta properly in a separate function, this is ok for now
        except Exception as ex:
            logger.error(f'Could not update DOI metadata for {doc.path}: {ex}')

        mutex.lock()
        session.add(doc)
        session.commit()
        mutex.unlock()
