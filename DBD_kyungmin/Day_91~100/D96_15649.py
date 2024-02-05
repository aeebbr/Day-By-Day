# [BOJ] 15649. N과 M (1)
# 풀이 시간 : 12 분 

def combi(nums):
    if len(nums) == M:
        print(*nums)
        return 

    for i in range(1, N+1):
        if i in nums:
            continue
        nums.append(i)
        combi(nums)
        nums.pop()

N, M = map(int, input().split())
combi([])
