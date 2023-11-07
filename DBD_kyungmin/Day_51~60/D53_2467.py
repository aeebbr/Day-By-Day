# [BOJ] 2467. 용액
# 풀이 시간 : 50 분

import sys
input = sys.stdin.readline

total = float("inf")
left_idx = 0
right_idx = 0

N = int(input())
water = list(map(int, input().split()))

for i in range(N-1):
    cur = water[i]

    start = i + 1
    end = N - 1

    while start <= end:
        mid = (start + end) // 2
        # 쌍의 합 
        tmp = cur + water[mid]

        # 0에 더 가깝다면 
        if abs(tmp) < total:
            total = abs(tmp)
            left_idx = i
            right_idx = mid
            
        # 0과 가까워지기 위한 작업 
            # 쌍의 합이 음수라면 합이 커져야 함
            # 쌍의 합이 양수라면 합이 작아저야 함
        if tmp < 0:
            start = mid + 1
        else:
            end = mid - 1

print(water[left_idx], water[right_idx])