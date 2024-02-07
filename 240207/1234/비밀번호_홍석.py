T = 10
def use_func(case_list, stack):
    for num in range(1, len(case_list)):
        if len(stack) > 0 and case_list[num] == stack[-1]:
            stack.pop()
            continue
        stack.append(case_list[num])
    return stack
for tc in range(1, T+1):
    num_count, num_list = input().split()
    stack = [num_list[0]]
    print(f'#{tc} {"".join(use_func(num_list, stack))}')