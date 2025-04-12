# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit
from instr import *
class FinalWin(QWidget):
    def __init__(self, exp):
        self.exp = exp
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
    def results(self):
        self.index = (4*(int(self.exp.t1)+int(self.exp.t2)+int(self.exp.t3))-200)/10
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index < 15 and self.index>= 11:
                return txt_res2
            elif self.index < 11 and self.index>= 6:
                return txt_res3
            elif self.index < 6 and self.index>= 0.5:
                return txt_res4
            else: 
                return txt_res5
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.move(win_width, win_height)
        self.resize(win_x, win_y)
    def initUI(self):
        self.workh_text = QLabel(txt_workheart + self.results())
        self.index_text = QLabel(txt_index + str(self.index))
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment= Qt.AlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment= Qt.AlignCenter)
        self.setLayout(self.layout_line)