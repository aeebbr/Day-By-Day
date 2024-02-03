# [BOJ] 1926. 그림
# 풀이 시간 : 13 분 

import sys
input = sys.stdin.readline
from collections import deque

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

total_cnt = 0
max_size = 0

def bfs(sr, sc):
    global visited
    global max_size

    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = True
    cnt = 1

    while q:
        cr, cc = q.popleft()

        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if board[nr][nc] == 1:
                    q.append((nr, nc))
                    visited[nr][nc] = True
                    cnt += 1

    max_size = max(max_size, cnt)

N, M = map(int, input().split())
board = []
start = []
visited = [[False] * M for _ in range(N)]

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(M):
        if row[j] == 1:
            start.append((i, j))

for sr, sc in start:
    if not visited[sr][sc]:
        total_cnt += 1
        bfs(sr, sc)
    
print(total_cnt)
print(max_size)