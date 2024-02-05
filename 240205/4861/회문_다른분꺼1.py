T = int(input())


def getPalindrome(n, m, array):
    for i in range(n):
        for j in range(n - m + 1):
            temp = array[i][j:j + m]
            if temp == temp[::-1]:  return temp


for _ in range(T):
    N, M = map(int, input().split())
    arr = [list(input()) for __ in range(N)]
    arr_col = [[arr[j][i] for j in range(N)] for i in range(N)]

    res = getPalindrome(N, M, arr)
    if res == None: res = getPalindrome(N, M, arr_col)
    res = ''.join(res)
    print(f'#{_ + 1} {res}')