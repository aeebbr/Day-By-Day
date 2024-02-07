# [BOJ] 18808. 스티커 붙이기 
# 풀이 시간 : 90++ 분 

import sys
input = sys.stdin.readline
from collections import deque

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

answer = 0

def rotate(arr):
    tmp = [] # 회전된 배열 
    # 90도 회전: 열이 행이 됨
    for i in range(c):
        col = []
        for j in range(r-1, -1, -1):
            col.append(arr[j][i])
        tmp.append(col)
    return tmp, c, r

# sticker 시작점 
def get_sticker_start(sticker):
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1:
                return i, j
    return r, c
# board 시작점 
def get_board_start(br, bc):
    if bc >= M-1: # board의 끝 열이라면 다음 행으로 
        bc = 0
        br += 1
    else:
        bc += 1
    return br, bc

def put_sticker(position):
    global board
    for r, c in position:
        board[r][c] = 1

def bfs(sticker, cnt, sr, sc):
    global answer
    board_q = deque()
    sticker_q = deque()
    visited = []
    br, bc = 0, -1 # board 시작점 

    # board의 모든 빈 칸에서부터 탐색 
    while True:
        visited = [[False] * c for _ in range(r)]
        br, bc = get_board_start(br, bc)
        # board의 모든 시작점을 다 찾아봤다면 실패, 종료 
        if (br, bc) == (N, 0):
            break
        if board[br][bc] == 1: 
            continue

        sticker_q.append((sr, sc))
        board_q.append((br, bc))
        visited[sr][sc] = True
        # board에 찍히는 유효 좌표 
        board_position = [(br, bc)]
    
        while board_q and sticker_q:
            bcr, bcc = board_q.popleft()
            scr, scc = sticker_q.popleft()

            # sticker 전부 채웠다면 성공, 종료 
            if cnt == len(board_position):
                # board에 스티커 붙이기 
                put_sticker(board_position)
                answer += cnt
                return True

            for dir in range(4):
                bnr = bcr + dr[dir]
                bnc = bcc + dc[dir]
                snr = scr + dr[dir]
                snc = scc + dc[dir]

                if 0 <= bnr < N and 0 <= bnc < M and 0 <= snr < r and 0 <= snc < c and not visited[snr][snc]:
                    # board는 비어있어야 하고, sticker는 채워져있어야 함
                    if board[bnr][bnc] == 0 and sticker[snr][snc] == 1:
                        board_q.append((bnr, bnc))
                        sticker_q.append((snr, snc))
                        visited[snr][snc] = True
                        board_position.append((bnr, bnc))
    return False

N, M, K = map(int, input().split())
board = [[0] * M for _ in range(N)] 
stickers = []
sticker_size = []
sticker_cnt = []

for _ in range(K):
    R, C = map(int, input().split())
    tmp = [list(map(int, input().split())) for _ in range(R)]
    stickers.append(tmp)
    sticker_size.append((R, C))

    # 스티커 칸 수 카운트 
    cnt = 0
    for i in range(R):
        cnt += tmp[i].count(1)

    sticker_cnt.append(cnt)

# 모든 스티커 순회 
for i in range(len(stickers)):
    cur = stickers[i]
    r, c = sticker_size[i]
    cnt = sticker_cnt[i]

    # 현재 스티커 3회 회전(0->90->180->270)
    for _ in range(4):
        sr, sc = get_sticker_start(cur)

        # 스티커 붙이기 성공
        if bfs(cur, cnt, sr, sc):
            break
        # 스티커 붙이기 실패, 회전
        cur, r, c = rotate(cur)

print(answer)
