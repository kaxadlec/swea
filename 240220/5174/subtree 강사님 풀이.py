from collections import deque

T = int(input())
for tc in range(T):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))
    tree = [[] for _ in range(E+2)]
    # 0 ~ N (0은 안 쓰고 1~N)
    for i in range(0, len(edges), 2):
        # 2씩 증가
        # i번째 노드 번호
        # i+1 연결된 하위 노드
        tree[edges[i]].append(edges[i+1])

    stack = deque()
    stack.append(N)
    cnt = 0
    print('tree', tree)
    while stack:
        print('stack', stack)
        cnt += 1
        node = stack.pop()
        print('node', node)
        for child in tree[node]:
            stack.append(child)

    print(f'#{tc + 1} {cnt}')