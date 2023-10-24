# [BOJ] 18404. 현명한 나이트
# 풀이 시간: 40 분

# bfs?
import sys
input = sys.stdin.readline
from collections import deque

# 나이트 이동 위치 
dr = [-2, -2, -1, -1, 1, 1, 2, 2]
dc = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs(sr, sc, board):
    q = deque()
    q.append((sr, sc))
    # 방문 처리를 위해서 초기 이동 횟수를 1로 설정하고 시작
    board[sr][sc] = 1

    answer = [0] * len(target)

    while q:
        cr, cc = q.popleft()

        # 모든 말을 다 잡았다면 각 말들에 대한 이동수가 저장되어 있음
        if 0 not in answer:
             return answer

        for dir in range(8):
            nr = cr + dr[dir]
            nc = cc + dc[dir]

            # 미방문: 0
            # 방문한 곳: 양수
            # 타겟: 음수(-1)
            if 0 <= nr < N and 0 <= nc < N and board[nr][nc] <= 0:
                # 타겟이라면 
                if board[nr][nc] == -1:
                    idx = target[(nr+1, nc+1)]
                    # 초기의 이동 횟수를 1에서부터 시작했으니 1 더해주지 않아도 됨
                    answer[idx] = board[cr][cc]
                
                q.append((nr, nc))
                board[nr][nc] = board[cr][cc] + 1

N, M = map(int, input().split())
X, Y = map(int, input().split())

board = [[0] * N for _ in range(N)]
target = {}

for i in range(M):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = -1
    target[(r, c)] = i

answer = bfs(X-1, Y-1, board)
print(*answer)

