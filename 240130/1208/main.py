T = 10
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):
        arr.sort()
        arr[0] = arr[0] + 1
        arr[-1] = arr[-1] - 1

    min_box = min(arr)
    max_box = max(arr)
    result = max_box - min_box

    print(f'#{t+1} {result}')