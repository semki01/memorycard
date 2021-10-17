from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox, QRadioButton, QGroupBox, QHBoxLayout



app = QApplication([])
window = QWidget()

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Сколько будет 2+2')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('5')
rbtn_2 = QRadioButton('4')
rbtn_3 = QRadioButton('22')
rbtn_4 = QRadioButton('Вот блин я тупой...')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignVCenter | Qt.AlignHCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line3.addWidget(btn_OK, stretch = 3)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)

window.setLayout(layout_card)
window.show()
app.exec_()