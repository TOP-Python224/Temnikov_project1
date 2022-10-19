"""Дополнительный модуль: глобальные переменные и константы."""


# глобальные константы
APP_TITLE = "КРЕСТИКИ-НОЛИКИ"
PROMPT = ' > '

PLAYERS_FILE = 'players.ini'
SAVES_FILE = 'saves.ini'


# глобальные переменные данных
STATS = {}
SAVES = {}

DIM = 3
RANGE = range(DIM)

PLAYERS =['Player1', 'Player2']
TOKENS = ['X', '0']
WINS_COORDS = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

TURNS = []
BOARD = list(range(1, 10))