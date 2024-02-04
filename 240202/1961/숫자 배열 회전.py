T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    board = [[0]*3 for i in range(N)]
    # 90도 회전한 모양
    for j in range(N):
        temp_arr= []
        for i in range(N):
            temp_arr.append(arr[i][j])
        temp_arr.reverse()
        rotate_90= ''.join(str(k) for k in temp_arr)
        board[j][0] = rotate_90
    # 180도 회전한 모양
    for i in range(N):
        temp_arr = []
        for j in range(N):
            temp_arr.append(arr[i][j])
        temp_arr.reverse()
        rotate_180 = ''.join(str(k) for k in temp_arr)
        board[N-i-1][1] = rotate_180
    # 270도 회전한 모양
    for j in range(N):
        temp_arr = []
        for i in range(N):
            temp_arr.append(arr[i][j])
        rotate_270 = ''.join(str(k) for k in temp_arr)
        board[N-j-1][2] = rotate_270

    print(f'#{tc + 1}')
    for index in board:
        result = ' '.join(str(i) for i in index)
        print(result)
