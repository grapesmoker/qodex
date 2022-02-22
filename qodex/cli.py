"""Console script for qodex."""
import sys
import click
from PySide6 import QtCore, QtGui, QtWidgets
import logging
from rich.logging import RichHandler
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from qodex.doctools.batch import OCRController
from qodex.app import MainWindow


logging.basicConfig(
    level='INFO', format='%(message)s', datefmt='[%X]', handlers=[RichHandler()]
)
logger = logging.getLogger(__name__)


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
def extract_meta(import_path: Path, output_file: Path, pages: int):

    logger.info(f'Extracting metadata from files in {import_path} into {output_file}')
    ocr = OCRController(import_path, output_file, pages)
    ocr.run()


if __name__ == "__main__":
    sys.exit(qodex())  # pragma: no cover
