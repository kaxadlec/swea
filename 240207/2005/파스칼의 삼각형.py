def pascal_tri(triangle, size, cnt):
    if size == 1:
        triangle.append([1])
        return triangle
    elif size == 2:
        triangle.append([1])
        triangle.append([1, 1])
        return triangle
    else:
        if cnt == 0:
            triangle.extend([[1], [1, 1], []])
        else:
            triangle.append([])
        N = cnt + 3
        stack = []
        print('작업 전 트라이앵글', triangle)
        stack.extend(triangle[N-2])
        print('스택', stack)
        for k in range(N):
            print()
            try:
                pre = stack.pop()
                print('pre', pre)
                if len(triangle[N - 1]) == N - 1:
                    triangle[N - 1].append(pre)
                    print('트라이앵글 끝', triangle)
                    print('cnt', cnt)
                    if len(triangle) == size:
                        return triangle
                    else:
                        cnt += 1
                        pascal_tri(triangle, size, cnt)

                elif not triangle[N - 1]:
                    print('비었다')
                    triangle[N - 1].append(pre)
                    print('트라이앵글 스타트', triangle)
                    stack.append(pre)

                elif triangle[N-1]:
                    print('안비었다')
                    now = stack.pop()
                    triangle[N - 1].append(pre + now)
                    print('트라이앵글 2', triangle)
                    stack.append(now)
            except IndexError:
                pass
                # if len(triangle) == size:
                #     return triangle
                # else:
                #     triangle.append([])
                #     print('파스칼 완성', triangle)
                #





T = int(input())
for tc in range(T):
    size = int(input())    # 삼각형의 크기
    # triangle = [[] for _ in range(size)]
    triangle = []
    cnt = 0
    print(f'-------------------------------{size}')
    new_triangle = pascal_tri(triangle, size, cnt)

    print(f'#{tc+1}')
    print(triangle)
    # for i in range(len(triangle)):
    #     print(*triangle[i])