def find_palindrome(pal_len, row):
    cnt = 0
    for i in range(8 - pal_len + 1):
        row_to_check_in_board = board[row][i:i + pal_len]
        row_to_check_in_turned_board = turned_board[row][i:i + pal_len]
        cnt += (row_to_check_in_board == row_to_check_in_board[::-1]) + (
                    row_to_check_in_turned_board == row_to_check_in_turned_board[::-1])

    return cnt


for tc in range(1, 11):
    pal_len = int(input())
    board = [list(input()) for _ in range(8)]
    turned_board = list(zip(*board))
    answer = 0

    for row in range(8):
        answer += find_palindrome(pal_len, row)

    print(f'#{tc} {answer}')