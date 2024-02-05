# [BOJ] 15683. 감시 
# 풀이 시간 : 86 분 

import sys
input = sys.stdin.readline
import copy

answer = float("inf")
# cctv별 방향
dr = [
    [], 
    # 1번: 우 / 하 / 좌 / 상 
    [[0], [1], [0], [-1]], 
    # 2번: 상하 / 좌우
    [[-1, 1], [0, 0]], 
    # 3번: 상우 / 우하 / 좌하 / 좌상
    [[-1, 0], [0, 1], [0, 1], [0, -1]], 
    # 4번: 좌상우 / 상우하 / 좌하우 / 하좌상
    [[0, -1, 0], [-1, 0, 1], [0, 1, 0], [1, 0, -1]], 
    # 5번: 우하좌상
    [[0, 1, 0, -1]]
]
dc = [
    [], 
    # 1번: 우 / 하 / 좌 / 상 
    [[1], [0], [-1], [0]], 
    # 2번: 상하 / 좌우
    [[0, 0], [-1, 1]], 
    # 3번: 상우 / 우하 / 좌하 / 좌상
    [[0, 1], [1, 0], [-1, 0], [-1, 0]], 
    # 4번: 좌상우 / 상우하 / 좌하우 / 하좌상
    [[-1, 0, 1], [0, 1, 0], [-1, 0, 1], [0, -1, 0]], 
    # 5번: 우하좌상
    [[1, 0, -1, 0]]
]

def cnt_blind(directions):
    global answer
    blind_size = total_size - len(cctv_type) # 사각지대 영역 카운트 
    copy_board = copy.deepcopy(board)

    for i in range(len(directions)):
        # 현재 씨씨티비 넘버 
        cur = cctv_type[i] 
        # 현재 씨씨티비에 주어진 방향
        dir = directions[i]
        cr, cc = cctv_position[i]

        # 현재 방향으로 퍼지기 
        for d in range(len(dr[cur][dir])):
            nr, nc = cr, cc
            while True:
                nr += dr[cur][dir][d]
                nc += dc[cur][dir][d]

                # 조건
                if 0 <= nr < N and 0 <= nc < M and board[nr][nc] != 6:
                    # 중복 방문이 아니고, 씨씨티비를 관통하는 게 아니라면 카운트 감소 
                    if copy_board[nr][nc] == 0:
                        blind_size -= 1
                        copy_board[nr][nc] = -1
                else:
                    break

    # 사각지대 최소 크기 갱신
    answer = min(answer, blind_size)

# idx: 현재 cctv, directinos: cctv 순서대로 각 방향
def dfs(idx, directions):
    # 기저 조건
    # 모든 씨씨티비 방향 결정했다면
    if len(directions) == len(cctv_type):
        cnt_blind(directions)
        return 

    # 씨씨티비 종류 
    for i in range(idx, len(cctv_type)):
        cur = cctv_type[i]

        # 현재 씨씨티비의 방향
        for j in range(len(dr[cur])):
            directions.append(j)
            # 다음 씨씨티비로 
            dfs(i+1, directions)
            directions.pop()

N, M = map(int, input().split())
board = []
cctv_position = []
cctv_type = []
total_size = N * M

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(M):
        if row[j] != 0 and row[j] != 6:
            cctv_position.append((i, j))
            cctv_type.append(row[j])
        elif row[j] == 6:
            total_size -= 1

dfs(0, [])
print(answer)
