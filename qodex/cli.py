#!/usr/bin/env python3
"""Console script for qodex."""
import multiprocessing
import os
import sys
import click
import time
from PySide6 import QtCore, QtGui, QtWidgets
import logging
from rich.logging import RichHandler
from rich.progress import track
from pathlib import Path

from qodex.db.models import Document
from qodex.db.settings import get_session

sys.path.append(str(Path(__file__).parent.parent))
from qodex.doctools.batch import CLIImportController, ImportController
from qodex.app import MainWindow


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(RichHandler(markup=True))


@click.group()
def qodex(args=None):

    pass


@qodex.command()
def run():

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()


@qodex.command()
@click.argument('import_path', type=click.Path(exists=True, file_okay=False, resolve_path=True, path_type=Path))
@click.option('--pages', default=10, type=click.INT)
@click.option('--processes', default=multiprocessing.cpu_count() // 4, type=click.INT)
@click.option('--ocr-meta', default=True, type=click.BOOL)
def bulk_import(import_path: Path, pages: int, processes: int, ocr_meta=True):

    limit = os.environ.get('OMP_THREAD_LIMIT', None)
    logger.info(f'Extracting metadata from files in {import_path}')
    logging.info(f'Using {processes} processes, thread limit is {limit}')
    ocr = CLIImportController(import_path, pages=pages, processes=processes, ocr_meta=ocr_meta)
    ocr.run()


@qodex.command()
@click.option('--pages', default=0, type=click.INT)
@click.option('--processes', default=multiprocessing.cpu_count() // 4, type=click.INT)
@click.option('--num-docs', default=1e10, type=click.INT)
@click.option('--ignore-current', default=False, type=click.BOOL)
@click.option('--fulltext', default=False, type=click.BOOL)
@click.option('--multiprocess', default=True, type=click.BOOL)
def ocr_docs(pages: int, processes: int, num_docs: int, ignore_current: bool, fulltext: bool, multiprocess: bool):

    s = get_session()
    doc_paths = sorted(
        [Path(doc.path)
         for doc in
         s.query(Document).filter(
             Document.authors == None
         ).filter(
             Document.isbn.is_(None)
         ).filter(
            Document.full_text.is_(None)
         ).all()]
    )

    limit = os.environ.get('OMP_THREAD_LIMIT', None)
    logger.info(f'Extracting OCR metadata from {len(doc_paths)} files')
    logging.info(f'Using {processes} processes, thread limit is {limit}')
    ocr = CLIImportController(
        doc_paths[0:num_docs],
        pages=pages,
        processes=processes,
        ocr_meta=True,
        ignore_current=ignore_current,
        fulltext=fulltext,
        multiprocess=multiprocess)
    ocr.run()


@qodex.command()
def bulk_refresh_meta():

    s = get_session()
    docs = s.query(Document).filter(Document.authors == None).filter(Document.isbn.is_not(None)).all()

    for doc in track(docs):
        ImportController.update_doc_meta(doc.id, False)
        time.sleep(0.5)


if __name__ == "__main__":
    sys.exit(qodex())  # pragma: no cover
