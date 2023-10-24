# [Programmers] 154538. 숫자 변환하기
# 풀이 시간: 60 분

# bfs
from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    
    q = deque()
    # 연산하는 수 방문처리(연산은 x에서 최대 y까지만 할 수 있음) 
    visited = [False] * (y+1)

    q.append((x, 0))
    visited[x] = True

    while q:
        cur, cnt = q.popleft()

        for i in range(3):
            if i == 0:
                tmp = cur * 3
            elif i == 1:
                tmp = cur * 2
            else:
                tmp = cur + n

            if tmp > y or visited[tmp]:
                continue
            elif tmp == y:
                return cnt + 1
            else:
                q.append((tmp, cnt + 1))
                visited[tmp] = True
                
    return - 1

# dfs(시간 초과)
# import sys
# sys.setrecursionlimit(10**4)

# answer = float("inf")
# def solution(x, y, n):
    
#     def dfs(num, cnt):
#         global answer
        
#         # 기저 조건
#         # 타겟일 경우(성공)
#         if num == y:
#             answer = min(answer, cnt)
#             return     
#         # 타겟을 초과한 경우(실패, 백트래킹) 
#         elif num > y: 
#             return 
#         # 카운트가 최소 횟수를 넘어간 경우(실패, 백트래킹)
#         elif cnt >= answer:
#             return 
        
#         for i in range(3):
#             if i == 0:
#                 dfs(num * 3, cnt + 1)
#             elif i == 1:
#                 dfs(num * 2, cnt + 1)
#             else:
#                 dfs(num + n, cnt + 1)
#     dfs(x, 0)
    
#     if answer == float("inf"):
#         return -1
#     else:
#         return answer