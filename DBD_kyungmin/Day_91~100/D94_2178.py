# [BOJ] 2178. 미로 탐색
# 풀이 시간 : 08 분 

from collections import deque

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(sr, sc):
    q = deque()
    visited = [[False] * M for _ in range(N)]
    q.append((sr, sc, 1))
    visited[sr][sc] = True

    while q:
        cr, cc, cnt = q.popleft()

        if (cr+1, cc+1) == (N, M):
            return cnt
        
        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if board[nr][nc] == 1:
                    q.append((nr, nc, cnt + 1))
                    visited[nr][nc] = True

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]

print(bfs(0, 0))