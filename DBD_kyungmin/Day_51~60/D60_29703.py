# [BOJ] 29703. 펭귄의 하루 
# 풀이 시간 : 90 분 ++

# E는 이동 불가 
# 1. S -> F 이동 
# 2. F -> H 이동 

# 1 최단 + 2 최단 (X)
# 1 최단에서 시작하는 2 경로가 2의 최단이 아닐 수도 있음 
# 1에서 모든 F로 가는 각각의 최단 경로를 구하고, 
# 2에서는 역으로 가는 각각의 최단 경로를 구하기
# => 그 둘의 모든 조합의 최소 합을 구하기 

from collections import deque

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

min_ans = float("inf")

def bfs(sr, sc, type):
    global start_board, end_board

    q = deque()
    q.append((sr, sc, 0))
    visited = [[False] * M for _ in range(N)]
    visited[sr][sc] = True

    while q:
        cr, cc, cnt = q.popleft()

        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if board[nr][nc] != 'D':
                    q.append((nr, nc, cnt + 1))
                    visited[nr][nc] = True

                    if type == 1:
                        start_board[nr][nc] = cnt + 1
                    elif type == 2:
                        end_board[nr][nc] = cnt + 1

N, M = map(int, input().split())
board = []
sr, sc = 0, 0
er, ec = 0, 0
for r in range(N):
    tmp = list(input())
    if 'S' in tmp:
        c = tmp.index('S')
        sr, sc = r, c
    if 'H' in tmp:
        c = tmp.index('H')
        er, ec = r, c
    board.append(tmp)

start_board = [[0] * M for _ in range(N)]
end_board = [[0] * M for _ in range(N)]

# 1 최단 
bfs(sr, sc, 1)
bfs(er, ec, 2)

# 모든 물고기 지점을 순회하면서 시작 경로와 종료 경로에서 최단으로 갈 수 있는 물고기 지점을 찾기 
for i in range(N):
    for j in range(M):
        if board[i][j] == 'F':
            # 물고기 지점이긴 한데 도달하지 못한 곳이라면(위험 지역으로 가로막혀서)
            if start_board[i][j] == 0 or end_board[i][j] == 0:
                continue
            min_ans = min(min_ans, start_board[i][j] + end_board[i][j])

if min_ans == float("inf"):
    print(-1)
else:
    print(min_ans)
