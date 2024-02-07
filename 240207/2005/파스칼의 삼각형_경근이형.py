T = int(input())
for tc in range(T):
    N = int(input())
    res = [[1]]
    for r in range(1, N):
        temp = [1]
        for c in range(r-1):
            temp.append(res[r-1][c]+res[r-1][c+1])
        temp.append(1)
        res.append(temp)
    print(f'#{tc+1}')
    for i in range(len(res)):
        print(*res[i])