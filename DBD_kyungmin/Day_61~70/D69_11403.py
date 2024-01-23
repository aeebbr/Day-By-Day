# [BOJ] 11403. 경로 찾기     
# 풀이 시간 : 60 분 

import sys
input = sys.stdin.readline

def dfs(from_edge):
    for to_edge in range(N):
        # 0 -> 4 -> 3 -> 6이라면, 0에서 4, 3, 6을 갈 수 있는 것임  
        if board[from_edge][to_edge] == 1 and visited[to_edge] == 0:
            visited[to_edge] = 1
            dfs(to_edge)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

for start_edge in range(N):
    visited = [0] * N
    dfs(start_edge)
    print(*visited)
