T = int(input())
for tc in range(T):
    test_num, length = map(str, input().split())
    length = int(length)
    arr = list(map(str, input().split()))
    order_arr = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    count_arr = [0] * 10
    sort_arr = []
    for i in range(length):
        for j in range(10):
            if arr[i] == order_arr[j]:
                count_arr[j] += 1
    for k in range(length):
        for idx in range(10):
            if count_arr[idx] > 0:
                sort_arr.append(order_arr[idx])
                count_arr[idx] -= 1
                break

    print(f'{test_num}')
    print(' '.join(str(i) for i in sort_arr))