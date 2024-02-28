from collections import deque

T = int(input())
for tc in range(T):
    # 컨테이너 수 N, 트럭 수 M
    N, M = map(int, input().split())
    # N개의 화물 각각의 무게
    weights = list(map(int, input().split()))
    weights.sort(reverse=True)
    # M개 트럭의 각각의 적재용량
    trucks = list(map(int, input().split()))
    trucks.sort()
    trucks = deque(trucks)

    sum_of_weight = 0
    for weight in weights:
        if not trucks:
            break
        truck = trucks.pop()
        if truck >= weight:
            sum_of_weight += weight
            continue
        else:
            trucks.append(truck)

    print(f'#{tc+1} {sum_of_weight}')


