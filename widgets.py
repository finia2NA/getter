from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFrame
from PyQt5.QtWidgets import QPushButton,  QLabel, QLineEdit, QComboBox, QFileDialog
from PyQt5.QtWidgets import QSizePolicy

import getter


class QuickButton(QPushButton):
  def __init__(self, descriptor, on_click=None):
    QPushButton.__init__(self, descriptor["name"])
    self.destination = descriptor["destination"]
    self.format = descriptor["format"]
    self.setOnClicked(on_click)

  def setOnClicked(self, on_clicked):
    if on_clicked != None:
      self.clicked.connect(on_clicked(self.destination, self.format))


class QuickWidget(QWidget):
  def __init__(self, on_click=None):
    QWidget.__init__(self)
    quickLayout = QHBoxLayout()
    self.setLayout(quickLayout)

    self.buttons = []

    for descriptor in getter.getSettings()["buttons"]:
      button = QuickButton(descriptor, on_click)
      self.buttons.append(button)

  def setOnClicked(self, on_click):
    for b in self.buttons:
      b.setOnClicked(on_click)


class PathWidget(QWidget):
  def __init__(self):
    QWidget.__init__(self)
    pathLayout = QHBoxLayout()
    self.setLayout(pathLayout)

    self.pathLocation = QLineEdit()

    self.pathSelectButton = QPushButton("select")
    self.pathSelectButton.clicked.connect(self.selectPath)

    pathLayout.addWidget(self.pathLocation)
    pathLayout.addWidget(self.pathSelectButton)

  def getPath(self) -> str:
    return self.pathLocation.text()

  def setPath(self, newPath: str):
    self.pathLocation.setText(newPath)

  def selectPath(self) -> str:
    path: str = QFileDialog.getExistingDirectory(self, "Select Destination")
    self.setPath(path)


class DownloadWidget(QWidget):
  def __init__(self, on_download=None):
    QWidget.__init__(self)
    downloadLayout = QHBoxLayout()
    self.setLayout(downloadLayout)
    self.formatSelector = QComboBox()
    formats = ["wav", "mp3", "mp4"]
    self.formatSelector.addItems(formats)

    self.downloadButton = QPushButton("download")
    if on_download != None:
      self.downloadButton.clicked.connect(on_download)

    downloadLayout.addWidget(self.formatSelector)
    downloadLayout.addWidget(self.downloadButton)

  def getFormat(self) -> str:
    return self.formatSelector.currentText()

  def setFormat(self, format: str) -> None:
    self.formatSelector.setCurrentText(format)

  def setOnDownload(self, fun):
    self.downloadButton.clicked.connect(fun)


class Seperator(QFrame):
  def __init__(self):
    QFrame.__init__(self)
    self.setFrameShape(QFrame.HLine)
    self.setFrameShadow(QFrame.Sunken)
