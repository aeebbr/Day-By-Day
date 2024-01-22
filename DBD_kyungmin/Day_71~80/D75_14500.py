# [BOJ] 14500. 테트로미노    
# 풀이 시간 : 30 분 

import sys
input = sys.stdin.readline

# 모든 모양의 경우(회전, 대칭 포함)
dr = [[0, 0, 0], [1, 1, 1], [0, 1, 0], [1, 1, 0], [0, 0, 1], [0, 1, 1], [1, 0, 0], [1, 0, 1], [0, -1, 0], [0, 0, 1], [0, -1, 2], [0, 0, -1], [1, 0, 1], [0, 1, 1], [1, 0, 0], [0, -1, -1], [0, 0, 1], [-1, 0, -1], [0, 1, 0]]
dc = [[1, 1, 1], [0, 0, 0], [1, 0, -1], [0, 0, 1], [1, 1, -2], [1, 0, 0], [0, -1, -1], [0, 1, 0], [1, 0, 1], [1, 1, -1], [1, 0, 0], [1, 1, -1], [0, 1, -1], [1, -1, 0], [0, 1, 1], [1, 0, 0], [1, 1, 0], [0, 1, 0], [1, 0, 1]]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0
max_r = []
max_c = []

for i in range(N):
    for j in range(M):
        for k in range(len(dr)):
            cr, cc = i, j
            total  = board[cr][cc]

            for dir in range(3):
                nr = cr + dr[k][dir]
                nc = cc + dc[k][dir]

                if 0 <= nr < N and 0 <= nc < M:
                    total += board[nr][nc]
                    cr, cc = nr, nc
                else:
                    break
            # 모양 완성
            else:
                answer = max(answer, total)

print(answer)
