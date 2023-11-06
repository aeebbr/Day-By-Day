# [BOJ] 13901. 로봇 
# 풀이 시간 : 40 분

import sys 
input = sys.stdin.readline

# 상 하 좌 우 
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, input().split())
K = int(input())
board = [[0] * C for _ in range(R)]
for i in range(K):
    br, bc = map(int, input().split())
    # 장애물: -1
    board[br][bc] = -1

cr, cc = map(int, input().split())
# 로봇 위치: 1
board[cr][cc] = 1

# 방향 숫자 1씩 줄여서 dr, dc 인덱스와 일치 시키기 
directions = list(map(lambda x: x - 1, map(int, input().split())))

# directions = list(map(int, input().split()))
# # 방향 숫자 1씩 줄여서 dr, dc 인덱스와 일치 시키기 
# directions = list(map(lambda x:x - 1, directions))

# 지정된 방향으로 무한히 돌기 
while True:
    # 이동 플래그. 한 번이라도 이동한다면 True로 갱신 
    isMove = False
    # 방향 한 사이클 다 돌았으면 다시 처음부터 
    for dir in directions:
        # 현 방향으로 일직선 쭉
        while True:
            cr += dr[dir]
            cc += dc[dir]

            # 조건 안 맞으면 전진 그만, 한 칸 전진한 것 다시 후진 
                # 범위 외, 재방문, 장애물 
            if 0 > cr or cr >= R or 0 > cc or cc >= C or board[cr][cc] > 0 or board[cr][cc] == -1:
                cr -= dr[dir]
                cc -= dc[dir]
    
                # 다음 방향으로 이동 
                break

            # 조건에 맞다면 한 칸 전진 
            board[cr][cc] = 1

            if not isMove:
                isMove = True

    # 사방탐색 끝
    # 전체 종료 조건: 사방 모두 불가능할 때 
    if not isMove:
        break

print(cr, cc)
