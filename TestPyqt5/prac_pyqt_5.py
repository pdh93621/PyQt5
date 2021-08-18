import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
    # move
    #     lbl1 = QLabel('Zetcode', self)
    #     lbl1.move(15,10)

    #     lbl2 = QLabel('tutorials', self)
    #     lbl2.move(35,40)

    #     lbl3 = QLabel('for programmers', self)
    #     lbl3.move(55,70)

    #     self.setGeometry(300, 300, 250,150)
    #     self.setWindowTitle('Absolute')
    #     self.show()
    # vbox, hbox, stretch
        # okButton = QPushButton("OK")
        # cancelButton = QPushButton("Cancel")

        # hbox = QHBoxLayout()
        # hbox.addStretch(1)
        # hbox.addWidget(okButton)
        # hbox.addWidget(cancelButton)

        # vbox = QVBoxLayout()
        # vbox.addStretch(1)
        # vbox.addLayout(hbox)

        # self.setLayout(vbox)

        # self.setGeometry(300,300,300,150)
        # self.setWindowTitle("Buttons")
        # self.show()
    #grid
        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                '7', '8', '9', '/',
                '4', '5', '6', '*',
                '1', '2', '3', '-',
                '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(300,150)
        self.setWindowTitle('Calculator')
        self.show()       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())