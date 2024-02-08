T = 10


def dfs(graph, v, visited):
    print(graph)
    visited[v] = True
    stack = []
    print('v0', v)
    while True:
        print('v 방문한 정점', v)
        for w in graph[v]:
            print('w 이제 향할 것인 정점', w)
            if visited[w] == False:
                stack.append(w)
                v = w
                visited[v] = True
                if v == 99:
                    return 1
                print('v 향해서 이제 방문할 것인 정점', v)
                break
        else:
            print('향할 정점이 없음')
            if stack:
                v = stack.pop()
            else:
                break
        print('stack', stack)
        print()
    return 0


for tc in range(T):
    tc_num, edge = map(int, input().split())    # 테스트케이스 번호 / 간선의 갯수
    arr = list(map(int, input().split()))       # 순서쌍
    graph =[[] for _ in range(100)]    # 정점의 개수 최대 100개
    for i in range(edge):
        n1, n2 = arr[i*2], arr[i*2+1]
        graph[n1].append(n2)
        # graph[n2].append(n1)  # 무방향 그래프이므로 주석처리
    visited = [False] * 100
    result = dfs(graph, 0, visited)
    print(f'#{tc+1} {result}')
    print()
