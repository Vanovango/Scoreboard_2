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

"""

# ⁡⁢⁣⁣​‌‍‌global variables for save state and links​⁡

SCOREBOARDS_LINKS = {}
SCOREBOARDS_NUMBERS = [0]


# ⁡⁣⁢⁣​‌‌‌Time functions​⁡
class TotalTime:
    def __init__(self):
        self.window_id = None
        self.TotalTimer = QTimer()
        self.TotalTimer.timeout.connect(self.update_timer)
        self.total_timer_time = QTime(0, 0)
        self.is_golden_score = False  # Флаг для режима Golden Score
        
    def set_time(self, window_id):
        try:
            self.window_id = window_id

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
            
            self.update()
        except Exception as e:
            print(f"Ошибка в set_time: {e}")

    def start_totla_time(self, window, time):
        try:
            window.close()

            self.total_timer_time = time
            self.is_golden_score = False  # Сбрасываем Golden Score при установке нового времени
            self.update()

            if not self.TotalTimer.isActive():
                self.TotalTimer.start(1000)

            self.TotalTimer.stop()
            self.update()
        except Exception as e:
            print(f"Ошибка в start_totla_time: {e}")

    def update_timer(self):
        try:
            # Проверяем, существует ли еще окно
            if self.window_id not in SCOREBOARDS_LINKS:
                self.TotalTimer.stop()
                return
                
            if self.total_timer_time == QTime(0, 0):
                # Проверяем условие для Golden Score
                if not self.is_golden_score:
                    self.check_golden_score_condition()
                self.TotalTimer.stop()
                return

            self.total_timer_time = self.total_timer_time.addSecs(-1)
            
            # Проверяем условие для Golden Score при каждом обновлении
            if self.total_timer_time == QTime(0, 0):
                self.check_golden_score_condition()
            
            self.update()
        except Exception as e:
            print(f"Ошибка в update_timer: {e}")

    def check_golden_score_condition(self):
        """Проверяет условие для активации Golden Score"""
        try:
            if self.window_id not in SCOREBOARDS_LINKS:
                return
                
            maneger_ui = SCOREBOARDS_LINKS[self.window_id]['maneger']['ui']
            score1 = int(maneger_ui.label_total_score_1.text())
            score2 = int(maneger_ui.label_total_score_2.text())
            
            # Если время истекло и счет равен - активируем Golden Score
            if score1 == score2:
                self.is_golden_score = True
                self.update_golden_score_display(True)
            else:
                self.is_golden_score = False
                self.update_golden_score_display(False)
        except Exception as e:
            print(f"Ошибка в check_golden_score_condition: {e}")

    def update_golden_score_display(self, is_golden):
        """Обновляет отображение для режима Golden Score"""
        try:
            if self.window_id not in SCOREBOARDS_LINKS:
                return
                
            scoreboard_ui = SCOREBOARDS_LINKS[self.window_id]['scoreboard']['ui']
            
            if is_golden:
                scoreboard_ui.label_total_time.setText("GOLDEN SCORE")
                scoreboard_ui.label_total_time.setStyleSheet("color: rgb(255, 215, 0);")  # Золотой цвет
            else:
                scoreboard_ui.label_total_time.setStyleSheet("color: rgb(136, 255, 0);")  # Возвращаем зеленый
        except Exception as e:
            print(f"Ошибка в update_golden_score_display: {e}")

    def update(self):
        try:
            # Проверяем существование окна перед обновлением
            if self.window_id not in SCOREBOARDS_LINKS:
                self.TotalTimer.stop()
                return
                
            # Если активен Golden Score, не обновляем время
            if self.is_golden_score:
                return
                
            maneger_ui = SCOREBOARDS_LINKS[self.window_id]['maneger']['ui']
            scoreboard_ui = SCOREBOARDS_LINKS[self.window_id]['scoreboard']['ui']
            
            maneger_ui.label_total_time.setText(self.total_timer_time.toString("mm:ss"))
            scoreboard_ui.label_total_time.setText(self.total_timer_time.toString("mm:ss"))
        except Exception as e:
            print(f"Ошибка в update: {e}")

