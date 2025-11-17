from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget,
                             QTimeEdit, QDialog, QMessageBox, QHBoxLayout)
from PyQt5.QtCore import QTimer, QTime, Qt

from config import SCOREBOARDS_LINKS, SCOREBOARDS_NUMBERS, TotalTime, HoldTime, update_scoreboard
from db import Database

class Ui_ManegePanel(object):
    def setupUi(self, MainWindow):
        try:
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(733, 700)  # Увеличили высоту для новых кнопок
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
            self.gridLayout.setContentsMargins(5, 5, 5, 5)
            self.gridLayout.setHorizontalSpacing(15)
            self.gridLayout.setVerticalSpacing(10)
            self.gridLayout.setObjectName("gridLayout")
            
            # ... (предыдущий код остается без изменений до места добавления новых элементов) ...

            self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 5)
            
            # ⁡⁣⁣⁢ДОБАВЛЯЕМ НОВЫЕ КНОПКИ ПОБЕДЫ⁡
            self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_7.setObjectName("horizontalLayout_7")
            
            # Кнопка победы для участника 1
            self.pushButton_win_1 = QtWidgets.QPushButton(self.centralwidget)
            font = QtGui.QFont()
            font.setPointSize(16)
            font.setBold(True)
            self.pushButton_win_1.setFont(font)
            self.pushButton_win_1.setStyleSheet("background-color: rgb(200, 200, 200);")
            self.pushButton_win_1.setObjectName("pushButton_win_1")
            self.horizontalLayout_7.addWidget(self.pushButton_win_1)
            
            # Кнопка победы для участника 2
            self.pushButton_win_2 = QtWidgets.QPushButton(self.centralwidget)
            font = QtGui.QFont()
            font.setPointSize(16)
            font.setBold(True)
            self.pushButton_win_2.setFont(font)
            self.pushButton_win_2.setStyleSheet("background-color: rgb(200, 200, 200);")
            self.pushButton_win_2.setObjectName("pushButton_win_2")
            self.horizontalLayout_7.addWidget(self.pushButton_win_2)
            
            self.gridLayout.addLayout(self.horizontalLayout_7, 6, 0, 1, 5)
            
            MainWindow.setCentralWidget(self.centralwidget)

            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

            # ​‌‌‌⁡⁢⁣⁣‍𝙢͟𝙮 𝙘͟𝙤͟𝙙͟𝙚 𝙥͟𝙖͟𝙧͟𝙩 ⁡​
            self.functions(MainWindow)

            # ⁡⁢⁣⁣​‌‌‍change punish buttons ​⁡
            self.pushButton_shido_1.setMouseTracking(True)
            self.pushButton_shido_1.mousePressEvent = \
                lambda event, name=self.label_shido_score_1, member_num='1': self.check_button_event(event, name, member_num)

            self.pushButton_shido_2.setMouseTracking(True)
            self.pushButton_shido_2.mousePressEvent = \
                lambda event, name=self.label_shido_score_2, member_num='2': self.check_button_event(event, name, member_num)

            # ⁡⁢⁣⁣​‌‌‍change score ​‌‌‍buttons⁡​
            # ⁡⁣⁢⁣​‌‍‌left side ​⁡
            self.pushButton_yko_1.setMouseTracking(True)
            self.pushButton_yko_1.mousePressEvent = \
                lambda event, name=self.label_yko_score_1, member_num='1': self.check_button_event(event, name, member_num)

            self.pushButton_vazari_1.setMouseTracking(True)
            self.pushButton_vazari_1.mousePressEvent = \
                lambda event, name=self.label_vazari_score_1, member_num='1': self.check_button_event(event, name, member_num)

            self.pushButton_ippon_1.setMouseTracking(True)
            self.pushButton_ippon_1.mousePressEvent = \
                lambda event, name=self.label_ippon_score_1, member_num='1': self.check_button_event(event, name, member_num)

            # ⁡⁣⁢⁣​‌‍‌right side ​⁡
            self.pushButton_yko_2.setMouseTracking(True)
            self.pushButton_yko_2.mousePressEvent =\
                lambda event, name=self.label_yko_score_2, member_num='2': self.check_button_event(event, name, member_num)

            self.pushButton_vazari_2.setMouseTracking(True)
            self.pushButton_vazari_2.mousePressEvent = \
                lambda event, name=self.label_vazari_score_2, member_num='2': self.check_button_event(event, name, member_num)

            self.pushButton_ippon_2.setMouseTracking(True)
            self.pushButton_ippon_2.mousePressEvent = \
                lambda event, name=self.label_ippon_score_2, member_num='2': self.check_button_event(event, name, member_num)
                
        except Exception as e:
            print(f"Ошибка в setupUi: {e}")

    def retranslateUi(self, MainWindow):
        try:
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
            self.label_yko_score_1.setText(_translate("MainWindow", "0"))
            self.pushButton_yko_1.setText(_translate("MainWindow", "ЮКО"))
            self.label_vazari_score_1.setText(_translate("MainWindow", "0"))
            self.pushButton_vazari_1.setText(_translate("MainWindow", "ВАЗАРИ"))
            self.label_ippon_score_1.setText(_translate("MainWindow", "0"))
            self.pushButton_ippon_1.setText(_translate("MainWindow", "ИППОН"))
            self.label_shido_score_1.setText(_translate("MainWindow", "0"))
            self.pushButton_shido_1.setText(_translate("MainWindow", "ШИДО"))
            self.label_team_1.setText(_translate("MainWindow", "ВЫБЕРИТЕ ВЕСОВУЮ КАТЕГОРИЮ"))
            self.label_total_score_1.setText(_translate("MainWindow", "0"))
            self.label_weight_category.setText(_translate("MainWindow", "Весовая категория"))
            self.label_total_time_name.setText(_translate("MainWindow", "Вермя"))
            self.label_total_time.setText(_translate("MainWindow", "00:00"))
            self.pushButton_total_time_start.setText(_translate("MainWindow", "Старт"))
            self.pushButton_total_time_stop.setText(_translate("MainWindow", "Стоп"))
            self.pushButton_chose_total_time.setText(_translate("MainWindow", "Выбрать время"))
            self.label_hold.setText(_translate("MainWindow", "Удержание"))
            self.label_hold_time.setText(_translate("MainWindow", "0.0"))
            self.pushButton_hold_start.setText(_translate("MainWindow", "Старт"))
            self.pushButton_hold_stop.setText(_translate("MainWindow", "Стоп"))
            self.label_team_2.setText(_translate("MainWindow", "ВЫБЕРИТЕ ВЕСОВУЮ КАТЕГОРИЮ"))
            self.label_total_score_2.setText(_translate("MainWindow", "0"))
            self.label_yko_score_2.setText(_translate("MainWindow", "0"))
            self.pushButton_yko_2.setText(_translate("MainWindow", "ЮКО"))
            self.label_vazari_score_2.setText(_translate("MainWindow", "0"))
            self.pushButton_vazari_2.setText(_translate("MainWindow", "ВАЗАРИ"))
            self.label_ippon_score_2.setText(_translate("MainWindow", "0"))
            self.pushButton_ippon_2.setText(_translate("MainWindow", "ИППОН"))
            self.label_shido_score_2.setText(_translate("MainWindow", "0"))
            self.pushButton_shido_2.setText(_translate("MainWindow", "ШИДО"))
            self.label_group.setText(_translate("MainWindow", "Группа"))
            
            # Текст для новых кнопок победы
            self.pushButton_win_1.setText(_translate("MainWindow", "ПОБЕДА\nСПОРТСМЕНА 1"))
            self.pushButton_win_2.setText(_translate("MainWindow", "ПОБЕДА\nСПОРТСМЕНА 2"))
        except Exception as e:
            print(f"Ошибка в retranslateUi: {e}")

    def functions(self, MainWindow):
        try:
            total_time = TotalTime()
            hold_time = HoldTime()
            
            # Сохраняем ссылки на таймеры для доступа извне
            self.total_time = total_time
            self.hold_time = hold_time

            # Обработчик закрытия окна
            MainWindow.closeEvent = self.close_event
            
            # Обработчик нажатия клавиш
            MainWindow.keyPressEvent = self.key_press_event

            # time functions
            self.pushButton_chose_total_time.clicked.connect(lambda: total_time.set_time(self.get_window_index()))
            self.pushButton_total_time_start.clicked.connect(lambda: total_time.TotalTimer.start())
            self.pushButton_total_time_stop.clicked.connect(lambda: total_time.TotalTimer.stop())

            # hold time
            self.pushButton_hold_start.clicked.connect(lambda: hold_time.start_hold_timer(self.get_window_index()))
            self.pushButton_hold_stop.clicked.connect(lambda: hold_time.stop_hold_time())
            
            # Кнопки победы
            self.pushButton_win_1.clicked.connect(lambda: self.toggle_winner(1))
            self.pushButton_win_2.clicked.connect(lambda: self.toggle_winner(2))

            # change combobox information - ПОСЛЕДОВАТЕЛЬНАЯ ЛОГИКА
            self.comboBox_weight_category.currentTextChanged.connect(lambda: self.update_weight_category(self.get_window_index()))
            self.comboBox_group.currentTextChanged.connect(lambda: self.update_group(self.get_window_index()))
            self.comboBox_member_1.currentTextChanged.connect(lambda: self.update_member_1(self.get_window_index()))
            self.comboBox_member_2.currentTextChanged.connect(lambda: self.update_member_2(self.get_window_index()))
        except Exception as e:
            print(f"Ошибка в functions: {e}")

    def key_press_event(self, event):
        """Обработка нажатий клавиш"""
        try:
            key = event.key()
            window_id = self.get_window_index()
            
            if window_id == 0:
                return
                
            # ЮКО: "1"
            if key == Qt.Key_1:
                if event.modifiers() & Qt.ShiftModifier:
                    self.minus_one_score(self.label_yko_score_1, '1')
                else:
                    self.plus_one_score(self.label_yko_score_1, '1')
                    
            # ВАЗАРИ: "2"  
            elif key == Qt.Key_2:
                if event.modifiers() & Qt.ShiftModifier:
                    self.minus_one_score(self.label_vazari_score_1, '1')
                else:
                    self.plus_one_score(self.label_vazari_score_1, '1')
                    
            # ИППОН: "3"
            elif key == Qt.Key_3:
                if event.modifiers() & Qt.ShiftModifier:
                    self.minus_one_score(self.label_ippon_score_1, '1')
                else:
                    self.plus_one_score(self.label_ippon_score_1, '1')
                    
            # ШИДО: "4"
            elif key == Qt.Key_4:
                if event.modifiers() & Qt.ShiftModifier:
                    self.minus_one_score(self.label_shido_score_1, '1')
                else:
                    self.plus_one_score(self.label_shido_score_1, '1')
                    
            # Alt: удержание (Пуск, Стоп, Сброс)
            elif key == Qt.Key_Alt:
                if self.hold_time.hold_flag:
                    self.hold_time.stop_hold_time()
                else:
                    self.hold_time.start_hold_timer(window_id)
                    
            # Space: основное время (Пуск, Стоп)
            elif key == Qt.Key_Space:
                if self.total_time.TotalTimer.isActive():
                    self.total_time.TotalTimer.stop()
                else:
                    self.total_time.TotalTimer.start()
                    
        except Exception as e:
            print(f"Ошибка в key_press_event: {e}")

    def toggle_winner(self, player_num):
        """Переключение состояния победы для участника"""
        try:
            window_id = self.get_window_index()
            if window_id == 0:
                return
                
            scoreboard_ui = SCOREBOARDS_LINKS[window_id]['scoreboard']['ui']
            
            if player_num == 1:
                button = self.pushButton_win_1
                label = scoreboard_ui.label_winer_1
                other_button = self.pushButton_win_2
                other_label = scoreboard_ui.label_winer_2
            else:
                button = self.pushButton_win_2
                label = scoreboard_ui.label_winer_2
                other_button = self.pushButton_win_1
                other_label = scoreboard_ui.label_winer_1
            
            # Если кнопка уже активна - сбрасываем
            if button.styleSheet() == "background-color: rgb(0, 255, 0);":
                button.setStyleSheet("background-color: rgb(200, 200, 200);")
                label.setText("")
                label.setStyleSheet("color: rgb(255, 217, 0);")
            else:
                # Активируем текущую кнопку и сбрасываем другую
                button.setStyleSheet("background-color: rgb(0, 255, 0);")
                label.setText("ПОБЕДА!")
                label.setStyleSheet("color: rgb(255, 215, 0);")  # Золотой цвет
                
                # Сбрасываем другую кнопку
                other_button.setStyleSheet("background-color: rgb(200, 200, 200);")
                other_label.setText("")
                
        except Exception as e:
            print(f"Ошибка в toggle_winner: {e}")

    def close_event(self, event):
        """Обработчик закрытия окна"""
        try:
            # Останавливаем таймеры при закрытии
            if hasattr(self, 'total_time'):
                self.total_time.TotalTimer.stop()
            if hasattr(self, 'hold_time'):
                self.hold_time.HoldTimer.stop()
            event.accept()
        except Exception as e:
            print(f"Ошибка в close_event: {e}")

    def check_button_event(self, event, name, member_num):
        try:
            if event.button() == Qt.LeftButton:
                self.plus_one_score(name, member_num)
            elif event.button() == Qt.RightButton:
                self.minus_one_score(name, member_num)
        except Exception as e:
            print(f"Ошибка в check_button_event: {e}")

    def minus_one_score(self, name, member_num):
        try:
            text = max(0, int(name.text()) - 1)  # Не позволяем уйти ниже 0
            name.setText(str(text))

            if name in [self.label_shido_score_1, self.label_shido_score_2]:
                self.give_punish_card(name, member_num)
            else:
                self.update_score(member_num)
        except Exception as e:
            print(f"Ошибка в minus_one_score: {e}")

    def plus_one_score(self, name, member_num):
        try:
            text = int(name.text()) + 1
            name.setText(str(text))

            if name in [self.label_shido_score_1, self.label_shido_score_2]:
                self.give_punish_card(name, member_num)
            else:
                self.update_score(member_num)
        except Exception as e:
            print(f"Ошибка в plus_one_score: {e}")

    ##################### score counter ############################
    def update_score(self, member_num):
        try:
            if member_num == '1':
                score = (int(self.label_yko_score_1.text()) +
                         10 * int(self.label_vazari_score_1.text()) +
                         100 * int(self.label_ippon_score_1.text()))
                self.label_total_score_1.setText(str(score))

            elif member_num == '2':
                score = (int(self.label_yko_score_2.text()) +
                         10 * int(self.label_vazari_score_2.text()) +
                         100 * int(self.label_ippon_score_2.text()))
                self.label_total_score_2.setText(str(score))

            update_scoreboard(self.get_window_index())
        except Exception as e:
            print(f"Ошибка в update_score: {e}")

    def give_punish_card(self, name, member_num):
        try:
            index = self.get_window_index()
            ui = SCOREBOARDS_LINKS[index]['scoreboard']['ui']

            if member_num == '1': # ​‌‌‍up member​
                if name.text() == '0':
                    self.label_card_1_1.setStyleSheet("background-color: rgb(255, 255, 255);")
                    self.label_card_1_2.setStyleSheet("background-color: rgb(255, 255, 255);")

                    ui.label_card_1_1.setStyleSheet("background-color: rgb(255, 255, 255);")
                    ui.label_card_1_2.setStyleSheet("background-color: rgb(255, 255, 255);")
                    
                elif name.text() == '1':
                    self.label_card_1_1.setStyleSheet("background-color: rgb(255, 255, 0);")
                    self.label_card_1_2.setStyleSheet("background-color: rgb(255, 255, 255);")

                    ui.label_card_1_1.setStyleSheet("background-color: rgb(255, 255, 0);")
                    ui.label_card_1_2.setStyleSheet("background-color: rgb(255, 255, 255);")

                elif name.text() == '2':
                    self.label_card_1_1.setStyleSheet("background-color: rgb(255, 255, 0);")
                    self.label_card_1_2.setStyleSheet("background-color: rgb(255, 255, 0);")
                    
                    ui.label_card_1_1.setStyleSheet("background-color: rgb(255, 255, 0);")
                    ui.label_card_1_2.setStyleSheet("background-color: rgb(255, 255, 0);")
                    
                elif name.text() == '3':
                    self.label_card_1_1.setStyleSheet("background-color: rgb(255, 0, 0);")
                    self.label_card_1_2.setStyleSheet("background-color: rgb(255, 255, 255);")
                    
                    ui.label_card_1_1.setStyleSheet("background-color: rgb(255, 0, 0);")
                    ui.label_card_1_2.setStyleSheet("background-color: rgb(255, 255, 255);")
                
            elif member_num == '2': # ​‌‌‍down member​
                if name.text() == '0':
                    self.label_card_2_1.setStyleSheet("background-color: rgb(255, 255, 255);")
                    self.label_card_2_2.setStyleSheet("background-color: rgb(255, 255, 255);")
                    
                    ui.label_card_2_1.setStyleSheet("background-color: rgb(0, 0, 255);")
                    ui.label_card_2_2.setStyleSheet("background-color: rgb(0, 0, 255);")
                    
                elif name.text() == '1':
                    self.label_card_2_1.setStyleSheet("background-color: rgb(255, 255, 0);")
                    self.label_card_2_2.setStyleSheet("background-color: rgb(255, 255, 255);")
                    
                    ui.label_card_2_1.setStyleSheet("background-color: rgb(255, 255, 0);")
                    ui.label_card_2_2.setStyleSheet("background-color: rgb(0, 0, 255);")
                    
                elif name.text() == '2':
                    self.label_card_2_1.setStyleSheet("background-color: rgb(255, 255, 0);")
                    self.label_card_2_2.setStyleSheet("background-color: rgb(255, 255, 0);")
                    
                    ui.label_card_2_1.setStyleSheet("background-color: rgb(255, 255, 0);")
                    ui.label_card_2_2.setStyleSheet("background-color: rgb(255, 255, 0);")
                    
                elif name.text() == '3':
                    self.label_card_2_1.setStyleSheet("background-color: rgb(255, 0, 0);")
                    self.label_card_2_2.setStyleSheet("background-color: rgb(255, 255, 255);")
                    
                    ui.label_card_2_1.setStyleSheet("background-color: rgb(255, 0, 0);")
                    ui.label_card_2_2.setStyleSheet("background-color: rgb(0, 0, 255);")
        except Exception as e:
            print(f"Ошибка в give_punish_card: {e}")
