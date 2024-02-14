def permutation(level):
    if level == N-1:
        print(path)
        return
    for i in range(N):
        if used[i]:
            continue
        path[level] = line_arr[i]
        used[i] = 1
        permutation(level+1)
        used[i] = 0


T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for k in range(N):
        line_arr = arr[k]
        path = [0] * (N-1)
        used = [0] * N
        print('한 줄', line_arr)
        permutation(0)

    print(f'#{tc+1}')



