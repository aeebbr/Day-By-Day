# [BOJ] 15662. 톱니바퀴 (2)
# 소요 시간 : 00 분 20:03~

from collections import deque
import sys
input = sys.stdin.readline


def work(idx, d):
    visited[idx] = True
    if 0 <= idx - 1 < T and not visited[idx - 1] and gears[idx][6] != gears[idx - 1][2]:
        work(idx - 1, -d)
    if 0 <= idx + 1 < T and not visited[idx + 1] and gears[idx][2] != gears[idx + 1][6]:
        work(idx + 1, -d)
    
    gears[idx].rotate(d)

T = int(input())
gears = [deque(input().rstrip()) for _ in range(T)]
K = int(input())

for _ in range(K):
    visited = [False] * T
    idx, d = map(int, input().split())
    work(idx - 1, d)

print(sum([int(gear[0]) for gear in gears]))