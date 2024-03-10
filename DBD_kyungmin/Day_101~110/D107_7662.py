# [BOJ] 7662. 이중 우선순위 큐   
# 풀이 시간 : 70 분 

import sys
input = sys.stdin.readline
import heapq

T = int(input())

for _ in range(T):
    K = int(input())
    min_q = [] # 오름차순 정렬
    max_q = [] # 내림차순 정렬 
    visited = [False] * K
    for i in range(K):
        commd, n = input().split()
        n = int(n)
        if commd == 'I':
            heapq.heappush(min_q, (n, i)) # 1, 2, 3, 4, 5
            heapq.heappush(max_q, (-n, i)) # 5, 4, 3, 2, 1
            visited[i] = True
        else:
            if n == 1:
                # 최소힙과 동기화 
                while max_q and not visited[max_q[0][1]]:
                    heapq.heappop(max_q)
                if max_q:
                    max_value = heapq.heappop(max_q)
                    visited[max_value[1]] = False
            else:
                # 최대힙과 동기화 
                while min_q and not visited[min_q[0][1]]:
                    heapq.heappop(min_q)
                if min_q:
                    min_value = heapq.heappop(min_q)
                    visited[min_value[1]] = False

    while min_q and not visited[min_q[0][1]]:
        heapq.heappop(min_q)
    while max_q and not visited[max_q[0][1]]:
        heapq.heappop(max_q)

    if min_q and max_q:
        print(-heapq.heappop(max_q)[0], heapq.heappop(min_q)[0])
    else:
        print("EMPTY")
