# QT
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QComboBox, QFileDialog

import videolist

app = QApplication([])
app.setApplicationName("Videohost")
app.setStyle("Fusion")  # TODO: figure out how to style universal

window = QWidget()
main_layout = QVBoxLayout()
window.setLayout(main_layout)

display = videolist.VideoWidget()

main_layout.addWidget(display)

window.show()
app.exec_()
