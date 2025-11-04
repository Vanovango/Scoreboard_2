import sqlite3
import pandas as pd

from config import SCOREBOARDS_LINKS, PATH_TO_EXCEL


class Database():
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()

        if PATH_TO_EXCEL is None:
            PATH_TO_EXCEL = 'C:\Code\Projects\Scoreboard_2\Шаблон соревнований.xlsx'
        self.path = PATH_TO_EXCEL
    
    def create_table(self):
        self.cursor.execute("DROP TABLE IF EXISTS members_list;")

        wb = pd.read_excel(self.path, sheet_name = None)

        for sheet in wb:
            wb[sheet].to_sql('members_list', self.connection, index=False)

        self.connection.commit()


    def fill_weight_category(self):
        weight_categories_list = []

        self.cursor.execute("SELECT DISTINCT Весовая_категория FROM members_list")
        rows = self.cursor.fetchall()

        for row in rows:
            weight_categories_list.append(row[0])

       

data = Database()
data.create_table()
data.fill_weight_category()