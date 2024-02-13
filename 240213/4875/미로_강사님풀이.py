
T = int(input())
for tc in range(T):
    N = int(input())
    maze = []
    for _ in range(N):
        maze.append(input())
    result = 0
    stack = []
    # 시작점
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                stack.append([i, j])    # 시작 좌표를 i, j 쌍으로 넣어줌

    # d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    di = [1, -1, 0, 0]
    dj = [0, 0, -1, 1]
    visited = [[0] * N for _ in range(N)]
    # 탐색
    while stack:
        print('stack', stack)
        i, j = stack.pop()  # [i, j]

        visited[i][j] = 1   # 방문
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                if maze[ni][nj] == '0':
                    stack.append([ni, nj])
                # if maze[ni][nj] == '1':
                #     pass
                if maze[ni][nj] == '3':
                    result = 1
                    stack.clear()
                    break

    print(f'#{tc+1} {result}')
