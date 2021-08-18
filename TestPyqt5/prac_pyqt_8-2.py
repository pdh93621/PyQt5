from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication

from PyQt5.QtCore import QBasicTimer
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.pbar = QProgressBar()