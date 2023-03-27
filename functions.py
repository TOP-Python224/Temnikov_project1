"""Дополнительный модуль: вспомогательные функции."""
# импорт из стандартной библиотеки
from configparser import ConfigParser
from shutil import get_terminal_size

# импорт дополнительных модулей проекта
import data
import help


def read_ini() -> bool:
    """Считывает статистику об игроках и сохраненные игры из ini-файлов и записывает данные в глобальную переменную STATS и SAVES,
    возвращает True если игра запущена впервые."""
    players = ConfigParser()
    players.read(data.PLAYERS_FILE, encoding='utf-8')
    for section in players.sections():
        data.STATS[section] = {
            key: int(value) if value.isdecimal() else value
            for key, value in players[section].items()
        }
    saves = ConfigParser()
    saves.read(data.SAVES_FILE, encoding='utf-8')
    for section in saves.sections():
        players = tuple(section.split(';'))
        turns = [int(i) for i in saves[section]['turns'].split(',')]
        data.SAVES[players] = turns
    if data.STATS:
        return False
    else:
        return True

def write_ini_stats() -> None:
    """Записывает данные из глобальной переменной STATS в ini-файл."""
    players = ConfigParser()
    players.read_dict(data.STATS)
    with open(data.PLAYERS_FILE, 'w', encoding='utf-8') as fileout:
        players.write(fileout)


def write_ini_saves() -> None:
    """Записывает данные из глобальной переменной SAVES в ini-файл."""
    saves = ConfigParser()
    for elem in data.SAVES:
        saves[';'.join(elem)] = {'turns': ','.join([str(i) for i in data.SAVES[elem]])}
    with open(data.SAVES_FILE, 'w', encoding='utf-8') as fileout:
        saves.write(fileout)


def get_player_nickname() -> None:
    """Запрашивает никнейм игрока, в случае отсутствия игрока в data.STATS добавляет запись о новом игроке, и добавляет имя игрока в data.PLAYERS."""
    while True:
        player = input('Введите свой никнейм: ')
        if player.startswith('#'):
            print('Ваш никнейм не должен начинаться с "#"!')
            continue
        else:
            if player not in data.STATS.keys():
                data.STATS[player] = {'wins': 0, 'losses': 0, 'ties': 0, 'training': 'True'}
                write_ini_stats()
                data.PLAYERS.append(player)
                help.game_tutorial()
            data.PLAYERS.append(player)
            break



def draw_board(board: list[str], align_right: bool = False) -> str:
    """Формирует и возвращает строку, содержащую изображение игрового поля."""
    cell_width = len(max(board, key=len))
    center_cell_value = [
        cell.center(cell_width + 2)
        for cell in [' ' * (cell_width - len(i)) + i for i in board]
    ]
    cross_line = '—' * (data.DIM * (cell_width + 2) + data.DIM - 1) + '\n'
    table = ''
    if align_right:
        align = get_terminal_size()[0] - 1
    else:
        align = len(cross_line) + 1
    for i in data.RANGE:
        row = '|'.join(center_cell_value[i * data.DIM: (i + 1) * data.DIM])
        table += f"{row.rjust(align - 1)}\n"
    cross_line = f"\n{cross_line.rjust(align)}"
    table = table.rstrip('\n').replace('\n', cross_line)
    return table


def tutorial(turn: int, token_index: int, align_right: bool = False) -> str:
    """Формирует и возвращает строку с подсказкой(для режима обучения)."""
    msg = f"Игрок '{data.PLAYERS[token_index]}' сделал ход '{data.TOKENS[token_index]}' в ячейке '{turn + 1}'"
    if align_right:
        align = get_terminal_size()[0] - 3
    else:
        align = len(msg)
    return msg.rjust(align)


def update_score(score: data.SCORE) -> None:
    """Обновляет глобальную переменную data.STATS."""
    for item in score:
        for player in item:
            for results in item.values():
                for result in results:
                    data.STATS[player][result] += results[result]
                    data.STATS[player]['training'] = False
    data.SAVES.pop(tuple(data.PLAYERS))
    write_ini_saves()
    write_ini_stats()


def show_stats() -> None:
    """Выводит статистику игроков."""
    for player in data.STATS:
        print("\t--------------------------------")
        print("\t         SCORE BOARD       ")
        print("\t--------------------------------")
        print("\t\t   ", f"Игрок {player}")
        print("\t\t   ", f"победил {data.STATS[player]['wins']} раз ")
        print("\t\t   ", f"проиграл {data.STATS[player]['losses']} раз ")
        print("\t\t   ", f"вничью {data.STATS[player]['ties']} раз ")
        print("\t--------------------------------\n")


def load() -> None:
    """Загружает сохраненную партию."""
    saves_slots = load_slots()
    slot = get_slot(saves_slots)
    load_game(slot, saves_slots)


def load_slots() -> dict:
    """Возвращает словарь с доступными сохраненными партиями для текущего игрока."""
    saves_slots = {}
    i = 1
    if data.SAVES:
        for k, v in data.SAVES.items():
            if data.PLAYERS[0] in k:
                saves_slots[i] = k, v
                i += 1
        return saves_slots


def get_slot(saves_slots: dict) -> int:
    """Запрашивает и возвращает номер сохраненной партии из выведенного списка."""
    if saves_slots:
        print(f"\nДоступны следующие сохраненные партии:")
        for k, v in saves_slots.items():
            print(k, v[0], sep=' = ')
    else:
        print('Нет доступных сохранений!')
    while True:
        slot = int(input(f"\nВведите номер сохраненной партии{data.PROMPT}"))
        if slot in saves_slots:
            return slot
        else:
            print('Вы ввели некорректный номер сохраненной партии!')


def load_game(slot: int, saves_slots: dict) -> None:
    """Загружает выбранное сохранение и отображает 2 последних хода."""
    data.PLAYERS = [*saves_slots[slot][0]]
    data.TURNS = saves_slots[slot][1]
    token_index = 0
    if len(data.TURNS) < 2:
        print('Сохраненные ходы не отображаются, т.к. сохранено менее 2-х ходов!')
        need_draw = []
    else:
        need_draw = data.TURNS[-2:]
    for turn in data.TURNS:
        data.BOARD[turn - 1] = data.TOKENS[token_index]
        if turn in need_draw:
            print(f"{tutorial(turn - 1, token_index, token_index)}\n")
            print(f"{draw_board(data.BOARD, token_index)}\n")
        token_index = abs(token_index - 1)