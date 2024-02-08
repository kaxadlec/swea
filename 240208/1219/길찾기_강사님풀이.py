T = 10
for tc in range(T):
    print(f'#{tc}', end=' ')
    _ = input()
    arr = list(map(int, input().split()))
    connect = [[] for _ in range(100)]
    for i in range(0, len(arr), 2):
        connect[arr[i]].append(arr[i+1])
    result = 0
    st = [0]    # 탐색을 시작할 노드를 스택에 넣음
    node = nxt = 0  # 현재노드 / 다음노드
    while st and nxt != 99:     # 스택이 비어있지 않고, 목표 노드에 도달하지 않으면
        node = st.pop()         # 스택에서 노드를 하나 꺼내 탐색을 진행
        for nxt in connect[node]:   # 현재 노드에 연결된 노드의 탐색을 진행
            if nxt == 99:
                result = 1
                break
            st.append(nxt)
    print(result)

