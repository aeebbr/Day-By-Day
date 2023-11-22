# [BOJ] 1941. 소문난 칠공주  
# 풀이 시간 : 90 분 
from collections import deque

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
answer = 0

board = [list(input()) for _ in range(5)]

def bfs(sel):
    global answer

    sr, sc = sel[0]
    q = deque()
    q.append((sr, sc))
    visited = [[False] * 5 for _ in range(5)]
    visited[sr][sc] = True
    cnt = 1

    while q:
        cr, cc = q.popleft()

        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]

            if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc] and (nr, nc) in sel:
                q.append((nr, nc))
                visited[nr][nc] = True
                cnt += 1

    if cnt == 7:
        answer += 1

def combi(idx, sel, s_cnt):
    if len(sel) == 7:
        if s_cnt >= 4:
            bfs(sel)
        return 

    for i in range(idx, 25):
        r = i // 5
        c = i % 5
        sel.append((r, c))

        if board[r][c] == 'S':
            combi(i + 1, sel, s_cnt + 1)
        else:
            combi(i + 1, sel, s_cnt)

        sel.pop()

# 0~ 25 조합 
combi(0, [], 0)
print(answer)