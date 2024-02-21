def preorder(node):
    global cnt
    cnt += 1
    if len(tree[node]) >= 1:
        preorder(tree[node][0])
    if len(tree[node]) >= 2:
        preorder(tree[node][1])
    else:
        return


T = int(input())
for tc in range(T):
    E, N = map(int,input().split())  # 노드 N을 루트로 하는 서브트리
    arr = list(map(int, input().split()))
    tree = [[] for i in range(E+2)]
    for i in range(E):
        tree[arr[2*i]].append(arr[2*i+1])
    cnt = 0
    preorder(N)
    print(f'#{tc+1} {cnt}')
