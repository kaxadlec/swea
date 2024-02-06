T = int(input())
for tc in range(T):
    A, B = input().split()
    cnt = 0
    word_list = []
    for s in A:
        word_list.append(s)
        word = ''.join(str(i) for i in word_list)
        if B in word:
            word_list = []
            cnt -= (len(B)-1)
        cnt += 1

    print(f'#{tc+1} {cnt}')