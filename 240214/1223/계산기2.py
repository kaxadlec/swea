def postfix_notation(formula):  # 후위표기법 표시
    icp = {'+': 1, '*': 2}  # in-coming priority
    isp = {'+': 1, '*': 2}  # in-stack priority
    stack = []      
    postfix = ''    # 후위표기로 된 식
    for token in formula:
        if token in '+*':  # 연산자이면
            if stack:
                if isp[stack[-1]] < icp[token]:  # 스택안의 연산자보다 들어가는 연산자의 우선순위가 높으면
                    stack.append(token)
                elif isp[stack[-1]] >= icp[token]:  # 스택안의 연산자가 들어가는 연산자의 우선순위보다 높으면
                    while stack and isp[stack[-1]] >= icp[token]:   # 계속해서
                        postfix += stack.pop()      # 스택에서 연산자를 빼내서 후위표기식에 표시
                    stack.append(token)             
            elif not stack:
                stack.append(token)

        elif token not in '+*':  # 피연산자이면
            postfix += token

    while stack:
        postfix += stack.pop()

    return postfix  # 최종 후위 표기식 도출


def calculation(postfix_formula):   # 후위표기로 된 식 계산
    stack = []
    for token in postfix_formula:
        if token in '+*':  # 연산자이면
            # 숫자 두개를 꺼내서 계산
            operand1 = int(stack.pop())
            operand2 = int(stack.pop())
            if token == '+':
                stack.append(operand2 + operand1)
            elif token == '*':
                stack.append(operand2 * operand1)
        else:   # 피연산자이면
            stack.append(token)

    return stack.pop()  # 최종계산 값 도출


T = 10
for tc in range(T):
    formula_length = int(input())
    formula = input()
    postfix = postfix_notation(formula)  # 문자열 계산식 후위표기법으로 표시
    result = calculation(postfix)   # 후위표기된 식 계산
    print(f'#{tc + 1} {result}')
