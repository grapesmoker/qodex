#!/usr/bin/env python3
"""Console script for qodex."""
import multiprocessing
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
logger.setLevel(logging.DEBUG)
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
@click.argument('output_file', type=click.Path(resolve_path=True, dir_okay=False, path_type=Path))
@click.option('--pages', default=10, type=click.INT)
@click.option('--processes', default=multiprocessing.cpu_count() // 4, type=click.INT)
@click.option('--ocr-meta', default=True, type=click.BOOL)
def bulk_import(import_path: Path, output_file: Path, pages: int, processes: int, ocr_meta=True):

    import os
    limit = os.environ.get('OMP_THREAD_LIMIT', None)
    logger.info(f'Extracting metadata from files in {import_path} into {output_file}')
    logging.info(f'Using {processes} processes, thread limit is {limit}')
    ocr = CLIImportController(import_path, output_file, pages=pages, processes=processes, ocr_meta=ocr_meta)
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
