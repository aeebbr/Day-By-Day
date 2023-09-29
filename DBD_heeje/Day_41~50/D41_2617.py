# [BOJ] 2617. 구슬 찾기
# 풀이 시간 : 00 분

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

bigger_list=[[] for _ in range(N + 1)]
smaller_list=[[] for _ in range(N + 1)]
mid = (N + 1) / 2 #개수 기준 중간값

for i in range(M):  #값 입력후 배열
    a, b = map(int, input().split())
    bigger_list[b].append(a)
    smaller_list[a].append(b)

def dfs(arr, start):
    cnt = 0
    visited[start] = True
    stack = deque()
    stack.append(start)
    while stack:
        x = stack.popleft()
        for i in arr[x]:
            if not visited[i]:
                cnt += 1
                visited[i] = True
                stack.append(i)
    return cnt
    
answer = 0

for i in range(1, N+1):
    visited = [False] * (N + 1)

    if dfs(bigger_list,i) >= mid:
        answer += 1

    if dfs(smaller_list,i) >= mid:
        answer += 1

print(answer)