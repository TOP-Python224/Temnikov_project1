"""Дополнительный модуль: настройка партии."""
import data
import functions

def game_mode() -> None:
    """Запрашивает режим игры: 2 игрока либо против компьютера."""
    print("Выберите режим игры: 1 - против Бота, 2 - против другого игрока:")
    inp = input(data.PROMPT)
    if int(inp) == 1:
        pass
    else:
        functions.get_second_player_nickname()

def choose_bot_difficulty_level() -> None:
    """Запрашивает уровень сложности бота."""
    pass
def choose_token() -> None:
    """Запрашивает токен, которым игрок будет играть партию."""
    pass

