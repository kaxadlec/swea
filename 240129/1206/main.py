
T = 10

for t in range(T):
     N = int(input())
<<<<<<< HEAD
     height = list(map(int, input().split()))
     result = []
     res_sum = 0
     for i in range(2, N-2):
         around_max = 0
         cnt = 0
         around_list = []
         for j in range(i-2, i+3):
             if height[i] > height[j]:
                cnt = cnt + 1
                around_list.append(height[j])
         if cnt == 4:
             around_max = max(around_list)
             res = height[i] - around_max
             res_sum += res

     print(f'#{t+1} {res_sum}')
=======
     arr = list(map(int, input().split()))

     result =[]
     for i in range(N-2):
         num_list= []
         for j in range(i-2, i+3):
             if arr[i] > arr[j]:
                 num_list.append(arr[i] - arr[j])
                 result.append(max(num_list))

     print(result)
>>>>>>> d5f810ed41e6df6ac27e9be7c61cccb983049d9c
