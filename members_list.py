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

        # Label
        self.label_name_weight_category = QtWidgets.QLabel(self.centralwidget)
        font_label = QtGui.QFont()
        font_label.setPointSize(18)
        self.label_name_weight_category.setFont(font_label)
        self.label_name_weight_category.setObjectName("label_name_weight_category")
        self.gridLayout.addWidget(self.label_name_weight_category, 0, 0, 1, 1)

        # ComboBox
        self.comboBox_weight_category = QtWidgets.QComboBox(self.centralwidget)
        font_combo = QtGui.QFont()
        font_combo.setPointSize(20)
        self.comboBox_weight_category.setFont(font_combo)
        self.comboBox_weight_category.setObjectName("comboBox_weight_category")
        self.gridLayout.addWidget(self.comboBox_weight_category, 0, 1, 1, 1)

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
        """Устанавливает заголовки таблицы — жирный шрифт, размер 16"""
        headers = ["Спортсмен", "Команда", "Побед|Поражений", "Место"]
        self.model.setHorizontalHeaderLabels(headers)

        # Шрифт для заголовков
        header_font = QtGui.QFont()
        header_font.setPointSize(16)
        header_font.setBold(True)

        for i in range(self.model.columnCount()):
            header_item = self.model.horizontalHeaderItem(i)
            if header_item:
                header_item.setFont(header_font)
                header_item.setTextAlignment(QtCore.Qt.AlignCenter)

        # Подключаем обработчик изменений
        self.model.dataChanged.connect(self.on_data_changed)

    def on_data_changed(self, topLeft, bottomRight, roles):
        """Обработка изменения данных в таблице"""
        row = topLeft.row()
        athlete_item = self.model.item(row, 0)
        if not athlete_item:
            return

        athlete_name = athlete_item.text()
        record = self.model.item(row, 2).text() if self.model.item(row, 2) else ""
        place_text = self.model.item(row, 3).text() if self.model.item(row, 3) else ""

        try:
            place = int(place_text) if place_text.strip() else None
        except ValueError:
            QtWidgets.QMessageBox.warning(None, "Ошибка", "Место должно быть целым числом.")
            self.update_members_list(self.comboBox_weight_category.currentText())
            return

        weight_category = self.comboBox_weight_category.currentText()

        success = self.data.update_member_in_db(athlete_name, record, place, weight_category)
        if not success:
            QtWidgets.QMessageBox.warning(None, "Ошибка", f"Не удалось обновить данные для {athlete_name}")
            self.update_members_list(weight_category)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Список участников"))
        self.label_name_weight_category.setText(_translate("MainWindow", "Весовая категория"))

    def update_members_list(self, weight_category):
        """
        Заполняет таблицу. Если 'Побед|Поражений' — None или пустое, отображаем пустую строку.
        """
        if not weight_category:
            return

        self.model.setRowCount(0)
        members_data = self.data.get_all_list(weight_category)

        edit_background = QtGui.QColor(245, 245, 245)  # Светло-серый фон
        font = QtGui.QFont()
        font.setPointSize(16)

        for member in members_data:
            name = member.get('Спортсмен', '')
            team = member.get('Команда', '')

            # Обработка "Побед|Поражений": None → пусто
            record_raw = member.get('Побед|Поражений')
            record = str(record_raw) if record_raw not in (None, '', 'None') else ""

            place = member.get('Место', '')

            try:
                place_int = int(place) if place and str(place).strip().isdigit() else ""
            except:
                place_int = ""

            item_name = QtGui.QStandardItem(name)
            item_team = QtGui.QStandardItem(team)
            item_record = QtGui.QStandardItem(record)
            item_place = QtGui.QStandardItem(str(place_int) if place_int != "" else "")

            # Применяем шрифт
            for item in [item_name, item_team, item_record, item_place]:
                item.setFont(font)

            # Выравнивание по центру
            item_record.setTextAlignment(QtCore.Qt.AlignCenter)
            item_place.setTextAlignment(QtCore.Qt.AlignCenter)

            # Только чтение: Спортсмен и Команда
            item_name.setEditable(False)
            item_team.setEditable(False)
            item_name.setBackground(QtGui.QColor(255, 255, 255))
            item_team.setBackground(QtGui.QColor(255, 255, 255))

            # Редактируемые — серый фон
            item_record.setEditable(True)
            item_place.setEditable(True)
            item_record.setBackground(edit_background)
            item_place.setBackground(edit_background)

            self.model.appendRow([item_name, item_team, item_record, item_place])

        # Настройка ширины столбцов: 3:3:2:2
        table_width = self.tableView_members_list.width()
        self.tableView_members_list.setColumnWidth(0, int(table_width * 0.30))  # Спортсмен
        self.tableView_members_list.setColumnWidth(1, int(table_width * 0.30))  # Команда
        self.tableView_members_list.setColumnWidth(2, int(table_width * 0.20))  # Побед|Поражений
        self.tableView_members_list.setColumnWidth(3, int(table_width * 0.20))  # Место

        # Адаптивное изменение ширины при ресайзе
        self.tableView_members_list.resizeEvent = self.make_resize_event()

    def make_resize_event(self):
        """Переопределяем resizeEvent для адаптивной ширины столбцов"""
        def _resize_event(event):
            QtWidgets.QTableView.resizeEvent(self.tableView_members_list, event)
            table_width = self.tableView_members_list.width()
            if table_width > 100:
                self.tableView_members_list.setColumnWidth(0, int(table_width * 0.30))
                self.tableView_members_list.setColumnWidth(1, int(table_width * 0.30))
                self.tableView_members_list.setColumnWidth(2, int(table_width * 0.20))
                self.tableView_members_list.setColumnWidth(3, int(table_width * 0.20))
        return _resize_event
