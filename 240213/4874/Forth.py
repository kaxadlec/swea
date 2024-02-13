T = int(input())
for tc in range(T):
    result = 0
    formula = input().split()
    stack = []

    for token in formula:
        try:
            if token not in '+-*/.':
                stack.append(token)

            elif token in '+-*/':
                operand1 = int(stack.pop())
                operand2 = int(stack.pop())
                if token == '+':
                    stack.append(operand2+operand1)
                elif token == '-':
                    stack.append(operand2-operand1)
                elif token == '*':
                    stack.append(operand2*operand1)
                elif token == '/':
                    stack.append(operand2//operand1)

            elif token == '.':
                if len(stack) == 1:
                    result = stack.pop()
                else:
                    result = 'error'

        except IndexError:
            result = 'error'

    print(f'#{tc+1} {result}')
