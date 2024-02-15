from collections import deque

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = deque(arr)
    for k in range(M):
        queue.append(queue.popleft())

    print(f'#{tc+1} {queue[0]}')