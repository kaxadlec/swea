T = 10
for tc in range(T):
    N = int(input()) # 테스트케이스 번호
    arr = [list(map(int, input().split())) for _ in range(100)] # 100 * 100 배열 받음

    sum1, sum2 = 0, 0
    for i in range(100):
        for j in range(100):
            if i == j:
                sum1 = sum1 + arr[i][j]
            elif i + j == 100:
                sum2 = sum2 + arr[i][j]

    max_i_sum = 0
    for i in range(100):
        i_sum = 0
        for j in range(100):
            i_sum = i_sum + arr[i][j]
            if max_i_sum < i_sum:
                max_i_sum = i_sum

    max_j_sum = 0
    for j in range(100):
        j_sum = 0
        for i in range(100):
            j_sum = j_sum + arr[i][j]
            if max_j_sum < j_sum:
                max_j_sum = j_sum

    result = max(sum1, sum2, max_i_sum, max_j_sum)

    print(f'#{tc+1} {result}')