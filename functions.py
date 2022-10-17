"""Дополнительный модуль: вспомогательные функции."""

from configparser import ConfigParser
from pprint import pprint

from data import STATS, players_file


def read_ini(file: str, statistics: dict) -> None:
    """Считывает статистику об игроках из ini-файла и записывает данные в глобальную переменную STATS."""
    config = ConfigParser()
    # ДОБАВИТЬ: кодировку ещё укажите явно
    config.read(file)
    for section in config.sections():
        statistics[section] = {key: int(value) for key, value in config[section].items()}


def write_ini(file: str, statistics: dict) -> None:
    """Записывает данные из глобальной переменной STATS в ini - файл."""
    config = ConfigParser()
    config.read_dict(statistics)
    # ДОБАВИТЬ: кодировку ещё укажите явно
    with open(file, 'w') as fileout:
        config.write(fileout)


if __name__ == '__main__':
    read_ini(players_file, STATS)
    pprint(STATS)
    STATS['Arisber'] = {'wins': 5, 'losses': 4, 'ties': 3}
    write_ini(players_file, STATS)
    read_ini(players_file, STATS)
    pprint(STATS)


# std_out:
# {'Player1': {'losses': 3, 'ties': 1, 'wins': 2},
#  'Player2': {'losses': 0, 'ties': 0, 'wins': 0}}
# {'Arisber': {'losses': 4, 'ties': 3, 'wins': 5},
#  'Player1': {'losses': 3, 'ties': 1, 'wins': 2},
#  'Player2': {'losses': 0, 'ties': 0, 'wins': 0}}
