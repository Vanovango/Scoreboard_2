from PyQt5 import QtCore, QtGui, QtWidgets
from db import Database


class Ui_MembersList(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)  # Увеличили ширину под 5 столбцов
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # Label
        self.label_name_weight_category = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_name_weight_category.setFont(font)
        self.label_name_weight_category.setObjectName("label_name_weight_category")
        self.gridLayout.addWidget(self.label_name_weight_category, 0, 0, 1, 1)

        # ComboBox
        self.comboBox_weight_category = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_weight_category.setFont(font)
        self.comboBox_weight_category.setObjectName("comboBox_weight_category")
        self.gridLayout.addWidget(self.comboBox_weight_category, 0, 1, 1, 1)

        # QTableView — теперь с 4 колонками
        self.tableView_members_list = QtWidgets.QTableView(self.centralwidget)
        self.tableView_members_list.setObjectName("tableView_members_list")
        self.tableView_members_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView_members_list.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.gridLayout.addWidget(self.tableView_members_list, 1, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        # === Инициализация ===
        self.data = Database()
        self.model = QtGui.QStandardItemModel()
        self.setup_table_headers()
        self.tableView_members_list.setModel(self.model)

        # Загрузка весовых категорий
        weight_categories = self.data.get_weight_categories()
        self.comboBox_weight_category.addItems(weight_categories)

        # Подключение сигнала
        self.comboBox_weight_category.currentTextChanged.connect(self.update_members_list)

        # Показать данные при старте
        if weight_categories:
            self.update_members_list(weight_categories[0])

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setup_table_headers(self):
        """Устанавливает заголовки таблицы"""
        headers = ["Спортсмен", "Команда", "Побед|Поражений", "Место"]
        self.model.setHorizontalHeaderLabels(headers)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Список участников"))
        self.label_name_weight_category.setText(_translate("MainWindow", "Весовая категория"))

    def update_members_list(self, weight_category):
        """
        Загружает и отображает данные участников с нужными колонками.
        Ожидается, что get_members_list возвращает список словарей вида:
        {
            'Спортсмен': 'Иванов Иван',
            'Команда': 'Динамо',
            'Побед|Поражений': '3-1',
            'Место': '1'
        }
        """
        if not weight_category:
            return

        # Очистка таблицы
        self.model.setRowCount(0)

        # Получаем данные
        members_data = self.data.get_all_list(weight_category)  # Должен вернуть список словарей

        for member in members_data:
            # Формируем ячейки
            item_name = QtGui.QStandardItem(member.get('Спортсмен', ''))
            item_team = QtGui.QStandardItem(member.get('Команда', ''))
            item_record = QtGui.QStandardItem(member.get('Побед|Поражений', 0))
            item_place = QtGui.QStandardItem(member.get('Место', ''))

            # Отключаем редактирование
            for item in [item_name, item_team, item_record]:
                item.setSelectable(False)

            # Добавляем строку
            self.model.appendRow([item_name, item_team, item_record, item_place])



# from PyQt5 import QtCore, QtGui, QtWidgets
# from db import Database

# class Ui_MembersList(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(875, 701)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
#         self.gridLayout.setObjectName("gridLayout")
#         self.label_name_weight_category = QtWidgets.QLabel(self.centralwidget)
#         font = QtGui.QFont()
#         font.setPointSize(18)
#         self.label_name_weight_category.setFont(font)
#         self.label_name_weight_category.setObjectName("label_name_weight_category")
#         self.gridLayout.addWidget(self.label_name_weight_category, 0, 0, 1, 1)
#         self.comboBox_weight_category = QtWidgets.QComboBox(self.centralwidget)
#         font = QtGui.QFont()
#         font.setPointSize(20)
#         font.setBold(False)
#         font.setWeight(50)
#         self.comboBox_weight_category.setFont(font)
#         self.comboBox_weight_category.setEditable(False)
#         self.comboBox_weight_category.setObjectName("comboBox_weight_category")
#         # load weight categories to combobox
#         self.data = Database()
#         self.comboBox_weight_category.addItems(self.data.get_weight_categories())
#         self.gridLayout.addWidget(self.comboBox_weight_category, 0, 1, 1, 1)
#         self.listView_members_list = QtWidgets.QListView(self.centralwidget)
#         self.listView_members_list.setObjectName("listView_members_list")
#         self.gridLayout.addWidget(self.listView_members_list, 1, 0, 1, 2)
#         MainWindow.setCentralWidget(self.centralwidget)

#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)

#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.label_name_weight_category.setText(_translate("MainWindow", "Весовая категория"))


#     def functions(self):
#         self.comboBox_weight_category.currentTextChanged.connect(self.update_members_list)


#     def update_members_list(self):
#         members_list = self.data.get_members_list(self.comboBox_weight_category.currentText())



