T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    max_fallen = 0
    for i in range(N-1):
        cnt = 0
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                cnt = cnt + 1
        if max_fallen < cnt:
            max_fallen = cnt

    print(f"#{tc+1} {max_fallen}")
