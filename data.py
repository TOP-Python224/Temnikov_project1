"""Дополнительный модуль: глобальные переменные и константы."""


# глобальные константы
APP_TITLE = "КРЕСТИКИ-НОЛИКИ"
PROMPT = ' > '

players_file = 'players.ini'


# глобальные переменные данных
STATS = {}
SAVES = {}

DIM = 3
RANGE = range(DIM)
RANGE_FLAT = range(DIM**2)

PLAYERS = []
TOKENS = ('X', 'O')
WINS_COORDS = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

TURNS = []
BOARD = list(range(1, 10))