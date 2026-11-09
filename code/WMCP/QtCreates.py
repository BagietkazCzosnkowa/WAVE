from PySide6 import QtWidgets, QtCore
from enums import Alignments, QtButtonTypes

def create_push_button(button_type: QtButtonTypes, text: str, layout: QtWidgets.QBoxLayout,
                       fixed: bool = False, align: QtCore.Qt.AlignmentFlag = Alignments.NONE):
    match button_type:
        case QtButtonTypes.PushButton:
            button = QtWidgets.QPushButton(text)
        case QtButtonTypes.ToolButton:
            button = QtWidgets.QToolButton()
        case QtButtonTypes.RadioButton:
            button = QtWidgets.QRadioButton(text)
    policy = QtWidgets.QSizePolicy.Policy.Fixed if fixed else QtWidgets.QSizePolicy.Policy.Preferred
    button.setSizePolicy(policy, policy)
    if align != 0:
        layout.addWidget(button, alignment=align)
    else:
        layout.addWidget(button)

    return button

def create_label(text: str, layout: QtWidgets.QBoxLayout, fixed: bool = False,
                 align: QtCore.Qt.AlignmentFlag = Alignments.NONE):
    label = QtWidgets.QLabel(text)
    policy = QtWidgets.QSizePolicy.Policy.Fixed if fixed else QtWidgets.QSizePolicy.Policy.Preferred
    label.setSizePolicy(policy, policy)
    if align:
        layout.addWidget(label, alignment=align)
    else:
        layout.addWidget(label)

    return label


def create_combo_box(object_name: str, options: list, placeholder: str, layout: QtWidgets.QBoxLayout):
    box = QtWidgets.QComboBox()
    box.setObjectName(object_name)
    box.addItems(options)
    box.setPlaceholderText(placeholder)
    box.setCurrentIndex(-1)
    box.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents)
    layout.addWidget(box)
    return box


