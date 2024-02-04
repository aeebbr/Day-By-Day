# [BOJ] 11652. 카드  
# 풀이 시간 : 20 분 

# 카운팅 소트 

import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()
dic = {}

for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

answer = max(dic, key=dic.get)
print(answer)

