T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    max_result = 0
    for i in range(N):
        for j in range(N):
            result = 0
            for r in range(M):
                for c in range(M):
                    if i+r < N and j+c < N:
                        result = result + board[i+r][j+c]
            if result > max_result:
                max_result = result

    print(f'#{tc+1} {max_result}')
