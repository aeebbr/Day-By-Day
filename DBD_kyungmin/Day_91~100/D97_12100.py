# [BOJ] 12100. 2048(Easy) 
# 풀이 시간 : 98 분 

import sys
input = sys.stdin.readline
import copy

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

answer = 0

# 블록 한 개에 대한 이동
def one_block_move(d, cr, cc, block_cnt, move_board, combined):
    nr, nc = cr, cc
    while True:
        nr += dr[d]
        nc += dc[d]

        # 조건
        if 0 <= nr < N and 0 <= nc < N:
            # 이동 위치에 다른 블록이 있다면? 합칠 수 있는지 확인
            if move_board[nr][nc] != 0:
                # 1) 이동 위치의 블록과 같은 수인가
                # 2) 이동 위치의 블록이 합 이력이 없는가 
                if move_board[nr][nc] == move_board[cr][cc] and not combined[nr][nc]:
                    move_board[nr][nc] += move_board[cr][cc]
                    move_board[cr][cc] = 0             
                    combined[nr][nc] = True    
                    # 합칠 때마다 블록 개수 하나 줄어듦
                    block_cnt -= 1           
                    cr, cc = nr, nc # 위치 갱신해야 리턴문에 현재값 넘길 수 있음 

                # 합치든 합치지 않든 이동 위치에 다른 블록 있으면 종료
                    # 이동 위치에 다른 블록이 있지만 합치기 실패 => 이동하지 않음  
                break

            # 이동
            move_board[nr][nc] = move_board[cr][cc]
            move_board[cr][cc] = 0        
            combined[nr][nc] = combined[cr][cc]
            combined[cr][cc] = False        
            # 위치 갱신
            cr, cc = nr, nc
        # 범위 벗어난다면 이동하지 않고 지금 자리에 머물기 
        else:
            break

    return block_cnt, move_board, combined, move_board[cr][cc]

# 해당 방향으로 모두 이동 
def move(d, block_cnt, move_board):
    # 방문배열처럼, 합쳐진 블록 여부 표시하는 배열. 원래 위치가 아닌 이동한 위치에 표시하기! 
    combined = [[False] * N for _ in range(N)]
    max_block = 0

    # 배열 끝이나, 다른 수와 마주칠 때까지 이동 
        # 위로 이동이라면: 가장 위 블록부터 이동
        # 오른쪽으로 이동이라면: 가장 오른쪽 블록부터 이동
    # 오른쪽 이동
    if d == 0:
        # 오른쪽 -> 왼쪽으로 순회 (상하는 상관없음)
        for cr in range(N):
            for cc in range(N-1, -1, -1):
                if move_board[cr][cc] == 0:
                    continue

                block_cnt, move_board, combined, block_num = one_block_move(d, cr, cc, block_cnt, move_board, combined)
                max_block = max(max_block, block_num)
    # 아래로 이동
    elif d == 1:
        # 아래 -> 위로 순회 (좌우는 상관없음)
        for cr in range(N-1, -1, -1):
            for cc in range(N):
                if move_board[cr][cc] == 0:
                    continue

                block_cnt, move_board, combined, block_num = one_block_move(d, cr, cc, block_cnt, move_board, combined)
                max_block = max(max_block, block_num)
    # 왼쪽 / 위으로 이동
    else:
        # 왼 -> 오른쪽, 위 -> 아래로 순회 
        for cr in range(N):
            for cc in range(N):
                if move_board[cr][cc] == 0:
                    continue
                
                block_cnt, move_board, combined, block_num = one_block_move(d, cr, cc, block_cnt, move_board, combined)
                max_block = max(max_block, block_num)

    # 모든 블록 이동 완료 
    return move_board, block_cnt, max_block

def dfs(move_cnt, block_cnt, max_block, board):
    global answer

    # 기저 조건
    # 1) 최대 횟수에 도달하지 않아도 종료하는 경우?? (가지치기): 블록이 하나 남았을 경우 
    # 2) 최대 횟수 도달
    if block_cnt <= 1 or move_cnt == 5:
        # 가장 큰 블록의 값 구하기 
        answer = max(answer, max_block)
        return 
    
    # 사방으로 이동
    for d in range(4):
        # 현재 방향으로 이동 
        move_board = copy.deepcopy(board)
        move_board, new_block_cnt, max_block = move(d, block_cnt, move_board)
        dfs(move_cnt + 1, new_block_cnt, max_block, move_board)

N = int(input())
board = []
block_cnt = 0
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    for i in row:
        answer = max(answer, i)
        if i != 0:
            block_cnt += 1

dfs(0, block_cnt, 0, board)
print(answer)