from collections import deque


def bfs(count_node, start, end, graph):
    queue = deque()
    visited = [0] * (count_node+1)
    queue.append(start)
    visited[start] = 1
    while queue:
        current_node = queue.popleft()
        for neighbor in graph[current_node]:
            if neighbor == end:
                return visited[current_node]
            if visited[neighbor] == 0:
                visited[neighbor] = visited[current_node] + 1
                queue.append(neighbor)
    return 0


T = int(input())
for tc in range(T):
    V, E = map(int, input().split())    # 정점, 간선 개수
    graph = {}
    for _ in range(E):
        node1, node2 = map(int, input().split())
        if node1 not in graph:
            graph[node1] = [node2]
        else:
            graph[node1].append(node2)
        if node2 not in graph:
            graph[node2] = [node1]
        else:
            graph[node2].append(node1)

    S, E = map(int, input().split())  # 출발, 도착 노드

    print(f'#{tc+1} {bfs(V, S, E, graph)}')

