T = int(input())
for tc in range(T):
    N = int(input())
    works = [list(map(int, input().split())) for _ in range(N)]
    works.sort(key=lambda x: x[1])

    cnt = 1
    start_time, end_time = works[0][0], works[0][1]
    for i in range(1, N):
        s, e = works[i][0], works[i][1]
        if s < end_time:
            continue
        else:
            start_time, end_time = s, e
            cnt += 1

    print(f'#{tc+1} {cnt}')

