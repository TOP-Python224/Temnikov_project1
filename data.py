"""Дополнительный модуль: глобальные переменные и константы."""
# импорт из стандартной библиотеки
from numbers import Real
from typing import Sequence


# глобальные переменные данных
STATS = {}
SAVES = {}
DIM = 3
CELLS = DIM**2
RANGE = range(DIM)
RANGE_FLAT = range(CELLS)
PLAYERS = []
TOKENS = ('X', 'O')
WEIGHT_OWN = 1.5
WEIGHT_FOE = 1
BOT_DIFFICULTY = 0
TURNS = []
BOARD = ['']*CELLS
TRAINING = False

# глобальные константы
APP_TITLE = "КРЕСТИКИ-НОЛИКИ"
PROMPT = ' > '
PLAYERS_FILE = 'players.ini'
SAVES_FILE = 'saves.ini'

# глобальные переменные типов для аннотаций
Series = Sequence[Real | str]
Matrix = Sequence[Series]
SCORE = tuple[dict, dict]
COMMANDS = {
    'новый игрок': ('player', 'игрок', 'p', 'н'),
    'начать новую партию': ('new', 'игра', 'n', 'и'),
    'включить обучение': ('tutorial', 'обучение', 'о'),
    'восстановить игру': ('load', 'загрузка', 'l', 'з'),
    'результаты': ('table', 'таблица', 't', 'т'),
    'выйти из игры': ('quit', 'выход', 'q', 'в')
}