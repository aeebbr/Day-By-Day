# [SWEA] 1217. 거듭 제곱    
# 풀이 시간 : 03 분 

import sys
sys.stdin = open("input_1217.txt", "r")

def action(num, cnt, N, M):
    if cnt == M:
        return num 
    
    return action(num * N, cnt + 1, N, M)

for _ in range(10):
    test_num = int(input())
    N, M = map(int, input().split())
    print(f"#{test_num} {action(1, 0, N, M)}")