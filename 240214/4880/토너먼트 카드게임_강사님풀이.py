T = int(input())


def rsp(idx1, idx2):
    # idx1 < idx2  : 비겼을 때 인덱스가 작은 쪽이 이긴다
    card1 = cards[idx1]
    card2 = cards[idx2]
    # 1: 가위, 2: 바위, 3: 보
    # 큰 인덱스가 이길 수 있는 세 가지 조건
    if card1 == '1' and card2 == '2':
        return idx2
    if card1 == '2' and card2 == '3':
        return idx2
    if card1 == '3' and card2 == '1':
        return idx2
    # 아니면
    return idx1     # 비겨도 idx1이 승자, 당연히 이기면 idx1이 승자


def divide(start, end):
    if start == end:
        return start    # 한 점으로 수렴
    # i ~ (i+j)//2      (i+j)//2+1 ~ j
    mid = (start + end) // 2
    g1 = divide(start, mid)
    g2 = divide(mid+1, end)
    return rsp(g1, g2)

for tc in range(T):
    _ = input()
    cards = input().split()
    print(f'#{tc+1}')
    print(cards)
    answer = divide(0, len(cards) - 1)
    print(answer+1)