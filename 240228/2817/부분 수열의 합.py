def sum_to_k():
    global cnt
    nums_sum = 0
    for i in range(N):
        if nums_sum > K:
            return

        if path[i]:
            nums_sum += nums[i]
           
    if nums_sum == K:
        cnt += 1


def func(level):
    if level == N:
        sum_to_k()
        return

    for i in range(2):
        path.append(check[i])
        func(level+1)
        path.pop()


T = int(input())
for tc in range(T):
    # N개의 자연수 
    # 최소 1개 이상의 수를 선택하여 그 합이 K가 되는 경우의 수 구하기
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    path = []
    check = [True, False]
    cnt = 0
    func(0)
    print(f'#{tc+1} {cnt}')