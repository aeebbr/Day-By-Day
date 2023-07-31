# [Programmers] 154540. 무인도 여행
# 풀이 시간: 50 분
# 실행 시간: 00 ms
# 메모리: 00 KB

import sys 
input = sys.stdin.readline

from collections import deque

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(r, c, maps, N, M): 
    # 큐 초기화 
    q = deque() 
    
    # 머물 수 있는 날 카운트 
    cnt = maps[r][c]
    
    # 큐 삽입 
    q.append((r, c))
    # 방문 처리 
    maps[r][c] = 0
    
    while q:
        # 큐에서 하나 빼기 
        cr, cc = q.popleft()
        
        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]
            
            if 0 <= nr < N and 0 <= nc < M and maps[nr][nc] != 0:
                q.append((nr, nc))
                cnt += maps[nr][nc]
                maps[nr][nc] = 0

    return cnt, maps  

def solution(maps):
    answer = []
    
    N = len(maps)
    M = len(maps[0]) 
        
    for i in range(N):
        tmp = maps[i].replace("X", "0")
        maps[i] = list(map(int, tmp))

    for i in range(N):
        for j in range(M):
            if maps[i][j] != 0:
                answer.append(0)
                answer[-1], maps = bfs(i, j, maps, N, M)
                
    answer.sort()
    return answer if answer else [-1] 