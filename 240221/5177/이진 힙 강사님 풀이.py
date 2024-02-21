T = int(input())
for tc in range(T):
    N = int(input())
    item = [0]*(N+1)
    nodes = list(map(int, input().split()))

    for i in range(1, N+1):
        item[i] = nodes[i-1]
        for j in range(i, -1, -1):
            if item[j//2] > item[j]:
                item[j//2], item[j] = item[j], item[j//2]
    ancestor_sum = 0
    parent_node = N // 2
    while parent_node > 0:
        ancestor_sum += item[parent_node]
        parent_node //= 2
    print(f'#{tc+1}')
    print(nodes)
    print(ancestor_sum)