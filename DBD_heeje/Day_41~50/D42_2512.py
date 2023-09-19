# [BOJ] 2512. 예산
# 풀이 시간 : 00 분

import sys
input = sys.stdin.readline

N = int(input())
costs = list(map(int, input().split()))
max_cost = int(input())

start = 1
end = 10 ** 9

if sum(costs) < max_cost:
    print(max(costs))
else:
    while start <= end:
        mid = (start + end) // 2
        total_cost = 0
        for cost in costs:
            total_cost += cost if cost <= mid else mid
        if max_cost == total_cost:
            break
        elif max_cost < total_cost:
            end = mid - 1
        else:
            start = mid + 1

    print(end)