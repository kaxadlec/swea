T = int(input())
for tc in range(T):
    N, K = map(int, input().split())    # N은 퍼즐의 가로, 세로 길이
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        word_cnt = 0
        for j in range(N):
            if puzzle[i][j] == 0:
                if word_cnt == K:
                    cnt += 1
                word_cnt = 0

            elif puzzle[i][j] == 1:
                word_cnt += 1

        if word_cnt == K:
            cnt += 1

    for j in range(N):
        word_cnt = 0
        for i in range(N):
            if puzzle[i][j] == 0:
                if word_cnt == K:
                    cnt += 1
                word_cnt = 0

            elif puzzle[i][j] == 1:
                word_cnt += 1

        if word_cnt == K:
            cnt += 1

    print(cnt)

