from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from visit_window import Ui_VisitWindow


from config import *
from db import Database



class App:
    def __init__(self):
        
        # ⁡⁢⁣⁣​‌‌‍‍initial windows​⁡
        self.VisitWindow = QtWidgets.QMainWindow()
        self.Ui_VisitWindow = Ui_VisitWindow()
        self.Ui_VisitWindow.setupUi(self.VisitWindow)


    def open_visit_window(self):
        self.VisitWindow.show()

        # push buttons
        self.Ui_VisitWindow.pushButton_close_app.clicked.connect(lambda: sys.exit())
        self.Ui_VisitWindow.pushButton_new_scoreboard.clicked.connect(self.open_scoreboard)
        self.Ui_VisitWindow.pushButton_close_all_scoreboards.clicked.connect(self.close_all_scoreboards)
        self.Ui_VisitWindow.pushButton_members_list.clicked.connect(self.open_members_list)
        self.Ui_VisitWindow.pushButton_load_data.clicked.connect(self.load_data)
        self.Ui_VisitWindow.pushButton_export_table.clicked.connect(self.export_data)


    def export_data(self):
        """Экспорт данных в Excel"""
        db = Database()
        success = db.export_to_excel()
        if success:
            print("Экспорт данных выполнен успешно")
        else:
            print("Экспорт данных отменен или завершился с ошибкой")


    def load_data(self):
        db = Database()
        db.upload_from_xl()


    def close_all_scoreboards(self):
        # Останавливаем все таймеры перед закрытием окон
        for key in list(SCOREBOARDS_LINKS.keys()):
            try:
                # Получаем UI менеджера для остановки таймеров
                maneger_ui = SCOREBOARDS_LINKS[key]['maneger']['ui']
                
                # Останавливаем таймеры через существующие методы
                # TotalTime таймер останавливается автоматически при проверке window_id
                # HoldTime нужно остановить явно
                hold_time = maneger_ui.hold_time  # Предполагая, что hold_time доступен
                if hasattr(hold_time, 'stop_hold_time'):
                    hold_time.stop_hold_time()
                    
            except (KeyError, AttributeError) as e:
                print(f"Ошибка при остановке таймеров: {e}")
            
            # Закрываем окна
            SCOREBOARDS_LINKS[key]['scoreboard']['window'].close()
            SCOREBOARDS_LINKS[key]['maneger']['window'].close()
            
        clean_links()

    def open_scoreboard(self):
        """
        Open new or exist scoreboard
        Save links to scoreboard in dictionary
        """
        from scoreboard import Ui_Scoreboard
        from manege_panel import Ui_ManegePanel

        new_index = SCOREBOARDS_NUMBERS[-1] + 1
        SCOREBOARDS_NUMBERS.append(new_index)

        Scoreboard = QtWidgets.QMainWindow()
        Ui_Scoreboard = Ui_Scoreboard()
        Ui_Scoreboard.setupUi(Scoreboard)

        ManegePanel = QtWidgets.QMainWindow()
        Ui_ManegePanel = Ui_ManegePanel()
        Ui_ManegePanel.setupUi(ManegePanel)

        SCOREBOARDS_LINKS[new_index] = {
            'scoreboard': {'window': Scoreboard, 'ui': Ui_Scoreboard, 'id': id(Ui_Scoreboard)},
            'maneger': {'window': ManegePanel, 'ui': Ui_ManegePanel, 'id': id(Ui_ManegePanel)}
        }

        SCOREBOARDS_LINKS[new_index]['scoreboard']['window'].show()
        SCOREBOARDS_LINKS[new_index]['maneger']['window'].show()


    def open_members_list(self):
        from members_list import Ui_MembersList

        self.MembersList = QtWidgets.QMainWindow()
        self.Ui_MembersList = Ui_MembersList()
        self.Ui_MembersList.setupUi(self.MembersList)
        
        self.MembersList.show()
    

    def run_app(self):
        self.open_visit_window()


if __name__ == '__main__':
    window = QtWidgets.QApplication(sys.argv)

    app = App()
    app.run_app()

    sys.exit(window.exec_())