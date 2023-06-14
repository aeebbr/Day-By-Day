# [BOJ] 17141. 연구소 2
# 풀이 시간: 30 분
# 실행 시간: 264 ms(PyPy3)
# 메모리: 117332 KB

import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline


def bfs(virus_list, blank):
    queue = deque(virus_list)

    while queue:
        y, x = queue.popleft()
        for d in range(4):
            move_y, move_x = y + dy[d], x + dx[d]
            if (
                0 <= move_y < N
                and 0 <= move_x < N
                and copied_matrix[move_y][move_x] in [0, 2]
            ):
                queue.append((move_y, move_x))
                copied_matrix[move_y][move_x] = copied_matrix[y][x] + 1
                blank -= 1
                if blank == 0:
                    return copied_matrix[move_y][move_x] - 3

    return -1


dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

N, M = map(int, input().split())
matrix = []
virus_list = []
blank = N**2 - M
min_time = 99999999
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 2:
            virus_list.append((i, j))
        if row[j] == 1:
            blank -= 1

    matrix.append(row)

if blank == 0:
    print(0)
else:
    for picked_virus_list in combinations(virus_list, M):
        copied_matrix = []
        for i in range(N):
            copied_matrix.append(matrix[i][:])

        for y, x in picked_virus_list:
            copied_matrix[y][x] = 3

        time = bfs(picked_virus_list, blank)
        if time > -1:
            min_time = min(min_time, time)

    print(-1 if min_time == 99999999 else min_time)
