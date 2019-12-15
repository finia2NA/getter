# System
# self
import core
# QT
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox

app = QApplication([])
# app.setApplicationName("Getter Visual")

window = QWidget()
main_layout = QVBoxLayout()
window.setLayout(main_layout)

def quickWidget():
  quickWidget = QWidget()
  quickLayout = QHBoxLayout()
  quickWidget.setLayout(quickLayout)
  video_button = QPushButton("video")
  itunes_button = QPushButton("itunes")
  quickLayout.addWidget(video_button)
  quickLayout.addWidget(itunes_button)
  return quickWidget

def pathWidget():
  pathWidget = QWidget()
  pathLayout = QHBoxLayout()
  pathWidget.setLayout(pathLayout)
  pathLocation = QLineEdit()
  pathSelectButton = QPushButton("select")
  pathLayout.addWidget(pathLocation)
  pathLayout.addWidget(pathSelectButton)
  return pathWidget

def downloadWidget():
  downloadWidget = QWidget()
  downloadLayout = QHBoxLayout()
  downloadWidget.setLayout(downloadLayout)
  formatSelector = QComboBox()
  downloadButton = QPushButton("download")
  downloadLayout.addWidget(formatSelector)
  downloadLayout.addWidget(downloadButton)
  return downloadWidget

main_layout.addWidget(quickWidget())
main_layout.addWidget(pathWidget())
main_layout.addWidget(downloadWidget())

window.show()
app.exec_()
