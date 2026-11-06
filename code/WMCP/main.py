import sys
import geopandas as gpd
import geojson
import files_lines
from enums import Alignments, QtButtonTypes
from WMCP import texts
from pathlib import Path
from PySide6 import QtWidgets, QtCore, QtGui


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


def create_combo_box(object_name: str):
    box = QtWidgets.QComboBox()
    box.setObjectName(object_name)


class WMCPWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.mission_data = 0

        central = QtWidgets.QWidget()
        self.setCentralWidget(central)

        central_layout = QtWidgets.QVBoxLayout(central)

        self.setWindowTitle("WMCP - Water Autonomous Vehicle Ecosystem")
        self.resize(1000, 1000)

        self.welcome_text = create_label(
            texts.TOP_MESSAGE, central_layout,
            fixed=True)

        self.tabs = QtWidgets.QTabWidget()
        self.tabs.setObjectName('tabs')
        central_layout.addWidget(self.tabs)

        # ============
        # Main window
        # ============

        main_tab = QtWidgets.QWidget()
        main_tab_layout = QtWidgets.QVBoxLayout(main_tab)

        main_tab_layout.setContentsMargins(10, 10, 10, 10)

        self.test_label = create_label('test text', main_tab_layout, fixed=True,
                                       align=Alignments.TOP | Alignments.CENTER)
        self.test_label.setStyleSheet('''border: 1px solid black; ''')

        self.test_combo_box = QtWidgets.QComboBox()
        self.test_combo_box.setObjectName('test_combo_box')
        self.test_combo_box.addItems(['Open street map', 'Google Maps', 'Apple Cars'])
        self.test_combo_box.setPlaceholderText('Chose map')
        self.test_combo_box.setCurrentIndex(-1)
        self.test_combo_box.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.test_combo_box.resize(200, 50)
        main_tab_layout.addWidget(self.test_combo_box)

        self.data_import_button = create_push_button(QtButtonTypes.PushButton, 'Import mission data', main_tab_layout,
                                                     fixed=True, align=Alignments.TOP | Alignments.LEFT)
        self.data_import_button.clicked.connect(self.data_import)

        self.tabs.addTab(main_tab, "Setup and data import")

    def data_import(self):
        # QtWidgets.QMessageBox.information(self, 'Import information',
        #                                   'For now WMCP works ONLY with .gpkg files, make sure, not to import any other, it will not work')
        file_path, selected_filter = QtWidgets.QFileDialog.getOpenFileName(self, "Import Geospatial data",
                                                                           files_lines.test_mission_line,
                                                                           "GeoJSON Files (*.geojson)")
        if not file_path:
            return
        self.mission_data = process_imports(file_path)
        print(self.mission_data, flush=True)


def process_imports(file_path: str):
    with open(file_path, 'r') as file:
        mission_data = geojson.load(file)
    return mission_data


app = QtWidgets.QApplication(sys.argv)
style_path = Path(__file__).parent / 'styles.qss'
app.setStyleSheet(style_path.read_text(encoding='utf-8'))
window = WMCPWindow()
window.show()

sys.exit(app.exec())
