# [BOJ] 2493. 탑 
# 풀이 시간 : 30 분

import sys
input = sys.stdin.readline

N = int(input())
tops = list(map(int, input().split()))
stack =[]
answer = [0] * N

# 모든 탑 순회 
for i in range(len(tops)):
    cur = tops[i]
    # 스택 순회 
    while stack:
        top, idx = stack.pop()
        # 비교탑이 더 크면 내 타겟임 
        if top > cur:
            answer[i] = idx
            # 비교 탑 다시 넣기 
            stack.append((top, idx))
            break

    # 나를 넣기 
    stack.append((cur, i+1))

print(*answer)        
