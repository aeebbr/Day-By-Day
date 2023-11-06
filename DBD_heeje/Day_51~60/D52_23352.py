# [BOJ] 23352. 방탈출
# 소요 시간 : 30 분

import sys
from collections import deque
input = sys.stdin.readline


def bfs(sy, sx):
    queue = deque()
    queue.append((sy, sx))
    visited = [[0] * M for _ in range(N)]
    visited[sy][sx] = 1

    while queue:
        y, x = queue.popleft()

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0 and matrix[ny][nx] != 0:
                visited[ny][nx] = visited[y][x] + 1
                queue.append((ny, nx))

    max_len = 0
    password = 0

    for i in range(N):
        for j in range(M):
            if max_len < visited[i][j]:
                max_len = visited[i][j]
                password = matrix[sy][sx] + matrix[i][j]
            elif max_len == visited[i][j]:
                password = max(matrix[sy][sx] + matrix[i][j], password)
    
    return max_len, password


direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
max_len = 0
answer = 0

for i in range(N):
    for j in range(M):
        if matrix[i][j] != 0:
            len, password = bfs(i, j)
            if max_len < len:
                max_len = len
                answer = password
            elif max_len == len:
                answer = max(answer, password)

print(answer)

