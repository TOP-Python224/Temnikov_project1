"""Дополнительный модуль: вспомогательные функции."""

from configparser import ConfigParser
from pprint import pprint

from data import BOARD, PLAYERS, SAVES_FILE, SAVES, STATS, DIM, PLAYERS_FILE, RANGE


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


# ИСПРАВИТЬ: аннотация возвращаемого значения не соответствует действительности
def get_nickname() -> list:
    """Запрашивает никнеймы игроков и записывает данные в глобальную переменную PLAYERS."""
    player_1 = input('Игрок_1 - введите свой никнейм: ')
    # ДОБАВИТЬ: проверку, существует ли имя, если нет, то добавить его в data.STATS — можно отдельной функцией, можно здесь же

    # УДАЛИТЬ: для теста хорошо, но не забывайте о режимах игры
    player_2 = input('Игрок_2 - введите свой никнейм: ')
    # УДАЛИТЬ: когда вы будете вызывать эту функцию второй раз, после выбора режима "два игрока", то в data.PLAYERS будет имя первого игрока — его нельзя вычистить
    PLAYERS.clear()
    # ИСПРАВИТЬ: лучше append(), insert() очень медленный в сравнении и применяется только от безысходности
    PLAYERS.insert(0, player_1)
    PLAYERS.insert(1, player_2)


# ИСПРАВИТЬ: используйте параметр, регулирующий выравнивание: влево, вправо, центр — например
#  def draw_board(align: Literal['left', 'right', 'center'] = 'left'):
def draw_board(pos_index: int, pos_arg: int) -> str:
    cross_line = '-------------'
    # ИСПРАВИТЬ: лучше вычислить величину отступа в зависимости от выравнивания и сохранить в отдельную переменную, которую потом умножить на ' ' и прибавлять к той же строке
    print(cross_line.rjust(pos_index))
    for i in RANGE:
        print('|'.rjust(pos_index - pos_arg),
              # ИСПРАВИТЬ: а вот здесь потенциально может потребоваться .rjust() или лучше .center() — на случай, если вы захотите выводить не только data.BOARD, но и другие матрицы
              BOARD[0 + i * DIM],
              '|',
              BOARD[1 + i * DIM],
              '|',
              BOARD[2 + i * DIM],
              '|')
    print(cross_line.rjust(pos_index))
    # ИСПРАВИТЬ: заявлено возвращаемое значение str, как и должно быть, в то же время функция возвращает None


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
