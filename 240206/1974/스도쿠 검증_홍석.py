T = int(input())
def check_row(lists):
    for item in lists:
        temp = set(item)
        if len(temp) != 9:
            return 0
    return 1
def check_col(lists):
    for col in range(9):
        item_list = []
        for row in range(9):
            item_list.append(lists[row][col])
        temp = set(item_list)
        if len(temp) != 9:
            return 0
    return 1
def check_square(lists):
    for col in range(0, 9, 3):
        for row in range(0, 9, 3):
            item_list = []
            for col_2 in range(3):
                for row_2 in range(3):
                    item_list.append(lists[row + row_2][col + col_2])
            temp = set(item_list)
            if len(temp) != 9:
                return 0
    return 1
for tc in range(1, T+1):
    case_list = [list(map(int, input().split())) for _ in range(9)]
    return_row = check_row(case_list)
    return_col = check_col(case_list)
    return_square = check_square(case_list)
    result = return_row + return_col + return_square
    if result == 3:
        result = 1
    else:
        result = 0
    print(f'#{tc} {result}')