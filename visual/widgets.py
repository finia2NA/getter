from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton,  QLabel, QLineEdit, QComboBox, QFileDialog

class quickWidget(QWidget):
  def __init__(self, on_itunes=None, on_video=None):
    QWidget.__init__(self)
    quickLayout = QHBoxLayout()
    self.setLayout(quickLayout)

    videoButton = QPushButton("video")
    itunesButton = QPushButton("itunes")
    if on_video != None:
      videoButton.clicked.connect(on_video)
    if on_itunes != None:
      itunesButton.clicked.connect(on_itunes)

    quickLayout.addWidget(videoButton)
    quickLayout.addWidget(itunesButton)


class pathWidget(QWidget):
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
    self.pathLocation.text()

  def setPath(self, newPath: str):
    self.pathLocation.setText(newPath)

  def selectPath(self) -> str:
    path: str = QFileDialog.getExistingDirectory(self, "Select Destination")
    self.setPath(path)


class downloadWidget(QWidget):
  def __init__(self, on_download=None):
    QWidget.__init__(self)
    downloadLayout = QHBoxLayout()
    self.setLayout(downloadLayout)
    self.formatSelector = QComboBox()
    formats = ["wav", "mp3", "mp4"]
    self.formatSelector.addItems(formats)
    self.downloadButton = QPushButton("download")
    downloadLayout.addWidget(self.formatSelector)
    downloadLayout.addWidget(self.downloadButton)

  def getFormat(self) -> str:
    return self.formatSelector.currentText()