import os
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton
from PyQt5.QtWidgets import QLabel, QFileDialog, QListView, QMessageBox
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtGui import QFont, QFontDatabase, QIcon
from PyQt5.QtCore import QSize

class CustomPPT(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel('Custom your Presentation', self)
        self.lbl.setGeometry(50, 60, 350, 60)
        self.lbl.setFont(QFont("Arial Black", 14))





        # Basic settings
        self.setWindowTitle("Custom PPT")
        self.setGeometry(200, 200, 800, 600)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    cp = CustomPPT()
    sys.exit(app.exec_())

