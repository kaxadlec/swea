def pascal_tri(triangle, size, cnt):
    if size == 1:
        triangle.append([1])
        return triangle
    elif size == 2:
        triangle.append([1])
        triangle.append([1, 1])
        return triangle
    else:   # 삼각형 크기 3 이상
        if cnt == 0:    # 처음 함수 호출이면
            triangle.extend([[1], [1, 1], []])
        else:           # 재귀 호출이면
            triangle.append([])
        N = cnt + 3
        stack = []
        stack.extend(triangle[N-2])
        for k in range(N):
            pre = stack.pop()
            if len(triangle[N - 1]) == N - 1:
                triangle[N - 1].append(pre)
                if len(triangle) == size:
                    return
                else:
                    cnt += 1
                    pascal_tri(triangle, size, cnt)

            elif not triangle[N - 1]:
                triangle[N - 1].append(pre)
                stack.append(pre)

            elif triangle[N-1]:
                now = stack.pop()
                triangle[N - 1].append(pre + now)
                stack.append(now)


T = int(input())
for tc in range(T):
    size = int(input())    # 삼각형의 크기
    triangle = []
    cnt = 0
    new_triangle = pascal_tri(triangle, size, cnt)
    print(f'#{tc+1}')
    for i in range(len(triangle)):
        print(*triangle[i])