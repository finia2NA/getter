# System
# self
# import core
# QT
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox

app = QApplication([])
# app.setApplicationName("Getter Visual")

window = QWidget()
main_layout = QVBoxLayout()
window.setLayout(main_layout)

class quickWidget(QWidget):
  def __init__(self):
    QWidget.__init__(self)
    quickLayout = QHBoxLayout()
    self.setLayout(quickLayout)
    video_button = QPushButton("video")
    itunes_button = QPushButton("itunes")
    quickLayout.addWidget(video_button)
    quickLayout.addWidget(itunes_button)

class pathWidget(QWidget):
  def __init__(self):
    QWidget.__init__(self)
    pathLayout = QHBoxLayout()
    self.setLayout(pathLayout)
    pathLocation = QLineEdit()
    pathSelectButton = QPushButton("select")
    pathLayout.addWidget(pathLocation)
    pathLayout.addWidget(pathSelectButton)

class downloadWidget(QWidget):
  def __init__(self):
    QWidget.__init__(self)
    downloadLayout = QHBoxLayout()
    self.setLayout(downloadLayout)
    formatSelector = QComboBox()
    downloadButton = QPushButton("download")
    downloadLayout.addWidget(formatSelector)
    downloadLayout.addWidget(downloadButton)

main_layout.addWidget(quickWidget())
main_layout.addWidget(pathWidget())
main_layout.addWidget(downloadWidget())

window.show()
app.exec_()
