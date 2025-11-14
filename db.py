import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import pandas as pd

from config import SCOREBOARDS_LINKS


class Database():
    def __init__(self):
        self.xl_path = None

        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()        


    def upload_from_xl(self):
        self.xl_path = QtWidgets.QFileDialog.getOpenFileName()[0]

        self.cursor.execute("DROP TABLE IF EXISTS members_list;")

        wb = pd.read_excel(self.xl_path, sheet_name=None)

        # типы данных для столбцов таблицы
        type_map = {
            'Спортсмен': 'TEXT',
            'Год рождения': 'TEXT',
            'Весовая_категория': 'INTEGER',
            'Группа': 'TEXT',
            'Команда': 'TEXT',
            'Возростная_категория': 'TEXT',
        }

        for sheet in wb:
            wb[sheet].to_sql('members_list', self.connection, index=False, dtype=type_map)

        self.cursor.execute("ALTER TABLE members_list ADD COLUMN 'Побед' INTEGER;")
        self.cursor.execute("ALTER TABLE members_list ADD COLUMN 'Поражений' INTEGER;")
        self.cursor.execute("ALTER TABLE members_list ADD COLUMN 'Место' INTEGER;")

        self.connection.commit()


    def get_weight_categories(self):
        weight_categories_list = []

        self.cursor.execute("SELECT DISTINCT Весовая_категория FROM members_list")
        rows = self.cursor.fetchall()

        for row in rows:
            weight_categories_list.append(str(row[0]))
        
        return weight_categories_list
    

    def get_groups(self, weight_category):
        groups_list = []

        self.cursor.execute(f"SELECT DISTINCT Группа FROM members_list WHERE Весовая_категория = {weight_category}")
        rows = self.cursor.fetchall()

        for row in rows:
            groups_list.append(str(row[0]))
        
        return groups_list


    def get_members_list(self, weight_category):
        members_list = {'Members': [], 'Teams': []}

        self.cursor.execute(f"SELECT Спортсмен, Команда FROM members_list WHERE Весовая_категория = {weight_category}")
        rows = self.cursor.fetchall()

        for row in rows:
            if row[0] != None:
                tmp_member_name = row[0].split()[0] + ' ' + row[0].split()[1][0] + '.'
                members_list['Members'].append(tmp_member_name)
                members_list['Teams'].append(row[1].replace(u'\xa0', u''))

        return members_list

    def get_all_list(self, weight_category, group):
        
        if weight_category is None or group is None:
            return []
        
        members_list = []

        self.cursor.execute(f"SELECT * FROM members_list WHERE Весовая_категория = {weight_category} AND Группа = {group}")
        rows = self.cursor.fetchall()

        for row in rows:
            if row[0] is not None:
                members_list.append({
                    'Спортсмен': row[0],
                    'Год рождения': row[1],
                    'Команда': row[4],
                    'Побед': row[6],
                    'Поражений': row[7],
                    'Место': row[8]
                })

        return members_list


    def update_member_in_db(self, member, wins, losses, place, weight_category):
        try:
            with sqlite3.connect('database.db') as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE members_list 
                    SET 'Побед' = ?, 'Поражений' = ?, 'Место' = ? 
                    WHERE 'Спортсмен' = ? AND 'Вес кат' = ?
                ''', (int(wins), int(losses), int(place), member, weight_category))
                conn.commit()
                return True
        except Exception as e:
            print(f"Ошибка обновления: {e}")
            return False

