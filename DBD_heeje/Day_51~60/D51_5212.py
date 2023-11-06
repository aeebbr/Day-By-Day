# [BOJ] 5212. 지구 온난화
# 소요 시간 : 30 분

import sys
input = sys.stdin.readline

def is_sinked(y, x):
    ground = 0
    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if 0 <= ny < R and 0 <= nx < C and matrix[ny][nx] == "X":
            ground += 1
    
    return ground <= 1

R, C = map(int, input().split())
matrix = [input() for _ in range(R)]
copied_matrix = []
min_y, max_y, min_x, max_x = R, 0, C, 0
direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

for i in range(R):
    row = ""
    for j in range(C):
        if matrix[i][j] == "X":
            if is_sinked(i, j):
                row += "."
            else:
                min_y = min(min_y, i)
                max_y = max(max_y, i)
                min_x = min(min_x, j)
                max_x = max(max_x, j)
                row += "X"
        else:
            row += "."
    copied_matrix.append(row)

for i in range(min_y, max_y + 1):
    print(copied_matrix[i][min_x : max_x + 1])