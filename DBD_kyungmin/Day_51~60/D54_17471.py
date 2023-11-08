# bfs
# brute force

import sys
input = sys.stdin.readline
from collections import deque

min_cnt = float("inf")

def bfs(arr):
    q = deque()
    q.append(arr[0])
    visited = [False] * (N + 1)
    visited[arr[0]] = True
    cnt = 1

    while q:
        cur = q.popleft()

        for near in (sections[cur]):
            if not visited[near] and near in arr:
                q.append(near)
                visited[near] = True
                cnt += 1

    if cnt != len(arr):
        return False
    else:
        return True

def population(arr):
    cnt = 0
    for i in arr:
        cnt += people[i]
    return cnt 
    
# 1이 들어간 경우만 따지기 
def combi(idx, arr):
    global min_cnt 

    if len(arr) == N:
        return 
    
    # print(arr)
    # 다른 구역 
    other = list(set(total) - set(arr))
    # 연결 확인 
    if bfs(arr) and bfs(other):
        # 인구 수 따지기 
        arr_cnt = population(arr)
        other_cnt = population(other)

        min_cnt = min(min_cnt, max(arr_cnt, other_cnt) - min(arr_cnt, other_cnt))

    for i in range(idx, N):
        arr.append(i+1)
        combi(i+1, arr)
        arr.pop()

N = int(input())
people = list(map(int, input().split()))
people.insert(0, 0)
sections = [0]
total = []

for i in range(N): 
    tmp = list(map(int, input().split()))
    del tmp[0]
    sections.append(tmp)
    total.append(i+1)
    
combi(1, [1])

if min_cnt == float("inf"):
    print(-1)
else:
    print(min_cnt)