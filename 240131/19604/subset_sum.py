T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    A = [i for i in range(1, 13)]
    A_len = len(A)

    result_sub_set = []
    for i in range(0, 1 << A_len):

        sub_set = []
        sum_sub_set = 0
        for j in range(A_len):
            if i & (1 << j):
                sub_set.append(A[j])
                sum_sub_set += A[j]
                if sum_sub_set == K:
                    if len(sub_set) == N:
                        if sub_set not in result_sub_set:
                            result_sub_set.append(sub_set)

    print(f'#{tc+1} {len(result_sub_set)}')