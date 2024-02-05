T = int(input())
for tc in range(T):
    word = input()
    if word == word[::-1]:
        result = 1
    else:
        result = 0
    print(f'#{tc+1} {result}')