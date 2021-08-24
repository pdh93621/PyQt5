from PyQt5.QtWidgets import QLineEdit, QPushButton, QWidget, QApplication,QLabel
from PyQt5.Qt import QSize
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(1200, 200, 300, 300)

        self.btnList = []
        self.btnTop = 100
        self.cnt = 0
        
        self.lbl = QLabel("생성 될 버튼의 수를 입력하세요.", self)
        self.lbl.move(10,10)

        self.txt = QLineEdit("",self)
        self.txt.move(10, self.lbl.height())

        self.btn = QPushButton("버튼생성", self)
        self.btn.resize(QSize(80,25))
        self.btn.move(10, self.lbl.height() + self.txt.height())

        self.btn.clicked.connect(self.createBtn)

        self.show()

    def createBtn(self):
        self.cnt = int(self.txt.text())
        for i in range(self.cnt):
            self.btnList.append(QPushButton(str(i+1) + '번째 버튼', self))
            self.btnList[i].resize(QSize(80,25))
            self.btnList[i].move(10, self.btnTop + (i * 25))
            self.btnList[i].show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())