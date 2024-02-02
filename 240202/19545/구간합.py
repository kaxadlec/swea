T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    partial_sum = 0
    start, end = 0, 0
    max_partial_sum = 0
    min_partial_sum = 21e8
    while end < N:
        partial_sum = 0
        end = start + M
        for k in range(start, end):
            partial_sum += arr[k]
        start = start + 1

        if max_partial_sum < partial_sum:
            max_partial_sum = partial_sum
        if min_partial_sum > partial_sum:
            min_partial_sum = partial_sum
    result = max_partial_sum - min_partial_sum

    print(f'#{tc+1} {result}')