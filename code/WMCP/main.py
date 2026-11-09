import sys
import geopandas
from PySide6.QtWidgets import QDialog

import files_lines__prv__
import QtCreates
from enums import Alignments, QtButtonTypes
from WMCP import texts
from pathlib import Path
from PySide6 import QtWidgets, QtCore, QtGui


class WMCPWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.mission_data = 0

        central = QtWidgets.QWidget()
        self.setCentralWidget(central)

        central_layout = QtWidgets.QVBoxLayout(central)

        self.setWindowTitle("WMCP - Water Autonomous Vehicle Ecosystem")
        self.resize(1000, 1000)

        self.welcome_text = QtCreates.create_label(
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

        self.test_label = QtCreates.create_label('test text', main_tab_layout, fixed=True,
                                                 align=Alignments.TOP | Alignments.CENTER)
        self.test_label.setStyleSheet('''border: 1px solid black; ''')

        self.test_combo_box = QtCreates.create_combo_box('test_combo_box',
                                                         ['Open street map', 'Google Maps', 'Apple Cars'], 'Chose map',
                                                         main_tab_layout)

        self.data_import_button = QtCreates.create_push_button(QtButtonTypes.PushButton, 'Import mission data',
                                                               main_tab_layout,
                                                               fixed=True, align=Alignments.TOP | Alignments.LEFT)
        self.data_import_button.clicked.connect(self.data_import)

        self.tabs.addTab(main_tab, "Setup and data import")

    def data_import(self):
        # QtWidgets.QMessageBox.information(self, 'Import information',
        #                                   'For now WMCP works ONLY with .gpkg files, make sure, not to import any other, it will not work')
        file_path, selected_filter = QtWidgets.QFileDialog.getOpenFileName(self, "Import Geospatial data",
                                                                           files_lines__prv__.test_mission_line,
                                                                           "GeoPackage Files (*.gpkg)")
        if not file_path:
            return
        list_of_layers, data = import_data(file_path)
        data_linking(data, list_of_layers)


def import_data(file_path: str):
    mission_data = geopandas.read_file(file_path)
    list_of_layers = geopandas.list_layers(mission_data)['name'].toList()
    return list_of_layers, mission_data


def data_linking(gpkg_package:geopandas.GeoDataFrame, list_of_layers: list):
    dialog = QDialog
    dialog.setWindowTitle('Data Configuration')

    layout = QtWidgets.QFormLayout()

    
    return 0

app = QtWidgets.QApplication(sys.argv)
style_path = Path(__file__).parent / 'styles.qss'
app.setStyleSheet(style_path.read_text(encoding='utf-8'))
window = WMCPWindow()
window.show()

sys.exit(app.exec())
