from collections import deque

T = int(input())
for tc in range(T):
    # N개의 피자 동시에 구울 수 있음
    # 1번부터 M번까지 M개의 피자 순서대로 넣음
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    pizza = [[i + 1, arr[i]] for i in range(M)]
    queue_ci = deque(pizza)
    queue_firepit = deque()

    # 화덕 N개 자리에 피자 넣을 수 있음
    for _ in range(N):
        queue_firepit.append(queue_ci.popleft())
    # 한바퀴 끝 (넣기만 함)

    result = 0
    while queue_firepit:   # 화덕에 피자 없을때까지
        for k in range(N):
            if len(queue_firepit) == 1:  # 화덕에 피자 하나 남으면
                result = queue_firepit.popleft()[0]  # 화덕에서 피자 빼고 피자번호 결과값에 할당
                break
            else:   # 화덕에 피자 남아있으면
                first_pizza = queue_firepit.popleft()   # 1번위치에서 피자 빼서
                first_cheeze = first_pizza.pop() // 2   # 피자의 치즈 양 반으로 만듬
                first_pizza.append(first_cheeze)

                if first_pizza[1] == 0:     # 만약 1번위치 피자의 치즈가 0 이면
                    if not queue_ci:        # M개의 피자가 다 소진되면
                        pass
                    else:                   # 화덕에 넣을 새로운 피자가 남아있으면
                        queue_firepit.append(queue_ci.popleft())    # 집어 넣음
                else:   # 1번 위치 피자의 치즈가 0이 아니면
                    queue_firepit.append(first_pizza)   # 다시 끝 자리에 피자 넣음

    # 화덕에서 가장 마지막까지 남아있는 피자 번호 출력
    print(f'#{tc + 1} {result}')
