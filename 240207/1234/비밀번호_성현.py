for tc in range(1,11):
    N, string = input().split()
    stack = []
    for num in string:
        if len(stack) > 0:
            if stack[-1] != num:
                stack.append(num)
            else:
                stack.pop()
        else:
            stack.append(num)
    print(f'#{tc} {"".join(stack)}')