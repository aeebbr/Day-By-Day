# [BOJ] 23352. 방 탈출
# 풀이 시간 : 00 분

# 가장 멀리 떨어진 두 쌍의 최단 경로 
    # 여러 개라면 두 쌍의 합이 큰 값을 출력 

import sys 
input = sys.stdin.readline
from collections import deque

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# (최장경로 카운트, 쌍의 합)
answer = []

def bfs(sr, sc, start):
    q = deque()
    q.append((sr, sc, 1))
    visited = [[0] * M for _ in range(N)]
    visited[sr][sc] = 1

    max_dis = []
    max_cnt = 1
 
    while q:
        cr, cc, cnt = q.popleft()

        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]

            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
            # if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if board[nr][nc] != 0:
                    q.append((nr, nc, cnt + 1))
                    visited[nr][nc] = cnt + 1

                    if max_cnt < cnt:
                        max_cnt = cnt
                        max_dis = [(cnt + 1, start + board[nr][nc])]
                    elif max_cnt == cnt:
                        max_dis.append((cnt + 1, start + board[nr][nc]))

    answer.extend(max_dis)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 모든 지점들에서 시작해서 bfs 탐색, 탐색 결과 가장 멀리 있는 수를 체킹 
for i in range(N):
    for j in range(M):
        if board[i][j] != 0:
            bfs(i, j, board[i][j])

# 1. 최장 경로 카운트 내림차순 
# 2. 쌍의 합 내림차순
answer.sort(key = lambda x:(-x[0], -x[1]))

if len(answer) == 0:
    print(0)
else:
    print(answer[0][1])