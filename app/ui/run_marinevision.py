import sys
from pathlib import Path

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QPushButton, QStackedWidget

app = QApplication(sys.argv)
path = Path(__file__).with_name("marinevision.ui")
file = QFile(str(path))
if not file.open(QFile.ReadOnly):
    raise RuntimeError(f"Could not open {path}")
window = QUiLoader().load(file)
file.close()
if window is None:
    raise RuntimeError("Qt could not load the .ui file")

pages = window.findChild(QStackedWidget, "pages")
if pages is None:
    raise RuntimeError("The page container was not found")

for button_name, page_index in {
    "homeButton": 0,
    "analyzeButton": 1,
    "mapButton": 2,
    "reportsButton": 3,
    "datasetButton": 4,
    "configButton": 5,
    "quickAnalyzeButton": 1,
    "heroAnalyzeButton": 1,
    "heroMapButton": 2,
}.items():
    button = window.findChild(QPushButton, button_name)
    if button is not None:
        button.clicked.connect(lambda checked=False, index=page_index: pages.setCurrentIndex(index))

window.show()
sys.exit(app.exec())
