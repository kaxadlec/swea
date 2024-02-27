di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]


def move(i, j, room, cnt):
    global max_cnt, result_room

    cnt += 1

    if max_cnt < cnt:
        max_cnt = cnt
        result_room = start_room
    elif max_cnt == cnt:
        if result_room > start_room:
            result_room = start_room

    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and room_board[ni][nj] == room+1:
            move(ni, nj, room+1, cnt)


T = int(input())
for tc in range(T):
    N = int(input())
    room_board = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    result_room = 21e8
    for r in range(N):
        for c in range(N):

            start_room = room_board[r][c]
            move(r, c, start_room, 0)

    print(f'#{tc+1} {result_room} {max_cnt}')
