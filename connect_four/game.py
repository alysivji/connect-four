"""Connect Four game"""

import itertools
import os
from typing import NamedTuple

PLAYER_ONE = '🔴'
PLAYER_TWO = '🔵'
EMPTY = ' '

NUM_COLS = 7
NUM_ROWS = 6


def all_same(items):
    return (items[0] != EMPTY and
            all(x == items[0] for x in items))


def find_empty_slot(dict_to_check, empty_value):
    """Given dictionary, find key of empty slot, else return -1"""
    for key, item in dict_to_check.items():
        if item == empty_value:
            return key
    return -1


class MoveStatus(NamedTuple):
    status: bool
    piece_position: tuple


class Board:
    """Connect Four gameboard

    board will be a dict containing dicts

    Do column first because ConnectFour is a column based game...
        * we need to place piece in first non-empty row of col
    Rows after since rows do not matter"""

    def __init__(self):
        board = {}
        for col in (range(NUM_COLS)):
            col_dict = {}
            for row in range(NUM_ROWS):
                col_dict[row] = EMPTY
            board[col] = col_dict
        self._grid = board

    def draw_board(self):
        board_output = []

        end_separator = '-----' * NUM_COLS + '-'
        middle_separator = '|----' * NUM_COLS + '|'
        board_output.append(end_separator)

        # go thru each column and get the i-th row
        for row in range(NUM_ROWS):
            collected_row = []
            for col in self._grid:
                collected_row.append(self._grid[col][row])

            row_output = '  | '.join(collected_row)
            board_output.append(f'| {row_output}  |')
            board_output.append(middle_separator)

        # reverse and print
        board_output.pop()  # remove last separator that is not required

        # add TODO column numbers at top
        return '\n'.join(reversed(board_output))

    def __repr__(self):
        return self.draw_board()

    def drop_piece(self, selected_col, piece):
        """Given a column number, put the piece in the first free slot"""

        try:
            col = self._grid[selected_col]
        except KeyError:
            print('Not a valid column!')
            return MoveStatus(False, (None))

        free_slot = find_empty_slot(col, EMPTY)

        if free_slot == -1:
            print('Column is full!')
            return MoveStatus(False, (None))

        col[free_slot] = piece
        return MoveStatus(True, (selected_col, free_slot))

    def check_win(self, position):
        """Given the position of a piece, check to see if there is a possible
        four in a row on the board"""

        # victory positions can go in 8 directions, get them all
        def calculate_line(pos, col_offset: int, row_offset: int):
            col, row = pos
            streak = [pos]
            for count in range(1, 4):
                streak.append((col + count * col_offset,
                               row + count * row_offset))
            return streak

        # cycle thru each direction and got possible streak paths
        # TODO this only cycles lines where position is first or last
        # need to think of a better way to do this, we should find longest
        # streak based on where the last position entered is
        possible_winning_lines = []
        possible_winning_lines.append(calculate_line(position, 0, 1))  # N
        possible_winning_lines.append(calculate_line(position, 1, 1))  # NE
        possible_winning_lines.append(calculate_line(position, 1, 0))  # E
        possible_winning_lines.append(calculate_line(position, 1, -1))  # SE
        possible_winning_lines.append(calculate_line(position, 0, -1))  # S
        possible_winning_lines.append(calculate_line(position, -1, -1))  # SW
        possible_winning_lines.append(calculate_line(position, -1, 0))  # W
        possible_winning_lines.append(calculate_line(position, -1, 1))  # NW

        for line in possible_winning_lines:
            try:
                board_values = [self._grid[col][row] for col, row in line]
            except KeyError:
                continue

            if all_same(board_values):
                print('Winner! Winner! Chicken Dinner!')
                print(f'{board_values[0]} wins!')
                return True

        return False

    def is_full(self):
        for num, col in self._grid.items():
            if find_empty_slot(col, EMPTY) != -1:
                return False
        return True


class GameStatus(NamedTuple):
    status: bool
    msg: str


class ConnectFour:
    def __init__(self):
        self.board = Board()
        self.game_pieces_cycle = itertools.cycle([PLAYER_ONE, PLAYER_TWO])
        self.turn = next(self.game_pieces_cycle)
        self.last_move = None

    def __repr__(self):
        return f'{self.board}'

    def next_turn(self):
        self.turn = next(self.game_pieces_cycle)

    def process_player_turn(self, column):
        """Walk thru the process of a player's turn"""

        try:
            column = int(column)
        except ValueError:
            return GameStatus(False, 'Please enter a number')

        if not (0 <= column <= NUM_COLS):
            return GameStatus(False,
                              f'Please enter a valid column (0-{NUM_COLS})')

        turn_success, position = self.board.drop_piece(column, self.turn)
        if not turn_success:
            return GameStatus(False, 'Position is already taken, try again')

        self.last_move = position
        return GameStatus(True, 'All good')

    def check_victory(self):
        return self.board.check_win(self.last_move)

    def tie_game(self):
        return self.board.is_full()


if __name__ == '__main__':
    game = ConnectFour()

    # Game Loop
    while True:
        # GUI
        os.system('cls' if os.name == 'nt' else 'clear')
        print(game)
        print(f"{game.turn}'s turn.")

        # Game Actions
        position = input('Enter a position: ')
        result = game.process_player_turn(position)

        if not result.status:
            print(result.msg)
            continue

        if game.check_victory():
            os.system('cls' if os.name == 'nt' else 'clear')
            print(game)
            print(f'{game.turn}  wins!')
            break

        if game.tie_game():
            print("Nobody wins! aka Everybody Loses!")
            break

        game.next_turn()
