# [Programmers] 43238. 입국심사  
# 풀이 시간 : 90 분 

# 찾고자 하는 것: 적절한 시간 
# 이분 탐색 범위: 최소 시간에서 최악의 경우에 나올 수 있는 시간 사이를 탐색
def solution(n, times):
    answer = 0
    
    # 시간 범위 
    left = 1 # 최소 시간
    right = max(times) * n # 최악의 경우에 나올 수 있는 시간
    
    # 이분 탐색
    while left <= right: # 탐색 기준: left가 right를 넘어서지 않기 
        # 중간 시간값
        mid = (left + right) // 2
        cnt = 0
        
        # 모든 심사대를 돌면서 현재 중간 시간값으로 몇 명을 심사할 수 있는지 카운트 
        for t in times:
            cnt += mid // t
            
        # n보다 많은 사람을 심사할 수 있다면 => 범위 줄이기 
            # n명의 사람에 심사 인원을 맞춘 경우도 포함
        if cnt >= n:
            right = mid - 1
            # 이 때의 중간 시간값을 답으로 갱신
            answer = mid
        # n보다 적은 사람을 심사할 수 있다면 => 범위 늘리기 
        elif cnt < n:
            left = mid + 1
    
    return answer