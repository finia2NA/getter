# System
# self
# import core
# QT
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton,  QLabel, QLineEdit, QComboBox, QFileDialog

app = QApplication([])
app.setApplicationName("Getter Visual")
app.setStyle("Fusion")  # TODO: figure out how to style universal

window = QWidget()
main_layout = QVBoxLayout()
window.setLayout(main_layout)


class quickWidget(QWidget):
  def __init__(self, on_itunes=None, on_video=None):
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


main_layout.addWidget(quickWidget())
main_layout.addWidget(pathWidget())
main_layout.addWidget(downloadWidget())


window.show()
app.exec_()
