def dfs(graph, start, goal, visited):
    visited[start] = True
    if visited[goal]:
        return
    for node in graph[start]:
        if not visited[node]:
            dfs(graph, node, goal, visited)


T = int(input())
for tc in range(T):
    # 입력
    v, e = map(int, input().split())    # num_vertex, num_edge
    edge_list = [list(map(int, input().split())) for _ in range(e)]
    s, g = map(int, input().split())    # start node, goal node

    graph = [[]for _ in range(v+1)]
    for i in range(e):
        graph[edge_list[i][0]].append(edge_list[i][1])
    visited = [False] * (v+1)
    dfs(graph, s, g, visited)
    if visited[g]:
        result = 1
    else:
        result = 0
    print(f'#{tc+1} {result}')
    print('vertex, edge', v, e)
    print(edge_list)
    print('시작. 도착', s, g)
    print(graph)

