from collections import deque
T = int(input())
for tc in range(T):
    # N개의 피자 동시에 구울 수 있음
    # 1번부터 M번까지 M개의 피자 순서대로 넣음
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    pizza = [[i+1, arr[i]] for i in range(M)]
    queue_ci = deque(pizza)
    queue_firepit = deque()

    # 화덕 N개 자리에 피자 넣을 수 있음
    for _ in range(N):
        # 1번 위치에서만 넣을 수 있음
        queue_firepit.append(queue_ci.popleft())
        # 한번 넣고 회전시작
        print('#', queue_firepit)

    cnt = 1
    result = 0
    while queue_firepit:
        print(f'{cnt}바퀴 돔')
        print()
        for k in range(N):
            if len(queue_firepit) == 1:
                result = queue_firepit.popleft()[0]
                break
            else:
                first_pizza = queue_firepit.popleft()
                first_cheeze = first_pizza.pop() // 2
                first_pizza.append(first_cheeze)
                print('first_num_pizza', first_pizza)

                if first_pizza[1] == 0:
                    if not queue_ci:
                        pass
                    else:
                        queue_firepit.append(queue_ci.popleft())
                else:
                    queue_firepit.append(first_pizza)
                
            print('화덕', queue_firepit)

        cnt += 1


    # 화덕에서 가장 마지막까지 남아있는 피자 번호
    print(f'#{tc+1} {result}')
