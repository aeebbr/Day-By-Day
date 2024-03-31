# [BOJ] 11724. 연결 요소의 개수
# 풀이 시간 : 20 분 

import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    global visited
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        cur = q.popleft()

        for i in range(1, len(linked_list[cur])): 
            next = linked_list[cur][i]

            if not visited[next]:
                q.append(next)
                visited[next] = True

answer = 0
N, M = map(int, input().split())
linked_list = [[0] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    linked_list[u].append(v)
    linked_list[v].append(u)

for i in range(1, len(linked_list)):
    if not visited[i]:
        bfs(i)
        answer += 1

print(answer)
