def postfix_notation(formula):
    stack = []
    postfix = ''    # 후위표기법
    for token in formula:
        # '+' 연산자이면
        if token == '+':
            stack.append(token)

        # 피연산자이면
        else:
            if not stack:
                postfix += token
            else:
                postfix += token
                postfix += stack.pop()
    return postfix


def calculation(postfix_formula):
    stack = []
    for token in postfix_formula:
        if token == '+':
            operand1 = int(stack.pop())
            operand2 = int(stack.pop())
            stack.append(operand2+operand1)
        else:
            stack.append(token)

    return stack.pop()


T = 10
for tc in range(T):
    formula_length = int(input())
    formula = input()
    result = 0
    postfix = postfix_notation(formula)
    result = calculation(postfix)
    print(f'#{tc+1} {result}')
