# [BOJ] 7576. 토마토 
# 풀이 시간 : 10 분 

import sys
input = sys.stdin.readline
from collections import deque

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs():
    global q
    global visited 
    total_cnt = 0

    while q:
        cr, cc, cnt = q.popleft()

        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if board[nr][nc] == 0:
                    q.append((nr, nc, cnt + 1))
                    visited[nr][nc] = True
                    total_cnt += 1
    
    if total_cnt == non_tomato:
        return cnt 
    else:
        return -1

M, N = map(int, input().split())
q = deque()
visited = [[False] * M for _ in range(N)]
non_tomato = 0

board = []
for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    non_tomato += row.count(0)
    for j in range(M):
        if row[j] == 1:
            q.append((i, j, 0))
            visited[i][j] = True

print(bfs())
