"""Дополнительный модуль: обработка игрового процесса."""

from data import BOARD, WINS_COORDS, TOKENS, TURNS, PLAYERS
from functions import draw_board


def take_input(player: str, player_token: str) -> str:
    """Запрашивает позицию в которую игрок хочет поставить 'X' или '0."""
    while True:
        value = input(player + ' Куда поставить: ' + player_token + '? ')
        if not (value in ('1', '2', '3', '4', '5', '6', '7', '8', '9')):
            print('Ошибка')
            continue
        value = int(value)
        TURNS.append(value)
        if str(BOARD[value - 1]) in 'X0':
            print('Занято')
            continue
        BOARD[value - 1] = player_token
        break

def check_win() -> bool:
    """Проверяет наличие выиграшной комбинации для каждого из игроков."""
    for each in WINS_COORDS:
        if (BOARD[each[0]-1]) == (BOARD[each[1]-1]) == (BOARD[each[2]-1]):
            return BOARD[each[1]-1]
    else:
        return False

if __name__ == '__main__':
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            take_input(PLAYERS[0], TOKENS[0])
        else:
            take_input(PLAYERS[1], TOKENS[1])
        if counter > 3:
            winner = check_win()
            if winner:
                if winner == 'X':
                    draw_board()
                    print(PLAYERS[0], 'выиграл')
                    break
                else:
                    draw_board()
                    print(PLAYERS[1], 'выиграл')
                    break
        counter += 1
        if counter > 8:
            draw_board()
            print('Ничья')
            break
    print(BOARD)
    print(TURNS)




# stdout:
# -------------
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |
# -------------
# Player1 Куда поставить: X? 5
# -------------
# | 1 | 2 | 3 |
# | 4 | X | 6 |
# | 7 | 8 | 9 |
# -------------
# Player2 Куда поставить: 0? 1
# -------------
# | 0 | 2 | 3 |
# | 4 | X | 6 |
# | 7 | 8 | 9 |
# -------------
# Player1 Куда поставить: X? 2
# -------------
# | 0 | X | 3 |
# | 4 | X | 6 |
# | 7 | 8 | 9 |
# -------------
# Player2 Куда поставить: 0? 4
# -------------
# | 0 | X | 3 |
# | 0 | X | 6 |
# | 7 | 8 | 9 |
# -------------
# Player1 Куда поставить: X? 8
# -------------
# | 0 | X | 3 |
# | 0 | X | 6 |
# | 7 | X | 9 |
# -------------
# Player1 выиграл
# ['0', 'X', 3, '0', 'X', 6, 7, 'X', 9]
# [5, 1, 2, 4, 8]


