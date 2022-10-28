"""Дополнительный модуль: вспомогательные функции."""

# импорт из стандартной библиотеки
from configparser import ConfigParser
from typing import Literal
from shutil import get_terminal_size
from pprint import pprint

# импорт дополнительных модулей проекта
import data


def read_ini() -> None:
    """Считывает статистику об игроках и сохраненные игры из ini-файлов и записывает данные в глобальную переменную STATS и SAVES."""
    players = ConfigParser()
    players.read(data.PLAYERS_FILE, encoding='utf-8')
    for section in players.sections():
        data.STATS[section] = {
            key: int(value) if value.isdecimal() else value
            for key, value in players[section].items()
        }
    saves = ConfigParser()
    saves.read(data.SAVES_FILE, encoding='utf-8')
    for section in saves.sections():
        players = tuple(section.split(';'))
        turns = [int(i) for i in saves[section]['turns'].split(',')]
        data.SAVES[players] = turns


def write_ini_stats() -> None:
    """Записывает данные из глобальной переменной STATS в ini-файл."""
    players = ConfigParser()
    players.read_dict(data.STATS)
    with open(data.PLAYERS_FILE, 'w', encoding='utf-8') as fileout:
        players.write(fileout)


def write_ini_saves() -> None:
    """Записывает данные из глобальной переменной SAVES в ini-файл."""
    saves = ConfigParser()
    for elem in data.SAVES:
        player1, player2 = list(elem)
        section = f"{player1};{player2}"
        saves[section] = {}
        saves[section]['turns'] = ','.join([str(i) for i in data.SAVES[elem]])
    with open(data.SAVES_FILE, 'w', encoding='utf-8') as fileout:
        saves.write(fileout)


def get_main_player_nickname() -> None:
    """Запрашивает никнейм главного пользователя, проверяет наличие пользователя в базе игроков, в случае отсутствия добавляет игрока в базу и записывает данные в глобальную переменную STATS и PLAYERS."""
    player_1 = input('Игрок_1 - введите свой никнейм: ')
    if player_1 not in data.STATS.keys():
        data.STATS[player_1] = {'wins': 0, 'losses': 0, 'ties': 0, 'training': False}
    data.PLAYERS.append(player_1)


def get_second_player_nickname() -> None:
    """Запрашивает никнейм второго пользователя, проверяет наличие пользователя в базе игроков, в случае отсутствия добавляет игрока в базу и записывает данные в глобальную переменную STATS и PLAYERS."""
    player_2 = input('Игрок_2 - введите свой никнейм: ')
    if player_2 not in data.STATS.keys():
        data.STATS[player_2] = {'wins': 0, 'losses': 0, 'ties': 0, 'training': False}
    data.PLAYERS.append(player_2)


def draw_board(align: Literal['left', 'right', 'center'] = 'left') -> None:
    cross_line = '-'*(data.DIM**2 + data.DIM + 1)
    # ИСПРАВИТЬ: лучше вычислить величину отступа в зависимости от выравнивания и сохранить в отдельную переменную, которую потом умножить на ' ' и прибавлять к той же строке
    print(cross_line)
    for i in data.RANGE:
        print('|',
              data.BOARD[0+i*data.DIM],
              '|',
              data.BOARD[1+i*data.DIM],
              '|',
              data.BOARD[2+i*data.DIM],
              '|')
        print(cross_line)


if __name__ == '__main__':
    draw_board('left')


# stdout:
# -------------
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |
# -------------
