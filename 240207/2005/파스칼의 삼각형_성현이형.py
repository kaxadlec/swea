def pascal_triangle(height):
    if height == 1:
        stack = [1]
    else:
        stack = [1]
        before_triangle = pascal_triangle(height - 1)
        for i in range(len(before_triangle) - 1):
            stack.append(before_triangle[i] + before_triangle[i + 1])
        stack.append(1)
    print(*stack)
    return stack


for t in range(1, int(input()) + 1):
    print(f'#{t}')
    N = int(input())
    pascal_triangle(N)