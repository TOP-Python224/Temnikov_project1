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
            # ИСПРАВИТЬ: у нас появился ключ с логическим значением — в нужный момент используйте метод getboolean() из модуля configparser
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
        # ИСПРАВИТЬ: два действия ниже можно заменить одним join()
        player1, player2 = list(elem)
        section = f"{player1};{player2}"
        # ИСПОЛЬЗОВАТЬ: словарь содержит только один элемент, так что можно сразу записывать
        saves[section] = {'turns': ','.join([str(i) for i in data.SAVES[elem]])}
    with open(data.SAVES_FILE, 'w', encoding='utf-8') as fileout:
        saves.write(fileout)


def get_main_player_nickname() -> None:
    """Запрашивает никнейм игрока, в случае отсутствия игрока в data.STATS добавляет запись о новом игроке, и добавляет имя игрока в data.PLAYERS."""
    # КОММЕНТАРИЙ: является ли указание здесь номера игрока обязательным?
    player_1 = input('Игрок_1 - введите свой никнейм: ')
    # ДОБАВИТЬ: у нас есть условие для имён игроков, они не должны начинаться с символа '#' — он зарезервирован для ботов

    if player_1 not in data.STATS:
        data.STATS[player_1] = {'wins': 0, 'losses': 0, 'ties': 0, 'training': False}
    data.PLAYERS.append(player_1)


# УДАЛИТЬ: данная функция ничем кроме имён и текста не отличается от предыдущей — это дублирование кода, которого следует избегать — подумайте, как при необходимости реорганизовать предыдущую функцию, чтобы она могла быть более универсальной
def get_second_player_nickname() -> None:
    """Запрашивает никнейм второго пользователя, проверяет наличие пользователя в базе игроков, в случае отсутствия добавляет игрока в базу и записывает данные в глобальную переменную STATS и PLAYERS."""
    player_2 = input('Игрок_2 - введите свой никнейм: ')
    if player_2 not in data.STATS.keys():
        data.STATS[player_2] = {'wins': 0, 'losses': 0, 'ties': 0, 'training': False}
    data.PLAYERS.append(player_2)


# ДОБАВИТЬ: строку документации
def draw_board(align: Literal['left', 'right', 'center'] = 'left') -> None:
    # СДЕЛАТЬ: лучше вычислить величину отступа в зависимости от выравнивания и сохранить в отдельную переменную, которую потом умножить на ' ' и прибавлять к той же строке
    cross_line = '-'*(data.DIM**2 + data.DIM + 1)
    # ИСПРАВИТЬ: согласно условию, функция должна возвращать строку, а не выводить её в stdout
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


def change_dimension(new_dimension: int) -> None:
    """Пересчитывает значения глобальных переменных при изменении размерности игрового поля."""
    data.DIM = new_dimension
    data.CELLS = new_dimension**2
    data.RANGE = range(new_dimension)
    data.RANGE_FLAT = range(data.CELLS)


if __name__ == '__main__':
    change_dimension(5)
    data.BOARD = list(map(str, data.RANGE_FLAT))
    draw_board()


# stdout:
# -------------
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |
# -------------

# КОММЕНТАРИЙ: с универсальностью у draw_board() пока так себе
# -------------------------------
# | 0 | 1 | 2 |
# -------------------------------
# | 5 | 6 | 7 |
# -------------------------------
# | 10 | 11 | 12 |
# -------------------------------
# | 15 | 16 | 17 |
# -------------------------------
# | 20 | 21 | 22 |
# -------------------------------
