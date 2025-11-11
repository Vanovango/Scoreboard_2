# тестирую код загрузки данных из Google Sheets, сгенерированный ИИ

import csv
import sqlite3
import requests

# Настройки
SHEET_URL = "https://docs.google.com/spreadsheets/d/{KEY}/export?format=csv"
DB_NAME = "data.db"
TABLE_NAME = "my_table"

# Загрузка данных из Google Sheets
response = requests.get(SHEET_URL)
response.encoding = "utf-8"  # Для корректного отображения кириллицы
data = response.text.splitlines()

# Чтение CSV
csv_reader = csv.reader(data)
headers = next(csv_reader)
rows = list(csv_reader)

# Подключение к SQLite
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# Создание таблицы (столбцы называются как в первой строке CSV)
columns = ", ".join([f'"{header}" TEXT' for header in headers])
cursor.execute(f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} ({columns})")

# Вставка данных
placeholders = ", ".join(["?"] * len(headers))
cursor.executemany(
    f"INSERT INTO {TABLE_NAME} VALUES ({placeholders})",
    rows
)

# Фиксация изменений и закрытие соединения
conn.commit()
conn.close()