# [BOJ] 15685. 드래곤 커브
# 풀이 시간: 90++ 분
# 실행 시간: 48 ms
# 메모리: 31256 KB

import sys
input = sys.stdin.readline

# 입력
N = int(input())

# 우 상 좌 하 
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

# 회전
# 우 -> 상 // 0 -> 1
# 하 -> 우 // 3 -> 0
# 좌 -> 하 // 2 -> 3
# 상 -> 좌 // 1 -> 2
# (dir + 1) % 4

# 100 * 100 배열 
board = [[0] * 101 for _ in range(101)] 

# 드래곤 커브 정보 입력
for _ in range(N):
    # 각 드래곤 커브 
    # 시작 열(x), 시작 행(y), 시작 방향, 세대  
    c, r, d, g = map(int, input().split()) 

    # 이동 방향 
    # 시작 방향으로 초기화 
    move = [d]

    # 시작 지점 1로
    board[r][c] = 1

    # 0세대부터 최종 세대까지 반복하며 이동하기
    for _ in range(g):
        # 현재 세대의 모든 방향 
        tmp = []
        for i in range(len(move)):
            # 이전 세대의 방향을 회전
            tmp.append((move[-i - 1] + 1) % 4)

        # move: 현재까지의 방향 + 현재까지의 방향을 회전한 방향
        move.extend(tmp)

    # 방향대로 이동 좌표에 이동 표시 
    for i in move:
        nr = r + dr[i]
        nc = c + dc[i]

        board[nr][nc] = 1

        # 현재 위치 갱신
        c = nc
        r = nr

# 전체 배열에서 정사각형 찾기 
square_cnt = 0
for i in range(100):
    for j in range(100):
        # 현재 위치 기준으로 각 지점이 드래곤 커브라면(1이라면) 카운트  
        if board[i][j] and board[i + 1][j] and board[i][j + 1] and board[i + 1][j + 1]:
            square_cnt += 1

print(square_cnt)