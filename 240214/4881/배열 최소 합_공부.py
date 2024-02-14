def permutation(level, current_sum):
    global min_sum_path
    print('current_sum', current_sum)
    if current_sum > min_sum_path:  # 과정 중 배열 합이 최소합보다 크면 중단
        return
    if level == N:  # N개의 행 다 하나씩 숫자 선택 완료
        min_sum_path = current_sum
        print('path', path)
        print()
        return

    for j in range(N):
        if used[j]:     # 방문한 열이면 스킵
            continue
        path[level] = arr[level][j]     # arr 배열의 행마다 숫자 선택
        used[j] = 1
        print('arr[level][j]', arr[level][j])

        permutation(level+1, current_sum + arr[level][j])
        used[j] = 0


T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum_path = 10*N+1
    current_sum = 0
    path = [0] * N  # 각 행마다 숫자 하나 골라 만든 배열
    used = [0] * N  # 각 열 방문 체크 (열 중복 방지를 위해)

    permutation(0, current_sum)

    print(f'#{tc+1} {min_sum_path}')



