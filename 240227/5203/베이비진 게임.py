def pick(level, start):
    global check
    if check == 1 or check == 2:
        return

    if level == 3:
        # print('path1', path1)
        # print('path2', path2)
        sorted_path1 = sorted(path1)
        sorted_path2 = sorted(path2)

        if check == 0 and (sorted_path1[0] == sorted_path1[1] == sorted_path1[2]):
            check = 1

        elif check == 0 and (sorted_path1[0]+1 == sorted_path1[1] and sorted_path1[1] + 1 == sorted_path1[2]):
            check = 1

        elif check == 0 and (sorted_path2[0] == sorted_path2[1] == sorted_path2[2]):
            check = 2

        elif check == 0 and (sorted_path2[0] + 1 == sorted_path2[1] and sorted_path2[1] + 1 == sorted_path2[2]):
            check = 2

        return

    for i in range(start, 6):
        path1[level] = player1_cards[i]
        path2[level] = player2_cards[i]
        pick(level+1, i+1)


T = int(input())
for tc in range(T):
    print(f'#{tc + 1}', end=' ')
    nums = list(map(int, input().split()))
    player1_cards, player2_cards = [], []
    for n in range(len(nums)):
        if n % 2 == 0:
            player1_cards.append(nums[n])
        else:
            player2_cards.append(nums[n])

    path1 = [0]*3
    path2 = [0]*3
    check = 0
    pick(0, 0)
    print(check)


