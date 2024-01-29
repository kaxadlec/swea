T = int(input())
for t in range(T):
    N = int(input())
    a = list(map(int, input().split()))

    max_val = max(a)
    min_val = min(a)
    print(f'#{t+1} {max_val - min_val}')
