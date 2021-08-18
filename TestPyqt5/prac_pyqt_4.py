import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu, qApp
from PyQt5.QtCore import QCoreApplication


class Exam(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar()
        self.statusBar().showMessage("안녕하세요!")

        menu = self.menuBar() #메뉴바
        menu_file = menu.addMenu('File') #그룹생성
        menu_edit = menu.addMenu('Edit') #그룹생성
        menu_view = menu.addMenu('View') #그룹생성

        file_exit = QAction('Exit', self)
        file_exit.setShortcut('Ctrl+Q')
        file_exit.setStatusTip('누르면 영원히 안녕~')
        new_txt = QAction('텍스트 파일', self)
        new_py = QAction('파이썬 파일', self)
        view_stat = QAction('상태 표시줄', self, checkable=True) #체크박스
        view_stat.setChecked(True)

        file_exit.triggered.connect(QCoreApplication.instance().quit)
        #QCoreApplication.instance().quit = qApp.quit
        view_stat.triggered.connect(self.tglStat)

        file_new = QMenu('New', self)
        file_new.addAction(new_txt)
        file_new.addAction(new_py)
        
        menu_file.addMenu(file_new)
        menu_file.addAction(file_exit)
        menu_view.addAction(view_stat)

        self.resize(500,500)
        self.show()
    
    def tglStat(self, state):
        if state:
            self.statusBar().show()
        else:
            self.statusBar().hide()
    
    def contextMenuEvent(self, QContextMenuEvent):
        cm = QMenu(self)

        quit = cm.addAction("Quit")

        action = cm.exec_(self.mapToGlobal(QContextMenuEvent.pos()))
        if action == quit:
            qApp.quit()
            

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())