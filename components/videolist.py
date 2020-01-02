from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton,  QLabel, QLineEdit, QComboBox, QFileDialog
from PyQt5.QtGui import QFont

from functools import reduce


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

    title = QLabel("Videos")
    title.setFont(QFont("Roboto", 20, QFont.Condensed))
    self.listLayout.addWidget(title)

    firstLine = Entry(self.spawnNextField)
    self.listLayout.addWidget(firstLine)

  def spawnNextField(self):
    nextField = Entry(self.spawnNextField)
    self.listLayout.addWidget(nextField)

  def getAsList(self):
    return reduce(lambda a, b: a + b,
                  map(lambda e: [e.text()] if e.text() != "" else [], self.findChildren(QLineEdit)))
