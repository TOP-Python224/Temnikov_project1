"""Дополнительный модуль: вспомогательные функции."""

# ИСПОЛЬЗОВАТЬ: из стандартной библиотеки лучше импортировать только необходимые объекты, чем модули целиком — последни могут быть весьма объёмными
from configparser import ConfigParser
from pprint import pprint

from data import STATS, players_file


def read_ini(file: str, statistics: dict) -> None:
    """Считывает статистику об игроках из ini-файла и записывает данные в глобальную переменную STATS."""
    config = ConfigParser()
    config.read(file)
    for section in config.sections():
        statistics[section] = {key: int(value) for key, value in config[section].items()}


# ДОБАВИТЬ: функцию write_ini()


# ИСПОЛЬЗОВАТЬ: не надо лишних сущностей — убираете тесты под проверку импорта и выполняете текущий модуль, этого достаточно
if __name__ == '__main__':
    read_ini(players_file, STATS)
    pprint(STATS)


# std_out:
# {'Player1': {'loses': 3, 'ties': 1, 'wins': 2},
#  'Player2': {'lose': 0, 'tie': 0, 'wins': 0}}