# System
# self
# import core
import widgets
# QT
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton,  QLabel, QLineEdit, QComboBox, QFileDialog

app = QApplication([])
app.setApplicationName("Getter Visual")
app.setStyle("Fusion")  # TODO: figure out how to style universal

window = QWidget()
main_layout = QVBoxLayout()
window.setLayout(main_layout)


main_layout.addWidget(widgets.quickWidget())
main_layout.addWidget(widgets.pathWidget())
main_layout.addWidget(widgets.downloadWidget())


window.show()
app.exec_()
