# [BOJ] 1025. 보물  
# 풀이 시간 : 10 분 

import sys
input = sys.stdin.readline

answer = 0

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort(reverse=True)

for i in range(N):
    answer += A[i] * B[i]

print(answer)
