# System
# self
import core
from components import widgets
from components import videolist

# QT
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFrame
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QComboBox, QFileDialog


def main():
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
    searchList = videoWidget.getAsList()
    for search in searchList:
      core.main(searchString=search, format=format, dest=path)

  def quick_clicked(path, format):
    pathWidget.setPath(path)
    downloadWidget.setFormat(format)

  quickWidget.setOnClicked(quick_clicked)

  downloadWidget.setOnDownload(download_clicked)

  main_layout.addWidget(videoWidget)
  main_layout.addWidget(seperator)
  main_layout.addWidget(quickWidget)
  main_layout.addWidget(pathWidget)
  main_layout.addWidget(downloadWidget)

  window.show()
  app.exec_()


if __name__ == "__main__":
  main()
