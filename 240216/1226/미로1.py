from collections import deque


def bfs(start, maze):
    di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]   # 상하좌우
    queue = deque()
    visited = [[0]*16 for _ in range(16)]
    queue.append(start)
    while queue:
        i, j = queue.popleft()
        visited[i][j] = 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<16 and 0<=nj<16 and not visited[ni][nj]:
                if maze[ni][nj] == 0:
                    queue.append((ni, nj))
                elif maze[ni][nj] == 3:
                    return 1
    return 0


T = 10
for tc in range(T):
    _ = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    # 0: 길, 1: 벽, 2: 출발점, 3: 도착점
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start_node = (i, j)

    result = bfs(start_node, maze)

    print(f'#{tc+1} {result}')
