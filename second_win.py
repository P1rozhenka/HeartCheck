# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont
from instr import *
from final_win import FinalWin
class Experiment():
    def __init__(self, hintage, hinttest1, hinttest2, hinttest3):
        self.age = hintage
        self.t1 = hinttest1
        self.t2 = hinttest2
        self.t3 = hinttest3
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
        self.question_age = QLabel(txt_age)
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
        self.l_line.addWidget(self.name, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.hintname, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.question_age, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.hintage, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.test1, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.starttest1, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.hinttest1, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.test2, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.starttest2, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.test3, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.starttest3, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.hinttest2, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.hinttest3, alignment= Qt.AlignLeft)
        self.r_line.addWidget(self.text_timer, alignment= Qt.AlignCenter)
        self.l_line.addWidget(self.button, alignment= Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    def connects(self):
        self.button.clicked.connect(self.next_click)
        self.starttest1.clicked.connect(self.timer_test)
        self.starttest2.clicked.connect(self.timer_sits)
        self.starttest3.clicked.connect(self.timer_final)
    def next_click(self):
        self.hide()
        self.exp = Experiment(self.hintage(), self.hinttest1(), self.hinttest2(), self.hinttest3())
        self.tw = FinalWin(exp)
    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1000)
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(0, 255, 0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(0, 255, 0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0, 0, 0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()