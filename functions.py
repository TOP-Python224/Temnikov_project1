"""Дополнительный модуль: вспомогательные функции."""
import configparser
from pprint import pprint
from data import STATS, players_file

def read_ini(file: str, statistics: dict) -> dict:
    # """Считывает статистику об игроках из ini-файла и записывает данные в глобальную переменную STATS."""
    config = configparser.ConfigParser()
    config.read(file)
    for section in config.sections():
        statistics[section] = {key: int(value) for key, value in config[section].items()}


def main():
    if __name__ == '__main__':
        read_ini(players_file, STATS)
        pprint(STATS)
main()


# std_out:
# {'Player1': {'loses': 3, 'ties': 1, 'wins': 2},
#  'Player2': {'lose': 0, 'tie': 0, 'wins': 0}}