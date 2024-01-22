# [SWEA] 1226. 미로 1  
# 풀이 시간 : 17 분 

import sys
sys.stdin = open("input_1226.txt", "r")

from collections import deque

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(sr, sc):
    global board

    q = deque()
    q.append((sr, sc))
    # 방문 처리 => 4로 표시 
    board[sr][sc] = 4

    while q:
        cr, cc = q.popleft()
        
        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]

            if 0 <= nr < 16 and 0 <= nc < 16 and board[nr][nc] != 1 and board[nr][nc] != 4:
                if board[nr][nc] == 3:
                    return 1
                q.append((nr, nc))
                board[nr][nc] = 4
    return 0

for _ in range(10):
    test_num = int(input())
    board = []
    sr, sc = 0, 0
    for i in range(16):
        row = list(map(int, input()))
        board.append(row)
        if 2 in row:
            sr = i
            sc = row.index(2)

    print(f"#{test_num} {bfs(sr, sc)}")