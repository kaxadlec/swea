T = int(input())
for tc in range(T):
    print(f'#{tc + 1}', end=' ')
    N = int(input())
    result = round(pow(N, 1/3))
    if pow(result, 3) == N:
        print(result)
    else:
        print(-1)
