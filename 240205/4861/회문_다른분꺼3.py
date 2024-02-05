T = int(input())

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    case_list = [input() for _ in range(N)]
    for item in case_list:
        for num in range(N - M + 1):
            new_str = item[0 + num:]
            reverse_str = new_str[::-1]
            if new_str == reverse_str:
                result = new_str

    for j in range(N):
        new_str = ""
        for i in range(N):
            new_str += case_list[i][j]
        for num in range(N - M + 1):
            new_strY = new_str[0 + num:]
            if new_strY == new_strY[-1::-1]:
                result = new_strY
    print(f'#{tc} {result}')