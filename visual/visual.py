# System
# self
# import core
# QT
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox

app = QApplication([])
app.setApplicationName("Getter Visual")

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
    self.pathLocation = QLineEdit()
    self.pathSelectButton = QPushButton("select")
    pathLayout.addWidget(self.pathLocation)
    pathLayout.addWidget(self.pathSelectButton)

  def getPath(self):
    self.pathLocation.text()

  def setPath(self, newPath: str):
    self.pathLocation.setText(newPath)


class downloadWidget(QWidget):
  def __init__(self):
    QWidget.__init__(self)
    downloadLayout = QHBoxLayout()
    self.setLayout(downloadLayout)
    self.formatSelector = QComboBox()
    formats = ["wav", "mp3", "mp4"]
    self.formatSelector.addItems(formats)
    self.downloadButton = QPushButton("download")
    downloadLayout.addWidget(self.formatSelector)
    downloadLayout.addWidget(self.downloadButton)

  def getFormat(self):
    return self.formatSelector.currentText()


main_layout.addWidget(quickWidget())
main_layout.addWidget(pathWidget())
main_layout.addWidget(downloadWidget())


window.show()
app.exec_()
