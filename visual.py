# System
# self
import getter
import widgets

# QT
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QComboBox, QFileDialog

app = QApplication([])
app.setApplicationName("Getter Visual")
app.setStyle("Fusion")  # TODO: figure out how to style universal

window = QWidget()
main_layout = QVBoxLayout()
window.setLayout(main_layout)

quickWidget = widgets.quickWidget()
pathWidget = widgets.pathWidget()
downloadWidget = widgets.downloadWidget()


def download_clicked():
  path = pathWidget.getPath()
  format = downloadWidget.getFormat()
  linkList = []  # TODO: replace with real list
  print("hi")
  for link in linkList:
    getter.downloadUrl(link, format, path)


def itunes_clicked():
  pathWidget.setPath("C:/Cache/hierituneseinfuegen")
  downloadWidget.setFormat("wav")


def video_clicked():
  pathWidget.setPath("C:/Videos")
  downloadWidget.setFormat("mp4")


downloadWidget.setOnDownload(download_clicked)
quickWidget.setOnItunesButton(itunes_clicked)
quickWidget.setOnVideoButton(video_clicked)

main_layout.addWidget(quickWidget)
main_layout.addWidget(pathWidget)
main_layout.addWidget(downloadWidget)


window.show()
app.exec_()
