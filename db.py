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
    
    def choose_upload_source(self):

        msgBox = QMessageBox()
        msgBox.setWindowTitle("Информация")
        msgBox.setText("Выберите способ загрузки таблицы с информацией об участниках.")
        btn_google = msgBox.addButton('Google', QMessageBox.ButtonRole.ActionRole)
        btn_excel = msgBox.addButton('Excel', QMessageBox.ButtonRole.ActionRole)
        msgBox.exec()

        if msgBox.clickedButton() == btn_google:
            print("Google")
        elif msgBox.clickedButton() == btn_excel:
            self.upload_from_xl()


    def upload_from_google(self):
        pass

    def upload_from_xl(self):
        self.xl_path = QtWidgets.QFileDialog.getOpenFileName()[0]

        self.cursor.execute("DROP TABLE IF EXISTS members_list;")

        wb = pd.read_excel(self.xl_path, sheet_name = None)

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


    def get_all_list(self, weight_category):
        members_list = []

        self.cursor.execute(f"SELECT * FROM members_list WHERE Весовая = {weight_category}")
        rows = self.cursor.fetchall()

        for row in rows:
            if row[0] != None:
                members_list.append(
                    {
                    'Спортсмен': row[0],
                    'Команда': row[1],
                    'Побед|Поражений': row[3],
                    'Место': row[4]
                    })

                
        # print(members_list)
        return members_list