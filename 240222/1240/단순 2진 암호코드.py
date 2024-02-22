'''
암호코드 8개 숫자
암호코드 (홀수 자리의 합 *3) + (짝수 자리 합) = 10의 배수
'''
def password():
    pass
from collections import deque
T = int(input())
for tc in range(T):
    # N 세로 크기, M 가로크기
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]
    rule = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

    for i in range(N):
        cnt = 0
        queue = deque()
        password_queue = deque()
        stack = deque()
        result = 0
        for j in range(M):
            queue.append(board[i][j])
            str_queue = ''.join(queue)
            print(str_queue)
            check = 0
            if len(queue) == 7:
                if str_queue[6] == '0':
                    queue.popleft()
                    continue

                for idx in range(10):
                    if str_queue == rule[idx]:
                        print('idx str_queue', idx, str_queue)
                        stack.append(queue)
                        password_queue.append(idx)
                        queue.clear()
                        check = 1
                    else:
                        stack.pop()
                        
                if not check:
                    queue.popleft()

            if len(password_queue) == 8:
                print(password_queue)
                odd, even = 0, 0
                for k in range(8):
                    if k % 2 == 0:
                        odd += password_queue[k]
                    else:
                        even += password_queue[k]
                temp_result = (odd*3) + even
                print('password_queue temp_result', password_queue, temp_result)
                if temp_result % 10 == 0:
                    result = odd+even
                    break
                else:
                    password_queue.popleft()
        if result != 0:
            break

    print(f'#{tc + 1} {result}')
    # print(N, M)