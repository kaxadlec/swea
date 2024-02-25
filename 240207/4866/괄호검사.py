from collections import deque

T = int(input())
for tc in range(T):
    arr = input()
    stack = deque()
    result = 1
    for s in arr:
        if s == '{' or s == '(' or s == '}' or s == ')':
            stack.append(s)
        if len(stack) > 1:
            s2 = stack.pop()
            s1 = stack.pop()
            if s1 == '{' and s2 == '}':
                pass
            elif s1 == '(' and s2 == ')':
                pass
            else:
                stack.append(s1)
                stack.append(s2)
    if stack:
        result = 0

    print(f'#{tc+1} {result}')
