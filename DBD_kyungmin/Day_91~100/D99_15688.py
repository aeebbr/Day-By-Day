# [BOJ] 15688. 수 정렬하기 5  
# 풀이 시간 : 05 분 

# 오름차순 정렬

import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()

for i in arr:
    print(i)