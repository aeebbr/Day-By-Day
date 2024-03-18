# [BOJ] 7785. 회사에 있는 사람   
# 풀이 시간 : 10 분 

import sys
input = sys.stdin.readline

N = int(input())
isEnter = {}

for _ in range(N):
    name, work = input().split()
    if work == "enter":
        isEnter[name] = True
    else:
        isEnter[name] = False

isEnter = sorted(isEnter.items(), key = lambda x:x[0], reverse=True)

for k, v in isEnter:
    if v == True: print(k)
