"""Connect Four game"""

PLAYER_ONE = '🔴'
PLAYER_TWO = '🔵'
EMPTY = ' '

NUM_COLS = 7
NUM_ROWS = 6


def all_same(items):
    return (items[0] != EMPTY and
            all(x == items[0] for x in items))


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
        # TODO column numers somewhere
        return '\n'.join(reversed(board_output))

    def __repr__(self):
        return self.draw_board()

    def drop_piece(self, selected_col, piece):
        """Given a column number, put the piece in the first free slot"""

        try:
            col = self._grid[selected_col]
        except KeyError:
            print('Not a valid key!')
            return False

        free_slot = None
        for key, item in col.items():
            if item == EMPTY:
                free_slot = key
                break

        if free_slot is None:
            print('Column is full!')
            return False

        col[free_slot] = piece
        return True

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
                print('Bad ', line)
                continue

            print('Good ', line)
            if all_same(board_values):
                print('Winner! Winner! Chicken Dinner!')
                print(f'{board_values[0]} wins!')
                return True

        return False


if __name__ == '__main__':
    new_game = Board()
    print(new_game)
