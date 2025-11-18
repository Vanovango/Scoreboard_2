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


    def generete_diploms(self):
        try:
            # Диалог выбора места сохранения
            path_to_save_pdf, _ = QFileDialog.getSaveFileName(
                None,
                "Путь сохранения маски для грамот",
                "",
                "PDF (.pdf);; All Files (*)"
            )
            
            if not path_to_save_pdf:
                return False  # Пользователь отменил диалог
            
            # Добавляем расширение .pdf если его нет
            if not path_to_save_pdf.lower().endswith('.pdf'):
                path_to_save_pdf += '.pdf'


            # место для моего кода
            query = """
                    SELECT Спортсмен, Весовая_категория, Группа, Возрастная_категория, Место
                    FROM members_list
                    WHERE Место IS NOT NULL;
                    """
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            print(rows)

            list_for_pdf = []

            for row in rows:
                list_for_pdf.append({
                    "Спортсмен": row[0],
                    "Весовая_категория": f"{row[1]} {row[2]}",
                    "Возрастная_категория": f"{row[3]}",
                    "Место": f"{row[4]}"
                })

            
            if self.ganerate_and_save_pdf(list_for_pdf, path_to_save_pdf):
                # Сообщение об успешном экспорте
                QMessageBox.information(
                    None, 
                    "Генерация завершина", 
                    f"Файл успешно сохранен здесь:\n{path_to_save_pdf}"
                )
                return True

        except Exception as e:
            error_msg = f"Ошибка при генерации грамот:\n{str(e)}"
            print(error_msg)
            QMessageBox.critical(
                None,
                "Ошибка экспорта",
                error_msg
            )
            return False


    def ganerate_and_save_pdf(self, list_for_pdf, path_to_save_pdf):
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import A4, landscape
        from reportlab.lib.units import mm
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        from pypdf import PdfReader, PdfWriter
        import io
        import os
        import copy
        from pathlib import Path

        # Регистрируем шрифт
        pdfmetrics.registerFont(TTFont('DejaVuSans', 'pdf_editor/DejaVuSans.ttf'))

        # Пути для сохранения
        mask_output_path = path_to_save_pdf
        merged_output_path = str(Path(path_to_save_pdf).parent / "пример_грамот.pdf")
        template_path = "pdf_editor/diploma.pdf"

        # Создаем кастомный размер страницы 309 × 222 мм в горизонтальной ориентации
        custom_size = (309 * mm, 222 * mm)  # 309 мм ширина, 222 мм высота

        # Создаем временный PDF в памяти для маски
        packet = io.BytesIO()

        # Создаем canvas с кастомным размером страницы
        can = canvas.Canvas(packet, pagesize=custom_size)

        # Проходим по всем элементам списка и создаем страницу для каждого
        for data in list_for_pdf:
            # ВАЖНО: Устанавливаем прозрачность через сохранение состояния
            can.saveState()
            
            # Рисуем прозрачный прямоугольник на всю страницу
            can.setFillColorRGB(1, 1, 1, alpha=0)  # Полностью прозрачный
            can.rect(0, 0, custom_size[0], custom_size[1], fill=1, stroke=0)
            can.restoreState()
            
            # Теперь устанавливаем черный цвет для текста
            can.setFillColorRGB(0, 0, 0)  # Черный текст
            
            # Рисуем центрированное ФИО
            self.draw_centered_text(can, data['Спортсмен'], 350, 'DejaVuSans', 24, custom_size)
            
            # Остальной текст рисуем как раньше (координаты остаются прежними)
            can.setFont("DejaVuSans", 24)
            can.drawString(430, 315, data['Место'])
            
            can.setFont("DejaVuSans", 16)
            can.drawString(280, 225, data['Весовая_категория'])
            can.drawString(530, 225, data['Возрастная_категория'])
            
            # Завершаем текущую страницу и начинаем новую (если это не последний элемент)
            if data != list_for_pdf[-1]:
                can.showPage()

        # Завершаем рисование
        can.save()

        # Перемещаем указатель на начало буфера
        packet.seek(0)

        # Сохраняем маску отдельно
        with open(mask_output_path, "wb") as output_stream:
            output_stream.write(packet.getvalue())

        # Теперь создаем версию с наложением на шаблон
        # Проверяем, существует ли файл шаблона
        if not os.path.exists(template_path):
            print(f"Файл шаблона не найден: {template_path}")
        else:
            # Читаем созданную маску
            new_pdf = PdfReader(packet)
            
            # Читаем исходный шаблон
            with open(template_path, "rb") as f:
                existing_pdf = PdfReader(f)
                output = PdfWriter()

                # Для каждой страницы маски создаем отдельную страницу с наложением
                for i in range(len(new_pdf.pages)):
                    # Берем страницу шаблона (если страниц меньше, чем в маске, используем первую)
                    if i < len(existing_pdf.pages):
                        # Создаем глубокую копию страницы шаблона
                        template_page = existing_pdf.pages[i]
                    else:
                        template_page = existing_pdf.pages[0]
                    
                    # Создаем временный PDF для отдельной страницы
                    single_page_packet = io.BytesIO()
                    single_page_writer = PdfWriter()
                    single_page_writer.add_page(template_page)
                    single_page_writer.write(single_page_packet)
                    single_page_packet.seek(0)
                    
                    # Читаем отдельную страницу
                    single_page_reader = PdfReader(single_page_packet)
                    single_page = single_page_reader.pages[0]
                    
                    # Накладываем маску на отдельную страницу шаблона
                    single_page.merge_page(new_pdf.pages[i])
                    output.add_page(single_page)

                # Сохраняем объединенный документ
                with open(merged_output_path, "wb") as output_stream:
                    output.write(output_stream)

        print(f"Маска успешно сохранена как {mask_output_path}")
        print(f"Файл с наложением на шаблон сохранен как {merged_output_path}")
        print(f"Файл для проверки был сохранен тут: {merged_output_path}")

        return True


    def draw_centered_text(self, canvas, text, y, font_name, font_size, custom_size):
        """
        Рисует текст по центру страницы по горизонтали.
        Вычисляет ширину текста и корректирует координату X.
        """
        canvas.setFont(font_name, font_size)
        text_width = canvas.stringWidth(text, font_name, font_size)
        x = (custom_size[0] - text_width) / 2  # Используем кастомную ширину
        canvas.drawString(x, y, text)


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
                    'Возрастная категория': row[5], 
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

