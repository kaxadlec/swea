# 1231. 중위순회
def inorder(node):
    # 왼쪽 자식노드
    if len(tree[node]) >= 2:
        inorder(tree[node][1])
    # 현재노드
    print(tree[node][0], end='')
    # 오른쪽 자식노드
    if len(tree[node]) >= 3:
        inorder(tree[node][2])


T = 10
for tc in range(T):
    N = int(input())  # 정점의 총 개수 = node 마지막 번호
    tree = [0] * (N + 1)
    for i in range(N):
        # node 번호 / node 문자 / left child 번호 / right child 번호
        arr = input().split()
        if len(arr) >= 3:
            arr[2] = int(arr[2])
        if len(arr) >= 4:
            arr[3] = int(arr[3])
        tree[i+1] = arr[1:4]

    # 완성된 트리 구조
    # 트리의 인덱스가 본인 노드 번호
    # tree = [node 문자, left child 번호, right child 번호], ...
    # 트리의 요소 중 left child 번호 or right child 번호가 없는 요소도 존재
    print(f'#{tc + 1}', end=' ')
    # print(tree)
    inorder(1)
    print()

