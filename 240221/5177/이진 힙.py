import heapq


def order(node):
    global result

    next_node = parent[node]
    if next_node > 0:
        result += heap[next_node-1]
        order(next_node)


T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    heap = []
    parent = [0]*(N+1)
    for i in range(N):
        heapq.heappush(heap, arr[i])
        parent[i+1] = (i+1) // 2

    result = 0
    order(N)
    print(f'#{tc+1} {result}')



