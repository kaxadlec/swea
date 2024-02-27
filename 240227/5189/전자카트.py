def battery(level, consumption_sum):
    global min_consumption_sum

    if consumption_sum >= min_consumption_sum:
        return

    if level == 1:
        consumption_sum += board[0][path[0]]
    elif level > 1:
        consumption_sum += board[path[level-2]][path[level-1]]

    if level == N-1:
        consumption_sum += board[path[-1]][0]
        if consumption_sum < min_consumption_sum:
            min_consumption_sum = consumption_sum
        return

    for i in range(N-1):
        if used[i] == 1:
            continue
        path.append(cases[i])
        used[i] = 1
        battery(level+1, consumption_sum)
        used[i] = 0
        path.pop()


T = int(input())
for tc in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    path = []
    used = [0] * (N-1)
    cases = [i for i in range(1, N)]
    min_consumption_sum = 21e8
    battery(0, 0)
    print(f'#{tc+1} {min_consumption_sum}')



