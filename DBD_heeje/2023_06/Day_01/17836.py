# [BOJ] 17836. 공주님을 구해라!
# 실행 시간: 80 ms
# 메모리: 34176 KB

# bfs로 matrix 순환
# 1. 만약, 그람을 만났다면, 현재 이동 시간 + 그 위치에서부터 (N, M)까지의 최단 시간을 따로 저장
# 2. bfs는 계속 진행, (N, M)에 닿을 시 해당 시간을 함께 저장
# min(1번 소요 시간, 2번 소요 시간)

import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    queue = deque()
    queue.append(start)
    walk_to_goal = 0
    gram_to_goal = T + 1

    while queue and walk_to_goal < T:
        walk_to_goal += 1

        for _ in range(len(queue)):
            y, x = queue.popleft()

            for d in range(4):
                move_y, move_x = y + dy[d], x + dx[d]
                if 0 <= move_y < N and 0 <= move_x < M and not visited[move_y][move_x]:

                    # 걸어서 도착한 경우
                    if move_y == N - 1 and move_x == M - 1:
                        return min(walk_to_goal, gram_to_goal)
                    if matrix[move_y][move_x] == 2:
                        matrix[move_y][move_x] = 0
                        gram_to_goal = (
                            walk_to_goal + (N - 1) - move_y + (M - 1) - move_x
                        )
                    if matrix[move_y][move_x] == 0:
                        visited[move_y][move_x] = True
                        queue.append((move_y, move_x))

    # 걷기 & 그람 줍기로도 최단 시간에 도착하지 못했을 경우
    if gram_to_goal > T:
        return "Fail"

    # 그람을 주웠을 때 도착 가능한 경우
    else:
        return gram_to_goal


dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

N, M, T = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

print(bfs((0, 0)))
