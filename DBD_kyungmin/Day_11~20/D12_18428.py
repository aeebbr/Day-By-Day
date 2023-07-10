# [BOJ] 18428. 감시 피하기
# 풀이 시간: 40 분
# 실행 시간: 148 ms
# 메모리: 34192 KB

import sys
from collections import deque
import copy

input = sys.stdin.readline

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 모든 선생님 한 명씩 사방 탐색하면서 감시 가능 여부 따지기 
def teacher_watch(arr):
    # 현재 탐색할 선생 위치 
    for cr, cc in teacher:
        # 각 방향으로 전진
        for dir in range(4): 
            # 탐색 위치 초기화 
            nr = cr
            nc = cc
            while True: 
                # 전진한 위치 
                nr += dr[dir]
                nc += dc[dir]

                # 전진 위치가 조건에 맞는다면 
                if 0 <= nr < N and 0 <= nc < N:
                    # 장애물과 만났다면 해당 방향 탐색 끝, 다음 방향으로 
                    if arr[nr][nc] == 'O':
                      break  
                    # 학생과 만났다면 감시 피하기 실패 
                    elif arr[nr][nc] == 'S':
                        return False

                # 범위에서 벗어났다면 다음 방향 탐색 시작
                else:
                    break

    # 모든 탐색 끝, 한 학생도 만나지 못했다면 감시 피하기 성공
    return True

# 장애물 놓기(조합) 
# depth: 
# cnt: 몇 번째 장애물인지 
# arr: 장애물이 반영된 배열 
def build_wall(depth, cnt, arr):
    # 종료 조건
    # 세 개를 다 놨을 때 
    if cnt == 3:
        # 선생님 감시 가능 여부 따지기 
        # 감시 피하기 성공했다면 전체 탐색 종료 
        if teacher_watch(arr):
            print("YES")
            exit(0)
        return 
    
    # 빈 곳을 돌면서 장애물 놓기 
    for i in range(depth, len(blank)):
        # 카피 배열
        copy_arr = copy.deepcopy(arr)

        # 현재 빈 칸
        r, c = blank[i]

        # 카피 배열에 장애물 놓기 
        copy_arr[r][c] = 'O'

        # 재귀 호출
        build_wall(i + 1, cnt + 1, copy_arr)

# 입력
N = int(input())

teacher = []
blank = []
board = []

for i in range(N):
    row = list(input().split())
    board.append(row)
    for j in range(N):
        if row[j] == 'T':
            teacher.append((i, j))
        elif row[j] == 'X':
            blank.append((i, j))

build_wall(0, 0, board)
print("NO")