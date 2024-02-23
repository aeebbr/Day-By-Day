# [BOJ] 1104. 동전 0  
# 풀이 시간 : 20분 

import sys
input = sys.stdin.readline

answer = 0
N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

coins.sort(reverse=True)
# 남은 액수가 0이 될 때까지 
while K != 0:
    # 동전 중에서 나눌 수 있는 가장 큰 수 찾기 
    for c in coins:
        tmp = K // c
        if tmp > 0:
            # 동전 찾음
            answer += tmp
            # 남은 액수 갱신 
            K = K % c  
            
            break
    
print(answer)