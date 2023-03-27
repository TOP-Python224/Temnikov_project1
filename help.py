"""Дополнительный модуль: справка и обучение"""

# импорт дополнительных модулей проекта
import data
import functions


def game_tutorial() -> None:
    """Выводит раздел помощи."""
    result = ''
    print(f"\n{data.APP_TITLE}\n")
    with open('./help.txt', encoding='utf-8') as info:
        for line in info:
            result += line
    result = result.replace('###', commands())
    print(f"{result}")
    print(f"{functions.draw_board([str(i) for i in range(1, data.CELLS + 1)])}\n")
    print(f"Удачи в игре {data.APP_TITLE}!")


def commands() -> str:
    """Выдает список команд."""
    result = ''
    for k, v in data.COMMANDS.items():
        result += f"{list(v)} - {k},\n"
    result = result.rstrip(',\n')
    result += '.'
    return result
