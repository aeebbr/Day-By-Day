# [BOJ] 3190. 뱀
# 풀이 시간: 90++ 분
# 실행 시간: 68 ms
# 메모리: 34192 KB

import sys
from collections import deque

input = sys.stdin.readline

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 입력
N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]

# 사과 입력
for i in range(K):
    j, k = map(int, input().split())
    # 사과 위치를 2로 표시 
    board[j - 1][k - 1] = 2

L = int(input())

# 뱀 위치를 담는 큐
snake_q = deque()
# 전환할 방향을 담는 딕셔너리 
dir_dict = dict()

# 뱀 초기 위치를 큐에 삽입 
snake_q.append((0, 0))

# 방향 입력
for i in range(L):
    j, k = input().split()
    # key: 시간(초), value: 방향
    dir_dict[int(j)] = k

# 현재 위치(뱀 초기 위치로 초기화) 
cr = 0
cc = 0
# 뱀 초기 위치 1로 표시 
board[cr][cc] = 1
time = 0
dir = 0

# 방향 전환 함수 
# 방향 전환 후 이동이 아니라, 앞으로 이동할 방향만 전환시켜 놓는 것
def turn(d):
    global dir

    # 왼쪽으로 회전이라면
    if d == 'L':    
        dir = (dir - 1) % 4
    # 오른쪽으로 회전이라면
    else: 
        dir = (dir + 1) % 4

# 무한루프 돌면서 조건에 부합하지 않을 때까지 전진
while True:
    # 시간 증가 
    time += 1

    # 현재 방향으로 1칸 이동 
    cr += dr[dir]
    cc += dc[dir]

    # 조건: 1) 범위 내 
    if 0 <= cr < N and 0 <= cc < N:
        # 자기 몸을 만난다면 탐색 끝
        if board[cr][cc] == 1:
            break

        # 사과가 없다면
        elif board[cr][cc] == 0:
            # 꼬리 제거(큐에서 제일 오래 삽입되어있는(가장왼쪽) 것 꺼내기)
            tr, tc = snake_q.popleft()
            board[tr][tc] = 0

        # 사과가 있던 없던 간에 머리는 이동 위치로 이동
        board[cr][cc] = 1
        # 뱀 위치 큐에 이동 위치 삽입
        snake_q.append((cr, cc))

        # 이동 끝(이번 시간 끝), 방향 전환할 시간인지 확인
        # 방향 딕셔너리에 이번 시간이 있다면 전환
        if time in dir_dict:
            # 이번 시간에 해당하는 방향을 인자로 
            turn(dir_dict[time])
        
    # 범위를 벗어난다면 탐색 끝
    else:
        break

print(time)

# 내가 시도한 코드 
# # 사과가 있는지 확인
# def isApple(r, c):
#     for r, c in apple:
#         # 사과가 있다면 
#         if r == r and c == c:
#             return True
        
#     return False

# def move():
#     board[0][0] = 1

#     # 머리, 꼬리 
#     hr, hc = 0
#     tr, tc = 0

#     # 소요 시간
#     time = 0
#     cr, cc = 0
#     # 전진 방향
#     # 시작은 오른쪽
#     dir = 0

#     # 회전 정보 
#     lotate_time, loate_dir = lotate_q.popleft()

#     # 무한 루프 돌면서 전진
#     while True:
#         # 시작 방향: 오른쪽(dir: 0)
#         cr += dr[dir]
#         cc += dc[dir]    

#         # 조건
#         # 1) 범위 내, 2) 자기 자신이 아닐 것
#         if 0 <= cr < N and 0 <= cc < N and not board[cr][cc] == 1:
#             # 이동 위치에 사과가 있는지 확인
#             # 모든 사과의 위치들과 이동 위치를 비교하여, 판단
#             if isApple(cr, cc):
#                 # 사과가 있다면 머리만 한 칸 전진
#                 hr = cr
#                 hc = cc

#             else:
#                 # 사과가 없다면 머리, 꼬리 함께 한 칸 전진
#                 hr = cr
#                 hc = cc

#                 # 꼬리가 없어진 칸에서 뱀 없애기 
#                 board[tr][tc] = 0

#                 tr += dr[dir]
#                 tc += dc[dir]

#             # 머리가 전진한 칸에 뱀 추가
#             board[cr][cr] = 1

#             # 전진 후 시간 증가 
#             time += 1
        
#         # 조건에 부합하지 않는다면
#         else:
#             # 게임 끝
#             return time
        
#         # 이번 시간 끝, 회전 가능성 확인
#         # 회전 시간이라면
#         if time == lotate_time:
#             # 회전

# # 입력
# N = int(input())
# K = int(input())
# board = [[0] * N for _ in range(N)]
# apple = [list(map(int, input().split())) for _ in range(K)]
# L = int(input())
# lotate_q = deque()
# for _ in range(L):
#     lotate_q.append(input().split())

# print()
