import sys
import PySide6.QtWidgets as QtWidgets


def create_push_button(text, layout, fixed: bool = False):
    button = QtWidgets.QPushButton(text)
    policy = QtWidgets.QSizePolicy.Policy.Fixed if fixed else QtWidgets.QSizePolicy.Policy.Preferred
    button.setSizePolicy(policy, policy)
    layout.addWidget(button)

    return button


def create_label(text, layout, fixed: bool = False):
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

        tabs = QtWidgets.QTabWidget()
        central_layout.addWidget(tabs)

        # ============
        # Main window
        # ============
        main_window = QtWidgets.QWidget()
        main_window_layout = QtWidgets.QVBoxLayout(main_window)

        self.setWindowTitle("WMCP")
        self.resize(800, 800)

        self.test_label = create_label('test text', main_window_layout, fixed=True)
        self.test_label.setStyleSheet('''border: 1px solid black; ''')

        tabs.addTab(main_window, "Main Window")

        # ==============
        # Second window
        # ==============
        secondary_window = QtWidgets.QWidget()
        secondary_window_layout = QtWidgets.QVBoxLayout(secondary_window)

        self.setWindowTitle('Secondary Window')
        self.resize(800, 800)

        self.additional_test_label = create_label('additional test text', secondary_window_layout, fixed=True)
        self.additional_test_label.setStyleSheet('''border 3px solid black''')

        self.test_text_import = QtWidgets.QLineEdit()
        self.test_text_import.setPlaceholderText('Type something')
        secondary_window_layout.addWidget(self.test_text_import)

        self.test_feedback_label = create_label('You typed/loaded:', secondary_window_layout, fixed=True)
        self.test_feedback_label.setStyleSheet('''border: 1px solid black''')

        self.test_button = create_push_button('Improt typed text', secondary_window_layout, fixed=True)

        self.test_button_2 = create_push_button('Load text', secondary_window_layout, fixed=True)

        tabs.addTab(secondary_window, "Secondary Window")


data = 'Some shit'

app = QtWidgets.QApplication(sys.argv)

window = WMCP()
window.show()

sys.exit(app.exec())
