def dp(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return 2 * dp(n-2) + dp(n-1)


T = int(input())
for tc in range(T):
    N = int(input()) // 10
    result = dp(N)
    print(f'#{tc+1} {result}')
