# [BOJ] 2458. 키 순서
# 풀이 시간 : 30 분

from collections import deque
import sys
input = sys.stdin.readline

def bfs(start_student, adj_list):
    visited = [False] * (N + 1)
    visited[start_student] = True
    queue = deque()
    queue.append(start_student)

    while queue:
        student = queue.popleft()
        for oth_student in adj_list[student]:
            if not visited[oth_student]:
                visited[oth_student] = True
                queue.append(oth_student)
    
    for i in range(1, N + 1):
        if visited[i]:
            total_visited[i] = True


N, M = map(int, input().split())
asc_adj_list = [[] for _ in range(N + 1)]
desc_adj_list = [[] for _ in range(N + 1)]
answer = 0

for _ in range(M):
    a, b = map(int, input().split())
    asc_adj_list[a].append(b)
    desc_adj_list[b].append(a)

for student in range(1, N + 1):
    total_visited = [False] * (N + 1)
    bfs(student, asc_adj_list)
    bfs(student, desc_adj_list)

    if all(total_visited[1:]):
        answer += 1

print(answer)