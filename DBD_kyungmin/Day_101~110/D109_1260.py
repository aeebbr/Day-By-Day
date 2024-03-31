# [BOJ] 1260. DFS와 BFS
# 풀이 시간 : 15 분 

import sys
input = sys.stdin.readline
from collections import deque

def dfs(cur):
    global visited
    print(cur, end=" ")

    for i in range(1, len(linked_list[cur])):
        next = linked_list[cur][i]
        if not visited[next]:
            visited[next] = True
            dfs(next)

def bfs(start, visited):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        cur = q.popleft()
        print(cur, end=" ")

        for i in range(1, len(linked_list[cur])): 
            next = linked_list[cur][i]
            if not visited[next]:
                q.append(next)
                visited[next] = True

N, M, V = map(int, input().split())
linked_list = [[0] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    linked_list[a].append(b)
    linked_list[b].append(a)

# 정렬 
for i in range(1, len(linked_list)):
    linked_list[i].sort()

visited = [False] * (N+1)
visited[V] = True
dfs(V)
print()

visited = [False] * (N+1)
bfs(V, visited)
