T = int(input())

for t in range(T):
    N = int(input())
    num_list = [2, 3, 5, 7, 11]
    i = 0
    temp_list = [0] * 5

    while i < 5:
        res = N % num_list[i]
        if res == 0:
            temp_list[i] = temp_list[i] + 1
            N = N // num_list[i]
            continue
        else:
            i = i + 1

    print(f"#{t+1} {' '.join(str(i) for i in temp_list)}")
