from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton,  QLabel, QLineEdit, QComboBox, QFileDialog


class Entry(QWidget):
  def __init__(self, returnAction=lambda: None, deleteAction=lambda: None):
    QWidget.__init__(self)

    self.returnAction = returnAction

    self.entryLayout = QHBoxLayout()
    self.setLayout(self.entryLayout)

    self.entryEdit = QLineEdit()
    self.entryDelete = QPushButton("X")
    main = self
    self.entryDelete.clicked.connect(main.deleteLater)

    self.entryEdit.returnPressed.connect(self.finalize)
    self.entryLayout.addWidget(self.entryEdit)

  def finalize(self):
    self.entryEdit.setReadOnly(True)

    self.entryLayout.addWidget(self.entryDelete)

    self.returnAction()


class VideoWidget(QWidget):
  def __init__(self):
    QWidget.__init__(self)
    self.listLayout = QVBoxLayout()
    self.setLayout(self.listLayout)

    title = QLabel("Video")
    self.listLayout.addWidget(title)

    firstLine = Entry(self.spawnNextField)
    self.listLayout.addWidget(firstLine)

    wowButton = QPushButton()
    wowButton.clicked.connect(self.getAsList)
    self.listLayout.addWidget(wowButton)

  def spawnNextField(self):
    nextField = Entry(self.spawnNextField)
    self.listLayout.addWidget(nextField)

  def getAsList(self):
    edits = self.findChildren(QLineEdit)
    # TODO: next should really be done with map() and filter()
    strings = []
    for e in edits:
      line = e.text()
      if line != "":
        strings.append(line)

    return strings
