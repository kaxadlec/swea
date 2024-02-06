T = 10
for tc in range(T):
    pln_len = int(input())  # 찾아야 하는 회문의 길이
    box = [(input()) for _ in range(8)] # 글자판
    cnt = 0
    for i in range(8):  # 글자판 행은 8개
        row_word = box[i]   # 글자판 행 하나
        for j in range(8-pln_len+1):    # 행 하나에서 회문 체크
            if j-1 == -1:   # 역순으로 문자 슬라이싱 할 때 문제가 생기는 것을 해결하는 조건
                if row_word[j:(j + pln_len)] == row_word[(j + pln_len - 1)::-1]:
                    cnt += 1
            if row_word[j:(j+pln_len)] == row_word[(j+pln_len-1):j-1:-1]:   # 회문이면
                cnt += 1    # 카운트

    col_box = list(zip(*box))   # 글자판 열을 기준으로 바라보기
    for j in range(8):
        col_word = col_box[j]   # 글자판 열 하나
        for i in range(8-pln_len+1):
            if i-1 == -1:
                if col_word[i:(i + pln_len)] == col_word[(i + pln_len - 1)::-1]:
                    cnt += 1
            if col_word[i:(i+pln_len)] == col_word[(i+pln_len-1):i-1:-1]:
                cnt += 1

    print(f'#{tc+1} {cnt}')

