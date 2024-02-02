import copy
T = 10
start_point_arr = []


def ladder(a):
    for j in range(100):
        if a[0][j] == 1:
            start_point_arr.append(j)
    arr = copy.deepcopy(a)
    for j in start_point_arr:
        i = 0
        x = j
        while i < 99:
            for di, dj in [[0, 1], [0, -1], [1, 0]]:  # 사다리타기 이동 우선순위
                ni, nj = i + di, j + dj  # 이동하기
                if 0 <= ni < 100 and 0 <= nj < 100:
                    if arr[ni][nj] == 1:  # 만약 이동가능하면
                        arr[i][j] = 0  # 다시 방문하지 않도록 0으로 초기화
                        i = ni  # i, j 현재위치 갱신
                        j = nj
                        break
                    elif arr[ni][nj] == 2:  # 만약 도착지점 도착하면
                        return x  # 출발점 반환


for tc in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = ladder(arr)
    print(f'#{tc + 1} {result}')