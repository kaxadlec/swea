def inorder(node):
    global number
    if tree[node][0] != 0:
        inorder(tree[node][0])

    tree[node].append(number)
    number += 1

    if tree[node][1] != 0:
        inorder(tree[node][1])


T = int(input())
for tc in range(T):
    N = int(input())
    tree = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        if 2*i <= N:
            tree[i].append(2*i)
        else:
            tree[i].append(0)
        if 2*i+1 <= N:
            tree[i].append(2 * i+1)
        else:
            tree[i].append(0)

    number = 1
    inorder(1)
    root = tree[1][2]
    result = tree[N//2][2]
    print(f'#{tc+1} {root} {result}')
    # print(tree)