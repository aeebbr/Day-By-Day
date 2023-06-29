# [BOJ] 2615. 오목
# 풀이 시간: 20 분
# 실행 시간: 40 ms
# 메모리: 31256 KB

import sys
input = sys.stdin.readline

def in_range(y, x):
    return 0 <= y < 19 and 0 <= x < 19


dy = [-1, 0, 1, 1]
dx = [1, 1, 1, 0]

board = [list(map(int, input().split())) for _ in range(19)]
breaker = False

for y in range(19):
    for x in range(19):
        if board[y][x] != 0:
            for d in range(4):
                back_y, back_x = y - dy[d], x - dx[d]
                if not in_range(back_y, back_x) or board[back_y][back_x] != board[y][x]:
                    cnt = 1
                    move_y, move_x = y + dy[d], x + dx[d]
                    while in_range(move_y, move_x) and board[y][x] == board[move_y][move_x]:
                        cnt += 1
                        move_y += dy[d]
                        move_x += dx[d]
                    
                    if cnt == 5:
                        print(board[y][x])
                        print(y + 1, x + 1)
                        breaker = True
                        break
            
            if breaker:
                break
    if breaker:
        break

else:
    print(0)
