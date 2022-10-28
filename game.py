"""Дополнительный модуль: обработка игрового процесса."""

# импорт дополнительных модулей проекта
import data
import functions


def take_input(player: str, player_token: str) -> None:
    """Запрашивает позицию в которую игрок хочет поставить токен 'X' или '0', проверяет возможность проставить токен в указанную клетку, отрисовывает доску с проставленным токеном и записывает ход в глобальную переменную TURNS."""
    while True:
        inp = input(player + f' Куда поставить: {player_token}? ')
        if not (inp in '123456789'):
            print('Ошибка')
            continue
        inp = int(inp)
        if str(data.BOARD[inp-1]) in data.TOKENS:
            print('Занято')
            continue
        data.BOARD[inp-1] = player_token
        data.TURNS.append(inp)
        break


def check_win() -> bool:
    """Проверяет наличие выигрышной комбинации."""
    for each in data.WINS_COORDS:
        if data.BOARD[each[0]-1] == data.BOARD[each[1]-1] == data.BOARD[each[2]-1]:
            return bool(data.BOARD[each[0]-1])
    else:
        return False


def game() -> None:
    """Обрабатывает игровую партию."""
    counter = 0
    while True:
        functions.draw_board('left')
        if counter % 2 == 0:
            take_input(data.PLAYERS[0], data.TOKENS[0])
        else:
            take_input(data.PLAYERS[1], data.TOKENS[1])
        if counter > 3:
            winner = check_win()
            if winner:
                if winner == data.TOKENS[0]:
                    functions.draw_board('center')
                    print(data.PLAYERS[0], 'выиграл')
                    break
                else:
                    functions.draw_board('center')
                    print(data.PLAYERS[1], 'выиграл')
                    break
        counter += 1
        if counter > 8:
            functions.draw_board('center')
            print('Ничья')
            break


if __name__ == '__main__':
    functions.get_main_player_nickname()
    functions.get_second_player_nickname()
    game()

    functions.read_ini()
    print(data.PLAYERS)
    print(data.BOARD)
    print(data.TURNS)
    print(data.STATS)
