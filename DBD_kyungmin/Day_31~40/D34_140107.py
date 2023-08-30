# [Programmers] 140107. 점 찍기
# 풀이 시간: 60 분

import math

# 0부터 k 단위로 점 찍기(각 k 배수에 점)
def solution(k, d):
    answer = 0
    
    # 0부터 d까지 k 단위로 순회하며 각 x 좌표에서 찍을 수 있는 y 좌표의 개수 구하기 
    for x in range(0, d + 1, k):
        # 현재 x에서 찍을 수 있는 y의 최대값
        max_y = math.floor(math.sqrt(d*d - x*x))
        # 1부터 max_y까지 k 단위로 쪼개어 개수 세기 
        # 0까지 포함해야 하니 + 1
        answer += (max_y // k) + 1
    
    return answer