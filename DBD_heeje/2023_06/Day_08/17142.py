# [BOJ] 17142. 연구소 3
# 풀이 시간: 30 분
# 실행 시간: 248 ms(PyPy3)
# 메모리: 117416 KB

def bfs(virus_case, blank):
    global min_time
    queue = deque(virus_case)

    while queue:
        y, x = queue.popleft()

        if min_time != -1 and copied_matrix[y][x] - 3 >= min_time:
            return

        for d in range(4):
            move_y, move_x = y + dy[d], x + dx[d]
            if 0 <= move_y < N and 0 <= move_x < N and copied_matrix[move_y][move_x] in [0, 2]:
                queue.append((move_y, move_x))
                if copied_matrix[move_y][move_x] == 0:
                    blank -= 1
                    if blank == 0:
                        time = copied_matrix[y][x] - 2
                        if min_time == -1:
                            min_time = time
                        else:
                            min_time = min(min_time, time)
                        return
                    
                copied_matrix[move_y][move_x] = copied_matrix[y][x] + 1

    return


import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

N, M = map(int, input().split())
matrix = []
virus_list = []
blank = N ** 2
min_time = -1
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):

        # 벽일 때
        if row[j] == 1:
            blank -= 1
        
        # 비활성 바이러스일 때
        if row[j] == 2:
            virus_list.append((i, j))
            blank -= 1

    matrix.append(row)

if blank == 0:
    print(0)
else:
    for virus_case in combinations(virus_list, M):

        copied_matrix = []
        for i in range(N):
            copied_matrix.append(matrix[i][:])

        for y, x in virus_case:
            copied_matrix[y][x] = 3

        bfs(virus_case, blank)

    print(min_time)