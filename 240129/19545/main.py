# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
T = int(input()) # 숫자 (int 생략하면 str 상태)
# TypeError: 'int' object is not iterable
print('T', T)
# for t in T: TypeError: 'int' object is not iterable

import math

def solution1(arr, neighbor):
    # 인덱스를 활용하여 특정한 범위의 합들을 연속적으로 구해주고
    # 해당 합들의 크기를 비교하여 최댓값, 최솟값을 구함
    # 값을 비교할 때 max_val, min_val, ... -> max, min 내장함수.
    # max_val = -math.inf
    # max_val = 0  # 최댓값의 초기값 => 가능한 가장 작은값.
    # min_val = math.inf
    # min_val = 10000 * neighbor
    # 첫번째의 값 기준으로 삼기 <-> 첫번째 원소의 값.(X)
    sum_val = sum(arr[0:neighbor])  # 첫 구간의 합
    min_val = max_val = sum_val
    print('min', min_val, 'max', max_val, 'sum', sum_val)
    # for i in range(1, len(arr) - neighbor + 1): # 첫구간의 합을 최대/최소로 써줬을 경우
    for i in range(0, len(arr) - neighbor + 1):
        sum_val = sum(arr[i:i+neighbor])
        min_val = min(min_val, sum_val)  # 삼항연산자, if.
        max_val = max(max_val, sum_val)
        print('i', i, 'min', min_val, 'max', max_val, 'sum', sum_val)
    return max_val - min_val


def solution2(arr, neighbor):
    sum_val = sum(arr[0:neighbor])  # 첫 구간의 합
    min_val = max_val = sum_val
    print('min', min_val, 'max', max_val, 'sum', sum_val)
    for i in range(neighbor, len(arr)):
        sum_val = sum_val - arr[i - neighbor] + arr[i]
        min_val = min(min_val, sum_val)  # 삼항연산자, if.
        max_val = max(max_val, sum_val)
        print('i', i, 'min', min_val, 'max', max_val, 'sum', sum_val)
    return max_val - min_val


for t in range(T):
    # 다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
    # N, M = int(input().split()) # int() argument must be a string
    N, M = map(int, input().split()) # N, M? -> map 언패킹.
    print('N', N, 'M', M)
    # 다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )
    # a = map(int, input().split())  # <map object at ...>
    a = list(map(int, input().split()))
    print(a)
    print(f'#{t+1} {solution1(a, M)}')