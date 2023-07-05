# [BOJ] 17141. 연구소 2
# 풀이 시간: 60 분
# 실행 시간: 1144 ms
# 메모리: 34264 KB

# 1. 완탐으로 M개씩 바이러스 놓기 
# 2. 다 놨으면 바이러스 퍼트리기 
# 3. 최소 시간 갱신하기

import sys
from collections import deque
import copy

input = sys.stdin.readline

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 최소 시간 
min_time = float("inf")

# bfs로 바이러스 퍼트리기 
def spread_virus(arr):
    # 큐 초기화 
    q = deque()
    # 방문 배열 초기화 
    visited = [[False] * N for _ in range(N)]

    # 바이러스를 큐에 삽입
    for i in range(N):
        for j in range(N):
            if(arr[i][j] == 7):
                # 좌표, 시간(7부터 시작)
                q.append((i, j, 7))
                visited[i][j] = True

    while q:
        # 큐에서 하나 빼기 
        cr, cc, time = q.popleft()

        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                # 1) 빈 공간이거나, 2) 바이러스가 놓일 수 있는 자리일 것
                if arr[nr][nc] == 0 or arr[nr][nc] == 2:
                    q.append((nr, nc, time + 1)) 
                    visited[nr][nc] = True
                    # 시간 갱신 
                    arr[nr][nc] = time + 1

# 시간 체크 
def time_check(arr):
    max_time = 0
    for i in range(N):
        for j in range(N):
            # 바이러스가 퍼지지 않은 곳이 있다면
            if arr[i][j] == 0 or arr[i][j] == 2:
                return -1
            elif arr[i][j] != 1:
                max_time = max(max_time, arr[i][j])

    return max_time
    
# M개의 바이러스 조합  
def combi_virus(idx, cnt, copy_arr):
    # 조합 완료 
    if cnt == M:
        spread_virus(copy_arr)

        time = time_check(copy_arr)

        # 바이러스가 모두 퍼졌다면 
        if time != -1:
            global min_time
            # 최소 시간 갱신 
            # 시작 시간을 0이 아닌 7부터 카운트했으니 7 빼기
            min_time = min(min_time, time - 7)

        return 
    
    for i in range(idx, len(virus)):
        # 복사 배열 
        tmp = copy.deepcopy(copy_arr)

        r, c = virus[i]
        tmp[r][c] = 7

        # 재귀 호출
        combi_virus(i + 1, cnt + 1, tmp)

# 입력
N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
virus = []
wall = []

for i in range(N):
    for j in range(N):
        # 2라면 바이러스 배열에 추가 
        if map[i][j] == 2:
            virus.append([i, j])

combi_virus(0, 0, map)

if min_time == float("inf"):
    print(-1)
else:
    print(min_time)