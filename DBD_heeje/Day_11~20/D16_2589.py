# [BOJ] 2589. 보물섬
# 풀이 시간: 20 분
# 실행 시간: 924 ms(PyPy3)
# 메모리: 122916 KB

from collections import deque
import sys
input = sys.stdin.readline

def bfs(sy, sx):
    visited = [[0] * M for _ in range(N)]
    visited[sy][sx] = 1
    queue = deque()
    queue.append((sy, sx))
    cnt = 0

    while queue:
        y, x = queue.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == "L" and visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                cnt = max(cnt, visited[ny][nx] - 1)
                queue.append((ny, nx))
    
    return cnt


dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

N, M = map(int, input().split())
board = [input() for _ in range(N)]
max_cnt = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == "L":
            max_cnt = max(max_cnt, bfs(i, j))

print(max_cnt)