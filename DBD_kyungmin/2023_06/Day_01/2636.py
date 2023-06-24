# [BOJ] 2636. 치즈
# 풀이 시간: 66 분
# 실행 시간: 92 ms
# 메모리: 34200 KB

# 배열의 가장자리는 무조건 빈 곳이니까 (0, 0)을 시작으로 배열 가장자리 한 덩어리를 탐색
# 치즈의 바깥 테두리는 이 한 덩어리와 닿아있으므로
# 탐색을 하면서 발견한 치즈(1)는 바깥 테두리와 인접해있는 치즈이므로 큐에 저장
# 한 번 탐색을 끝내면 큐에 저장되어 있는 치즈 테두리를 0으로 갱신하여 치즈를 없앰

# 이 때, 큐에 아무것도 저장되어 있지 않다면 남은 치즈가 없다는 것을 의미하므로 종료
# 치즈가 남아있지 않으면 -> False 반환, 남아있다면 -> True 반환

# bfs 함수 종료되고 반환된 것이 False라면 전체 탐색 종료, 결과값 출력 

import sys
from collections import deque

input = sys.stdin.readline

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 날짜 카운트 
day_cnt = 0

# 가장자리 치즈 조각 수 
total_edge = 0

def bfs():
    # 큐 초기화 
    # 탐색을 위한 큐 
    findQ = deque()
    # 치즈 테두리를 담는 큐
    edgeQ = deque()

    # 방문 배열 초기화 
    visited = [[False] * M for _ in range(N)]

    # 시작 지점을 큐에 담기 
    findQ.append((0, 0))
    visited[0][0] = True

    while findQ:
        # 큐에서 하나 꺼내기 
        cr, cc = findQ.popleft()

        # 사방 탐색
        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]

            # 1) 범위 내인지, 2) 방문하지 않은 곳인지 
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                # 탐색 지점이 0이라면
                if map[nr][nc] == 0:
                    findQ.append((nr, nc))
                # 탐색 지점이 1이라면
                elif map[nr][nc] == 1:
                    edgeQ.append((nr, nc))

                # 방문 처리 
                visited[nr][nc] = True   

    # 탐색 끝
    
    # 치즈 가장자리가 남아있는지 확인
    # 남아있지 않다면 False 리턴
    if not edgeQ:
        return False

    # 치즈 가장자리 수 갱신
    # 치즈 가장자리가 남아있지 않은 상태에서 갱신한다면 0으로 갱신되기 때문에 남아있는 것을 확인하고 나서 갱신
    global total_edge
    total_edge = len(edgeQ)

    # 치즈 가장자리 없애기 
    while edgeQ:
        er, ec = edgeQ.popleft()
        
        map[er][ec] = 0

    # 작업 다 끝나고 가장자리 수 리턴
    return True

N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]

while True:
    # 한 사이클 = 하루 
    # False가 반환되었다면 치즈가 모두 녹은 것
    if not bfs():
        break

    # 하루 끝
    day_cnt += 1

print(day_cnt)
print(total_edge)