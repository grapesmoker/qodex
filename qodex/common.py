from PySide6.QtCore import QObject, Signal
from enum import Enum


class UpdateMode(Enum):

    UPDATE = 'update'
    DELETE = 'delete'


class WorkerSignals(QObject):

    ready = Signal()
    progress = Signal(int)
