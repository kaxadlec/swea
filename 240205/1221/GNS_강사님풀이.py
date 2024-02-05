# Direct Address Table
# 배열의 값을 다른 배열의 index로 활용
testcase = int(input())
for tc in range(1, testcase):
    ans = []
    n = list(input().split())   # 이런 식으로 저장됨 -> ['#1', '7041']
    lst = list(input().split())
    num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    # 입력받은 단어 리스트의 길이
    word_cnt = int(n[1])
    bucket = [0]*10
    for i in range(word_cnt):
        for j in range(10):
            if lst[i] == num[j]: # 입력받은 값이 num 배열의 문자와 같다면
                bucket[j] += 1
    for i in range(10):
        if bucket[i] != 0:
            for j in range(bucket[i]):
                ans.append(num[i])

    print(f'#{tc}')
    print(*ans)
