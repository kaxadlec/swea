from collections import deque


T = int(input())
for tc in range(T):
    # 손님 N명
    # 0초 ~ M초 동안
    # K개의 붕어빵을 만들 수 있음
    N, M, K = map(int, input().split())
    # 각 사람이 언제 도착하는지를 나타내는 배열
    arr = list(map(int, input().split()))
    new_arr = sorted(arr)
    queue = deque(new_arr)

    customer, sec, fish_shaped_bun = N, M, K

    while queue:
        for _ in range(fish_shaped_bun):
            if queue:
                cus = queue.popleft()
                if cus < sec:
                    result = 'Impossible'
                    break
                else:
                    result = 'Possible'

        if result == 'Impossible':
            break
        sec += M

    print(f'#{tc + 1} {result}')


