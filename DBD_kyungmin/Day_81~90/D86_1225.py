# [SWEA] 1225. 암호생성기  
# 풀이 시간 : 10 분 

import sys
sys.stdin = open("input_1225.txt", "r")

from collections import deque

def cycle(q):
    for i in range(1, 6):
        left = q.popleft()
        left -= i
        if left <= 0:
            left = 0
            q.append(left)
            return q, True
        
        q.append(left)
        
    return q, False

for _ in range(10):
    test_num = int(input())
    q = deque()
    data = list(map(int, input().split()))
    for num in data:
        q.append(num)

    while True:
        # 한 사이클 
        q, isStop = cycle(q)
        if isStop:
            break
    print(f"#{test_num} ", end="")
    print(*q)