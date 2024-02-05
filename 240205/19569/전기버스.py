def electric_bus(max_move, end_pos, charge_bus_stop_cnt, charge_bus_stop_arr):
    current_pos = 0
    cnt_charge = 0
    move = max_move
    before_pos = 0
    while 1:
        if current_pos == 0:
            current_pos += move
            continue
        if current_pos >= end_pos:
            return cnt_charge
        if current_pos in charge_bus_stop_arr:
            before_pos = current_pos
            cnt_charge += 1
            current_pos = current_pos + move
        elif current_pos not in charge_bus_stop_arr:
            current_pos -= 1
            if current_pos == before_pos:
                return 0


T = int(input())
for tc in range(T):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    result = electric_bus(K, N, M, arr)
    print(f'#{tc + 1} {result}')
