T = int(input())
for tc in range(T):
    paren_arr = list(input())
    check_stack = []
    laser = []
    iron_bar = []
    for idx in range(len(paren_arr)):
        if not check_stack:
            check_stack.append([idx, paren_arr[idx]])
            continue
        else:
            pop_item = check_stack.pop()
        if pop_item[0] == idx - 1 and pop_item[1] == '(' and paren_arr[idx] == ')': # 레이저 조건
            laser.append([pop_item[0], idx])
        elif pop_item[1] == '(' and paren_arr[idx] == ')':  # 쇠막대기 조건
            iron_bar.append([pop_item[0], idx])
        else:   # 두 조건 다 아니면 그냥 스택에 쌓음
            check_stack.append(pop_item)
            check_stack.append([idx, paren_arr[idx]])

    cnt = 0
    cnt_arr = []
    for i in range(len(iron_bar)):
        cnt = 0
        for j in range(len(laser)):
            if laser[j][0] > iron_bar[i][0] and laser[j][1] < iron_bar[i][1]:   # 레이저가 쇠막대기를 지나는 조건
                cnt += 1
        cnt_arr.append(cnt)

    result = sum([i+1 for i in cnt_arr])
    print(f'#{tc+1} {result}')



