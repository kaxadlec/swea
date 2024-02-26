T = int(input())
for tc in range(T):
    print(f'#{tc + 1}', end=' ')
    N = int(input())
    cards = input().split()
    a = 0
    b = (N+1) // 2
    for turn in range(N):
        if turn % 2 == 0:
            print(cards[a], end=' ')
            a = a + 1
        else:
            print(cards[b], end=' ')
            b = b + 1

    print()


