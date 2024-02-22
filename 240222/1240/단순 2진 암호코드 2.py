from collections import deque


def find_password(j):
    global password_found
    global password

    code = arr[j:j + 7]
    check = 0
    if len(stack) == 8:
        odd, even = 0, 0
        while stack:
            even += stack.pop()
            odd += stack.pop()
        temp_password = odd * 3 + even
        password_found = 1
        if temp_password % 10 == 0:
            password = odd + even
            return

    if len(code) == 7 and code[-1] == '1':
        for idx in range(10):
            if code == rule[idx]:
                check = 1
                stack.append(idx)
                find_password(j + 7)

        if not check and stack:
            stack.clear()
            return


T = int(input())
for tc in range(T):
    # N 세로 크기, M 가로크기
    N, M = map(int, input().split())
    rule = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111',
            '0001011']
    stack = deque()
    password_found = 0
    password = 0
    for i in range(N):
        arr = input()
        for j in range(M):
            find_password(j)
            if password_found == 1:
                break

    print(f'#{tc + 1} {password}')
