T = int(input())
for tc in range(T):
    paren_arr = list(input())
    check_stack = []
    piece = 0
    for idx in range(len(paren_arr)):
        if paren_arr[idx] == '(':
            if paren_arr[idx+1] == ')':
                piece += len(check_stack)
            else:
                check_stack.append(paren_arr[idx])
        elif paren_arr[idx] == ')':
            if paren_arr[idx-1] == ')':
                check_stack.pop()
                piece += 1

    print(f'#{tc+1} {piece}')



