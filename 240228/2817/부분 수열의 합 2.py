def func(level, sum_of_nums):
    global cnt

    if sum_of_nums > K:
        return

    if level > 0:
        if path[level-1] == 'check':
            sum_of_nums += nums[level-1]

    if level == N:
        if sum_of_nums == K:
            cnt += 1
        return

    for i in range(2):
        path.append(check[i])
        func(level + 1, sum_of_nums)
        path.pop()


T = int(input())
for tc in range(T):
    # N개의 자연수
    # 최소 1개 이상의 수를 선택하여 그 합이 K가 되는 경우의 수 구하기
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    path = []
    check = ['check', 'x']
    cnt = 0
    func(0, 0)
    print(f'#{tc + 1} {cnt}')