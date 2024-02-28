def func(level, start, idx_change):
    # print(nums)
    if level == times:
        return

    max_num = 0
    max_i = -1
    for i in range(start, N):
        # print('i', i)
        if nums[i] >= max_num:
            max_num = nums[i]
            max_i = i
            # print('max_num max_i', max_num, max_i)

    # print('--', idx_change)
    # print('&&', max_i)

    if idx_change != max_i:
        nums[idx_change], nums[max_i] = nums[max_i], nums[idx_change]
        func(level+1, start+1, idx_change+1)

    elif idx_change == max_i:
        func(level, start+1, idx_change+1)


T = int(input())
for tc in range(T):
    nums, times = (input().split())
    nums = list(map(int, list(nums)))
    times = int(times)
    N = len(nums)

    func(0, 0, 0)
    result = ''.join(str(i) for i in nums)
    print(f'#{tc+1} {result}')

