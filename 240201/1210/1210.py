import copy
T = 10


def ladder(a):
    for j in range(100):
        x = j   # 출발점 저장
        arr = copy.deepcopy(a)
        i = 0
        if arr[i][j] == 1:
            while i < 99:
                for di, dj in [[0, 1], [0, -1], [1, 0]]:    # 사다리타기 이동 우선순위
                    ni, nj = i + di, j + dj     # 이동하기
                    if 0 <= ni < 100 and 0 <= nj < 100:
                        if arr[ni][nj] == 1:    # 만약 이동가능하면
                            arr[i][j] = 0       # 다시 방문하지 않도록 0으로 초기화
                            i = ni              # i, j 현재위치 갱신
                            j = nj
                            break
                        elif arr[ni][nj] == 2:  # 만약 도착지점 도착하면
                            return x    # 출발점 반환


for tc in range(T):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(100)]
    result = ladder(array)
    print(f'#{n} {result}')