
T = int(input())

for t in range(T):
     N = int(input())
     arr = list(map(int, input().split()))

     max_i = 0
     for i in range(N-2):
         for j in range(i-2, i+3):
             if arr[i] > arr[j]:
                 result = arr[i] - arr[j]
                 if max_i < result:
                     max_i = result

     print(max_i)