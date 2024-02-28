from collections import deque

def pick():
    sorted_nums = sorted(nums)
    print('sorted_nums', sorted_nums)
    if times <= N/2:
        for idx in range(N-1, -1, -1):
            picked_nums.append(sorted_nums[idx])
        print('picked_nums', picked_nums)
    else:
        for idx in range(N-1, -1, -1):
            picked_nums.append(sorted_nums[idx])
        print('picked_nums', picked_nums)


def change(level):
    print('--', nums, level)
    if times <= N / 2:
        if level == times:
            print('최종 nums', nums)
            return

        temp_num = picked_nums.popleft()
        for idx in range(N-1, level-1, -1):
            if nums[idx] == temp_num:
                # if nums[idx_to_change] == nums[idx]:
                #     picked_nums.append(temp_num)
                #     idx_to_change += 1
                #     change(level)
                # else:
                nums[level], nums[idx] = nums[idx], nums[level]
                change(level+1)



T = int(input())
for tc in range(T):
    print(f'#{tc + 1}')
    nums, times = (input().split())
    nums = list(map(int, list(nums)))
    N = len(nums)
    times = int(times)
    picked_nums = deque()
    print(times)
    print(nums)
    pick()

    idx_to_change = 0
    change(0)
    print(nums)

