# [Programmers] 148653. 마법의 엘리베이터
# 풀이 시간: 20 분

def solution(storey):
    
    def dfs(storey, cnt):
        if storey == 0:
            nonlocal answer
            answer = min(answer, cnt)
            return
        
        if cnt > answer:
            return
        
        # 밑으로 내릴 때
        dfs(storey // 10, cnt + storey % 10)
        
        # 위로 올릴 때
        dfs(storey // 10 + 1, cnt + 10 - storey % 10)
    
    answer = float("inf")
    dfs(storey, 0)
    return answer