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
        scoreboard = SCOREBOARDS_LINKS[self.window_id]['scoreboard']['ui']

        try:
            window.close()

            # Сбрасываем Golden Score при установке нового времени
            self.is_golden_score = False  
            
            time_font = QtGui.QFont()
            time_font.setPointSize(100)
            scoreboard.label_total_time.setStyleSheet("color: rgb(136, 255, 0);")  # Возвращаем зеленый
            scoreboard.label_total_time.setFont(time_font)

            self.total_timer_time = time
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
                
            scoreboard = SCOREBOARDS_LINKS[self.window_id]['scoreboard']['ui']
            
            golden_font = QtGui.QFont()
            golden_font.setPointSize(70)

            if is_golden:
                scoreboard.label_total_time.setText("GOLDEN\nSCORE")
                scoreboard.label_total_time.setStyleSheet("color: rgb(255, 215, 0);")  # Золотой цвет
                scoreboard.label_total_time.setFont(golden_font)
            

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


class HoldTime():
    def __init__(self):
        self.window_id = None
        self.HoldTimer = QTimer()
        self.HoldTimer.setInterval(100)
        self.HoldTimer.timeout.connect(self.update_hold_time)
        self.hold_time = 0.0
        self.hold_flag = False

    def start_hold_timer(self, window_id):
        self.window_id = window_id
        if not self.hold_flag:
            self.hold_flag = True
            self.HoldTimer.start()  # Запускаем таймер (если не запущен)

            SCOREBOARDS_LINKS[self.window_id]['scoreboard']['ui'].label_hold_time.setStyleSheet("color: rgb(255, 0, 0);")
            SCOREBOARDS_LINKS[self.window_id]['scoreboard']['ui'].label_hold.setStyleSheet("color: rgb(255, 0, 0);")
            
    def update_hold_time(self):
        # Проверяем существование окна
        if self.window_id not in SCOREBOARDS_LINKS:
            self.HoldTimer.stop()
            return
            
        if self.hold_flag:
            self.hold_time += 0.1
            self.update(f"{self.hold_time:.1f}")

    def stop_hold_time(self):
        if self.hold_flag:
            self.hold_flag = False
            self.HoldTimer.stop()  # Останавливаем таймер

            SCOREBOARDS_LINKS[self.window_id]['scoreboard']['ui'].label_hold_time.setStyleSheet("color: rgb(255, 255, 255);")
            SCOREBOARDS_LINKS[self.window_id]['scoreboard']['ui'].label_hold.setStyleSheet("color: rgb(255, 255, 255);")

            self.update(f"{self.hold_time:.1f}")

            SCOREBOARDS_LINKS[self.window_id]['maneger']['ui'].pushButton_hold_stop.setText('Сброс')
        else:
            # Сброс полностью
            self.hold_time = 0.0
            self.update("0.0")
            self.hold_flag = False
            self.HoldTimer.stop()

            # Обновляем текст кнопки
            if self.window_id in SCOREBOARDS_LINKS:
                SCOREBOARDS_LINKS[self.window_id]['maneger']['ui'].pushButton_hold_stop.setText('Стоп')

    def update(self, time: str):
        # Проверяем существование окна перед обновлением
        if self.window_id not in SCOREBOARDS_LINKS:
            self.HoldTimer.stop()
            return
            
        try:
            maneger_ui = SCOREBOARDS_LINKS[self.window_id]['maneger']['ui']
            scoreboard_ui = SCOREBOARDS_LINKS[self.window_id]['scoreboard']['ui']

            maneger_ui.label_hold_time.setText(time)
            scoreboard_ui.label_hold_time.setText(time)
        except KeyError:
            self.HoldTimer.stop()



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
    SCOREBOARDS_NUMBERS = [0]