"""Дополнительный модуль: вспомогательные функции."""

from configparser import ConfigParser
from pprint import pprint

from data import STATS, SAVES, players_file, saves_file, RANGE, BOARD, DIM, PLAYERS

def get_nickname() -> list:
    player_1 = input('Игрок_1 - введите свой никнейм: ')
    player_2 = input('Игрок_2 - введите свой никнейм: ')
    PLAYERS.clear()
    PLAYERS.insert(0, player_1)
    PLAYERS.insert(1, player_2)

def read_ini(file: str, statistics: dict) -> None:
    """Считывает статистику об игроках из ini-файла и записывает данные в глобальную переменную STATS."""
    config = ConfigParser()
    config.read(file, encoding='utf-8')
    for section in config.sections():
        statistics[section] = {key: int(value) for key, value in config[section].items()}

def write_ini(file: str, statistics: dict) -> None:
    """Записывает данные из глобальной переменной STATS в ini - файл."""
    config = ConfigParser()
    config.read_dict(statistics)
    with open(file, 'w', encoding='utf-8') as fileout:
        config.write(fileout)


def draw_board(pos_index: int, pos_arg: int) -> str:
    cross_line = '-------------'
    print(cross_line.rjust(pos_index))
    for i in RANGE:
        print('|'.rjust(pos_index - pos_arg), BOARD[0 + i * DIM], '|', BOARD[1 + i * DIM], '|', BOARD[2 + i * DIM], '|')
    print(cross_line.rjust(pos_index))

if __name__ == '__main__':
    draw_board(0, 0)

# stdout:
# -------------
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |
# -------------

