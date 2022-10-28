"""Дополнительный модуль: обработка игрового процесса."""

# импорт дополнительных модулей проекта
import data
import functions


# ИСПОЛЬЗОВАТЬ: раз у вас эта функция не просто принимает пользовательский ввод, а делает весь ход, то и называть её следует соответственно
def human_turn(player: str, player_token: str) -> None:
    """Запрашивает позицию в которую игрок хочет поставить токен, проверяет возможность проставить токен в указанную клетку, отрисовывает доску с проставленным токеном и записывает ход в глобальную переменную TURNS."""
    while True:
        inp = input(player + f' Куда поставить: {player_token}? ')
        # ИСПОЛЬЗОВАТЬ: в Python есть оператор not in, его использование позволяет избежать лишних скобок
        # ИСПРАВИТЬ: опять же, это слишком лобовая проверка, она исключает масштабирование: например, на поле 5x5 игрок введёт номер клетки 19, и такой ввод не пройдёт текущую проверку
        if inp not in '123456789':
            print('Ошибка')
            continue
        inp = int(inp)
        # ИСПРАВИТЬ: зачем здесь приведение к строковому представлению? в глобальной переменной data.BOARD у нас и так строки должны быть
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
        # КОММЕНТАРИЙ: этот вывод вроде как для режима обучения подходит больше?
        functions.draw_board('left')
        # ИСПРАВИТЬ: условная конструкция не нужна, результат выражения counter % 2 можно использовать в качестве индекса
        if counter % 2 == 0:
            human_turn(data.PLAYERS[0], data.TOKENS[0])
        else:
            human_turn(data.PLAYERS[1], data.TOKENS[1])
        if counter > 3:
            winner = check_win()
            # ИСПРАВИТЬ: про дублирование кода в этом блоке я вам уже писал — посмотрите в истории коммитов
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
        # ИСПРАВИТЬ: продолжаю настаивать на написании более универсального кода: используйте здесь data.DIM**2, а лучше data.CELLS
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
