T = int(input())
for tc in range(T):
    # 노드 개수, 리프 노드 개수, 값 출력할 노드 번호
    N, M, L = map(int, input().split())
    node_value = [[] for _ in range(N+1)]
    for _ in range(M):
        leaf_node, leaf_node_value = map(int, input().split())
        node_value[leaf_node] = leaf_node_value

    for idx in range(N, 0, -1):
        if not node_value[idx]:
            if idx*2+1 <= N:
                node_value[idx] = node_value[2*idx] + node_value[2*idx+1]
            elif idx*2 <= N:
                node_value[idx] = node_value[2*idx]

    print(f'#{tc+1} {node_value[L]}')


