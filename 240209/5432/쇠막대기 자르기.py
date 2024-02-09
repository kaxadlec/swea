T = int(input())
for tc in range(T):
    iron_bar = list(input())
    check_stack = [0, iron_bar[0]]
    laser = []
    piece = []
    for idx in range(1, len(iron_bar)):
        pop_item = check_stack.pop()
        if pop_item[0] == idx - 1 and pop_item[1] == '(' and iron_bar(idx) == ')':
            laser.append(idx)
        else:
            check_stack.append(pop_item)
            check_stack.append([idx, iron_bar[idx]])




    print(f'#{tc+1} ')
    print(iron_bar)
    print(check_stack)
    print(check_stack.pop()[0])
    print(check_stack)
