# [BOJ] 1931. 회의실 배정  
# 풀이 시간 : 15 분 

import sys
input = sys.stdin.readline

answer = 0
N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]

# 정렬 
    # 1) 종료 시간을 기준으로 오름차순
    # 2) 시작 시간을 기준으로 오름차순
times.sort(key = lambda x: (x[1], x[0]))
tmp = []

i = 0
while i < N:
    answer += 1
    cur_end = times[i][1]
    tmp.append(times[i])

    # 현재 종료보다 시작이 같거나 큰 것 찾기 
        # 시작과 동시에 종료하는 경우를 배제하기 위해서 i+1부터  
    for j in range(i+1, N):
        next_start = times[j][0]
        if next_start >= cur_end:
            # 현재 갱신 
            i = j
            break
    else:
        break

print(answer)

# 12
# 3 3
# 1 4
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14