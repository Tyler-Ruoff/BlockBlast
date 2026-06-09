import board as board_module

def check_and_clear():
    rows_to_clear = []
    cols_to_clear = []

    for row in range(board_module.ROWS):
        if all(board_module.board[row][col] != 0 for col in range(board_module.COLS)):
            rows_to_clear.append(row)

    for col in range(board_module.COLS):
        if all(board_module.board[row][col] != 0 for row in range(board_module.ROWS)):
            cols_to_clear.append(col)

    for row in rows_to_clear:
        for col in range(board_module.COLS):
            board_module.board[row][col] = 0

    for col in cols_to_clear:
        for row in range(board_module.ROWS):
            board_module.board[row][col] = 0

    return len(rows_to_clear), len(cols_to_clear)
