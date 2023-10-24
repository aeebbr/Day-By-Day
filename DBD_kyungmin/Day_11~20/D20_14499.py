# [BOJ] 14499. 주사위 굴리기
# 풀이 시간: 90++ 분
# 실행 시간: 48 ms
# 메모리: 31256 KB

# 주사위 굴리기 
# 1) 칸이 0이라면: 주사위 바닥 수가 칸에 삽입
# 2) 칸이 0이 아니라면: 칸의 수가 주사위 바닥 수로, 칸의 수를 0으로 

# 주사위가 맵 범위 벗어나면 명령 무시, 출력 하지 않음

# 구할 것: 주사위 이동할 때마다 위에 쓰여있는 수 출력

# 주사위 시작 위치 칸은 무조건 0
# 시작할 때 주사위의 모든 면에는 0만

import sys

input = sys.stdin.readline

# 우 좌 상 하
# 동 서 북 남
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

# 주사위 6면의 정보 
# 바닥, 좌, 앞, 뒤, 우, 위 
dice = [0, 0, 0, 0, 0, 0]

# 주사위를 굴릴 수 있는 모든 방향에 대한 이동 함수 
def move_right():
    temp = dice[1]
    dice[1] = dice[0]
    dice[0] = dice[4]
    dice[4] = dice[5]
    dice[5] = temp

def move_left():
    temp = dice[4]
    dice[4] = dice[0]
    dice[0] = dice[1]
    dice[1] = dice[5]
    dice[5] = temp

def move_front():
    temp = dice[3]
    dice[3] = dice[0]
    dice[0] = dice[2]
    dice[2] = dice[5]
    dice[5] = temp

def move_back():
    temp = dice[5]
    dice[5] = dice[2]
    dice[2] = dice[0]
    dice[0] = dice[3]
    dice[3] = temp

# 입력
N, M, sr, sc, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))

cr, cc = sr, sc
# 각 명령에 대한 탐색
for dir in command:
    # 이동 위치가 범위 내인지 확인
    nr = cr + dr[dir - 1]
    nc = cc + dc[dir - 1]

    if 0 <= nr < N and 0 <= nc < M:
        if dir == 1:
            move_right()
        elif dir == 2:
            move_left()
        elif dir == 3:
            move_back()
        elif dir == 4:
            move_front()

        # 이동 끝
        # 이동 칸이 0이라면 주사위 바닥면 삽입
        if board[nr][nc] == 0:
            board[nr][nc] = dice[0]
        # 0이 아니라면 이동 칸의 수를 주사위 바닥면에 삽입하고, 이동 칸을 0으로 
        else:
            dice[0] = board[nr][nc]
            board[nr][nc] = 0

        # 명령 하나에 대한 탐색 끝
        cr = nr
        cc = nc

        # 주사위 윗면 출력
        print(dice[5])