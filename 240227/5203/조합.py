card = [1, 2, 3, 4]
path = [0]*3


def abc(level, start):
    if level == 3:
        print(path)
        return

    for i in range(start, 4):
        path[level] = card[i]
        abc(level+1, i+1)


abc(0, 0) # level start