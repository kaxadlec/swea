def find_min_sum(level, cdn_value, path_sum):
    global min_path_sum, new_cdn_value

    dr, dc = cdn_value
    if 0 > dr or dr >= N or 0 > dc or dc >= N:
        return

    if level == (N-1)*2:
        if path_sum < min_path_sum:
            min_path_sum = path_sum
        return

    path_sum += board[dr][dc]
    if path_sum >= min_path_sum:
        return

    for i in range(2):
        r, c = cdn_value
        path[level] = board[r][c]
        if dir[i] == 'down':
            nr = r+1
            nc = c
            new_cdn_value = (nr, nc)
        elif dir[i] == 'right':
            nr = r
            nc = c+1
            new_cdn_value = (nr, nc)
        find_min_sum(level+1, new_cdn_value, path_sum)


T = int(input())
for tc in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    dir = ['down', 'right']
    path = [0]*((N-1)*2)
    start = (0, 0)
    min_path_sum = 21e8
    find_min_sum(0, start, 0)

    print(f'#{tc+1} {min_path_sum+board[N-1][N-1]}')
