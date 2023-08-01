# [BOJ] 1107. 리모컨
# 풀이 시간: 90++ 분
# 실행 시간: 240 ms
# 메모리: 115284 KB

import sys

input = sys.stdin.readline

# 입력
N = int(input())
M = int(input())

if M:
    brokens = list(map(str, input().split()))
else:
    brokens = []

# 버튼을 누르는 최대 경우의 수: + / - 버튼을 일일히 눌러서 1씩 증감해야 하는 경우
cnt = abs(100 - N)

# 0에서 100만까지의 모든 수를 탐색하며 해당 수가 가능한 수인지 따지기 
# 최대로 목표할 수 있는 수가 50만이므로, 50만보다 크면서 최악의 경우(9만 가능한 경우)의 수까지 조합하면
for num in range(1000001):
    # 현재 숫자의 한 자리씩 탐색
    for n in str(num):
        # 고장난 버튼이라면
        if n in brokens:
            break
    # 고장난 버튼이 하나도 없다면
    else:
        # cnt 갱신
        cnt = min(cnt, len(str(num)) + abs(num - N)) # ~ 이동할 숫자의 총 자리 개수 + 이동한 숫자에서 N까지 증감 버튼을 일일히 누르는 경우 수

print(cnt) 

# 시도: 재귀 무한 루프 걸려서 장렬히 실패
# 세 가지 경우로 나눠서 카운트 내고, 가장 적은 카운트를 답으로 
# 1) 목표 수에 고장 수가 포함되지 않을 때까지 목표 수에서 1씩 증 or 감
# 3) 100에서 목표 수까지 1씩 증 or 감
# # 현재 수 
# cur_num = 100

# # 버튼 누르는 최소 카운트 
# min_cnt = float("inf")

# if M:
#     brokens = list(map(int, input().split()))

# # 고장 수가 포함되어 있는지 확인
# def is_include_broken(num):
#     nums = list(map(int, str(num)))

#     for n in nums:
#         # 고장 수가 포함되어 있다면 
#         if n in brokens:
#             return True

#     return False

# def move_channel(num, cal, cnt):
#     # 목표 수에 고장 수가 포함되어 있다면 
#     if is_include_broken(num):
#         # 1씩 증 or 감
#         num += 1 * cal

#         return move_channel(num, cal, cnt + 1)
#     else:
#         # 이동한 카운트 + 자리 수 
#         tmp =  cnt + len(str(num))
#         return tmp
    
# # 고장 수가 없다면
# if M == 0:
#     print(len(str(N)))
# # 현재 수가 목표 수가 아니라면
# elif cur_num != N:
#     # 목표 수에서 증가하는 경우 
#     min_cnt = min(min_cnt, move_channel(N, 1, 0))
    
#     # 목표 수에서 감소하는 경우 
#     min_cnt = min(min_cnt, move_channel(N, -1, 0))
    
#     # 100에서 목표수까지 1씩 증 or 감하는 경우
#     if 100 < N:
#         min_cnt = min(min_cnt, N - 100)
#     else:
#         min_cnt = min(min_cnt, 100 - N)
        
#     print(min_cnt)
# # 현재 수가 목표 수라면
# elif cur_num == N:
#     print(0)