# [BOJ] 16929. Two Dots
# 풀이 시간: 15 분
# 실행 시간: 68 ms
# 메모리: 31300 KB


def in_range(y, x):
    return 0 <= y < N and 0 <= x < M


def dfs(y, x, cnt):
    global is_cycle
    if is_cycle:
        return
    
    for d in range(4):
        ny, nx = y + dy[d], x + dx[d]
        if ny == i and nx == j and cnt >= 4:
            is_cycle = True
            return
        if in_range(ny, nx) and not visited[ny][nx] and board[ny][nx] == board[y][x]:
            visited[ny][nx] = True
            dfs(ny, nx, cnt + 1)


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
is_cycle = False

for i in range(N):
    for j in range(M):
        if not is_cycle:
            visited = [[False] * M for _ in range(N)]
            visited[i][j] = True
            dfs(i, j, 1)
        else:
            break
    if is_cycle:
        break

print("Yes" if is_cycle else "No")