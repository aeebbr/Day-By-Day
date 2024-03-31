# [BOJ] 1715. 카드 정렬하기    
# 풀이 시간 : 50 분 

import sys
input = sys.stdin.readline
import heapq

answer = 0
N = int(input())
# card는 heapq
card = []
for _ in range(N):
    heapq.heappush(card, int(input()))

while len(card) > 1:
    # 최소값 두 개 뽑아서 더하기 
    total = heapq.heappop(card) + heapq.heappop(card)
    answer += total
    heapq.heappush(card, total)

print(answer)

'''
# 잘못된 알고리즘 
    # 가장 작은 두 묶음을 더해야 하는데, 오름차순 정렬한 묶음을 순서대로 묶으며 누적하다보면
    # 누적한 값이 다음 묶음보다 커질 때가 오기 때문에 가장 작은 두 묶음을 더하는 것이 아니다
import sys
input = sys.stdin.readline

N = int(input())
card = [int(input().rstrip()) for _ in range(N)]
card.sort()
answer = card[0]

for i in range(1, len(card)):
    answer += answer + card[i]
    if i == 1:
        answer -= card[0]

print(answer)
'''

