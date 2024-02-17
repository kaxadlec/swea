from collections import deque


def bfs(start, maze):
    di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]   # 상하좌우
    queue = deque()
    visited = [[0]*100 for _ in range(100)]
    queue.append(start)
    while queue:
        i, j = queue.popleft()
        visited[i][j] = 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<100 and 0<=nj<100 and not visited[ni][nj]:
                if maze[ni][nj] == 0:
                    queue.append((ni, nj))
                elif maze[ni][nj] == 3:
                    return 1
    return 0

T = 10
for tc in range(T):
    _ = input()
    board = [list(map(int, input())) for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if board[i][j] == 2:
                start_node = (i, j)

    result = bfs(start_node, board)

    print(f'#{tc+1} {result}')

