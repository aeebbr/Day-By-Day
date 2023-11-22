# [BOJ] 1863. 스카이라인 쉬운거 
# 풀이 시간 : 20 분

# 새로운 입력 => 카운트 1 증가 
# 예외
    # 이미 선점된 높이일 경우 
    # 0일 경우 

import sys
input = sys.stdin.readline

answer = 0
height = []

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(len(arr)):
    x, y = arr[i]

    if y == 0:
        height = []
        continue

    isPass = False
    
    del_arr = []
    for j in range(len(height)):
        # 이미 선점된 높이가 있다면, 한 덩어리가 지속되고 있는 것 => 새 덩어리로 카운트 불가 
        if height[j] == y:
            isPass = True
       # 현재 높이보다 높은 높이가 height에 있다면 그 높은 높이는 제거 
        elif height[j] > y:
            del_arr.append(j)

    # 리스트 제거 시 인덱스 에러 없도록 뒤의 인덱스부터 제거 
    del_arr.sort(reverse=True)
    for k in del_arr:
        del height[k]

    if not isPass:
        answer += 1
        height.append(y)

print(answer)