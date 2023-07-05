# [BOJ] 15683. 감시
# 풀이 시간: 40 분
# 실행 시간: 2984 ms
# 메모리: 31832 KB

import sys
import copy
input = sys.stdin.readline

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 사각지대 최소값
min_blind = float("inf")

# cctv별 방향: 1번 ~ 5번
# 각 cctv 방향은 방향의 인덱스로 표시 
cctv_dir = [[], 
            [[0], [1], [2], [3]], 
            [[0, 2], [1, 3]], 
            [[0, 3], [0, 1], [2, 3], [1, 2]], 
            [[0, 2, 3], [0, 1, 3], [0, 1, 2], [1, 2, 3]], 
            [[0, 1, 2, 3]]]

# 사각지대 카운트 
def count_blind(arr):
    cnt = 0
    global min_blind
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                cnt += 1

    min_blind = min(min_blind, cnt)

# cctv 방향 표시하기
def mark_dir(r, c, dir, arr):
    # 현재 위치를 모두 탐색 
    for d in dir:
        nr = r
        nc = c
        while True:
            # 이동 위치 
            nr += dr[d]
            nc += dc[d]
            # 1) 배열 끝이거나, 2) 벽이 나올 때까지 
            if 0 > nr or nr >= N or 0 > nc or nc >= M or arr[nr][nc] == 6:
                break
                # 다음 방향으로

            # 조건에 맞는다면 이동 방향에 표시 
            arr[nr][nc] = "#"

    return arr

def dfs(idx, arr):
    # 종료 조건: 모든 cctv를 탐색했을 경우 
    if idx == len(cctv):
        # 사각지대 카운트하기
        count_blind(arr)
        return 
    
    # 현재 배열을 복사하여 복사 배열에 감시 범위 표시 
    copy_arr = copy.deepcopy(arr)
    # 현재 cctv 정보 
    num, r, c = cctv[idx]

    # 현재 cctv의 모든 방향 탐색 
    for d in cctv_dir[num]:
        # 감시 범위 탐색 
        copy_arr = mark_dir(r, c, d, copy_arr)

        # 재귀 호출
        # 다음 cctv 탐색
        dfs(idx + 1, copy_arr)

        # 다른 cctv 탐색 완료, 다시 현재 cctv의 다른 방향 탐색 이어가기
        # 현재 방향으로 표시한 것 지우기
        copy_arr = copy.deepcopy(arr)

# 입력
N, M = map(int, input().split())

board = []
cctv = []

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if 1 <= row[j] <= 5:
            cctv.append([row[j], i, j])
    board.append(row)

dfs(0, board)
print(min_blind)