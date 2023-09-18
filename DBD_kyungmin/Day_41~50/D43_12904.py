# [BOJ] 12904. A와 B
# 풀이 시간 : 00 분

import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

while len(T):
    s = T[-1]
    del T[-1]
    if s == 'B':
        T = T[::-1]
    if T == S:
        print(1)
        exit()

print(0)
