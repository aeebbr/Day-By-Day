# [Programmers] 42587. 프로세스  
# 풀이 시간 : 30 분 

from collections import deque

def solution(priorities, location):
    answer = 0 # 실행 순서 
    q = deque()
    
    for i in range(len(priorities)):
        q.append((i, priorities[i]))
    priorities.sort(reverse=True)
    max_i = 0
    
    while q:
        i, p = q.popleft()
        if p < priorities[max_i]:
            q.append((i, p))
        else:
            answer += 1
            if i == location:
                break
            max_i += 1
                 
    return answer