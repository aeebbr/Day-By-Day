# [BOJ] 21609. 상어 중학교
# 풀이 시간: ?? 분
# 실행 시간: 92 ms
# 메모리: 34304 KB

# 1. 블록 그룹 찾기 
# 배열 전체 탐색 돌리기 
# 현재 시작 지점이 일반 블록이라면 탐색
    # 1) 현재 블록과 같은 값의 블록이거나, 
    # 2) 무지개 블록이라면 큐에 삽입

# 탐색 끝나고 전역의 최대 블록 수와 비교해서 현재 블록 수가 더 크면 갱신
# 같다면, 무지개 블록 수가 더 많은 것 갱신
# 같다면, 블록 행이 더 큰 것을 갱신
# 같다면, 블록 열이 더 큰 것을 갱신

# 2. 찾은 그룹의 블록 없애고 전역에 점수 갱신하기 

# 3. 중력 작용시키기 
# 배열 전체 탐색하며 아래쪽이 블록이 없다면 아래에 -1이 있거나, 범위 끝일 때까지 반복하며 내려주기 

# 4. 90도 반시계 회전
# (0, 0) -> (1, 0)
# (0, 1) -> (0, 0)
# (1, 0) -> (1, 1)
# (1, 1) -> (0, 1)

# 5. 다시 중력 작용

import sys 
from collections import deque

input = sys.stdin.readline

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 가장 큰 블록 

# 그룹 찾기 
def bfs(row, col, color):
    # 큐 초기화
    # 탐색을 위한 큐 
    q = deque()

    # 한 덩어리를 넣은 큐 
    # 큐에 시작 지점 넣기 
    q.append((row, col))

    # 전체 블록 개수
    # 시작 블록이 있는 상태이니 블록 개수에 1 카운트
    total_block_cnt = 1
    # 무지개 블록 개수 
    rainbow_cnt = 0

    # 블록 위치 넣을 리스트 
    # 일반 블록과 무지개 블록의 위치를 따로 저장(탐색 후 무지개 블록의 방문 처리를 무효할 것이기 때문)
    # 시작 위치를 블록 리스트에 삽입
    blocks = [[row, col]]
    # 무지개 블록 위치 넣을 리스트 
    rainbows = []

    while q:
        # 큐에서 하나 꺼내기 
        cr, cc = q.popleft()

        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                # 1) 현재 값과 같은 일반 블록인 경우
                if color == map[nr][nc]:
                    q.append([nr, nc])                    
                    visited[nr][nc] = True
                    total_block_cnt += 1
                    blocks.append([nr, nc])
                # 2) 무지개 블록이라면
                if map[nr][nc] == 0:
                    q.append([nr, nc])                    
                    visited[nr][nc] = True
                    total_block_cnt += 1
                    rainbow_cnt += 1
                    rainbows.append([nr, nc])

    # 탐색 끝 
    # 무지개 블록은 블록 그룹끼리 중복이 가능하기 때문에 방문을 해제 
    for r, c in rainbows:
        visited[r][c] = False
    
    # 전체 블록 수, 무지개 블록 수, 일반 블록 + 무지개 블록 위치 리턴
    return [total_block_cnt, rainbow_cnt, blocks + rainbows]

def remove(block):
    for r, c in block:
        # 제거된 블록은 -2로 표시
        map[r][c] = -2

# 3
# 2
# 0
# => 3을 먼저 2의 위치로 내렸을 때, 다음 턴에서 2도 0의 자리로 내려야한다 
# => 위에서 아래로 탐색하는 것이 아니라, 아래에서 위로 탑색
def gravity():
    global map
    # 배열 마지막 행에서부터 탐색
    for i in range(N - 2, -1, -1):
        # 현재 행의 모든 열 확인
        for j in range(N):
            #  -1이 아니라면 아래로 내리기 
            if map[i][j] > -1:
                # 현재 행에서부터 탐색 시작
                r = i

                while True:
                    # 다음 행이 1) 범위 내일 것, 2) -2일 것 
                    if 0 <= r + 1 < N and map[r + 1][j] == -2:
                        #아래로 내리기
                        map[r + 1][j] = map[r][j]
                        map[r][j] = -2
                        # 다음 행으로 갱신
                        r += 1
                    else:
                        break

# 반시계 90도 회전
def rot90():
    # 회전된 배열
    roted_map = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            roted_map[N - 1 - j][i] = map[i][j]

    # 회전된 배열 반환
    return roted_map

# 입력 
N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]

# 점수 
score = 0

# 오토 플레이 
while True:
    # 방문 배열 초기화 
    visited = [[False] * N for _ in range(N)]
    # 가능한 블록 그룹을 넣을 리스트 
    blocks = []

    for i in range(N):
        for j in range(N):
            # 1) 일반 블록일 것, 2) 방문하지 않았을 것
            if 1 <= map[i][j] <= M and not visited[i][j]: 
                # 현재 위치 방문 처리 
                visited[i][j] = True

                # bfs 탐색 결과: 블록 수, 무지개 블록 수, 블록 + 무지개 블록 위치 리턴
                block_info = bfs(i, j, map[i][j])
                
                # 탐색 결과, 블록 수가 2개 이상이어야 그룹으로 인정
                if block_info[0] >= 2:
                    blocks.append(block_info)

    # 배열 전체 탐색하는 한 사이클 종료 
    # 블록 그룹 정렬
    # 내림차순 정렬하여 블록 수가 많은 것 -> 적은 것으로 내림차순
    # 첫 조건(블록 수)가 같다면 두번째 조건(무지개 수), 두 번째 조건이 같다면 세 번째 ... 자동으로 다음 조건으로 비교
    blocks.sort(reverse=True)

    # 배열 전체를 탐색했는데도 블록 그룹을 찾지 못했다면 전체 종료 
    if not blocks:
        break

    # 블록 제거
    # 블록 그룹을 인자로 넘겨서 해당 위치의 블록들 제거 
    remove(blocks[0][2])

    # 점수 갱신
    score += blocks[0][0]**2

    # 중력 가하기 
    gravity()

    # 90도 회전
    map = rot90()

    # 중력 가하기 
    gravity()

print(score)