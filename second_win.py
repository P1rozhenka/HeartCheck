# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton
from instr import *
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.move(win_width, win_height)
        self.resize(win_x, win_y)
    def initUI(self):
        self.name = QLabel(txt_name)
        self.hintname = QLineEdit(txt_hintage)
        self.age = QLabel(txt_age)
        self.hintage = QLineEdit(txt_hintage)
        self.test1 = QLabel(txt_test1)
        self.starttest1 = QPushButton(txt_starttest1)
        self.hinttest1 = QLineEdit(txt_hinttest1)
        self.test2 = QLabel(txt_test2)
        self.starttest2 = QPushButton(txt_starttest2)
        self.test3 = QLabel(txt_test3)
        self.starttest3 = QPushButton(txt_starttest3)
        self.hinttest2 = QLineEdit(txt_hinttest2)
        self.hinttest3 = QLineEdit(txt_hinttest3)
        self.button = QPushButton(txt_sendresults)
        self.text_timer = QLabel(txt_timer)
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()
        self.l_line.addWidget(self.hello_text, alignment= Qt.AlignLeft)
    def connects(self):
        self.button.clicked.connect(self.next_click)
    def next_click(self):
        self.tw = FinalWin()
        self.hide
