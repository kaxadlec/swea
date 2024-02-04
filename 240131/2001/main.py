T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # di, dj: 이동 인덱스
    di = []
    dj = []
    for p in range(M):
        for q in range(M):
            di.append(p)
            dj.append(q)

    max_pari_sum = 0    # M*M 배열의 최대 파리개수 합
    for i in range(N-M+1):  # 기준점 설정    # N-M+1 범위 설정을 통해 이동 인덱스가 N*N 배열 벗어나지 않도록 함.
        for j in range(N-M+1):
            pari_sum = 0
            for k in range(M * M):
                # 특정 기준점 (i, j)에서 M*M 배열 박스 안 돌아다님
                ni = i + di[k]  
                nj = j + dj[k]
                pari_sum = pari_sum + arr[ni][nj]   # 특정 기준점의 M*M 배열 안 파리개수 합

            if max_pari_sum < pari_sum:
                max_pari_sum = pari_sum

    print(f'#{tc+1} {max_pari_sum}')
