from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFrame
from PyQt5.QtWidgets import QPushButton,  QLabel, QLineEdit, QComboBox, QFileDialog

from PyQt5.QtWidgets import QSizePolicy


class QuickWidget(QWidget):
  def __init__(self, on_itunes=None, on_video=None):
    QWidget.__init__(self)
    quickLayout = QHBoxLayout()
    self.setLayout(quickLayout)

    self.videoButton = QPushButton("video")
    self.itunesButton = QPushButton("itunes")
    if on_video != None:
      self.videoButton.clicked.connect(self.on_video)
    if on_itunes != None:
      self.itunesButton.clicked.connect(self.on_itunes)

    quickLayout.addWidget(self.videoButton)
    quickLayout.addWidget(self.itunesButton)

  def setOnVideoButton(self, fun):
    self.videoButton.clicked.connect(fun)

  def setOnItunesButton(self, fun):
    self.itunesButton.clicked.connect(fun)


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
