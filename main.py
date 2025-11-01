from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from visit_window import Ui_VisitWindow

from config import *



class App:
    def __init__(self):
        
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
        for key in list(SCOREBOARDS_LINKS.keys()): 
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

    def run_app(self):
        self.open_visit_window()


if __name__ == '__main__':
    window = QtWidgets.QApplication(sys.argv)

    app = App()
    app.run_app()

    sys.exit(window.exec_())