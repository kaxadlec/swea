def binary_search(l, r, find_page):
    cnt = 0
    while l <= r:
        cnt += 1
        c = int((l + r) // 2)
        if c == find_page:
            break
        elif c > find_page:
            r = c
        elif c < find_page:
            l = c
    return cnt


T = int(input())
for tc in range(T):
    P, P_a, P_b = map(int, input().split())
    cnt_a = binary_search(1, P, P_a)
    cnt_b = binary_search(1, P, P_b)
    if cnt_a < cnt_b:
        result = 'A'
    elif cnt_a > cnt_b:
        result = 'B'
    elif cnt_a == cnt_b:
        result = 0

    print(f'#{tc+1} {result}')
