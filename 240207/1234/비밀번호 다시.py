from collections import deque
T = 10
for tc in range(T):
    N, arr = input().split()
    stack = deque()
    password = []
    for idx in range(len(arr)):
        stack.append(arr[idx])
        if len(stack) > 1:
            num2 = stack.pop()
            num1 = stack.pop()
            if num1 != num2:
                stack.append(num1)
                stack.append(num2)

    result = ''.join(str(i) for i in stack)
    print(f'#{tc+1} {result}')



