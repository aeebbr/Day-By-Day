# [Programmers] 172927. 광물 캐기
# 풀이 시간: 90++ 분

def solution(picks, minerals):
    answer = 0
    
    s = 0
    # 곡괭이 수 계산 
    s = sum(picks)
    
    # 광물은 다섯개씩 묶어서 캘 수 있음 
    # 가지고 있는 곡괭이로 캘 수 있는 광물의 개수 
    num_min = s * 5
    
    # 캘 수 있는 광물의 수보다 주어진 광물이 더 많다면 캘 수 있는 광물의 수만큼만 남기기 
    if len(minerals) > num_min:
        minerals = minerals[:num_min]
        
    # 광물 조사 
    # 한 번에 캘 수 있는 광물 양을 확인하기 위해 광물을 5개씩 묶기 
    # 한 줄에는 [다이아, 철, 돌]이며, 한 번에 캘 수 있는 각 광물 양임
    cnt_min = [[0, 0, 0] for _ in range(10)] # 광물의 최대 길이가 50이기 때문
    
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            cnt_min[i//5][0] += 1
        elif minerals[i] == 'iron': 
            cnt_min[i//5][1] += 1
        else : 
            cnt_min[i//5][2] += 1

    # for j in cnt_min:
    #     print(j)
    # print("----------")
    
    # 피로도 높은 턴(5개씩 묶은)부터 차례대로 턴 정렬
    sorted_cnt_min = sorted(cnt_min, key = lambda x: (-x[0], -x[1], -x[2]))
    
    # for j in sorted_cnt_min:
    #     print(j)
        
    # 피로도 계산 
    # 각 턴 실행
    for d, i, s in sorted_cnt_min: # 현재 턴에서 캐야하는 다이아, 철, 돌
        # 다이아 곡, 철 곡, 돌 곡 순서대로, 강한 곡괭이 먼저 사용
        # 곡괭이 배열에 있는 곡괭이 수가 남아있을 때까지 
        
        # 주어진 곡괭이 배열 순회하면서 각 곡괭이가 유효한 것인지 확인하고 광물 캐기 
        for p in range(len(picks)):
            if p == 0 and picks[p] > 0: # 다이아 곡괭이 
                # 곡괭이 사용, 감소 시키기
                picks[p] -= 1
                # 현재 턴에서 캐야할 광물의 피로도 누적
                answer += d + i + s
                # 광물 캤으니 다음 턴으로
                break
            elif p == 1 and picks[p] > 0: # 철 곡괭이 
                picks[p] -= 1
                answer += d * 5 + i + s
                break
            elif p == 2 and picks[p] > 0: # 돌 곡괭이 
                picks[p] -= 1
                answer += d * 25 + i * 5 + s
                break
    
    return answer

# 잘못된 아이디어 
# min_tired = float("inf")

# def solution(picks, minerals):
    
#     # 딕셔너리 
#     # 광물: [곡괭이 a, b, c 피로도]
#     tired_dic = {'diamond': [1, 5, 25], 'iron': [1, 1, 5], 'stone': [1, 1, 1]}
    
#     # 곡괭이 idx, 광물 idx, 피로도 누적,  
#     def dfs(p_idx, m_idx, tired):
#         global min_tired
#         # 기저 조건
#         # 남은 곡괭이 없거나 남은 광물이 없다면
#         if m_idx >= len(minerals) or p_idx >= sum(picks):
#             # 최소 피로도 갱신
#             min_tired = min(min_tired, tired)
#             return 
        
#         # 가지 치기: 최소 피로도를 넘어선다면 탐색 필요 없음 
#         if tired >= min_tired:
#             return 
        
#         for i in range(sum(picks)):
#             # 현재 곡괭이로 남은 광물 5개 깨기 
#             # m_idx에서부터 5개까지 현재 곡괭이로 깼을 때의 피로도를 누적
            
#             # 현재 곡괭이로 생기는 피로도 
#             tmp = 0
            
#             for j in range(m_idx, min(m_idx + 5, len(minerals))):
#                 # 깨야하는 광물 
#                 this_pick = tired_dic[minerals[j]]
#                 # print(this_pick)
#                 # 현재 곡괭이로 깰 때 피로도 
#                 t = this_pick[p_idx]
#                 tmp += t
                
            
            
#             dfs(p_idx + 1, m_idx + 5, tired + tmp)
                
                
        
#     dfs(0, 0, 0)
    
#     return min_tired