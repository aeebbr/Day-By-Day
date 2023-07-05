# [BOJ] 18428. 감시 피하기
# 풀이 시간: 20 분
# 실행 시간: 60 ms
# 메모리: 31256 KB

import sys
from itertools import combinations
input = sys.stdin.readline



def in_range(y, x):
    return 0 <= y < N and 0 <= x < N


def is_escaped(teachers):
    for t_y, t_x in teachers:
        for d in range(4):
            move_y, move_x = t_y + dy[d], t_x + dx[d]
            while in_range(move_y, move_x):
                if copied_matrix[move_y][move_x] == "S":
                    return False
                elif copied_matrix[move_y][move_x] == "O":
                    break
                move_y += dy[d]
                move_x += dx[d]

    return True

N = int(input())
matrix = []
blanks = []
teachers = []

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

for i in range(N):
    row = input().split()
    for j in range(N):
        if row[j] == "X":
            blanks.append((i, j))
        elif row[j] == "T":
            teachers.append((i, j))
    matrix.append(row)

for obstacles in combinations(blanks, 3):
    copied_matrix = []
    for i in range(N):
        copied_matrix.append(matrix[i][:])
    
    for y, x in obstacles:
        copied_matrix[y][x] = "O"

    if is_escaped(teachers):
        print("YES")
        break

else:
    print("NO")