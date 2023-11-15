# [BOJ] 1743. 음식물 피기  
# 풀이 시간 : 9 분

import sys
input = sys.stdin.readline
from collections import deque

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

max_cnt = 0

def bfs(sr, sc):
    global visited
    global max_cnt
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

    max_cnt = max(max_cnt, cnt)

N, M, K = map(int, input().split())
board = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
start = []

for _ in range(K):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    board[r][c] = 1
    start.append((r, c))

for r, c in start:
    if not visited[r][c]:
        bfs(r, c)

print(max_cnt)