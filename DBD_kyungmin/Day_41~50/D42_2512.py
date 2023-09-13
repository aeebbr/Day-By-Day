# [BOJ] 2512. 예산
# 풀이 시간 : 30 분

import sys 
input = sys.stdin.readline

N = int(input())
list = list(map(int, input().split()))
M = int(input())

max_budget = 0
mid_budget = M // N

# 현재 턴의 상한액
for i in range(mid_budget, 100000+1):
    total = 0
    # 이번 턴의 최대 배정 예산 
    this_max = 0
    # 요청 예산 
    for j in list:
        if j > i:
            this_max = max(this_max, i)
            total += i
        else:
            this_max = max(this_max, j)
            total += j

    if total > M:
        # print(i)
        break
    else:
        max_budget = max(max_budget, this_max)
    
print(max_budget)