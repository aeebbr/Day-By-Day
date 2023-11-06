# [BOJ] 5212. 지구 온난화 
# 풀이 시간 : 00 분

# 사라지는 섬
    # 섬을 기준으로 사방을 봤을 때, 사방에
    # . 이 있고,
    # 범위를 넘어간 곳이 있다면, 
    # 이들의 합이 3개 이상이라면 사라지는 것 

# 모든 행, 열 순회하면서 현재의 행 또는 열에 섬이 없다면 해당 부분은 지우기 

import copy

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
copy_board = copy.deepcopy(board)

for i in range(R):
    for j in range(C):
        if copy_board[i][j] == 'X':
            cnt = 0
            # 사방 탐색 
            for dir in range(4):
                nr = i + dr[dir]
                nc = j + dc[dir]

                # 범위 벗어났거나, 바다라면
                if 0 > nr or nr >= R or 0 > nc or nc >= C or copy_board[nr][nc] == '.':
                    cnt += 1
                    
                    continue
                
            if cnt >= 3:
                board[i][j] = '.'

remove_r = []
remove_c = []

last_row = 0

# 윗 행 순회 
for i in range(R):
    if not 'X' in board[i]:
        remove_r.append(i)
        last_row = i + 1
    else:
        break
# 아래 행 순회 
for i in range(R-1, -1, -1):
    if not 'X' in board[i]:
        remove_r.append(i)
    else:
        break
# 왼쪽 열 순회 
for i in range(C):
    isRemoved = False
    for j in range(R):
        if board[j][i] == 'X':
            break
    else:
        remove_c.append(i)
        isRemoved = True
    if not isRemoved:
        break
# 오른쪽 열 순회 
for i in range(C-1, -1, -1):
    isRemoved = False
    for j in range(R):
        if board[j][i] == 'X':
            break
    else:
        remove_c.append(i)
        isRemoved = True
    if not isRemoved:
        break

for i in range(R):
    for j in range(C):
        if not i in remove_r and not j in remove_c:
            if i != last_row:
                print()
            print(board[i][j], end="")
            last_row = i
