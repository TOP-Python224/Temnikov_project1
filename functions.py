"""Дополнительный модуль: вспомогательные функции."""

from configparser import ConfigParser
from pprint import pprint

from data import STATS, players_file, RANGE, BOARD, DIM


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


def draw_board() -> str:
    cross_line = '-------------'
    print(cross_line)
    for i in RANGE:
        print('|', BOARD[0 + i * DIM], '|', BOARD[1 + i * DIM], '|', BOARD[2 + i * DIM], '|')
    print(cross_line)

if __name__ == '__main__':
    draw_board()

# stdout:
# -------------
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |
# -------------

