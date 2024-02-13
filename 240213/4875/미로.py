result = 0
def search(i, j, maze, visited):
    global result

    for k in range(4):
        if result == 1:
            return
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            if maze[ni][nj] == 3:
                visited[ni][nj] = True
                result = 1
                return

            elif maze[ni][nj] == 0 and visited[ni][nj] == False:
                visited[ni][nj] = True
                search(ni, nj, maze, visited)



T = int(input())
for tc in range(T):
    result = 0
    N = int(input().strip())
    maze = [list(map(int, input().strip())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                visited[i][j] = True
                search(i, j, maze, visited)

    print(f'#{tc + 1} {result}')
