"""Console script for qodex."""
import sys
import click
from PySide6 import QtCore, QtGui, QtWidgets

from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from qodex.app import MainWindow


@click.command()
def main(args=None):
    """Console script for qodex."""
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
