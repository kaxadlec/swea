T = int(input())
for tc in range(T):
    N = int(input())
    n = (N//10)
    res, res1 = 1, 1
    if n % 2 == 1:
        for _ in range(n // 2):
            res1 = res1 * 3
        res2 = res1 * ((n // 2) + 1)
        res = res2 - (res1 - ((n // 2) + 1))

    else:
        for _ in range(n // 2):
            res = res * 3

    print(f'#{tc+1} {res}')
