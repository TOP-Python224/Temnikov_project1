"""Дополнительный модуль: вспомогательные функции."""

from configparser import ConfigParser

from data import RANGE, BOARD, DIM, PLAYERS


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


# ИСПРАВИТЬ: аннотация возвращаемого значения не соответствует действительности
def get_nickname() -> list:
    # ДОБАВИТЬ: строку документации
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
              BOARD[0 + i*DIM],
              '|',
              BOARD[1 + i*DIM],
              '|',
              BOARD[2 + i*DIM],
              '|')
    print(cross_line.rjust(pos_index))
    # ИСПРАВИТЬ: заявлено возвращаемое значение str, как и должно быть, в то же время функция возвращает None


if __name__ == '__main__':
    draw_board(0, 0)


# stdout:
# -------------
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |
# -------------

