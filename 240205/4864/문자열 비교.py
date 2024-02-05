T = int(input())
for tc in range(T):
    str1 = input()
    str2 = input()
    if str1 in str2:
        result = 1
    else:
        result = 0
    print(f'#{tc+1} {result}')
