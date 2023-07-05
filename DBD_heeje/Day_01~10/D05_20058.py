# [BOJ] 20058. 마법사 상어와 파이어스톰
# 풀이 시간: 60 분
# 실행 시간: 744 ms(PyPy3)
# 메모리: 118784 KB

import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def rotate_matrix():
    rotate_x = 0
    while rotate_x < two_power_N:
        rotate_y = 0
        while rotate_y < two_power_N:
            before_rotate = []
            for i in range(two_power_L):
                before_rotate.append(
                    matrix[rotate_x + i][rotate_y : rotate_y + two_power_L]
                )
            after_rotate = [
                [row[i] for row in before_rotate[::-1]]
                for i in range(len(before_rotate[0]))
            ]
            for i in range(two_power_L):
                matrix[rotate_x + i][rotate_y : rotate_y + two_power_L] = after_rotate[
                    i
                ]
            rotate_y += two_power_L
        rotate_x += two_power_L


def reduce_ice_amount():
    reduce_ice_amount_list = []
    for x in range(two_power_N):
        for y in range(two_power_N):
            if matrix[x][y] != 0:
                cnt = 0
                for d in range(4):
                    move_x, move_y = x + dx[d], y + dy[d]
                    if (
                        0 <= move_x < two_power_N
                        and 0 <= move_y < two_power_N
                        and matrix[move_x][move_y] != 0
                    ):
                        cnt += 1
                else:
                    if cnt < 3:
                        reduce_ice_amount_list.append((x, y))

    for reduce_x, reduce_y in reduce_ice_amount_list:
        matrix[reduce_x][reduce_y] -= 1


def get_total_ice():
    return sum([sum(matrix[i]) for i in range(two_power_N)])


def get_cnt_of_biggest_ice_area():
    max_cnt = 0
    visited = [[False] * two_power_N for _ in range(two_power_N)]
    for x in range(two_power_N):
        for y in range(two_power_N):
            if not visited[x][y] and matrix[x][y] != 0:
                cur_cnt = 1
                visited[x][y] = True
                queue = [(x, y)]
                while queue:
                    cur_x, cur_y = queue.pop(0)
                    for d in range(4):
                        move_x, move_y = cur_x + dx[d], cur_y + dy[d]
                        if (
                            0 <= move_x < two_power_N
                            and 0 <= move_y < two_power_N
                            and not visited[move_x][move_y]
                            and matrix[move_x][move_y] != 0
                        ):
                            cur_cnt += 1
                            visited[move_x][move_y] = True
                            queue.append((move_x, move_y))

                if max_cnt < cur_cnt:
                    max_cnt = cur_cnt
    return max_cnt


N, Q = map(int, input().split())
two_power_N = 2**N
matrix = [list(map(int, input().split())) for _ in range(two_power_N)]
L_list = list(map(int, input().split()))

for L in L_list:
    two_power_L = 2**L
    rotate_matrix()
    reduce_ice_amount()

print(get_total_ice(), get_cnt_of_biggest_ice_area(), sep="\n")
