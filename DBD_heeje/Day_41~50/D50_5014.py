# [BOJ] 5014. 스타트링크
# 소요 시간 : 20 분

import sys
from collections import deque
input = sys.stdin.readline

def bfs(s):
    queue = deque()
    queue.append((s, 0))

    while queue:
        floor, cnt = queue.popleft()

        if floor == G:
            return cnt

        for move in [floor + U, floor - D]:
            if 0 < move <= F and not visited[move]:
                visited[move] = True
                queue.append((move, cnt + 1))
    return "use the stairs"


F, S, G, U, D = map(int, input().split())
visited = [False] * (F + 1)
visited[0] = True
visited[S] = True

print(bfs(S))