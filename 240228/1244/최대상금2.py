def func(level, start):

    if level == times:
        return

    for i in range(start, N):
        for j in range(i+1, N):
            if (i, j) not in check_list:
                nums[i], nums[j] = nums[j], nums[i]
                check_list.append((i, j))
                nums[i], nums[j] = nums[j], nums[i]
                # print(nums)
                func(level, start)

T = int(input())
for tc in range(T):
    nums, times = (input().split())
    nums = list(map(int, list(nums)))
    times = int(times)
    N = len(nums)

    check_list = []
    func(0, 0)
    print(f'#{tc+1}')
    print(nums)

