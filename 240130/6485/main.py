T = int(input())    # 테스트케이스 개수

for t in range(T):
    N = int(input())    # 버스 노선 개수
    ab_list =[]
    for n in range(N):
        a, b = map(int, input().split()) # 버스는 번호가 a 이상 b 이하만 다님
        ab_list.append([a,b])

    P = int(input())    # 버스 정류장 개수
    print_list = [0] * P
    c_list = [0] * P
    for p in range(P):
        c_list[p] = int(input())
        for ab in ab_list:
            if ab[0] <= c_list[p] <= ab[1]:
                print_list[p] += 1
    print(f'#{t+1} {" ".join(str(i) for i in print_list)}')

