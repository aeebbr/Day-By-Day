# [Programmers] 43165. 타겟 넘ㅓ  
# 풀이 시간 : 5 분

answer = 0
def solution(numbers, target):
    def dfs(idx, num):
        global answer
    
        if idx == len(numbers):
            if num == target:
                answer += 1
            return 
    
        dfs(idx+1, num + (numbers[idx]))
        dfs(idx+1, num + (numbers[idx] * -1))
                
    dfs(0, 0)
    
    return answer