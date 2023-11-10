# [BOJ] 1043. 거짓말 
# 풀이 시간 : 40 분

# 진실을 알고 있는 숫자가 포함되어 있으면 제외 
# 제외된 숫자가 포함되어 있으면 제외 
# => 어떻게 짧은 시간을 써서 퍼져 나가는 관계를 다 순회할 것인가? 
# => bfs
# 같은 파티에 속한 숫자들끼리는 연결된 관계임 

import sys
input = sys.stdin.readline
import copy
from collections import deque

def bfs(start):
    global visited
    q = deque()
    q.append(start)

    while q:
        cur = q.pop()

        for i in range(len(people[cur])):
            near = people[cur][i]
            if not visited[near]:
                q.append(near)
                visited[near] = True

N, M = map(int, input().split())
truth = list(map(int, input().split())) # 진실을 알고있는 사람

# 진실을 알고있는 사람이 없다면 종료 
if truth == [0]:
    print(M)
    exit(0)

del truth[0]

visited = [False] * (N+1)
people = {} # 전체 사람들의 연결 리스트 
party = [] # 각 파티 정보 

for i in range(N):
    people[i+1] = []

# 파티 순회하면서 연결 관계 만들기 
for _ in range(M):
    tmp = list(map(int, input().split()))
    del tmp[0]
    # 파티 정보 저장 
    party.append(tmp)

    for i in range(len(tmp)):
        relative = copy.deepcopy(tmp)
        # 파티 참석 리스트에서 나 자신 제외하고 나와의 연결 관계에 추가 
        del relative[i]
        people[tmp[i]].extend(relative)

# 진실을 알고있는 사람들 순회하며 전체 연결 관계 체크 
for i in range(len(truth)):
    cur = truth[i]
    visited[cur] = True

    if len(people[cur]) != 0:
        bfs(cur)

# 모든 파티 순회하며 불가능한 파티 제외 
for p in party:
    for i in range(len(p)):
        cur = p[i]
        if visited[cur]:
            M -= 1
            break

print(M)