# System
# self
import getter
import widgets
import videolist

# QT
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFrame
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QComboBox, QFileDialog

app = QApplication([])
app.setApplicationName("Getter Visual")
app.setStyle("Fusion")  # TODO: figure out how to style universal

window = QWidget()
main_layout = QVBoxLayout()
window.setLayout(main_layout)

videoWidget = videolist.VideoWidget()
seperator = widgets.Seperator()
quickWidget = widgets.QuickWidget()
pathWidget = widgets.PathWidget()
downloadWidget = widgets.DownloadWidget()


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

main_layout.addWidget(videoWidget)
main_layout.addWidget(seperator)
main_layout.addWidget(quickWidget)
main_layout.addWidget(pathWidget)
main_layout.addWidget(downloadWidget)


window.show()
app.exec_()
