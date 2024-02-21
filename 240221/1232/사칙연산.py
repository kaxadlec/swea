def postorder(node):
    global result

    if len(tree[node]) == 3:
        postorder(tree[node][1])
    else:
        stack.append(tree[node][0])

    if len(tree[node]) == 3:
        postorder(tree[node][2])
    else:
        if stack:
            pass
        else:
            stack.append(tree[node][0])

    if len(tree[node]) == 3:
        operator = tree[node][0]
        operand1 = stack.pop()
        operand2 = stack.pop()
        if operator == '+':
            result = operand2 + operand1
        elif operator == '-':
            result = operand2 - operand1
        elif operator == '*':
            result = operand2 * operand1
        elif operator == '/':
            result = operand2 // operand1
        stack.append(result)
    else:
        pass


T = 10
for tc in range(T):
    N = int(input())
    tree = [0] * (N+1)
    for i in range(N):
        arr = input().split()
        if arr[1].isnumeric():  # 정점이 정수면
            # 정점번호 / 양의 정수
            tree[i+1] = [int(arr[1])]
        else: # 정점이 연산자이면
            # 정점번호 / 연산자 / left child / right child
            arr[2] = int(arr[2])
            arr[3] = int(arr[3])
            tree[i+1] = arr[1:4]
    result = 0
    stack = []
    postorder(1)
    print(f'#{tc+1} {result}')
    # print(tree)


