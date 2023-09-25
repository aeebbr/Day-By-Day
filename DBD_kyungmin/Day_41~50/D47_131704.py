# [Programmers] 131704. 택배상자
# 풀이 시간 : 20 분

from collections import deque

def solution(order):
    answer = 0
    
    # 현재 찾아야 하는 상자의 인덱스 
    cur_idx = 0
    # 보조 컨테이너 역할을 하는 큐 
    q = deque()
    
    # 1 ~ 모든 상자 순회하며 현재 상자 찾기 
    for n in range(1, len(order) + 1):
        # 큐 확인 
        # 보조 컨테이너에서 현재 상자를 뺄 수 있는지 확인 
        if q:
            pop = q.pop()
            if pop == order[cur_idx]:
                answer += 1
                cur_idx += 1
            # 뺄 수 없다면 다시 보조 컨테이너에 올리기 
            else:
                q.append(pop)

        # 탐색 상자와 현재 상자가 일치한다면
        if n == order[cur_idx]:
            # 상자 수 증가 
            answer += 1
            # 현재 인덱스 갱신
            cur_idx += 1
        # 일치하지 않는다면 큐에 삽입 
        else:
            q.append(n)
    
    # 순서대로 초기 상자 모두 순회 끝
    # 큐 순회하며 보조 컨테이너에 있는 상자 탐색 
    while q:
        pop = q.pop()
        
        if order[cur_idx] == pop:
            answer += 1
            cur_idx += 1
        else:
            break
    
    return answer