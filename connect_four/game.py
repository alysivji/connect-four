"""Connect Four game"""

PLAYER_ONE = '🔴'
PLAYER_TWO = '🔵'

NUM_COLS = 7
NUM_ROWS = 6


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
                col_dict[row] = ' '
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


if __name__ == '__main__':
    new_game = Board()
    print(new_game)
