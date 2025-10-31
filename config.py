"""
​‌‍‌Файл конфигруации и глобальных переменных​
в дальнейшем здесь будет обработка всей информации в том числе и БД


⁡⁢⁢⁢​‌‍‌‍links dict structure:​⁡
SCOREBOARDS_LINKS = {
                    1: {'scoreboard': {'window': Scoreboard, 'ui': Ui_Scoreboard, 'id': id(Ui_Scoreboard)},
                        'maneger': {'window': ManegePanel, 'ui': Ui_ManegePanel, 'id': id(Ui_ManegePanel)}}            
        }

        
⁡⁢⁣⁢​‌‌‌Подсказака​⁡

self.label_yellow_card_2_1.setStyleSheet("background-color: rgb(255, 255, 0);")

"""

# ⁡⁢⁣⁣​‌‍‌global variables for save state and links​⁡

SCOREBOARDS_LINKS = {}
SCOREBOARDS_NUMBERS = [0]


def update_state(index: int) -> None:
    if index == 0:
        print("Window not found")

    if index in SCOREBOARDS_LINKS:
        
        scoreboard = SCOREBOARDS_LINKS[index]['scoreboard']['ui']
        maneger = SCOREBOARDS_LINKS[index]['maneger']['ui']

        # total score
        scoreboard.label_score_1.setText(maneger.label_total_score_1.text())
        scoreboard.label_score_2.setText(maneger.label_total_score_2.text())

        # members
        # scoreboard.label_member_1.setText(maneger.comboBox_member_1.currentText())
        # scoreboard.label_member_2.setText(maneger.comboBox_member_2.currentText())

    else:
        print("Error: index not found in SCOREBOARDS_STATE")
        chekout_links()
        print(SCOREBOARDS_NUMBERS)



# ⁡⁢⁢⁢​‌‌‍chekout functions​⁡

def chekout_links():
    if SCOREBOARDS_LINKS:
        print("Links:")
        for key, value in SCOREBOARDS_LINKS.items():
            print(f"{key}: {value}")
            print("___________________________________________\n")
    else:
        print("No links found.")


def clean_links():
    """
    clean links dict and numbers list
    """
    SCOREBOARDS_LINKS.clear()
    SCOREBOARDS_NUMBERS.clear()

    SCOREBOARDS_NUMBERS = [0]