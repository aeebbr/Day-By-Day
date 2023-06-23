# [BOJ] 17142. 연구소 3
# 풀이 시간: 0 분
# 실행 시간: 0 ms
# 메모리: 0 KB

# 전체 바이러스 중 M개를 활성화 -> 활성화 바이러스만 퍼진다 

import sys 
import copy
from collections import deque

input = sys.stdin.readline

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 최소 시간
min_time = float("inf")

def spread_virus(arr, blank):
    global min_time
    # 큐 초기화 
    q = deque()
    # 방문배열 초기화 
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 7:
                # 큐에 활성 바이러스 삽입
                q.append([i, j, 7])
                visited[i][j] = True

    while q:
        # 큐에서 하나 빼기 
        cr, cc, time = q.popleft()

        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                # 0이거나 2일 때 
                if arr[nr][nc] == 0 or arr[nr][nc] == 2:
                    q.append([nr, nc, time + 1])       
                    visited[nr][nc] = True

                    # 0이라면 
                    if arr[nr][nc] == 0:      
                        blank -= 1

                    arr[nr][nc] = time + 1
                    
                    # 빈 칸이 남지 않았을 때(바이러스가 모두 퍼졌을 때)
                    if blank == 0:
                        # 최소 크기 갱신 
                        min_time = min(min_time, time - 6)
                        return 
                    
    return 
                        
def active_virus(depth, cnt, arr):
    # 종료 조건: M개의 바이러스를 활성화
    if cnt == M:
        # 바이러스 퍼트리기 
        spread_virus(arr, blank)
        return 
    
    for i in range(depth, len(virus)):
        # 카피 배열
        copy_arr = copy.deepcopy(arr)

        # 현재 바이러스 
        r, c = virus[i]

        # 카피 배열에 활성화 표시 
        copy_arr[r][c] = 7

        # 재귀 호출
        active_virus(i + 1, cnt + 1, copy_arr)

# 입력
N, M = map(int, input().split())

board = []
virus = []
blank = 0

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(N):
        if row[j] == 2:
            virus.append([i, j])
        elif row[j] == 0:
            blank += 1

if blank == 0:
    print(0)
else:
    active_virus(0, 0, board)

    if min_time == float('inf'):
        print(-1)
    else:
        print(min_time)