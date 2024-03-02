# [BOJ] 10816. 숫자 카드 2   
# 풀이 시간 : 18 분 

import sys
input = sys.stdin.readline

def binary_search(target):
    start, end = 0, N-1
    while start <= end:
        mid = (start + end) // 2

        if Ns[mid] < target:
            start = mid + 1
        elif Ns[mid] > target:
            end = mid - 1
        else:
            return dic[target]
        
    return 0

N = int(input())
Ns = sorted(list(map(int, input().split())))
M = int(input())
Ms = list(map(int, input().split()))

dic = {}
for n in Ns:
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1

for m in Ms:
    print(binary_search(m), end=" ")
