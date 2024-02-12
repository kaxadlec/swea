def dp(n):
    if n == 1:  # 1인경우의 개수는 1개
        return 1
    elif n == 2:  # 2인 경우의 개수는 3개
        return 3  # 점화식이 2(n-2) 라고 2개가 아님
    return dp(n - 1) + 2 * (dp(n - 2))


testCase = int(input())
for i in range(testCase):
    n = int(input())
    print('#' + str(i + 1) + ' ' + str(dp(n // 10)))
