for _ in range(10):
    N, s = input().split()
    s = list(s)
    N = int(N)

    rm = 0
    while True:
        find = False
        for i in range(N - 1 - rm):
            if s[i] == s[i + 1]:
                find = True
                s.pop(i)
                s.pop(i)
                rm += 2
                break
        if not find: break

    print(f'#{_ + 1}', ''.join(s))