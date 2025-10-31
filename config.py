from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget,
                             QTimeEdit, QDialog, QMessageBox, QHBoxLayout)
from PyQt5.QtCore import QTimer, QTime, Qt

"""
​‌‍‌Файл конфигруации и глобальных переменных​
в дальнейшем здесь будет обработка всей информации в том числе и БД


⁡⁢⁢⁢​‌‍‌‍links dict structure:​⁡
SCOREBOARDS_LINKS = {
                    1: {'scoreboard': {'window': Scoreboard, 'ui': Ui_Scoreboard, 'id': id(Ui_Scoreboard)},
                        'maneger': {'window': ManegePanel, 'ui': Ui_ManegePanel, 'id': id(Ui_ManegePanel)}}            
        }

        
⁡⁢⁣⁢​‌‌‌Подсказака​⁡

self.label_yellow_card_2_1.setStyleSheet("background-color: rgb(255, 255, 0);")

"""

# ⁡⁢⁣⁣​‌‍‌global variables for save state and links​⁡

SCOREBOARDS_LINKS = {}
SCOREBOARDS_NUMBERS = [0]



# ⁡⁣⁢⁣​‌‌‌Time functions​⁡
class Time:
    def __init__(self, window_id):
        self.window_id = window_id

        # ⁡⁣⁢⁣​‌‌​‌‍‌⁡⁢⁢⁢‍Time variables⁡​
        self.TotalTimer = QTimer()
        self.TotalTimer.timeout.connect(lambda: self.update_timer())
        self.total_timer_time = QTime(0, 0)
     
    def set_time(self):
            ChoseTime = QDialog()
            ChoseTime.setWindowTitle("Выберите время")
            ChoseTime.resize(260, 231)

            time_edit = QTimeEdit()
            time_edit.setDisplayFormat("mm:ss")
            time_edit.setGeometry(QtCore.QRect(40, 90, 181, 51))
            font = QtGui.QFont()
            font.setPointSize(30)
            time_edit.setFont(font)
            time_edit.setAlignment(QtCore.Qt.AlignCenter)

            pushButton_ok_time = QPushButton("OK")
            pushButton_ok_time.setGeometry(QtCore.QRect(60, 170, 141, 41))
            font = QtGui.QFont()
            font.setPointSize(20)
            pushButton_ok_time.setFont(font)

            layout = QVBoxLayout()
            layout.addWidget(time_edit)
            layout.addWidget(pushButton_ok_time)
            ChoseTime.setLayout(layout)

            pushButton_ok_time.clicked.connect(lambda: self.start_totla_time(ChoseTime, time_edit.time()))

            ChoseTime.exec_()

            update_scoreboard(self.window_id)

    def start_totla_time(self, window, time):
            window.close()

            total_timer_time = time
            self.update_timer_display()

            if not self.TotalTimer.isActive():
                self.TotalTimer.start(1000)  # Обновляем каждую секунду

            self.TotalTimer.stop()

            update_scoreboard(self.window_id)

    def update_timer(self):
        if self.total_timer_time == QTime(0, 0):
            total_time.stop()
            return

        total_time = total_time.addSecs(-1)

        update_scoreboard(self.window_id)



def update_scoreboard(index: int) -> None:
    if index == 0:
        print("Window not found")

    if index in SCOREBOARDS_LINKS:
        
        scoreboard = SCOREBOARDS_LINKS[index]['scoreboard']['ui']
        maneger = SCOREBOARDS_LINKS[index]['maneger']['ui']

        # total score
        scoreboard.label_score_1.setText(maneger.label_total_score_1.text())
        scoreboard.label_score_2.setText(maneger.label_total_score_2.text())

        # members
        # scoreboard.label_member_1.setText(maneger.comboBox_member_1.currentText())
        # scoreboard.label_member_2.setText(maneger.comboBox_member_2.currentText())

    else:
        print("Error: index not found in SCOREBOARDS_STATE")
        chekout_links()
        print(SCOREBOARDS_NUMBERS)

# ⁡⁢⁢⁢​‌‌‍chekout functions​⁡
def chekout_links():
    if SCOREBOARDS_LINKS:
        print("Links:")
        for key, value in SCOREBOARDS_LINKS.items():
            print(f"{key}: {value}")
            print("___________________________________________\n")
    else:
        print("No links found.")


def clean_links():
    """
    clean links dict and numbers list
    """
    SCOREBOARDS_LINKS.clear()
    SCOREBOARDS_NUMBERS.clear()

    SCOREBOARDS_NUMBERS = [0]