T = 10


def dfs(graph, v, visited):
    visited[v] = True
    stack = []
    while True:
        for w in graph[v]:
            if visited[w] == False:
                stack.append(w)
                v = w
                visited[v] = True
                if v == 99:
                    return 1
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break
    return 0


for tc in range(T):
    tc_num, edge = map(int, input().split())    # 테스트케이스 번호 / 간선의 갯수
    arr = list(map(int, input().split()))       # 순서쌍
    graph =[[] for _ in range(100)]    # 정점의 개수 최대 100개
    for i in range(edge):    # 방향 그래프
        n1, n2 = arr[i*2], arr[i*2+1]
        graph[n1].append(n2)
    visited = [False] * 100
    result = dfs(graph, 0, visited)
    print(f'#{tc+1} {result}')

