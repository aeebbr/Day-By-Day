# [BOJ] 17140. 이차원 배열과 연산  
# 풀이 시간 : 40 분 

import sys
input = sys.stdin.readline
import copy

answer = 0

R, C, K = map(int, input().split())
R -= 1
C -= 1
board = [list(map(int, input().split())) for _ in range(3)]

while True:
    if len(board) > R and len(board[0]) > C and board[R][C] == K:
        break
    if answer == 101:
        answer = -1
        break

    # 행 길이 
    r_len = len(board)
    c_len = len(board[0])

    new_board = []
    max_len = 0

    if r_len >= c_len:
        # 모든 행 순회 
        for i in range(r_len):
            # 중복 제거 
            set_line = set(board[i])
            cnt_line = []

            for j in set_line:
                if j == 0:
                    continue
                cnt = board[i].count(j)
                cnt_line.append([j, cnt])

            # 정렬 
            cnt_line.sort(key=lambda x:[x[1], x[0]])

            # 리스트로 변환해서 넣기 
            new_line = []
            for a, b in cnt_line:
                new_line.append(a)
                new_line.append(b)
            new_board.append(new_line)
            max_len = max(max_len, len(new_line))
        # 0 붙이기 
        for row in new_board:
            if len(row) < max_len:
                for _ in range(max_len - len(row)):
                    row.append(0)
        board = copy.deepcopy(new_board)
    # C 연산
    else:
        # 모든 열 순회 
        for i in range(c_len):
            col = []
            for j in range(r_len):
                col.append(board[j][i])
            # 중복 제거 
            set_line = set(col)
            cnt_line = []

            for j in set_line:
                if j == 0:
                    continue
                cnt = col.count(j)
                cnt_line.append([j, cnt])

            # 정렬 
            cnt_line.sort(key=lambda x:[x[1], x[0]])

            # 리스트로 변환해서 넣기 
            new_line = []
            for a, b in cnt_line:
                new_line.append(a)
                new_line.append(b)
            new_board.append(new_line)
            max_len = max(max_len, len(new_line))

        board = [[0] * len(new_board) for _ in range(max_len)]
        # 행, 열 뒤집기   
        for i in range(len(new_board)):
            for j in range(len(new_board[i])):
                board[j][i] = new_board[i][j]

    answer += 1

print(answer)
