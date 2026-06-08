from board import board, COLS, ROWS

def check_and_clear():
    rows_to_clear = []
    cols_to_clear = []

    for row in range(ROWS):
        if all(board[row][col] != 0 for col in range(COLS)):
            rows_to_clear.append(row)

    for col in range(COLS):
        if all(board[row][col] != 0 for row in range(ROWS)):
            cols_to_clear.append(col)

    for row in rows_to_clear:
        for col in range(COLS):
            board[row][col] = 0

    for col in cols_to_clear:
        for row in range(ROWS):
            board[row][col] = 0
          
    return len(rows_to_clear), len(cols_to_clear)
