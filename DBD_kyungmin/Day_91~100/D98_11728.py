# [BOJ] 11728. 배열 합치기 
# 풀이 시간 : 07 분 

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []

for _ in range(2):
    arr.extend(list(map(int, input().split())))

arr.sort()
print(*arr)
