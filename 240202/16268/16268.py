T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    max_pollen_sum = 0
    for i in range(N):
        for j in range(M):
            base_point = arr[i][j]
            pollen_sum = base_point
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    pollen_sum += arr[ni][nj]
            if max_pollen_sum < pollen_sum:
                max_pollen_sum = pollen_sum

    print(f'#{tc+1} {max_pollen_sum}')