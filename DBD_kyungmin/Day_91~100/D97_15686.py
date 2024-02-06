# [BOJ] 15686. 치킨 배달  
# 풀이 시간 : 18 분 

import sys
input = sys.stdin.readline
from collections import deque

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

answer = float("inf")

# 치킨집이 아니라 가정집을 기준으로 순회하기 
def find_short(sel):
    global answer
    city_short = 0 # 도시의 치킨 거리 

    # 모든 집 순회 
    for hr, hc in home:
        shortest = float("inf") # 현재 집과 가장 가까운 치킨 거리 
        for cr, cc in sel:
            shortest = min(shortest, abs(hr - cr) + abs(hc - cc))
        city_short += shortest
        
        # 더 이상의 탐색이 의미 없음 
        if city_short >= answer:
            return 

    answer = min(answer, city_short)

def combi(idx, sel):
    if len(sel) > M:
        return 
    
    # 거리 판단 
    if len(sel) != 0:
        find_short(sel)

    for i in range(idx, len(chicken)):
        sel.append(chicken[i])
        combi(i+1, sel)
        sel.pop()

N, M = map(int, input().split())
board = []
home = []
chicken = []
for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(N):
        if row[j] == 1:
            home.append((i, j))
        elif row[j] == 2:
            chicken.append((i, j))

combi(0, [])
print(answer)
