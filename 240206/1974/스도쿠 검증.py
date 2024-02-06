T = int(input())


def sudoku(grid):
    # 1. 3*3 격자 안에서 1~9 숫자 겹치면 안 됨
    tuned_grid = []
    for n in range(3):
        for m in range(3):
            for i in range(n * 3, n * 3 + 3):
                for j in range(m * 3, m * 3 + 3):
                    tuned_grid.append(grid[i][j])
            tuned_grid.sort()
            if tuned_grid != [i for i in range(1, 10)]:
                return 0
            tuned_grid = []

    # 2. 가로 행, 세로 열에서 1~9 숫자 겹치면 안 됨
    tuned_grid_row, tuned_grid_col = [], []
    for i in range(9):
        for j in range(9):
            tuned_grid_row.append(grid[i][j])
            tuned_grid_col.append(grid[j][i])
        tuned_grid_row.sort()
        tuned_grid_col.sort()
        tuned_grid = tuned_grid_row + tuned_grid_col
        if tuned_grid != [i for i in range(1, 10)] * 2:
            return 0
        tuned_grid_row, tuned_grid_col, tuned_grid = [], [], []

    return 1


for tc in range(T):
    result = 0
    grid = [list(map(int, input().split())) for _ in range(9)]   # 9*9 격자인것
    result = sudoku(grid)

    print(f'#{tc+1} {result}')
