def inorder_traversal(root):
    if root:
        inorder_traversal(left_child[root])
        print(node_value[root], end='')
        # print(root, end='')
        inorder_traversal(right_child[root])


T = 10
for tc in range(T):
    N = int(input())    # 정점의 총 수
    arr = [list(input().split()) for _ in range(N)]
    left_child = [0] * (N + 1)     # 인덱스는 parent 번호, 요소는 left child 번호
    right_child = [0] * (N + 1)    # 인덱스는 parent 번호, 요소는 right child 번호
    parent = [0]*(N+1)   # 인덱스는 child 번호, 요소는 parent 번호
    node_value = [0] * (N + 1)  # 인덱스는 node 번호, 요소는 node 문자
    
    # 정점 정보
    # current_node 번호 / current_node 문자 / left child 번호 / right child 번호
    for node_info in arr:
        node, node_str = int(node_info[0]), node_info[1]
        node_value[node] = node_str
        if len(node_info) == 3:     # left child만 있는 경우
            lc = int(node_info[2])
            parent[lc] = node
            left_child[node] = lc
        if len(node_info) == 4:     # left child, right child 둘다 있는 경우
            lc, rc = int(node_info[2]), int(node_info[3])
            parent[lc], parent[rc] = node, node
            left_child[node], right_child[node] = lc, rc

    c = N
    while parent[c] != 0:   # 마지막 번호 노드부터 부모로 거슬러 올라감
        c = parent[c]
    root = c
    
    print(f'#{tc+1}', end=' ')
    inorder_traversal(root)
    print()

