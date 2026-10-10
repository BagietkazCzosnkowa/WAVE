import sys
import enums
from WMCP import texts
from pathlib import Path
import PySide6.QtWidgets as QtWidgets


def create_push_button(button_type: enums.QtButtonTypes, text: str, layout: QtWidgets.QLayout,
                       fixed: bool = False):
    match button_type:
        case enums.QtButtonTypes.PushButton:
            button = QtWidgets.QPushButton(text)
        case enums.QtButtonTypes.ToolButton:
            button = QtWidgets.QToolButton()
        case enums.QtButtonTypes.RadioButton:
            button = QtWidgets.QRadioButton(text)
    policy = QtWidgets.QSizePolicy.Policy.Fixed if fixed else QtWidgets.QSizePolicy.Policy.Preferred
    button.setSizePolicy(policy, policy)
    layout.addWidget(button)

    return button


def create_label(text: str, layout: QtWidgets.QLayout, fixed: bool = False):
    label = QtWidgets.QLabel(text)
    policy = QtWidgets.QSizePolicy.Policy.Fixed if fixed else QtWidgets.QSizePolicy.Policy.Preferred
    label.setSizePolicy(policy, policy)
    layout.addWidget(label)

    return label


class WMCP(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        central = QtWidgets.QWidget()
        self.setCentralWidget(central)

        central_layout = QtWidgets.QVBoxLayout(central)


        self.welcome_text = create_label(
            texts.TOP_MESSAGE, central_layout,
            fixed=False)

        self.tabs = QtWidgets.QTabWidget()
        self.tabs.setObjectName('tabs')
        central_layout.addWidget(self.tabs)

        # ============
        # Main window
        # ============
        main_tab = QtWidgets.QWidget()
        main_tab_layout = QtWidgets.QVBoxLayout(main_tab)

        self.setWindowTitle("WMCP - Water Autonomous Vehicle Ecosystem")
        self.resize(1000, 1000)

        self.test_label = create_label('test text', main_tab_layout, fixed=True)
        self.test_label.setStyleSheet('''border: 1px solid black; ''')

        self.tabs.addTab(main_tab, "Main Window")

        # ==============
        # Second window
        # ==============
        second_tab = QtWidgets.QWidget()
        second_tab.setObjectName('second_tab')
        second_tab_layout = QtWidgets.QVBoxLayout(second_tab)

        self.additional_test_label = create_label('additional test text', second_tab_layout, fixed=True)
        self.additional_test_label.setStyleSheet('''border: 3px solid black''')

        self.test_text_import = QtWidgets.QLineEdit()
        self.test_text_import.setPlaceholderText('Type something')
        second_tab_layout.addWidget(self.test_text_import)

        self.test_feedback_label = create_label('You typed/loaded:', second_tab_layout, fixed=True)
        self.test_feedback_label.setStyleSheet('''border: 1px solid black''')

        self.test_button = create_push_button(enums.QtButtonTypes.PushButton, 'Import typed text',
                                              second_tab_layout, fixed=True)

        self.test_button_2 = create_push_button(enums.QtButtonTypes.PushButton, 'Load text', second_tab_layout,
                                                fixed=True)

        self.tabs.addTab(second_tab, "Secondary Window")


app = QtWidgets.QApplication(sys.argv)
style_path = Path(__file__).parent / 'styles.qss'
app.setStyleSheet(style_path.read_text(encoding='utf-8'))
window = WMCP()
window.show()

sys.exit(app.exec())
