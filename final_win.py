# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit
from instr import *
class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.move(win_width, win_height)
        self.resize(win_x, win_y)
    def initUI(self):
        self.workh_text = QLabel(txt_workheart)
        self.index_text = QLabel(txt_index)
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment= Qt.AlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment= Qt.AlignCenter)
        self.setLayout(self.layout_line)