from PyQt5 import QtCore, QtGui, QtWidgets
from db import Database


class Ui_MembersList(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # Label weight_category
        self.label_name_weight_category = QtWidgets.QLabel(self.centralwidget)
        font_label = QtGui.QFont()
        font_label.setPointSize(18)
        self.label_name_weight_category.setFont(font_label)
        self.label_name_weight_category.setObjectName("label_name_weight_category")
        self.gridLayout.addWidget(self.label_name_weight_category, 0, 0, 1, 1)

        # ComboBox weight_category
        self.comboBox_weight_category = QtWidgets.QComboBox(self.centralwidget)
        font_combo = QtGui.QFont()
        font_combo.setPointSize(20)
        self.comboBox_weight_category.setFont(font_combo)
        self.comboBox_weight_category.setObjectName("comboBox_weight_category")
        self.gridLayout.addWidget(self.comboBox_weight_category, 0, 1, 1, 1)

        # Label group
        self.label_name_group = QtWidgets.QLabel(self.centralwidget)
        font_label = QtGui.QFont()
        font_label.setPointSize(18)
        self.label_name_group.setFont(font_label)
        self.label_name_group.setObjectName("label_name_group")
        self.gridLayout.addWidget(self.label_name_group, 1, 0, 1, 1)

        # ComboBox group
        self.comboBox_group = QtWidgets.QComboBox(self.centralwidget)
        font_combo = QtGui.QFont()
        font_combo.setPointSize(20)
        self.comboBox_group.setFont(font_combo)
        self.comboBox_group.setObjectName("comboBox_group")
        self.gridLayout.addWidget(self.comboBox_group, 1, 1, 1, 1)

        # QTableView
        self.tableView_members_list = QtWidgets.QTableView(self.centralwidget)
        self.tableView_members_list.setObjectName("tableView_members_list")
        self.tableView_members_list.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.tableView_members_list.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableView_members_list.setShowGrid(True)
        self.tableView_members_list.setGridStyle(QtCore.Qt.SolidLine)
        self.tableView_members_list.setStyleSheet("""
            QTableView {
                gridline-color: #CCCCCC;
                border: 1px solid #CCCCCC;
            }
            QHeaderView::section {
                border-bottom: 2px solid #888888;
            }
        """)
        self.gridLayout.addWidget(self.tableView_members_list, 2, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        # === Инициализация ===
        self.data = Database()
        self.model = QtGui.QStandardItemModel()
        self.setup_table_headers()
        self.tableView_members_list.setModel(self.model)

        # Загрузка весовых категорий
        self.group = []
        self.weight_categories = self.data.get_weight_categories()  # Уже отсортированы по возрастанию
        self.comboBox_weight_category.addItems(self.weight_categories)

        # Подключение сигнала
        self.comboBox_weight_category.currentTextChanged.connect(lambda: self.update_group_combobox(int(self.comboBox_weight_category.currentText())))


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setup_table_headers(self):
        """Устанавливает заголовки таблицы — жирный шрифт, размер 16"""
        headers = ["Спортсмен", "Год рождения", "Команда", "Побед", "Поражений", "Место"]
        self.model.setHorizontalHeaderLabels(headers)

        # Шрифт для заголовков
        header_font = QtGui.QFont()
        header_font.setPointSize(10)
        header_font.setBold(True)

        for i in range(self.model.columnCount()):
            header_item = self.model.horizontalHeaderItem(i)
            if header_item:
                header_item.setFont(header_font)
                header_item.setTextAlignment(QtCore.Qt.AlignCenter)

        # Подключаем обработчик изменений
        self.model.dataChanged.connect(self.on_data_changed)

    def on_data_changed(self, topLeft, bottomRight, roles):
        """Обработка изменения данных с валидацией"""
        row = topLeft.row()

        # Проверяем, что строка существует
        athlete_item = self.model.item(row, 0)
        if not athlete_item:
            return

        member_item = athlete_item.text()
        
        # Получаем элементы с проверкой на существование
        wins_item = self.model.item(row, 3)  # Столбец "Побед"
        losses_item = self.model.item(row, 4)  # Столбец "Поражений"  
        place_item = self.model.item(row, 5)  # Столбец "Место"

        # Безопасное получение значений
        wins = wins_item.text().strip() if wins_item else ""
        losses = losses_item.text().strip() if losses_item else ""
        place = place_item.text().strip() if place_item else ""

        # Валидация числовых полей
        if wins and not wins.isdigit():
            QtWidgets.QMessageBox.warning(None, "Ошибка", "Поле 'Побед' должно содержать только цифры")
            return
            
        if losses and not losses.isdigit():
            QtWidgets.QMessageBox.warning(None, "Ошибка", "Поле 'Поражений' должно содержать только цифры")
            return

        weight_category = self.comboBox_weight_category.currentText()

        success = self.data.update_member_in_db(member_item, wins, losses, place, weight_category)
        if not success:
            QtWidgets.QMessageBox.warning(None, "Ошибка", f"Не удалось обновить данные для {member_item}")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Список участников"))
        self.label_name_weight_category.setText(_translate("MainWindow", "Весовая категория"))
        self.label_name_group.setText(_translate("MainWindow", "Группа"))
    

    def update_group_combobox(self, weight_category):
        self.comboBox_group.clear()

        # Загрузка групп

        groups = self.data.get_groups(weight_category)
        self.comboBox_group.addItems(sorted(groups))

        self.comboBox_group.currentTextChanged.connect(lambda: self.update_members_list(weight_category, self.comboBox_group.currentText()))


    def update_members_list(self, weight_category, group):
        if not weight_category or not group:
            return

        self.model.setRowCount(0)
        members_data = self.data.get_all_list(weight_category, group)

        edit_background = QtGui.QColor(245, 245, 245)
        font = QtGui.QFont()
        font.setPointSize(10)

        for member in members_data:
            name = member.get('Спортсмен', '')
            date_of_birth = member.get('Год рождения', '')
            team = member.get('Команда', '')
            wins = str(member.get('Побед', '') or '').strip()
            losses = str(member.get('Поражений', '') or '').strip()
            place = str(member.get('Место', '') or '').strip()

            item_name = QtGui.QStandardItem(name)
            item_date_of_birth = QtGui.QStandardItem(date_of_birth)
            item_team = QtGui.QStandardItem(team)
            item_wins = QtGui.QStandardItem(wins)
            item_losses = QtGui.QStandardItem(losses)
            item_place = QtGui.QStandardItem(place)

            for item in [item_name, item_date_of_birth, item_team, item_wins, item_losses, item_place]:
                item.setFont(font)

            # Выравнивание
            item_date_of_birth.setTextAlignment(QtCore.Qt.AlignCenter)
            item_wins.setTextAlignment(QtCore.Qt.AlignCenter)
            item_losses.setTextAlignment(QtCore.Qt.AlignCenter)
            item_place.setTextAlignment(QtCore.Qt.AlignCenter)

            # Только чтение: Спортсмен и Команда
            item_name.setEditable(False)
            item_team.setEditable(False)
            item_name.setBackground(QtGui.QColor(255, 255, 255))
            item_team.setBackground(QtGui.QColor(255, 255, 255))

            # Редактируемые
            item_wins.setEditable(True)
            item_losses.setEditable(True)
            item_place.setEditable(True)
            for item in [item_wins, item_losses, item_place]:
                item.setBackground(edit_background)

            # Добавляем строку: 0=Спортсмен, 1=Год рождения, 2=Группа, 3=Команда, 4=Побед, 5=Поражений, 6=Место
            self.model.appendRow([item_name, item_date_of_birth, item_team, item_wins, item_losses, item_place])

  