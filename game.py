"""Дополнительный модуль: обработка игрового процесса."""

from data import BOARD, WINS_COORDS, TOKENS, TURNS, PLAYERS
from functions import draw_board


def take_input(player: str, player_token: str) -> str:
    """Запрашивает позицию в которую игрок хочет поставить 'X' или '0."""
    while True:
        value = input(player.rjust(49 if player_token == '0' else 0) + ' Куда поставить: ' + player_token + '? ')
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
        pos_index = 70 if counter % 2 != 0 else 0
        pos_arg = 12 if counter % 2 != 0 else 0
        draw_board(pos_index, pos_arg)
        if counter % 2 == 0:
            take_input(PLAYERS[0], TOKENS[0])
        else:
            take_input(PLAYERS[1], TOKENS[1])
        if counter > 3:
            winner = check_win()
            if winner:
                if winner == 'X':
                    draw_board(42, 12)
                    print(PLAYERS[0].rjust(35), 'выиграл')
                    break
                else:
                    draw_board()
                    print(PLAYERS[1].rjust(35), 'выиграл')
                    break
        counter += 1
        if counter > 8:
            draw_board(42, 12)
            print('Ничья'.rjust(38))
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
#                                                          -------------
#                                                          | 1 | 2 | 3 |
#                                                          | 4 | X | 6 |
#                                                          | 7 | 8 | 9 |
#                                                          -------------
#                                           Player2 Куда поставить: 0? 2
# -------------
# | 1 | 0 | 3 |
# | 4 | X | 6 |
# | 7 | 8 | 9 |
# -------------
# Player1 Куда поставить: X? 1
#                                                          -------------
#                                                          | X | 0 | 3 |
#                                                          | 4 | X | 6 |
#                                                          | 7 | 8 | 9 |
#                                                          -------------
#                                           Player2 Куда поставить: 0? 9
# -------------
# | X | 0 | 3 |
# | 4 | X | 6 |
# | 7 | 8 | 0 |
# -------------
# Player1 Куда поставить: X? 4
#                                                          -------------
#                                                          | X | 0 | 3 |
#                                                          | X | X | 6 |
#                                                          | 7 | 8 | 0 |
#                                                          -------------
#                                           Player2 Куда поставить: 0? 6
# -------------
# | X | 0 | 3 |
# | X | X | 0 |
# | 7 | 8 | 0 |
# -------------
# Player1 Куда поставить: X? 8
#                                                          -------------
#                                                          | X | 0 | 3 |
#                                                          | X | X | 0 |
#                                                          | 7 | X | 0 |
#                                                          -------------
#                                           Player2 Куда поставить: 0? 7
# -------------
# | X | 0 | 3 |
# | X | X | 0 |
# | 0 | X | 0 |
# -------------
# Player1 Куда поставить: X? 3
#                              -------------
#                              | X | 0 | X |
#                              | X | X | 0 |
#                              | 0 | X | 0 |
#                              -------------
#                                  Ничья
# ['X', '0', 'X', 'X', 'X', '0', '0', 'X', '0']
# [5, 2, 1, 9, 4, 6, 8, 7, 3]





