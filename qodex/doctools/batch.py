import time

from PySide6.QtCore import QObject, QThread, QMutex, Slot, Signal, QRunnable
from qodex.db.models import Document, Category
from qodex.db.settings import get_session
from qodex.doctools.utils import rename
from qodex.common import WorkerSignals

from typing import List
from multiprocessing import Pool
from pathlib import Path
import shutil


def renamer_func(doc: Document, pattern: str):

    time.sleep(0.25)
    return doc.path


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
