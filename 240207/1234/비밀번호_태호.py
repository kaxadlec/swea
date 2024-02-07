for test_case in range(10):
    N, arr = map(str,input().split())
    arr = list(arr) # str으로 받아야 리스트로 만들수잇음
    N = int(N)
    i = 0 # 처음 인덱스는 0
    while i < len(arr)-1: # 인덱스가 어레이 안에있을때만 돌도록
        if arr[i] == arr[i+1]: # 연속된 2개가 같다면
            arr.pop(i + 1) # 큰놈부터 빼주고
            arr.pop(i)  # 작은애 빼주고
            i = 0   # 다시 처음부터 돌기
        else:
            i += 1 # 없다면 인덱스 +1
    print(f'#{test_case+1}',''.join(arr))