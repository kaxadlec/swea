import heapq

# 빈 힙 생성
heap = []

# 힙에 요소 삽입
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print("After push:", heap)  # 힙에 요소를 삽입한 후

# 힙에서 요소 삭제
print("pop:", heapq.heappop(heap))  # 가장 작은 요소를 삭제하고 반환
print("After pop:", heap)  # 요소를 삭제한 후

# 리스트를 힙으로 변환
list1 = [4, 1, 7, 3, 8, 5]
heapq.heapify(list1)
print("heapify:", list1)  # 리스트를 힙으로 변환한 결과
