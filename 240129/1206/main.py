
T = int(input())

for t in range(T):
     N = int(input())
     arr = list(map(int, input().split()))

     result =[]
     for i in range(N-2):
         num_list= []
         for j in range(i-2, i+3):
             if arr[i] > arr[j]:
                 num_list.append(arr[i] - arr[j])
                 result.append(max(num_list))

     print(result)