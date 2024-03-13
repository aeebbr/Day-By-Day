# [BOJ] 1806. 부분합 
# 풀이 시간 : 40 분 

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

total = arr[0]
end = 0
answer = float("inf")
for start in range(N):
    # S 이상이 나올 때까지 end 증가, total 누적 
    while end < N and total < S:
        end += 1
        if end != N:
            total += arr[end]

    # end 범위 out
    if end == N:
        break
    
    # S 이상이 나왔으니 갱신
    total -= arr[start] 
    answer = min(answer, end-start+1)
    # start 1 감소시키러 go

if answer == float("inf"):
    print(0)
else:
    print(answer)


