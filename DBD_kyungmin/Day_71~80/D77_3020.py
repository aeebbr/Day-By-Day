# [BOJ] 3020. 개똥벌레   
# 풀이 시간 : 90++ 분 

# 밑, 위, 밑, 위 ... 
import sys
input = sys.stdin.readline

N, H = map(int, input().split())
min_cnt = N # 가장 큰 경우의 수 
section_cnt = 0
up = [] # 위에 달린 종유석
down = [] # 아래에 달린 석순
for i in range(N):
    if i % 2 == 0:
        down.append(int(input()))
    else:
        up.append(int(input()))

up.sort()
down.sort()

# 이분 탐색 
def binary_search(arr, target):
    start = 0 # 첫번째 인덱스 
    end = len(arr) - 1 # 마지막 인덱스 

    while start <= end:
        mid = (start + end) // 2

        # 타겟보다 작거나 같다면 start 키우기 
        if arr[mid] < target:
            start = mid + 1
        # 타겟보다 크다면 end 줄이기 
        else:
            end = mid - 1

    return len(arr) - start 

# 모든 높이에 대한 탐색(높이 1부터 가장 높은 높이까지) 
for i in range(1, H + 1):
    # 석순 이분탐색
    down_cnt = binary_search(down, i - 0.5) 
    # 종유석 이분탐색
    up_cnt = binary_search(up, H - i + 0.5)

    # 석순과 종유석 카운트 합해서 최소의 경우 구하기 
    total_cnt = down_cnt + up_cnt
    # 최소값 갱신
    if min_cnt > total_cnt:
        min_cnt = total_cnt
        section_cnt = 1 # 새로운 범위에서 새로 시작하는 거니까 카운트 1로 시작
    # 현재 최소값과 같은 수라면 현재 구간의 카운트 1 증가 
    elif min_cnt == total_cnt:
        section_cnt += 1

print(min_cnt, section_cnt)