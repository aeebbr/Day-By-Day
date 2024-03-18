# [BOJ] 1620. 나는야 포켓몬 마스터 이다솜
# 풀이 시간 : 10 분 

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}

for i in range(1, N+1):
    name = input().rstrip()
    dic[name] = i
    dic[i] = name

for _ in range(M):
    question = input().rstrip()
    if question.isdigit():
        print(dic[int(question)])
    else:
        print(dic[question])
