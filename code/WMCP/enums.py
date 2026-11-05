from enum import Enum, auto
from PySide6 import QtCore


class QtButtonTypes(Enum):
    PushButton = auto()
    ToolButton = auto()
    RadioButton = auto()


class Alignments:
    RIGHT = QtCore.Qt.AlignmentFlag.AlignRight
    LEFT = QtCore.Qt.AlignmentFlag.AlignLeft
    CENTER = QtCore.Qt.AlignmentFlag.AlignCenter
    TOP = QtCore.Qt.AlignmentFlag.AlignTop
    BOTTOM = QtCore.Qt.AlignmentFlag.AlignBottom
    NONE = QtCore.Qt.AlignmentFlag(0)
