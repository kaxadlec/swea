for tc in range(1, 11):
    stack = []
    len_nums, nums = input().split()
    nums_str = str(nums)
    for num in nums_str:
        if not stack:
            stack.append(num)
        else:
            if stack[-1] == num:
                stack.pop()
            else:
                stack.append(num)

    print(f'#{tc} ', *stack, sep='')
