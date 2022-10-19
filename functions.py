"""Дополнительный модуль: вспомогательные функции."""

from configparser import ConfigParser
from pprint import pprint

from data import STATS, SAVES, PLAYERS_FILE, SAVES_FILE, RANGE, BOARD, DIM, PLAYERS, TURNS

def get_nickname() -> list:
    """Запрашивает никнеймы игроков и записывает данные в глобальную переменную PLAYERS."""
    player_1 = input('Игрок_1 - введите свой никнейм: ')
    player_2 = input('Игрок_2 - введите свой никнейм: ')
    PLAYERS.clear()
    PLAYERS.insert(0, player_1)
    PLAYERS.insert(1, player_2)

def read_ini() -> None:
    """Считывает статистику об игроках из ini-файла и записывает данные в глобальную переменную STATS."""
    players = ConfigParser()
    players.read(PLAYERS_FILE, encoding='utf-8')
    for section in players.sections():
        STATS[section] = {key: int(value) for key, value in players[section].items()}
    saves = ConfigParser()
    saves.read(SAVES_FILE, encoding='utf-8')
    for section in saves.sections():
        players = section.split(';')
        players_key = (players[0], players[1])
        turns = [int(i) for i in saves[section]['turns'].split(',')]
        SAVES[players_key] = {players[0]: [], players[1]: [], 'turns': turns}
        for i, turn in enumerate(turns):
            SAVES[players_key][players[i % 2]].append(turn)


def write_ini() -> None:
    """Записывает данные из глобальной переменной STATS в ini - файл."""
    players = ConfigParser()
    players.read_dict(STATS)
    with open(PLAYERS_FILE, 'w', encoding='utf-8') as fileout:
        players.write(fileout)
    saves = ConfigParser()
    saves.read_dict(SAVES)
    for elem in PLAYERS:
        section = f"{PLAYERS[0]};{PLAYERS[1]}"
        saves[section] = {}
        saves[section]['turns'] = ','.join([str(i) for i in TURNS])
    with open(SAVES_FILE, 'a', encoding='utf-8') as fileout:
        saves.write(fileout)


def draw_board(pos_index: int, pos_arg: int) -> str:
    cross_line = '-------------'
    print(cross_line.rjust(pos_index))
    for i in RANGE:
        print('|'.rjust(pos_index - pos_arg), BOARD[0 + i * DIM], '|', BOARD[1 + i * DIM], '|', BOARD[2 + i * DIM], '|')
    print(cross_line.rjust(pos_index))

if __name__ == '__main__':
#     draw_board(0, 0)
    write_ini()
    pprint(SAVES)



# stdout:
# -------------
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |
# -------------

