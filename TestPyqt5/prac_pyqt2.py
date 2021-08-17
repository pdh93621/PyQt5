import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu
from PyQt5.QtCore import QCoreApplication


class Exam(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar()
        self.statusBar().showMessage('hi')

        menu = self.menuBar()
        menu_file = menu.addMenu('File')
        menu_edit = menu.addMenu('Edit')

        file_exit = QAction('Exit', self)
        file_exit.setShortcut('Ctrl+Q')
        file_exit.setStatusTip('누르면 영원히 안녕~')
        new_txt = QAction('텍스트 파일', self)
        new_py = QAction('파이썬 파일', self)

        file_exit.triggered.connect(QCoreApplication.instance().quit)

        file_new = QMenu('New', self)
        file_new.addAction(new_txt)
        file_new.addAction(new_py)

        menu_file.addMenu(file_new)
        menu_file.addAction(file_exit)
        self.resize(500,500)
        self.show()

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())