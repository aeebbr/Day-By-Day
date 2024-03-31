# [BOJ] 11286. 절댓값 힙   
# 풀이 시간 : 08 분 

'''
-> 오름차순 
큐: (절대값, 값)
'''

import sys
input = sys.stdin.readline
import heapq

N = int(input())
q = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])
    else:
        heapq.heappush(q, (abs(x), x))