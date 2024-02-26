from collections import deque
T = int(input())
for tc in range(T):
    N = int(input())
    electric_line = [list(map(int, input().split())) for _ in range(N)]
    queue = deque(electric_line)
    cnt = 0
    for i in range(N):
        Ai, Bi = queue.popleft()
        for _ in range(i+1, N):
            item = queue.popleft()
            if (item[0] > Ai and item[1] < Bi) or (item[0] < Ai and item[1] > Bi):
                cnt += 1
            queue.append(item)

    print(f'#{tc+1} {cnt}')

