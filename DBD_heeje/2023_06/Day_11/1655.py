# [BOJ] 1655. 가운데를 말해요
# 풀이 시간: 90 분
# 실행 시간: 216 ms
# 메모리: 43476 KB
# 모르겠으면 검색해보고 이해해주세요!

import heapq, sys
input = sys.stdin.readline

N = int(input())
left_heap = []
right_heap = []
answer = []
for i in range(N):
    num = int(input())
    if i % 2:
        heapq.heappush(right_heap, num)
    else:
        heapq.heappush(left_heap, -num)
    
    if right_heap and -left_heap[0] > right_heap[0]:
        max_left_heap = heapq.heappop(left_heap)
        max_right_heap = heapq.heappop(right_heap)

        heapq.heappush(left_heap, -max_right_heap)
        heapq.heappush(right_heap, -max_left_heap)

    answer.append(-left_heap[0])

print(*answer, sep="\n")
    