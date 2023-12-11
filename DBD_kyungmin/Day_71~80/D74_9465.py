# [BOJ] 9465. 스티커   
# 풀이 시간 : 40 분 

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(2)]

    if n > 1:
        board[0][1] += board[1][0]
        board[1][1] += board[0][0]
    # 모든 열 탐색하면서 값 누적 
        # 2번째 인덱스부터
    for i in range(2, n):
        # 0번 열의 대각선 아래 
        board[0][i] += max(board[1][i-1], board[1][i-2])
        # 1번 열의 대각선 위 
        board[1][i] += max(board[0][i-1], board[0][i-2])

    # 현재 케이스 출력
        # 마지막 열
    print(max(board[0][n-1], board[1][n-1]))