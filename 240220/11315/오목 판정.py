T = int(input())
for tc in range(T):
    N = int(input())
    result = 'NO'
    col_arr = [0] * N
    # diagonal_cnt = 0
    # diagonal_reverse_cnt = 0
    diagonal_arr = [0] * N
    diagonal_reverse_arr = [0] * N
    for i in range(N):
        # N개의 줄, 길이가 N인 문자열
        arr = input()  # o 돌이 있는칸  . 돌이 없는칸
        row_cnt = 0
        for j in range(N):
            # 연속인 조건
            if arr[j] == 'o':
                row_cnt += 1
                if row_cnt == 5:
                    result = 'YES'
                    break
                col_arr[j] += 1
                if col_arr[j] == 5:
                    result = 'YES'
                    break
                if i == 0:
                    diagonal_arr[j] = 1
                    diagonal_reverse_arr[j] = 1
                elif i != 0:
                    if diagonal_arr[j-1] == 1:
                        diagonal_arr[j] = 1
                    if (j+1) <= N-1 and diagonal_reverse_arr[j+1] == 1:
                        diagonal_reverse_arr[j] = 1

            elif arr[j] == '.':
                row_cnt = 0  # 가로 연속 아닌 조건
                col_arr[j] = 0  # 세로 연속 아닌 조건

            diagonal_arr[j - 1] = 0
            if (j+1) <= N-1:
                diagonal_reverse_arr[j + 1] = 0
        print(diagonal_arr, diagonal_reverse_arr)
    print(f"#{tc + 1} {result}")
