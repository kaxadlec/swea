T = int(input())
for tc in range(T):
    D, A, B, F = map(int, input().split())
    crush_time = D / (A+B)  # 충돌까지 걸리는 시간
    mosquito_distance = crush_time * F

    print(f'#{tc+1} {mosquito_distance}')