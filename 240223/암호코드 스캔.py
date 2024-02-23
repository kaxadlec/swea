def transform(i, start_j, end_j):
    global result

    hex_num = arr[i][start_j:end_j]
    dec_num = int(hex_num, 16)
    bin_num = bin(dec_num)[2:]
    while 1:
        if bin_num[-1] == '0':
            bin_num = bin_num[0:-1]
        else:
            break

    if len(bin_num) % 56 != 0:
        pre_str = '0' * (((len(bin_num) // 56) + 1) * 56 - len(bin_num))
        new_bin_num = pre_str + bin_num

    # print(new_bin_num)
    # print(len(new_bin_num))
    # cross = len(new_bin_num) // 56
    # new_new_bin_num = None
    # new_new_bin_num = new_bin_num[0]
    # print(type(new_new_bin_num))

    item_num_list = []
    for k in range(0, len(new_bin_num) // 7):
        item_bin_num = new_bin_num[7*k:7*k+7]
        item_num_list.append(dict.get(item_bin_num))
    # print(item_num_list)

    odd, even = 0, 0

    for idx in range(len(item_num_list)):
        if idx == 7:
            check_code = item_num_list[idx]
        elif idx % 2 == 0:
            odd += item_num_list[idx]
        else:
            even += item_num_list[idx]

    if (odd*3 + even + check_code) % 10 == 0:
        result = check_code + odd + even

    return


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())    # 세로크기, 가로크기
    arr = [input() for _ in range(N)]
    result = 0
    stack = []
    check = 0
    dict = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9
    }
    for i in range(N):
        for j in range(M):
            if arr[i][j] != '0':
                if not stack:
                    stack.append(j)
            if stack and arr[i][j] == '0':
                start_j = stack.pop()
                end_j = j
                check = 1
                transform(i, start_j, end_j)
                break
        if check == 1:
            break


    print(f'#{tc+1} {result}')
    # print(arr)
