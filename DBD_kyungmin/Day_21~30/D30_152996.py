# [Programmers] 152996. 시소 짝꿍
# 풀이 시간: 40 분

from collections import Counter

def solution(weights):
    answer = 0
    
    # 1:1 비율인 쌍 개수 구하기 
    counter = Counter(weights)
    
    for k, v in counter.items():
        # 같은 무게가 2개 이상이라면(해당 몸무게 구성원들이 1:1이라면)
        if v >= 2:
            # 해당 무게 쌍 개수 구하기 
            answer += v * (v - 1) // 2
    
    # 무게 중복 제거 
    weights = set(weights)
    
    # 2:3, 2:4, 3:4 비율인 쌍 개수 구하기 
    for w in weights:
        # 현재 무게와 찾아야 하는 비율 관계인 무게가 있다면
        if w*2/3 in weights:
            # 두 무게로 쌍을 낼 수 있는 경우의 수 구하기 
            answer += counter[w*2/3] * counter[w]
        if w*2/4 in weights:
            # 두 무게로 쌍을 낼 수 있는 경우의 수 구하기 
            answer += counter[w*2/4] * counter[w]
        if w*3/4 in weights:
            # 두 무게로 쌍을 낼 수 있는 경우의 수 구하기 
            answer += counter[w*3/4] * counter[w]
    
    return answer

# 시간 초과 난 코드 
# import copy

# def solution(weights):
#     answer = 0
    
#     distance = [ 1, 4 / 2, 4 / 3, 3 / 2]
#     # 360 270 180 100 100
#     weights.sort(reverse = True)
    
#     while weights:
#         top = weights.pop()
        
#         # arr = copy.deepcopy(weights)
        
#         for num in weights:
#             if num / top in distance:
#                 # 쌍 찾음
#                 # print(num, top)
#                 answer += 1
    
#     return answer