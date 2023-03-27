"""Модуль верхнего уровня: для учебного проекта Крестики-Нолики."""
from importlib import reload
from shutil import get_terminal_size
# импорт дополнительных модулей проекта
import data
import functions
import help
import gameset
import game


print(''.center(get_terminal_size()[0] - 1, '*'))
print(data.APP_TITLE.center(get_terminal_size()[0] - 1, '*'))
print(''.center(get_terminal_size()[0] - 1, '*'), end='\n\n')

if functions.read_ini():
    help.game_tutorial()
functions.get_player_nickname()


while True:
    gameset.check_training()
    print(['', f"\nДоступны следующие команды:\n{help.commands()}"][data.TRAINING])
    command = input(f"Введите команду{data.PROMPT}")

    if command in data.COMMANDS['начать новую партию']:
        FIRST_PLAYER = data.PLAYERS[0]
        gameset.game_mode()
        gameset.check_training()
        res = game.game()
        functions.update_score(res)
        reload(data)
        functions.read_ini()
        data.PLAYERS = [FIRST_PLAYER]

    if command in data.COMMANDS['новый игрок']:
        functions.read_ini()
        functions.get_player_nickname()

    if command in data.COMMANDS['восстановить игру']:
        FIRST_PLAYER = data.PLAYERS[0]
        functions.load()
        res = game.game(load_game=True)
        functions.update_score(res)
        data.PLAYERS = [FIRST_PLAYER]

    if command in data.COMMANDS['включить обучение']:
        data.TRAINING = True
        help.game_tutorial()

    if command in data.COMMANDS['результаты']:
        functions.show_stats()

    if command in data.COMMANDS['выйти из игры']:
        break


print(f"Ждем вас в игре {data.APP_TITLE}!")