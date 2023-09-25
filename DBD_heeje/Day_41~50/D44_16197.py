# [BOJ] 16197. 두 동전
# 풀이 시간 : 00 분

import sys
from collections import deque
input = sys.stdin.readline


def validate(y, x):
    if 0 <= y < N and 0 <= x < M:
        return 0
    return 1


def bfs():
    visited = set()
    visited.add((coins[0], coins[1]))
    queue = deque()
    queue.append((coins[0], coins[1], 0))

    while queue:
        coin1, coin2, cnt = queue.popleft()

        if cnt == 10:
            return -1

        for dy, dx in direction:
            ny1, nx1 = coin1[0] + dy, coin1[1] + dx
            ny2, nx2 = coin2[0] + dy, coin2[1] + dx

            chk = validate(ny1, nx1) + validate(ny2, nx2)
            if chk == 1:
                return cnt + 1
            elif chk == 0:
                if matrix[ny1][nx1] == "#":
                    ny1, nx1 = coin1[0], coin1[1]
                if matrix[ny2][nx2] == "#":
                    ny2, nx2 = coin2[0], coin2[1]

                if ny1 > ny2 or (ny1 == ny2 and nx1 > nx2):
                    ny1, nx1, ny2, nx2 = ny2, nx2, ny1, nx1
                
                if ((ny1, nx1), (ny2, nx2)) in visited: continue
                visited.add(((ny1, nx1), (ny2, nx2)))
                queue.append(((ny1, nx1), (ny2, nx2), cnt + 1))

    return -1

direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

N, M = map(int, input().split())
matrix = []
coins = []

for i in range(N):
    row = input()
    for j in range(M):
        if row[j] == "o":
            coins.append((i, j))

    matrix.append(row)

print(bfs())

