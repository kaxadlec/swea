T = int(input())


def pollen_cnt(base, i, j):
    new_di = []
    new_dj = []
    pollen_sum = base
    for b in range(1, base+1):
        for k in range(4):
            new_di.append(di[k] * b)
            new_dj.append(dj[k] * b)

    for order in range(4*base):
        ni = i + new_di[order]
        nj = j + new_dj[order]
        if 0<=ni<N and 0<=nj<M:
            pollen_sum += arr[ni][nj]

    return pollen_sum


for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    pollen_sum_max = 0
    for i in range(N):
        for j in range(M):
            base_point = arr[i][j]
            pollen_sum = pollen_cnt(base_point, i, j)
            if pollen_sum > pollen_sum_max:
                pollen_sum_max = pollen_sum

    print(f'#{tc+1} {pollen_sum_max}')
