def palindrome(N, M, box):
    cnt = 0
    for i in range(N):
        start = 0
        end = M
        while end <= N:
            line = box[i][0]
            word = []
            reverse_word = []
            for j in range(start, end):
                word.append(line[j])
            for j in range(end-1, start-1, -1):
                reverse_word.append(line[j])
            if word == reverse_word:
                cnt += 1
                return word
            start += 1
            end += 1

    if cnt == 0:
        for j in range(N):
            start = 0
            end = M
            while end <= N:
                word = []
                reverse_word = []
                for i in range(start, end):
                    line = box[i][0][j]
                    word.append(line)
                for i in range(end-1, start-1, -1):
                    line = box[i][0][j]
                    reverse_word.append(line)
                if word == reverse_word:
                    return word
                start += 1
                end += 1


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    box = [list(map(str, input().split())) for _ in range(N)]
    word = palindrome(N, M, box)
    result = ''.join(str(i) for i in word)
    print(f'#{tc+1} {result}')

