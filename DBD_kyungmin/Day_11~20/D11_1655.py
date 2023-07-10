# [BOJ] 1655. 가운데를 말해요
# 풀이 시간: 90++ 분
# 실행 시간: 236 ms
# 메모리: 37268 KB
# 모르겠으면 검색해보고 이해해주세요!

import heapq
import sys

input = sys.stdin.readline

n = int(input())
left_heap = []
right_heap = []

for _ in range(n):
    x = int(input())
    
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -x)
    
    else:
        heapq.heappush(right_heap, x)
        
    if left_heap and right_heap and left_heap[0] * -1 > right_heap[0]:
        max_value = heapq.heappop(left_heap)
        min_value = heapq.heappop(right_heap)
        
        heapq.heappush(left_heap, min_value * -1)
        heapq.heappush(right_heap, max_value * -1)

    print(left_heap[0] * -1)