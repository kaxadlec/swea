T = int(input())
for tc in range(T):
    # 노드 개수, 리프 노드 개수, 값 출력할 노드 번호
    N, M, L = map(int, input().split())
    parent = [i // 2 for i in range(0, N+1)]
    tree = [0] * (N+1)
    for _ in range(M):
        n, v = map(int, input().split())
        tree[n] = v
    for i in range(N, 0, -1):
        if tree[i]:
            continue
        for j in range(len(parent)):
            if i == parent[j]:
                tree[i] += tree[j]

    print(f'#{tc+1} {tree[L]}')