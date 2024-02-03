# [BOJ] 1697. 숨바꼭질
# 풀이 시간 : 30 분 

from collections import deque

N, K = map(int, input().split())

def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [False] * (100000 + 1)
    visited[start] = True

    while q:
        cur, cnt = q.popleft()

        if cur == K:
            return cnt

        for next in (cur - 1, cur + 1, cur * 2):
            if 0 <= next < len(visited) and not visited[next]:
                q.append((next, cnt + 1))
                visited[next] = True

print(bfs(N))