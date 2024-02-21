import heapq

# 빈 힙 생성
heap = []

# 힙에 요소 삽입 (부호를 변경해서 삽입)
heapq.heappush(heap, -1*4)
heapq.heappush(heap, -1*1)
heapq.heappush(heap, -1*7)
heapq.heappush(heap, -1*3)
print("After push:", [-1*i for i in heap])  # 힙에 요소를 삽입한 후 (부호를 원래대로 복원해서 출력)

# 힙에서 요소 삭제 (부호를 변경해서 반환)
print("pop:", -1*heapq.heappop(heap))  # 가장 큰 요소를 삭제하고 반환 (부호를 원래대로 복원해서 출력)
print("After pop:", [-1*i for i in heap])  # 요소를 삭제한 후 (부호를 원래대로 복원해서 출력)

# 리스트를 힙으로 변환 (부호를 변경해서 변환)
list1 = [4, 1, 7, 3, 8, 5]
heapq.heapify(list1)
print("heapify:", [-1*i for i in list1])  # 리스트를 힙으로 변환한 결과 (부호를 원래대로 복원해서 출력)
