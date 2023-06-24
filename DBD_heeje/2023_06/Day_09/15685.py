# [BOJ] 15685. 드래곤 커브
# 풀이 시간: 30 분
# 실행 시간: 52 ms
# 메모리: 31256 KB

import sys
input = sys.stdin.readline

#우하좌상(0123)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

N = int(input())
matrix = [[0] * 101 for _ in range(101)]
generation = [[0]]
count = 0

for _ in range(N):
    x, y, d, g = map(int, input().split())
    while g >= len(generation):
        generation.append(generation[-1] + list(map(lambda x: (x - 1) % 4, generation[-1][::-1])))

    matrix[y][x] = 1
    for curve_dir in generation[g]:
        y, x = y + dy[curve_dir - d], x + dx[curve_dir - d]
        matrix[y][x] = 1

for i in range(100):
    for j in range(100):
        if sum(matrix[i][j:j + 2]) + sum(matrix[i + 1][j:j + 2]) == 4:
            count += 1

print(count)