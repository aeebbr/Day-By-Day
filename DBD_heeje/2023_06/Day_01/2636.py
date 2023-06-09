# [BOJ] 2636. 치즈
# 풀이 시간: 20 분
# 실행 시간: 84 ms
# 메모리: 31256 KB

import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def outside_bfs(start):
    copy_matrix[start[0]][start[1]] = 2
    queue = [start]
    while queue:
        x, y = queue.pop(0)
        for d in range(4):
            move_x, move_y = x + dx[d], y + dy[d]
            if 0 <= move_x < N and 0 <= move_y < M and copy_matrix[move_x][move_y] == 0:
                copy_matrix[move_x][move_y] = 2
                queue.append((move_x, move_y))


N, M = map(int, input().split())
matrix = []
cnt_cheese = 0
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if row[j] == 1:
            cnt_cheese += 1
    matrix.append(row)
time = 0
while cnt_cheese > 0:
    pre_cnt_cheese = cnt_cheese
    time += 1
    copy_matrix = []
    for i in range(N):
        copy_matrix.append(matrix[i][:])
    outside_bfs((0, 0))
    for i in range(N):
        for j in range(M):
            if copy_matrix[i][j] == 1:
                cnt = 0
                for d in range(4):
                    move_i, move_j = i + dx[d], j + dy[d]
                    if (
                        0 <= move_i < N
                        and 0 <= move_j < M
                        and copy_matrix[move_i][move_j] == 2
                    ):
                        # cnt += 1
                        matrix[i][j] = 0
                        cnt_cheese -= 1
                        break
                # if cnt >= 2:
                #     matrix[i][j] = 0
                #     cnt_cheese -= 1

print(time)
print(pre_cnt_cheese)
