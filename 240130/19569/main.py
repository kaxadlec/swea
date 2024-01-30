T = int(input())

for t in range(T):
    K, N, M = map(int, input().split()) # 점프가능거리, 종점, 정류장 개수
    charge_bus_stop = list(map(int, input().split())) # 충전기 버스정류장 리스트
    all_bus_stop = [0 for i in range(0, N + 3)]  # 전체 버스정류장 리스트 초기화
    my_pos = 0  # 초기 위치
    cnt = 0

    for i in charge_bus_stop:
        all_bus_stop[i] = 1 # 충전기 있는 버스정류장 인덱스 값은 1

    print(all_bus_stop)

    while my_pos < N+1:
        print('my_pos', my_pos)
        pos_max = my_pos + K
        pos_min = my_pos
        print(pos_max, 'pos_max')
        print(pos_min, 'pos_min')
        if pos_max >= N:
            break
        none_cnt = 0
        for pos in range(pos_max, pos_min, -1):
            if all_bus_stop[pos] == 1:
                my_pos = pos
                cnt = cnt + 1
                break
            else:
                none_cnt = none_cnt + 1

            if none_cnt >= K:
                break






    #
    # if my_pos == N:
    #     print(f'#{t} result')