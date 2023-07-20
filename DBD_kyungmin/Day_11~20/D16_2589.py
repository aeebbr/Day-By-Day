# [BOJ] 2589. 보물섬
# 풀이 시간:  분
# 실행 시간: 1024 ms
# 메모리: 123576 KB

from collections import deque

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 가장 긴 시간(이 걸리는 최단 거리) 
max_time = 0

def bfs(sr, sc):
    global max_time

    # 큐 초기화 
    q = deque()
    # 방문 배열 초기화 
    visited = [[False] * M for _ in range(N)]

    # 큐에 시작 지점, 시간 삽입
    q.append((sr, sc, 0))
    # 시작 지점 방문 처리 
    visited[sr][sc] = True

    while q:
        cr, cc, time = q.popleft()

        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]

            # 조건: 1) 범위 내, 2) 미방문, 3) 땅
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if board[nr][nc] == 'L':
                    q.append((nr, nc, time + 1))
                    visited[nr][nc] = True

        # 시간 갱신 
        max_time = max(max_time, time)

# 입력
N, M = map(int, input().split())

# 땅 위치 
land = []
board = []

for i in range(N):
    row = list(input())
    board.append(row)
    
    for j in range(M):
        if row[j] == 'L':
            land.append((i, j))

for r, c in land:
    bfs(r, c)

print(max_time)