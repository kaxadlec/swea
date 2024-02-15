from collections import deque

T = 10
for tc in range(T):
    tc_num = int(input())
    arr = list(map(int, input().split()))
    queue = deque(arr)

    new_num = 21e8
    while queue[-1] > 0:
        # 한 사이클은 5번
        for k in range(1, 6):
            num = queue.popleft()
            new_num = num - k
            if new_num < 0:
                new_num = 0
            queue.append(new_num)
            if new_num == 0:
                break

    result = ' '.join(str(i) for i in queue)

    print(f'#{tc_num} {result}')

