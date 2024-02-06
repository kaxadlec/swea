def check_row(row):
    return set(board[row]) == set(standard)


def check_col(col):
    new_board = list(zip(*board))
    return set(new_board[col]) == set(standard)


def check_square(row, col):
    new_board = [row[col:col + 3] for row in board[row:row + 3]]
    new_board = [num for row in new_board for num in row]
    return set(new_board) == set(standard)


T = int(input())

for tc in range(1, T + 1):
    standard = list(range(1, 10))
    unique_row = 0
    unique_col = 0
    unique_square = 0
    board = [list(map(int, input().split())) for _ in range(9)]

    for row in range(9):
        unique_row += check_row(row)
    for col in range(9):
        unique_col += check_col(col)
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            unique_square += check_square(row, col)

    total = unique_row + unique_col + unique_square

    print(f'#{tc} {int(total == 27)}')