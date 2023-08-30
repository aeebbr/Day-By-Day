# [Programmers] 138476. 귤 고르기
# 풀이 시간: 40 분

def solution(k, tangerine):
    dic = {}
    for i in tangerine:
        if dic.get(i):
            dic[i] += 1
        else:
            dic[i] = 1
    
    dic = dict(sorted(dic.items(), key=lambda x:x[1], reverse=True))
        
    # for key, value in dic.items():
    #     print(key, value)
    # print("---------")
        
    kind_cnt = 0
    total_cnt = 0
    
    # 딕셔너리 순회
    for key, value in dic.items():
        kind_cnt += 1
        total_cnt += value
        
        # print(key, value)
        # print(kind_cnt, total_cnt)
        # print()
        
        # 토탈값이 k를 이상이라면 성공 
        if total_cnt >= k:
            return kind_cnt