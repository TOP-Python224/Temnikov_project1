"""Дополнительный модуль: настройка партии."""

# импорт дополнительных модулей проекта
import data
import functions

def game_mode() -> None:
    """Запрашивает режим игры: 2 игрока либо против компьютера."""
    while True:
        print("Выберите режим игры: 1 - против Бота, 2 - против другого игрока:")
        inp = input(data.PROMPT)
        if inp not in ['1', '2']:
            continue
        else:
            if int(inp) == 1:
                choose_bot_difficulty_level()
            else:
                functions.get_player_nickname()
        choose_token()
        break


def choose_bot_difficulty_level() -> None:
    """Запрашивает уровень сложности бота."""
    while True:
        print("Выберите уровень сложности бота: 1 - легкий, 2 - сложный:")
        inp = input(data.PROMPT)
        if inp not in ['1', '2']:
            continue
        else:
            data.BOT_DIFFICULTY = int(inp)
            bot_name = '#' + str(data.BOT_DIFFICULTY)
            data.PLAYERS.append(bot_name)
            if bot_name not in data.STATS:
                data.STATS[bot_name] = {'wins': 0, 'losses': 0, 'ties': 0, 'training': False}
            functions.write_ini_stats()
            break


def choose_token() -> None:
    """Запрашивает токен, которым игрок будет играть партию."""
    while True:
        print("Выберите знак которым вы будете играть: X или O?")
        inp = input(data.PROMPT)
        if inp.upper() not in data.TOKENS:
            continue
        else:
            if inp.upper() == 'O':
                data.PLAYERS.reverse()
        print()
        break


def check_training():
    """Проверяет, является ли данная партия первой для любого из игроков и устанавливает глобальную переменную. """
    for player in data.PLAYERS:
        if data.STATS[player]['training'] == 'True':
            data.TRAINING = True
