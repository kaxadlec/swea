def password(num_len, num_arr):
    temp_arr = []
    temp_arr.extend(num_arr)
    new_arr = []
    while 1:
        if len(num_arr) == 1:
            new_arr.append(num_arr.pop())
        if len(num_arr) == 0:
            break
        else:
            end_num = num_arr.pop()
            compare_num = num_arr.pop()
            if compare_num == end_num:
                continue
            elif compare_num != end_num:
                new_arr.append(end_num)
                num_arr.append(compare_num)
    new_arr.reverse()
    if temp_arr == new_arr:
        result = ''.join(str(i) for i in temp_arr)
        print(f'#{tc + 1} {result}')
    else:
        password(len(new_arr), new_arr)


T = 10
for tc in range(T):
    num_len, arr = input().split()
    arr = list(arr)
    num_len = int(num_len)
    num_arr = [int(i) for i in arr]
    password(num_len, num_arr)


