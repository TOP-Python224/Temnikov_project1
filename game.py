"""Дополнительный модуль: обработка игрового процесса."""
from shutil import get_terminal_size
# импорт дополнительных модулей проекта
import bot
import data
import functions

def human_turn() -> int:
    """Запрашивает позицию в которую игрок хочет поставить токен, проверяет возможность проставить токен в указанную клетку, отрисовывает доску с проставленным токеном и записывает ход в глобальную переменную TURNS."""
    while True:
        turn = input(f"Введите номер ячейки для Вашего хода\n{data.PROMPT}")
        if turn == '':
            if len(data.PLAYERS) == 2 and len(data.TURNS) > 0:
                data.SAVES[tuple(data.PLAYERS)] = data.TURNS
                functions.write_ini_saves()
            continue
        if turn.isdecimal():
            turn = int(turn)
        else:
            print(f"Введите значение от 1 до {data.CELLS}!")
            continue
        if turn < 1 or turn > data.CELLS:
            print(f"Введите значение от 1 до {data.CELLS}!")
            continue
        if data.BOARD[turn - 1] != '':
            print(f"Ячейка занята, выберите другую!")
            continue
        else:
            return turn - 1


def bot_turn() -> int:
    """Вычисляет и возвращает координату ячейки для текущего хода выбранного бота."""
    return [bot.easy_bot, bot.hard_bot][data.BOT_DIFFICULTY - 1]()


def check_win() -> bool:
    """Проверяет наличие выигрышной комбинации."""
    series = []
    main_diag, anit_diag = [], []
    for i in data.RANGE:
        series += [data.BOARD[i * data.DIM:(i + 1) * data.DIM]]
        series += [data.BOARD[i::data.DIM]]
        main_diag += [data.BOARD[i + i * data.DIM]]
        anit_diag += [data.BOARD[(i + 1) * data.DIM - i - 1]]
    series += [main_diag, anit_diag]

    for seq in series:
        if len(set(seq)) == 1:
            if all(seq):
                return True
    return False


def game(load_game: bool = False) -> data.SCORE | None:
    """Обрабатывает игровую партию."""
    remove_reverse = tuple(list(reversed(data.PLAYERS)))
    if load_game:
        turns_cnt = len(data.TURNS)
        token_index = turns_cnt % 2
    else:
        turns_cnt = 1
        token_index = 0
    turns = [human_turn, human_turn]
    for player in data.PLAYERS:
        if player.startswith('#'):
            turns[data.PLAYERS.index(player)] = bot_turn
    while True:
        print(['', f"Ход игрока '{data.PLAYERS[token_index]}'".center(get_terminal_size()[0] - 1)][data.TRAINING])
        turn = turns[token_index]()
        data.BOARD[turn] = data.TOKENS[token_index]
        data.TURNS.append(turn + 1)
        data.SAVES[tuple(data.PLAYERS)] = data.TURNS
        if len(data.TURNS) == 1 and remove_reverse in data.SAVES:
            data.SAVES.pop(remove_reverse)
        functions.write_ini_saves()
        print(f"\n{functions.draw_board(data.BOARD, token_index)}\n")
        print(f"{['', functions.tutorial(turn, token_index, token_index)][data.TRAINING]}")
        if check_win():
            print(f"Игрок '{data.PLAYERS[token_index]}' победил!\n")
            return {data.PLAYERS[token_index]: {'wins': 1, 'training': False}}, \
                   {data.PLAYERS[abs(token_index - 1)]: {'losses': 1, 'training': False}}
        token_index = abs(token_index - 1)
        turns_cnt += 1
        if turns_cnt > data.CELLS and not check_win():
            print(f"Ничья!\n")
            return {data.PLAYERS[0]: {'ties': 1, 'training': False}}, \
                   {data.PLAYERS[1]: {'ties': 1, 'training': False}}
