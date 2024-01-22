# [SWEA] 1211. Ladder2  
# 풀이 시간 : 40 분 

import sys
sys.stdin = open("input_1211.txt", "r")
import copy

# 좌 우 하 
dr = [0, 0, 1]
dc = [-1, 1, 0]

for _ in range(10):
    answer = 0
    min_cnt = float("inf")
    test_num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    sc = []
    for i in range(100):
        if arr[0][i] == 1:
            sc.append(i)      
    cr, cc = 0, 0
    # 모든 시작점에서 순회 시작
    for cc in sc:
        cr = 0
        cnt = 1
        copy_arr = copy.deepcopy(arr)
        while cr != 99:
            # print(cr, cc)
            for dir in range(3):
                nr = cr + dr[dir]
                nc = cc + dc[dir]

                # 조건 
                if 0 <= nr < 100 and 0 <= nc < 100 and copy_arr[nr][nc] == 1:
                    cr, cc = nr, nc
                    copy_arr[cr][cc] = 3
                    # arr[cr][cc] = 3
                    cnt += 1
        
        if min_cnt >= cnt:
            # print(cnt, cc)
            min_cnt = cnt
            answer = cc

    print(f"#{test_num} {answer}")
