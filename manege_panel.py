from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget,
                             QTimeEdit, QDialog, QMessageBox, QHBoxLayout)
from PyQt5.QtCore import QTimer, QTime, Qt

from config import SCOREBOARDS_LINKS, SCOREBOARDS_NUMBERS, TotalTime, HoldTime, update_scoreboard

class Ui_ManegePanel(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(733, 638)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.line_2.setFont(font)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 2, 0, 1, 5)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 5, 0, 1, 5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_yko_score_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_yko_score_1.setFont(font)
        self.label_yko_score_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_yko_score_1.setObjectName("label_yko_score_1")
        self.verticalLayout_6.addWidget(self.label_yko_score_1)
        self.pushButton_yko_1 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_yko_1.setFont(font)
        self.pushButton_yko_1.setObjectName("pushButton_yko_1")
        self.verticalLayout_6.addWidget(self.pushButton_yko_1)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_vazari_score_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_vazari_score_1.setFont(font)
        self.label_vazari_score_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_vazari_score_1.setObjectName("label_vazari_score_1")
        self.verticalLayout_7.addWidget(self.label_vazari_score_1)
        self.pushButton_vazari_1 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_vazari_1.setFont(font)
        self.pushButton_vazari_1.setObjectName("pushButton_vazari_1")
        self.verticalLayout_7.addWidget(self.pushButton_vazari_1)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_ippon_score_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_ippon_score_1.setFont(font)
        self.label_ippon_score_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ippon_score_1.setObjectName("label_ippon_score_1")
        self.verticalLayout_8.addWidget(self.label_ippon_score_1)
        self.pushButton_ippon_1 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_ippon_1.setFont(font)
        self.pushButton_ippon_1.setObjectName("pushButton_ippon_1")
        self.verticalLayout_8.addWidget(self.pushButton_ippon_1)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_shido_score_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_shido_score_1.setFont(font)
        self.label_shido_score_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_shido_score_1.setObjectName("label_shido_score_1")
        self.verticalLayout_9.addWidget(self.label_shido_score_1)
        self.pushButton_shido_1 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_shido_1.setFont(font)
        self.pushButton_shido_1.setObjectName("pushButton_shido_1")
        self.verticalLayout_9.addWidget(self.pushButton_shido_1)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.comboBox_member_1 = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_member_1.setFont(font)
        self.comboBox_member_1.setObjectName("comboBox_member_1")
        self.comboBox_member_1.addItem("")
        self.comboBox_member_1.addItem("")
        self.verticalLayout_4.addWidget(self.comboBox_member_1)
        self.label_organization_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_organization_1.setFont(font)
        self.label_organization_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_organization_1.setObjectName("comboBox_organization_1")
        self.verticalLayout_4.addWidget(self.label_organization_1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.label_total_score_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_total_score_1.setFont(font)
        self.label_total_score_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_total_score_1.setObjectName("label_total_score_1")
        self.horizontalLayout_5.addWidget(self.label_total_score_1)
        self.fine_layout_1 = QtWidgets.QHBoxLayout()
        self.fine_layout_1.setContentsMargins(-1, 10, -1, 10)
        self.fine_layout_1.setSpacing(20)
        self.fine_layout_1.setObjectName("fine_layout_1")
        self.label_yellow_card_1_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_yellow_card_1_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_yellow_card_1_1.setText("")
        self.label_yellow_card_1_1.setObjectName("label_yellow_card_1_1")
        self.fine_layout_1.addWidget(self.label_yellow_card_1_1)
        self.label_yellow_card_1_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_yellow_card_1_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_yellow_card_1_2.setText("")
        self.label_yellow_card_1_2.setObjectName("label_yellow_card_1_2")
        self.fine_layout_1.addWidget(self.label_yellow_card_1_2)
        self.label_red_card_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_red_card_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_red_card_1.setText("")
        self.label_red_card_1.setObjectName("label_red_card_1")
        self.fine_layout_1.addWidget(self.label_red_card_1)
        self.horizontalLayout_5.addLayout(self.fine_layout_1)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 5)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_weight_category = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_weight_category.setFont(font)
        self.label_weight_category.setAlignment(QtCore.Qt.AlignCenter)
        self.label_weight_category.setObjectName("label_weight_category")
        self.verticalLayout_5.addWidget(self.label_weight_category)
        self.comboBox_weight_category = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_weight_category.setFont(font)
        self.comboBox_weight_category.setObjectName("comboBox_weight_category")
        self.comboBox_weight_category.addItem("")
        self.comboBox_weight_category.addItem("")
        self.comboBox_weight_category.addItem("")
        self.comboBox_weight_category.addItem("")
        self.verticalLayout_5.addWidget(self.comboBox_weight_category)
        self.gridLayout.addLayout(self.verticalLayout_5, 6, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_total_time_name = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_total_time_name.setFont(font)
        self.label_total_time_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_total_time_name.setObjectName("label_total_time_name")
        self.verticalLayout.addWidget(self.label_total_time_name)
        self.label_total_time = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_total_time.setFont(font)
        self.label_total_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_total_time.setObjectName("label_total_time")
        self.verticalLayout.addWidget(self.label_total_time)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_total_time_start = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_total_time_start.setFont(font)
        self.pushButton_total_time_start.setObjectName("pushButton_total_time_start")
        self.horizontalLayout_3.addWidget(self.pushButton_total_time_start)
        self.pushButton_total_time_stop = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_total_time_stop.setFont(font)
        self.pushButton_total_time_stop.setObjectName("pushButton_total_time_stop")
        self.horizontalLayout_3.addWidget(self.pushButton_total_time_stop)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.pushButton_chose_total_time = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_chose_total_time.setFont(font)
        self.pushButton_chose_total_time.setObjectName("pushButton_chose_total_time")
        self.verticalLayout.addWidget(self.pushButton_chose_total_time)
        self.gridLayout.addLayout(self.verticalLayout, 6, 2, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_hold = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_hold.setFont(font)
        self.label_hold.setAlignment(QtCore.Qt.AlignCenter)
        self.label_hold.setObjectName("label_hold")
        self.verticalLayout_2.addWidget(self.label_hold)
        self.label_hold_time = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_hold_time.setFont(font)
        self.label_hold_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_hold_time.setObjectName("label_hold_time")
        self.verticalLayout_2.addWidget(self.label_hold_time)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_hold_start = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_hold_start.setFont(font)
        self.pushButton_hold_start.setObjectName("pushButton_hold_start")
        self.horizontalLayout_4.addWidget(self.pushButton_hold_start)
        self.pushButton_hold_stop = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_hold_stop.setFont(font)
        self.pushButton_hold_stop.setObjectName("pushButton_hold_stop")
        self.horizontalLayout_4.addWidget(self.pushButton_hold_stop)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_2, 6, 4, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 6, 3, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 6, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboBox_member_2 = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_member_2.setFont(font)
        self.comboBox_member_2.setObjectName("comboBox_member_2")
        self.comboBox_member_2.addItem("")
        self.comboBox_member_2.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_member_2)
        self.label_organization_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_organization_2.setFont(font)
        self.label_organization_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_organization_2.setObjectName("label_organization_2")
        self.verticalLayout_3.addWidget(self.label_organization_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.label_total_score_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_total_score_2.setFont(font)
        self.label_total_score_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_total_score_2.setObjectName("label_total_score_2")
        self.horizontalLayout_6.addWidget(self.label_total_score_2)
        self.fine_layout_2 = QtWidgets.QHBoxLayout()
        self.fine_layout_2.setContentsMargins(-1, 10, -1, 10)
        self.fine_layout_2.setSpacing(20)
        self.fine_layout_2.setObjectName("fine_layout_2")
        self.label_yellow_card_2_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_yellow_card_2_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_yellow_card_2_1.setText("")
        self.label_yellow_card_2_1.setObjectName("label_yellow_card_2_1")
        self.fine_layout_2.addWidget(self.label_yellow_card_2_1)
        self.label_yellow_card_2_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_yellow_card_2_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_yellow_card_2_2.setText("")
        self.label_yellow_card_2_2.setObjectName("label_yellow_card_2_2")
        self.fine_layout_2.addWidget(self.label_yellow_card_2_2)
        self.label_red_card_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_red_card_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_red_card_2.setText("")
        self.label_red_card_2.setObjectName("label_red_card_2")
        self.fine_layout_2.addWidget(self.label_red_card_2)
        self.horizontalLayout_6.addLayout(self.fine_layout_2)
        self.gridLayout.addLayout(self.horizontalLayout_6, 3, 0, 1, 5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_yko_score_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_yko_score_2.setFont(font)
        self.label_yko_score_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_yko_score_2.setObjectName("label_yko_score_2")
        self.verticalLayout_10.addWidget(self.label_yko_score_2)
        self.pushButton_yko_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_yko_2.setFont(font)
        self.pushButton_yko_2.setObjectName("pushButton_yko_2")
        self.verticalLayout_10.addWidget(self.pushButton_yko_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_vazari_score_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_vazari_score_2.setFont(font)
        self.label_vazari_score_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_vazari_score_2.setObjectName("label_vazari_score_2")
        self.verticalLayout_11.addWidget(self.label_vazari_score_2)
        self.pushButton_vazari_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_vazari_2.setFont(font)
        self.pushButton_vazari_2.setObjectName("pushButton_vazari_2")
        self.verticalLayout_11.addWidget(self.pushButton_vazari_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_ippon_score_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_ippon_score_2.setFont(font)
        self.label_ippon_score_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ippon_score_2.setObjectName("label_ippon_score_2")
        self.verticalLayout_12.addWidget(self.label_ippon_score_2)
        self.pushButton_ippon_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_ippon_2.setFont(font)
        self.pushButton_ippon_2.setObjectName("pushButton_ippon_2")
        self.verticalLayout_12.addWidget(self.pushButton_ippon_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_12)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_shido_score_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_shido_score_2.setFont(font)
        self.label_shido_score_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_shido_score_2.setObjectName("label_shido_score_2")
        self.verticalLayout_13.addWidget(self.label_shido_score_2)
        self.pushButton_shido_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_shido_2.setFont(font)
        self.pushButton_shido_2.setObjectName("pushButton_shido_2")
        self.verticalLayout_13.addWidget(self.pushButton_shido_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_13)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 5)
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

        # ⁡⁢⁣⁣​‌‌‍change score buttons​⁡
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


    def retranslateUi(self, MainWindow):
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
        self.comboBox_member_1.setItemText(0, _translate("MainWindow", "БОЖЕВАЛЬНИКОВ Г."))
        self.comboBox_member_1.setItemText(1, _translate("MainWindow", "АБДУЛКАДЫРОВ И."))
        self.label_organization_1.setText(_translate("MainWindow", "Одинцовская СОШ №3"))
        self.label_total_score_1.setText(_translate("MainWindow", "0"))
        self.label_weight_category.setText(_translate("MainWindow", "Весовая категория"))
        self.comboBox_weight_category.setItemText(0, _translate("MainWindow", "23"))
        self.comboBox_weight_category.setItemText(1, _translate("MainWindow", "25"))
        self.comboBox_weight_category.setItemText(2, _translate("MainWindow", "27"))
        self.comboBox_weight_category.setItemText(3, _translate("MainWindow", "28"))
        self.label_total_time_name.setText(_translate("MainWindow", "Вермя"))
        self.label_total_time.setText(_translate("MainWindow", "00:00"))
        self.pushButton_total_time_start.setText(_translate("MainWindow", "Старт"))
        self.pushButton_total_time_stop.setText(_translate("MainWindow", "Стоп"))
        self.pushButton_chose_total_time.setText(_translate("MainWindow", "Выбрать время"))
        self.label_hold.setText(_translate("MainWindow", "Удержание"))
        self.label_hold_time.setText(_translate("MainWindow", "0.0"))
        self.pushButton_hold_start.setText(_translate("MainWindow", "Старт"))
        self.pushButton_hold_stop.setText(_translate("MainWindow", "Стоп"))
        self.comboBox_member_2.setItemText(0, _translate("MainWindow", "БОЖЕВАЛЬНИКОВ Г."))
        self.comboBox_member_2.setItemText(1, _translate("MainWindow", "АБДУЛКАДЫРОВ И."))
        self.label_organization_2.setText(_translate("MainWindow", "Технолицей им. В.И. Долгих"))
        self.label_total_score_2.setText(_translate("MainWindow", "0"))
        self.label_yko_score_2.setText(_translate("MainWindow", "0"))
        self.pushButton_yko_2.setText(_translate("MainWindow", "ЮКО"))
        self.label_vazari_score_2.setText(_translate("MainWindow", "0"))
        self.pushButton_vazari_2.setText(_translate("MainWindow", "ВАЗАРИ"))
        self.label_ippon_score_2.setText(_translate("MainWindow", "0"))
        self.pushButton_ippon_2.setText(_translate("MainWindow", "ИППОН"))
        self.label_shido_score_2.setText(_translate("MainWindow", "0"))
        self.pushButton_shido_2.setText(_translate("MainWindow", "ШИДО"))


    def functions(self, MainWindow):
        total_time = TotalTime()
        hold_time = HoldTime()

        # ​‌‌‍time functions    ​  
        # total time
        self.pushButton_chose_total_time.clicked.connect(lambda: total_time.set_time(self.get_window_index()))
        self.pushButton_total_time_start.clicked.connect(lambda: total_time.TotalTimer.start())
        self.pushButton_total_time_stop.clicked.connect(lambda: total_time.TotalTimer.stop())

        # hold time
        self.pushButton_hold_start.clicked.connect(lambda: hold_time.start_hold_timer(self.get_window_index()))
        self.pushButton_hold_stop.clicked.connect(lambda: hold_time.stop_hold_time())

        # change combobox information
        self.comboBox_weight_category.currentTextChanged.connect(lambda: self.update_weight_category(self.get_window_index()))
        

    def check_button_event(self, event, name, member_num):
        if event.button() == Qt.LeftButton:
            self.plus_one_score(name, member_num)
        elif event.button() == Qt.RightButton:
            self.minus_one_score(name, member_num)


    def minus_one_score(self, name, member_num):
        text = int(name.text()) - 1
        name.setText(str(text))

        if name in [self.label_shido_score_1, self.label_shido_score_2]:
            self.give_punish_card(name, member_num)
        else:
            self.update_score(member_num)


    def plus_one_score(self, name, member_num):
        text = int(name.text()) + 1
        name.setText(str(text))

        if name in [self.label_shido_score_1, self.label_shido_score_2]:
            self.give_punish_card(name, member_num)
        else:
            self.update_score(member_num)


    ##################### score counter ############################
    def update_score(self, member_num):
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


    def give_punish_card(self, name, member_num):
        index = self.get_window_index()
        ui = SCOREBOARDS_LINKS[index]['scoreboard']['ui']

        if member_num == '1': # ​‌‌‍up member​
            if name.text() == '0':
                self.label_yellow_card_1_1.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.label_yellow_card_1_2.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.label_red_card_1.setStyleSheet("background-color: rgb(255, 255, 255);")

                ui.label_yellow_card_1_1.setStyleSheet("background-color: rgb(255, 255, 255);")
                ui.label_yellow_card_1_2.setStyleSheet("background-color: rgb(255, 255, 255);")
                ui.label_red_card_1.setStyleSheet("background-color: rgb(255, 255, 255);")

            elif name.text() == '1':
                self.label_yellow_card_1_1.setStyleSheet("background-color: rgb(255, 255, 0);")
                self.label_yellow_card_1_2.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.label_red_card_1.setStyleSheet("background-color: rgb(255, 255, 255);")

                ui.label_yellow_card_1_1.setStyleSheet("background-color: rgb(255, 255, 0);")
                ui.label_yellow_card_1_2.setStyleSheet("background-color: rgb(255, 255, 255);")
                ui.label_red_card_1.setStyleSheet("background-color: rgb(255, 255, 255);")

            elif name.text() == '2':
                self.label_yellow_card_1_1.setStyleSheet("background-color: rgb(255, 255, 0);")
                self.label_yellow_card_1_2.setStyleSheet("background-color: rgb(255, 255, 0);")
                self.label_red_card_1.setStyleSheet("background-color: rgb(255, 255, 255);")

                ui.label_yellow_card_1_1.setStyleSheet("background-color: rgb(255, 255, 0);")
                ui.label_yellow_card_1_2.setStyleSheet("background-color: rgb(255, 255, 0);")
                ui.label_red_card_1.setStyleSheet("background-color: rgb(255, 255, 255);")

            elif name.text() == '3':
                self.label_yellow_card_1_1.setStyleSheet("background-color: rgb(255, 255, 0);")
                self.label_yellow_card_1_2.setStyleSheet("background-color: rgb(255, 255, 0);")
                self.label_red_card_1.setStyleSheet("background-color: rgb(255, 0, 0);")

                ui.label_yellow_card_1_1.setStyleSheet("background-color: rgb(255, 255, 0);")
                ui.label_yellow_card_1_2.setStyleSheet("background-color: rgb(255, 255, 0);")
                ui.label_red_card_1.setStyleSheet("background-color: rgb(255, 0, 0);")
            
        elif member_num == '2': # ​‌‌‍down member​
            if name.text() == '0':
                self.label_yellow_card_2_1.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.label_yellow_card_2_2.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.label_red_card_2.setStyleSheet("background-color: rgb(255, 255, 255);")

                ui.label_yellow_card_2_1.setStyleSheet("background-color: rgb(0, 0, 255);")
                ui.label_yellow_card_2_2.setStyleSheet("background-color: rgb(0, 0, 255);")
                ui.label_red_card_2.setStyleSheet("background-color: rgb(0, 0, 255);")

            elif name.text() == '1':
                self.label_yellow_card_2_1.setStyleSheet("background-color: rgb(255, 255, 0);")
                self.label_yellow_card_2_2.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.label_red_card_2.setStyleSheet("background-color: rgb(255, 255, 255);")

                ui.label_yellow_card_2_1.setStyleSheet("background-color: rgb(255, 255, 0);")
                ui.label_yellow_card_2_2.setStyleSheet("background-color: rgb(0, 0, 255);")
                ui.label_red_card_2.setStyleSheet("background-color: rgb(0, 0, 255);")

            elif name.text() == '2':
                self.label_yellow_card_2_1.setStyleSheet("background-color: rgb(255, 255, 0);")
                self.label_yellow_card_2_2.setStyleSheet("background-color: rgb(255, 255, 0);")
                self.label_red_card_2.setStyleSheet("background-color: rgb(255, 255, 255);")

                ui.label_yellow_card_2_1.setStyleSheet("background-color: rgb(255, 255, 0);")
                ui.label_yellow_card_2_2.setStyleSheet("background-color: rgb(255, 255, 0);")
                ui.label_red_card_2.setStyleSheet("background-color: rgb(0, 0, 255);")

            elif name.text() == '3':
                self.label_yellow_card_2_1.setStyleSheet("background-color: rgb(255, 255, 0);")
                self.label_yellow_card_2_2.setStyleSheet("background-color: rgb(255, 255, 0);")
                self.label_red_card_2.setStyleSheet("background-color: rgb(255, 0, 0);")

                ui.label_yellow_card_2_1.setStyleSheet("background-color: rgb(255, 255, 0);")
                ui.label_yellow_card_2_2.setStyleSheet("background-color: rgb(255, 255, 0);")
                ui.label_red_card_2.setStyleSheet("background-color: rgb(255, 0, 0);")

        
    #################### update fighter information ######################
    def update_weight_category(self, window_id):
        scoreboard = SCOREBOARDS_LINKS[window_id]['scoreboard']['ui']
        maneger = SCOREBOARDS_LINKS[window_id]['maneger']['ui']

        scoreboard.label_weight_category.setText(maneger.comboBox_weight_category.currentText())


    def get_window_index(self) -> int:
        """
        return index of window where this function was called
        """
        memory_address = id(self)

        # # ​‌‍‌test prints​
        # print(memory_address)
        # print(SCOREBOARDS_LINKS)

        for index in SCOREBOARDS_LINKS:
            if SCOREBOARDS_LINKS[index]['maneger']['id'] == memory_address:
                return index
        return 0
            
       