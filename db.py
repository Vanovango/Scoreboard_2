import sys
from PyQt5 import QtWidgets
import sqlite3
import pandas as pd

from config import SCOREBOARDS_LINKS


class Database():
    def __init__(self):
        self.path = None

        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()        
    
    def create_table(self):

        # get path to db befor start app
        QtWidgets.QMessageBox.warning(None, 'Предупреждение', 'Выберите файл с данными об участниках')
        self.path = QtWidgets.QFileDialog.getOpenFileName()[0]

        self.cursor.execute("DROP TABLE IF EXISTS members_list;")

        wb = pd.read_excel(self.path, sheet_name = None)

        for sheet in wb:
            wb[sheet].to_sql('members_list', self.connection, index=False)

        self.connection.commit()


    def get_weight_categories(self):
        weight_categories_list = []

        self.cursor.execute("SELECT DISTINCT Весовая FROM members_list")
        rows = self.cursor.fetchall()

        for row in rows:
            weight_categories_list.append(str(row[0]))
        
        return weight_categories_list
    

    def get_members_list(self, weight_category):
        members_list = {'Members': [], 'Teams': []}

        self.cursor.execute(f"SELECT Спортсмен, Команда FROM members_list WHERE Весовая = {weight_category}")
        rows = self.cursor.fetchall()

        for row in rows:
            if row[0] != None:
                tmp_member_name = row[0].split()[0] + ' ' + row[0].split()[1][0] + '.'
                members_list['Members'].append(tmp_member_name)
                members_list['Teams'].append(row[1].replace(u'\xa0', u''))

        # print(members_list)
        return members_list

