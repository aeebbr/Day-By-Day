# [BOJ] 14718. 용감한 용사 진수    
# 풀이 시간 : 90++ 분 

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = float("inf")

# stat: [힘, 민첩, 지능]
def fight(stat):
    global answer
    win_cnt = 0 

    # 각 병사 
    for i in range(N):
        is_win = True
        # 현재 병사의 현재 능력치 비교 
        for j in range(3):
            if stat[j] < board[i][j]:
                is_win = False

        # 현재 병사와 싸웠을 때 이겼다면 
        if is_win:
            win_cnt += 1

    # 현재 스탯으로 k명 이상을 이겼다면 
    if win_cnt >= K:
        # 최소값 갱신 
        answer = min(answer, sum(stat))
    
def dfs(depth, stat):
    if depth == 3:
        # 능력치 조합 완료, 해당 능력치로 모든 병사와 싸우기 
        fight(stat)
        return 
    for i in range(0, N):
        stat.append(board[i][depth])
        dfs(depth+1, stat)
        stat.pop()

# 완탐 
    # 각 능력치의 모든 조합 
dfs(0, [])
print(answer)