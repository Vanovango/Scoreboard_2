import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import sqlite3
import pandas as pd
import os
from datetime import datetime

from config import SCOREBOARDS_LINKS


class Database():
    def __init__(self):
        self.xl_path = None
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()      


    def upload_from_xl(self):
        try:
            self.xl_path = QtWidgets.QFileDialog.getOpenFileName(
                None,
                "Загрузка данных из Excel",
                "",
                "Excel Files (*.xlsx);;All Files (*)"
            )[0]

            if not self.xl_path:
                return False

            self.cursor.execute("DROP TABLE IF EXISTS members_list;")

            wb = pd.read_excel(self.xl_path, sheet_name=None)

            # типы данных для столбцов таблицы
            type_map = {
                'Спортсмен': 'TEXT',
                'Год рождения': 'TEXT',
                'Весовая_категория': 'INTEGER',
                'Группа': 'TEXT',
                'Команда': 'TEXT',
                'Возрастная_категория': 'TEXT',
            }

            for sheet in wb:
                wb[sheet].to_sql('members_list', self.connection, index=False, dtype=type_map)

            # Добавляем колонки для результатов если их нет
            self.cursor.execute("PRAGMA table_info(members_list)")
            columns = [column[1] for column in self.cursor.fetchall()]
            
            if 'Побед' not in columns:
                self.cursor.execute("ALTER TABLE members_list ADD COLUMN 'Побед' INTEGER;")
            if 'Поражений' not in columns:
                self.cursor.execute("ALTER TABLE members_list ADD COLUMN 'Поражений' INTEGER;")
            if 'Место' not in columns:
                self.cursor.execute("ALTER TABLE members_list ADD COLUMN 'Место' INTEGER;")

            self.connection.commit()
            
            QMessageBox.information(
                None,
                "Загрузка завершена",
                f"Данные успешно загружены из файла:\n{self.xl_path}"
            )
            return True
            
        except Exception as e:
            error_msg = f"Ошибка при загрузке из Excel:\n{str(e)}"
            print(error_msg)
            QMessageBox.critical(
                None,
                "Ошибка загрузки",
                error_msg
            )
            return False


    def export_to_excel(self):
        """
        Экспорт всей базы данных в Excel файл
        Пользователь выбирает путь и название файла
        """
        try:
            # Диалог выбора места сохранения
            file_path, _ = QFileDialog.getSaveFileName(
                None,
                "Экспорт результатов в Excel",
                "",
                "Excel Files (*.xlsx);;All Files (*)"
            )
            
            if not file_path:
                return False  # Пользователь отменил диалог
            
            # Добавляем расширение .xlsx если его нет
            if not file_path.lower().endswith('.xlsx'):
                file_path += '.xlsx'
            
            # Читаем все данные из базы
            query = """
            SELECT 
                Спортсмен,
                "Год рождения" as "Год рождения",
                Весовая_категория as "Весовая категория",
                Группа,
                Команда,
                Возрастная_категория as "Возрастная категория",
                "Побед",
                "Поражений",
                "Место"
            FROM members_list 
            ORDER BY "Весовая категория", Группа, "Место", "Побед" DESC
            """
            
            df = pd.read_sql_query(query, self.connection)
            
            # Создаем Excel writer
            with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
                # Основной лист с данными
                df.to_excel(writer, sheet_name='Результаты', index=False)
                
                # Автоподбор ширины колонок
                worksheet = writer.sheets['Результаты']
                for column in worksheet.columns:
                    max_length = 0
                    column_letter = column[0].column_letter
                    for cell in column:
                        try:
                            if len(str(cell.value)) > max_length:
                                max_length = len(str(cell.value))
                        except:
                            pass
                    adjusted_width = min(max_length + 2, 50)
                    worksheet.column_dimensions[column_letter].width = adjusted_width
                
                # Дополнительный лист со сводкой по весовым категориям
                summary_query = """
                SELECT 
                    Весовая_категория as "Весовая категория",
                    Группа,
                    COUNT(*) as "Количество участников",
                    COUNT(CASE WHEN "Место" = 1 THEN 1 END) as "Первых мест",
                    COUNT(CASE WHEN "Место" = 2 THEN 1 END) as "Вторых мест", 
                    COUNT(CASE WHEN "Место" = 3 THEN 1 END) as "Третьих мест"
                FROM members_list 
                GROUP BY "Весовая категория", Группа
                ORDER BY "Весовая категория", Группа
                """
                
                summary_df = pd.read_sql_query(summary_query, self.connection)
                summary_df.to_excel(writer, sheet_name='Сводка', index=False)
                
                # Автоподбор ширины колонок для сводки
                worksheet_summary = writer.sheets['Сводка']
                for column in worksheet_summary.columns:
                    max_length = 0
                    column_letter = column[0].column_letter
                    for cell in column:
                        try:
                            if len(str(cell.value)) > max_length:
                                max_length = len(str(cell.value))
                        except:
                            pass
                    adjusted_width = min(max_length + 2, 30)
                    worksheet_summary.column_dimensions[column_letter].width = adjusted_width
            
            # Сообщение об успешном экспорте
            QMessageBox.information(
                None, 
                "Экспорт завершен", 
                f"Данные успешно экспортированы в файл:\n{file_path}"
            )
            return True
            
        except Exception as e:
            error_msg = f"Ошибка при экспорте в Excel:\n{str(e)}"
            print(error_msg)
            QMessageBox.critical(
                None,
                "Ошибка экспорта",
                error_msg
            )
            return False


    def get_weight_categories(self):
        weight_categories_list = []

        self.cursor.execute("SELECT DISTINCT Весовая_категория FROM members_list WHERE Весовая_категория IS NOT NULL")
        rows = self.cursor.fetchall()

        for row in rows:
            if row[0] is not None:
                try:
                    # Преобразуем в число для правильной сортировки
                    weight = int(row[0])
                    weight_categories_list.append(weight)
                except (ValueError, TypeError):
                    # Если не число, добавляем как есть (на случай текстовых значений)
                    weight_categories_list.append(str(row[0]))
        
        # Сортируем по возрастанию
        try:
            # Пытаемся отсортировать как числа
            weight_categories_list.sort()
        except TypeError:
            # Если есть смешанные типы, сортируем как строки
            weight_categories_list.sort(key=lambda x: str(x))
        
        # Преобразуем обратно в строки для комбобокса
        weight_categories_list = [str(weight) for weight in weight_categories_list]
        
        return weight_categories_list


    def get_groups(self, weight_category):
        """
        Получить список групп для указанной весовой категории
        """
        groups_list = []

        try:
            self.cursor.execute(
                "SELECT DISTINCT Группа FROM members_list WHERE Весовая_категория = ? AND Группа IS NOT NULL", 
                (weight_category,)
            )
            rows = self.cursor.fetchall()

            for row in rows:
                if row[0] is not None:
                    groups_list.append(str(row[0]))
            
            # Сортируем группы в алфавитном порядке
            groups_list.sort()
            
        except Exception as e:
            print(f"Ошибка при получении групп для весовой категории {weight_category}: {e}")
        
        return groups_list


    def get_members_list(self, weight_category, group=None):
        members_list = {'Members': [], 'Teams': []}

        if group:
            # Загружаем участников для конкретной группы
            self.cursor.execute(
                "SELECT Спортсмен, Команда FROM members_list WHERE Весовая_категория = ? AND Группа = ?", 
                (weight_category, group)
            )
        else:
            # Загружаем всех участников весовой категории (для обратной совместимости)
            self.cursor.execute(
                "SELECT Спортсмен, Команда FROM members_list WHERE Весовая_категория = ?", 
                (weight_category,)
            )
        
        rows = self.cursor.fetchall()

        for row in rows:
            if row[0] is not None:
                # Форматируем имя: "Имя Ф."
                name_parts = row[0].split()
                if len(name_parts) >= 2:
                    tmp_member_name = name_parts[0] + ' ' + name_parts[1][0] + '.'
                else:
                    tmp_member_name = row[0]  # fallback если формат нестандартный
                    
                members_list['Members'].append(tmp_member_name)
                
                # Обрабатываем команду - проверяем на None
                team_name = row[1]
                if team_name is not None:
                    # Убираем неразрывные пробелы и лишние пробелы
                    cleaned_team = team_name.replace(u'\xa0', u' ').strip()
                else:
                    cleaned_team = "Не указана"  # Значение по умолчанию для пустых команд
                    
                members_list['Teams'].append(cleaned_team)

        return members_list


    def get_all_list(self, weight_category, group):
        
        if weight_category is None or group is None:
            return []
        
        members_list = []
        
        self.cursor.execute("SELECT * FROM members_list WHERE Весовая_категория = ? AND Группа = ?", (weight_category, group))        
        rows = self.cursor.fetchall()

        for row in rows:
            if row[0] is not None:
                members_list.append({
                    'Спортсмен': row[0],
                    'Год рождения': row[1].split()[0],
                    'Команда': row[4],
                    'Побед': row[6],
                    'Поражений': row[7],
                    'Место': row[8]
                })

        return members_list


    def update_member_in_db(self, member, wins, losses, place, weight_category):
        try:
            # Обработка пустых значений
            wins_int = int(wins) if wins and wins.strip() else 0
            losses_int = int(losses) if losses and losses.strip() else 0
            
            # Место может быть пустым или содержать текст
            place_value = place if place and place.strip() else None
            
            with sqlite3.connect('database.db') as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE members_list 
                    SET "Побед" = ?, "Поражений" = ?, "Место" = ? 
                    WHERE "Спортсмен" = ? AND "Весовая_категория" = ?
                ''', (wins_int, losses_int, place_value, member, weight_category))
                conn.commit()
                return True
        except ValueError as e:
            print(f"Ошибка преобразования данных: {e}")
            return False
        except Exception as e:
            print(f"Ошибка обновления: {e}")
            return False

