# [BOJ] 2217. 로프  
# 풀이 시간 : 15 분 

import sys
input = sys.stdin.readline

answer = 0
N = int(input())
ropes = []
for _ in range(N):
    ropes.append(int(input()))
ropes.sort()

for i in range(N):
    cur = ropes[i]
    k = N - i
    tmp = cur * k 

    if answer < tmp:
        answer = tmp

print(answer)

# 3
# 13
# 10
# 15

# 3
# 13
# 2
# 15

