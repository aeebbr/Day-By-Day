# [BOJ] 16197. 두 동전
# 풀이 시간 : 00 분

from collections import deque

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(sr1, sc1, sr2, sc2):
    q = deque()
    q.append((sr1, sc1, sr2, sc2, 0))
    visited = set()
    visited.add((sr1, sc1, sr2, sc2))

    while q:
        cr1, cc1, cr2, cc2, cnt = q.popleft()

        if cnt == 10:
            print(-1)
            return 
        
        for dir in range(4):
            nr1 = cr1 + dr[dir]
            nc1 = cc1 + dc[dir]
            nr2 = cr2 + dr[dir]
            nc2 = cc2 + dc[dir]

            # 범위 검사 
            # 둘 다 범위 내라면 고 
            if 0 <= nr1 < N and 0 <= nc1 < M and 0 <= nr2 < N and 0 <= nc2 < M:
                if board[nr1][nc1] == '#':
                    nr1, nc1 = cr1, cc1
                if board[nr2][nc2] == '#':
                    nr2, nc2 = cr2, cc2

                if (nr1, nc1, nr2, nc2) in visited:
                    continue

                q.append((nr1, nc1, nr2, nc2, cnt+1))

                if nr2 > nr1 or (nr2 == nr1 and nc2 > nc1):
                    visited.add((nr2, nc2, nr1, nc1))
                else:
                    visited.add((nr1, nc1, nr2, nc2))

            # 1만 범위 내 
            elif (0 <= nr1 < N and 0 <= nc1 < M) and (0 > nr2 or nr2 >= N or 0 > nc2 or nc2 >= M):
                print(cnt+1)
                return 

            # 2만 범위 내 
            elif (0 <= nr2 < N and 0 <= nc2 < M) and (0 > nr1 or nr1 >= N or 0 > nc1 or nc1 >= M):
                print(cnt+1)
                return 

    print(-1)
    return 

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
start = []

for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            start.append(i)
            start.append(j)
            if len(start) == 4:
                bfs(start[0], start[1], start[2], start[3])
                exit()
