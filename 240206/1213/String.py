T = 10
for tc in range(T):
    tc_num = int(input())
    string_find = input()
    sentence_search = input()
    cnt = 0
    for i in range(len(sentence_search)-len(string_find)+1):
        if string_find == sentence_search[i:i+len(string_find)]:
            cnt += 1
    print(f'#{tc+1} {cnt}')