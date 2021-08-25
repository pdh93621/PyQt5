import os
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton
from PyQt5.QtWidgets import QLabel, QFileDialog, QListView, QMessageBox
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtGui import QFont, QFontDatabase, QIcon
from PyQt5.QtCore import QSize

class CustomPPT(QWidget):
    classes = ['StartEnd', 'NextSlide', 'PreviousSlide', 'AddMedia',
                'AddLink']
    
    motions = ['none', 'zero', 'one', 'two', 'three', 'four', 'five',
                'L', 'K']

    def __init__(self):
        super().__init__()
        self.current_class = None
        self.current_motion = None
        self.current_exepath = None
        self.current_mediapath = None
        self.current_link = None

        self.initUI()


    def initUI(self):
        self.lbl = QLabel('Custom your Presentation', self)
        self.lbl.setGeometry(70, 40, 350, 60)
        self.lbl.setFont(QFont("Arial Black", 14))

        self.subtitle = QLabel('Select command', self)
        self.subtitle.setGeometry(120, 160, 150, 30)
        self.subtitle.setFont(QFont("Arial", 11))

        # command list
        self.choose_class = QComboBox(self)
        self.choose_class.setGeometry(120, 200, 150, 30)
        for c in CustomPPT.classes:
            self.choose_class.addItem(c)

        self.choose_class.activated[str].connect(self.onActivated)

        # motion1 list
        self.choose_motion1 = QComboBox(self)
        self.choose_motion1.setGeometry(120, 250, 60, 25)
        for motion in CustomPPT.motions:
            self.choose_motion1.addItem(motion)

        # motion2 list
        self.choose_motion2 = QComboBox(self)
        self.choose_motion2.setGeometry(120, 290, 60, 25)
        for motion in CustomPPT.motions:
            self.choose_motion2.addItem(motion)    

        # current motion lists
        self.motion_sub = QLabel('Motion lists',self)
        self.motion_sub.setGeometry(490, 160, 100, 16)
        self.motion_sub.setFont(QFont("Arial", 10))

        self.motion_list = QListView(self)
        self.motion_list.setGeometry(490, 180, 260, 370)

        # push button
        self.push_btn = QPushButton('Push', self)
        self.push_btn.setGeometry(340, 280, 75, 25)
        
        # delete button
        self.del_btn = QPushButton('Delete', self)
        self.del_btn.setGeometry(340, 390, 75, 25)

        # save button
        self.save_btn = QPushButton('Save', self)
        self.save_btn.setFont(QFont("Arial", 12))
        self.save_btn.setGeometry(120, 520, 60, 30)

        # Basic settings
        self.setWindowTitle("Custom PPT")
        self.setGeometry(200, 200, 800, 600)
        self.show()

    def onActivated(self, text):
        if text == CustomPPT.classes[0]:
            print(text)    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    cp = CustomPPT()
    sys.exit(app.exec_())

