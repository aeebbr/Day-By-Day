# [BOJ] 20058. 마법사 상어와 파이어스톰
# 풀이 시간: 00 분
# 실행 시간: 0 ms
# 메모리: 0 KB

# 1. L 단계별로 부분 격자 나누기 
# 2. 각 부분 격자를 90도 시계 회전
# 3. 얼음 줄이기 
# 4. 모든 L 단계(총 Q번) 다 끝났으면, 
    # 1) 배열에 남아있는 모든 수 합하기
    # 2) 배열에서 가장 큰 얼음 한 덩어리 구하고, 그 덩어리 크기(총 개수) 구하기 

import sys
from collections import deque

input = sys.stdin.readline

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def melt_ice():
    # 녹을 얼음 좌표 
    melt_arr = []

    for r in range(len_board):
        for c in range(len_board):
            ice_cnt = 0

            for dir in range(4):
                nr = r + dr[dir]
                nc = c + dc[dir]

                # 얼음이라면
                if 0 <= nr < len_board and 0 <= nc < len_board and 0 < board[nr][nc]:
                    ice_cnt += 1
            
            # 현재 위치에서 사방 탐색 끝 
            # 얼음이 녹을 조건
                # 1) 현재 위치와 인접해있는 얼음이 세 개 미만일 것
                # 2) 현재 위치가 얼음일 것
            if ice_cnt < 3 and board[r][c] != 0:
                melt_arr.append((r, c))
    
    # 얼음 녹이기 
    for r, c in melt_arr:
        board[r][c] -= 1

    return board

def seperate_part(l):
    rotated_arr = [[0] * len_board for _ in range(len_board)]

    # 격자 한 변 사이즈 
    len_part = 2 ** l

    # 0에서 배열 범위까지, 격자 한 변 간격으로 
    for r in range(0, len_board, len_part):
        for c in range(0, len_board, len_part):
            # 한 격자의 세로 
            for i in range(len_part):
                # 한 격자의 가로 
                for j in range(len_part):
                    global board
                    rotated_arr[r + j][c + len_part - i - 1] = board[r + i][c + j]
    
    # 모든 배열의 회전 끝 
    # 회전시킨 배열을 반영
    board = rotated_arr

    # 얼음 녹이기 
    return melt_ice()

def check():
    # 방문 배열 초기화 
    visited = [[False] * len_board for _ in range(len_board)]
    # 남아있는 얼음 총 합
    total_ice = 0
    # 최대 얼음 덩어리 크기 
    max_area_size = 0

    for i in range(len_board):
        for j in range(len_board):
            # 현재 탐색 얼음 덩어리 크기 
            area_size = 0
            # 1) 방문하지 않았을 것, 2) 얼음일 것
            if not visited[i][j] and not board[i][j] == 0:
                # bfs
                q = deque()
                # 시작 지점을 큐에 삽입 
                q.append((i, j))
                # 시작 지점을 방문 처리 
                visited[i][j] = True

                while q:
                    # 큐에서 하나 빼기 
                    cr, cc = q.popleft()
                    total_ice += board[cr][cc]
                    area_size += 1

                    for dir in range(4):
                        nr = cr + dr[dir]
                        nc = cc + dc[dir]

                        if 0 <= nr < len_board and 0 <= nc < len_board and not visited[nr][nc]:
                            # 탐색 위치가 얼음일 때
                            if board[nr][nc] != 0:
                                visited[nr][nc] = True
                                q.append((nr, nc))

                # 최대 얼음 크기 갱신 
                max_area_size = max(max_area_size, area_size)

    print(total_ice)           
    print(max_area_size)

# 입력
N, Q = map(int, input().split())
len_board = 2 ** N
board = [list(map(int, input().split())) for _ in range(len_board)]
L = list(map(int, input().split()))

# 각 단계에 맞게 파이어스톰 실행
for l in L:

    board = seperate_part(l)

# 모든 파이어스톰 끝
check()