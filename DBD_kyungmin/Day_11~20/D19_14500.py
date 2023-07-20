# [BOJ] 14500. 테트로미노
# 풀이 시간: 00 분
# 실행 시간: 180 ms
# 메모리: 38004 KB

# 완탐: 모든 종류의 테트로미노인 경우를 다 따지기 

import sys

input = sys.stdin.readline

# 우 하 좌 상
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# idx: 현재까지의 블럭 개수, total: 누적합
def dfs(r, c, idx, total):
    global ans

    # 종료 조건
    if ans >= total + max_val * (3 - idx):
        return
    if idx == 3:
        ans = max(ans, total)
        return
    
    # 사방탐색 
    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]

        if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
            # 블럭 두 개째라면 
            if idx == 1:
                visit[nr][nc] = 1
                # 현재 위치에서 다시 탐색
                dfs(r, c, idx + 1, total + arr[nr][nc])
                visit[nr][nc] = 0

            visit[nr][nc] = 1
            # 다음 위치로 넘어가기 
            dfs(nr, nc, idx + 1, total + arr[nr][nc])
            visit[nr][nc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [([0] * M) for _ in range(N)]

ans = 0
max_val = max(map(max, arr))

# 모든 위치를 탐색 
for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs(r, c, 0, arr[r][c])
        visit[r][c] = 0

print(ans)