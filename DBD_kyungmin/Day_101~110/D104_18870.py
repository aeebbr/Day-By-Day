# [BOJ] 18870. 좌표 압축  
# 풀이 시간 : 10 분 

import sys
input = sys.stdin.readline

def binary_search(target):
    start, end = 0, len(sort_Xs)-1

    while start <= end:
        mid = (start+end) // 2

        if sort_Xs[mid] < target:
            start = mid + 1
        elif sort_Xs[mid] > target:
            end = mid - 1
        else:
            return mid 
    return 0

N = int(input())
Xs = list(map(int, input().split()))

sort_Xs = sorted(list(set(Xs)))

for x in Xs:
    print(binary_search(x), end=" ")
