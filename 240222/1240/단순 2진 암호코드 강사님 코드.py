T = int(input())
code = [
    0b0001101,
    0b0011001,
    0b0010011,
    0b0111101,
    0b0100011,
    0b0110001,
    0b0101111,
    0b0111011,
    0b0110111,
    0b0001011
]

for tc in range(T):
    print(f'#{tc+1}', end=' ')
    # N 세로 크기, M 가로크기
    N, M = map(int, input().split())
    matrix = [input() for _ in range(N)]
    # print(matrix)
    matrix_set = list(set(matrix))
    # print(matrix_set)
    secret = 0
    for m in matrix_set:
        # m = int(m, 2)
        m = int('0' + m.rstrip('0'), 2)
        # print(m)
        if m:
            secret = m
    # print(secret)
    answer = []
    while secret:
        for i in range(len(code)):
            mask = (1 << 7) - 1     # 10000000 - 1 = 1111111(2)
            # print(f'{secret & mask:#b}')
            # print(f'{code[i] & mask:#b}')
            if secret & mask == code[i]:
                # print(i)
                answer.append(i)
                break
        secret >>= 7
    answer.reverse()
    # answer[::-1]
    # print(answer)
    odd = sum([answer[i] for i in range(0, len(answer), 2)])
    even = sum([answer[i] for i in range(1, len(answer), 2)])
    if (odd*3 + even) % 10 == 0:
        print(sum(answer))
    else:
        print(0)