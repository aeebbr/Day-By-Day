# [BOJ] 1182. 부분수열의 합  
# 풀이 시간 : 23 분 

import sys
input = sys.stdin.readline

answer = 0
def combi(total, idx, arr):
    global answer
    # 기저 조건
    # 성공 
    if len(arr) != 0 and total == S: # 길이가 양수인 부분 수열이니까 공집합 제외 
        answer += 1
        # return 하면 안됨, 이후의 수열에서 도합이 S인 수열이 나올 수도 있기 때문
    # 실패 
    elif N == idx:
        return 
    
    for i in range(idx, len(nums)):
        arr.append(nums[i])
        combi(total + nums[i], i + 1, arr)
        arr.pop()

N, S = map(int, input().split())
nums = list(map(int, input().split()))

combi(0, 0, [])
print(answer)
