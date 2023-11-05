# [BOJ] 17471. 게리맨더링
# 소요 시간 : 00 분 10:51

from collections import deque
import sys
input = sys.stdin.readline

def is_connected(section):
    queue = deque()
    queue.append(section[0])
    v = set(section)
    v.remove(section[0])
    
    while queue:
        s = queue.popleft()

        for w in adj_list[s]:
            if w in v:
                v.remove(w)
                queue.append(w)
    
    return len(v) == 0


N = int(input())
population = list(map(int, input().split()))
adj_list = [[] for _ in range(N + 1)]
visited = set()

for i in range(1, N + 1):
    infos = list(map(int, input().split()))
    adj_list[i].extend(infos[1:])

for i in range(2 ** N):
    if i in visited: continue
    visited.add(i)
    visited.add(2 ** N - 1 - i)
    A, B = [], []
    for j in range(N):
        if (i & (1 << j)):
            A.append(j + 1)
        else:
            B.append(j + 1)
    
    if is_connected(A) and is_connected(B):
