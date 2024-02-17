from collections import deque


def bfs(maze, start):
    queue = deque()
    visited = [[0]*N for _ in range(N)]
    di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]   # 상하좌우
    si, sj = start
    queue.append(start)
    visited[si][sj] = 1
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<= ni < N and 0<= nj < N and maze[ni][nj] != 1:
                if maze[ni][nj] == 3:
                    return visited[i][j] - 1
                elif visited[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + 1
                    queue.append((ni, nj))
    return 0


T = int(input())
for tc in range(T):
    N = int(input())    # 미로의 크기 N
    board = [list(map(int, input())) for _ in range(N)]
    # 1: 벽, 0: 통로, 2: 시작점, 3: 목표점

    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                s = (i, j)

    print(f'#{tc+1} {bfs(board, s)}')

