import sys
from PyQt5 import QtWidgets
import sqlite3
import pandas as pd

from config import SCOREBOARDS_LINKS


class Database():
    def __init__(self):
        
        # get path to db befor start app
        QtWidgets.QMessageBox.warning(None, 'Предупреждение', 'Выберите файл с данными об участниках')
        self.path = QtWidgets.QFileDialog.getOpenFileName()[0]

        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()        
    
    def create_table(self):

        self.cursor.execute("DROP TABLE IF EXISTS members_list;")

        wb = pd.read_excel(self.path, sheet_name = None)

        for sheet in wb:
            wb[sheet].to_sql('members_list', self.connection, index=False)

        self.connection.commit()

        print("DB is currently created!")


    def fill_weight_category(self):
        weight_categories_list = []

        self.cursor.execute("SELECT DISTINCT Весовая FROM members_list")
        rows = self.cursor.fetchall()

        for row in rows:
            weight_categories_list.append(row[0])


# data = Database()
# data.create_table()
# data.fill_weight_category()