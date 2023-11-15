# [BOJ] 2240. 자두 나무 
# 풀이 시간 : 90 분 ++

import sys
input = sys.stdin.readline

T, W = map(int, input().split())
tmp = []
for _ in range(T):
    tmp.append(int(input()))

last = tmp[0]
arr = [1]
for i in range(1, T):
    cur = tmp[i]
    if last != cur:
        arr.append(1)
        last = cur
    else:
        arr[-1] += 1

# 이전과 같은 숫자 나오면 카운트만 1 증가 
# 이전과 다른 숫자 나오면 이동 카운트 1 감소, 카운트 1 증가 
# 이전과 다른 숫자 나왔을 때 이동 카운트가 0이라면 이동 불가, 카운트 증가 없음

# 선택지 
# 1. 1과 2 중 어디서 시작하느냐
# 2. 이동할 수 있는 시점에서 이동을 하느냐, 혹은 하지 않느냐 

# 한 구간의 자두 개수를 덩어리로 저장해놓기 
# [1, 2, 2, 2] => 짝수 인덱스 나무 // 홀수 인덱스 나무 

# 홀 -> 홀 // 짝 -> 짝은 이동 카운트 증가 없음 
# 홀 -> 짝 // 짝 -> 홀은 이동 카운트 증가 있음 

max_cnt = 0

def combi(idx, move_cnt, jadu_cnt, debug):
    global max_cnt
    if move_cnt > W:
        # print()
        return 
    max_cnt = max(max_cnt, jadu_cnt)
    
    for i in range(idx, len(arr)):
        # 현재의 idx와 i의 짝홀 타입이 다르다면
        if len(debug) != 0 and debug[-1] % 2 != i % 2:
            debug.append(i)
            combi(i+1, move_cnt+1, jadu_cnt + arr[i], debug)
        else:
            debug.append(i)
            combi(i+1, move_cnt, jadu_cnt + arr[i], debug)
        debug.pop()
        
combi(0, 0, 0, [])
    
print(max_cnt)
