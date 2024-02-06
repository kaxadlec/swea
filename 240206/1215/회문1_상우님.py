def getPalindrome(array, length):
    cnt = 0
    for s in array:
        for i in range(len(s) - length + 1):
            if s[i:i + length] == s[i:i + length][::-1]:
                cnt += 1
    return cnt


for _ in range(10):
    l = int(input())
    arr = [input() for __ in range(8)]
    arr_col = [[arr[j][i] for j in range(8)] for i in range(8)]

    res = 0
    res += getPalindrome(arr, l)
    res += getPalindrome(arr_col, l)

    print(f'#{_ + 1} {res}')
