from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from visit_window import Ui_VisitWindow




class App:
    def __init__(self):
        # ​‌‌‍⁡⁢⁣⁣global variables⁡​
        self.scoreboards_list = {}
        self.buttons_cofig = {}
        self.scoreboards_numbers = [0]
        
        # ⁡⁢⁣⁣​‌‌‍‍initial windows​⁡
        self.VisitWindow = QtWidgets.QMainWindow()
        self.Ui_VisitWindow = Ui_VisitWindow()
        self.Ui_VisitWindow.setupUi(self.VisitWindow)
    

    def open_visit_window(self):
        self.VisitWindow.show()

        # ⁡⁢⁣⁣​‌‌‍push buttons​⁡
        self.Ui_VisitWindow.pushButton_close_app.clicked.connect(lambda: sys.exit())
        self.Ui_VisitWindow.pushButton_new_scoreboard.clicked.connect(self.open_scoreboard)
        self.Ui_VisitWindow.pushButton_close_all_scoreboards.clicked.connect(self.close_all_scoreboards)

    def close_all_scoreboards(self):
        for key in list(self.scoreboards_list.keys()):  # Используем list() для безопасного удаления во время итерации
            self.scoreboards_list[key]['scoreboard']['window'].close()
            self.scoreboards_list[key]['maneger']['window'].close()
            del self.scoreboards_list[key]

    def open_scoreboard(self):
        """
        Open new or exist scoreboard
        Save links to scoreboard in dictionary
        """
        from scoreboard import Ui_Scoreboard
        from manege_panel import Ui_ManegePanel

        new_index = self.scoreboards_numbers[-1] + 1
        self.scoreboards_numbers.append(new_index)

        Scoreboard = QtWidgets.QMainWindow()
        Ui_Scoreboard = Ui_Scoreboard()
        Ui_Scoreboard.setupUi(Scoreboard)

        ManegePanel = QtWidgets.QMainWindow()
        Ui_ManegePanel = Ui_ManegePanel()
        Ui_ManegePanel.setupUi(ManegePanel)

        self.scoreboards_list[new_index] = {
            'scoreboard': {'window': Scoreboard, 'ui': Ui_Scoreboard},
            'maneger': {'window': ManegePanel, 'ui': Ui_ManegePanel}
        }

        self.scoreboards_list[new_index]['scoreboard']['window'].show()
        self.scoreboards_list[new_index]['maneger']['window'].show()

        print(self.scoreboards_list)


    def run_app(self):
        self.open_visit_window()
# main.py - основные изменения в методе open_scoreboard
def open_scoreboard(self):
    """
    Open new or exist scoreboard
    Save links to scoreboard in dictionary
    """
    from scoreboard import Ui_Scoreboard
    from manege_panel import Ui_ManegePanel

    new_index = self.scoreboards_numbers[-1] + 1
    self.scoreboards_numbers.append(new_index)

    # Создаем окна
    Scoreboard = QtWidgets.QMainWindow()
    Ui_Scoreboard = Ui_Scoreboard()
    Ui_Scoreboard.setupUi(Scoreboard)

    ManegePanel = QtWidgets.QMainWindow()
    Ui_ManegePanel = Ui_ManegePanel()
    Ui_ManegePanel.setupUi(ManegePanel)

    # Устанавливаем связь между панелью управления и табло
    Ui_ManegePanel.scoreboard = Ui_Scoreboard  # Добавляем ссылку на табло
    Ui_Scoreboard.manege_panel = Ui_ManegePanel  # Добавляем обратную ссылку

    # Сохраняем окна в словаре
    self.scoreboards_list[new_index] = {
        'scoreboard': {'window': Scoreboard, 'ui': Ui_Scoreboard},
        'maneger': {'window': ManegePanel, 'ui': Ui_ManegePanel}
    }

    # Показываем окна
    self.scoreboards_list[new_index]['scoreboard']['window'].show()
    self.scoreboards_list[new_index]['maneger']['window'].show()

    print(self.scoreboards_list)
# main.py - основные изменения в методе open_scoreboard
def open_scoreboard(self):
    """
    Open new or exist scoreboard
    Save links to scoreboard in dictionary
    """
    from scoreboard import Ui_Scoreboard
    from manege_panel import Ui_ManegePanel

    new_index = self.scoreboards_numbers[-1] + 1
    self.scoreboards_numbers.append(new_index)

    # Создаем окна
    Scoreboard = QtWidgets.QMainWindow()
    Ui_Scoreboard = Ui_Scoreboard()
    Ui_Scoreboard.setupUi(Scoreboard)

    ManegePanel = QtWidgets.QMainWindow()
    Ui_ManegePanel = Ui_ManegePanel()
    Ui_ManegePanel.setupUi(ManegePanel)

    # Устанавливаем связь между панелью управления и табло
    Ui_ManegePanel.scoreboard = Ui_Scoreboard  # Добавляем ссылку на табло
    Ui_Scoreboard.manege_panel = Ui_ManegePanel  # Добавляем обратную ссылку

    # Сохраняем окна в словаре
    self.scoreboards_list[new_index] = {
        'scoreboard': {'window': Scoreboard, 'ui': Ui_Scoreboard},
        'maneger': {'window': ManegePanel, 'ui': Ui_ManegePanel}
    }

    # Показываем окна
    self.scoreboards_list[new_index]['scoreboard']['window'].show()
    self.scoreboards_list[new_index]['maneger']['window'].show()

    print(self.scoreboards_list)

  
if __name__ == '__main__':
    window = QtWidgets.QApplication(sys.argv)

    app = App()
    app.run_app()

    sys.exit(window.exec_())