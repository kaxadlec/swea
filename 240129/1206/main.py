
T = 10

for t in range(T):
     N = int(input())
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
