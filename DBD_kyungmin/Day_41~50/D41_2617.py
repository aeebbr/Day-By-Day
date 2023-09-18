# [BOJ] 2617. 구슬 찾기
# 풀이 시간 : 90++ 분

# 중간값보다 작은 수 개수: 전체개수 // 2
# 중간값보다 큰 수 개수: 전체개수 // 2
# 이 개수보다 많이 작은 수 or 큰 수를 가지고 있다면, 중간값이 아님 
# (예시) A > B > C > D > E > 
    # [N보다 큰값 개수] 0, 1, 2, 3, 4
    # [N보다 작은값 개수] 4, 3, 2, 1, 0
    # A, B, D, E는 각각 3개 이상의 큰값 or 작은값을 가지고 있으니 탈락

import sys 
input = sys.stdin.readline

def dfs(node, list):
    global visited
    global cnt 
    visited[node] = True
    # 현재 노드보다 작거나 / 무거운 수 순회 
    for i in list[node]:
        if not visited[i]:
            cnt += 1
            # 무거운 수의 무거운 수 탐색 
            # or 작은 수의 작은 수 탐색 
            dfs(i, list)

N, M = map(int, input().split())

heavier = [[] for _ in range(N+1)]
lighter = [[] for _ in range(N+1)]

for _ in range(M):
    heavy, light = map(int, input().split())
    heavier[light].append(heavy)
    lighter[heavy].append(light)

mid = (N+1) // 2
not_mid_cnt = 0
# 모든 수 순회 
for i in range(1, N+1):
    # dfs로 현재 수보다 무거운 수들의 개수를 전부 카운트 
    visited = [False] * (N+1)
    # 더 큰 값 카운트 
    cnt = 0
    dfs(i, heavier)
    # (중간값보다 크고, 작은 개수) 보다 많은 큰 값을 가지고 있다면 탈락
    if cnt >= mid:
        not_mid_cnt += 1

    # 더 작은 값 카운트 
    cnt = 0
    dfs(i, lighter)
    if cnt >= mid:
        not_mid_cnt += 1

print(not_mid_cnt)

'''
# 무게 가중치 계산? 
# 매 턴마다 
# N보다 무거운 것, N보다 가벼운 것을 각 딕셔너리로 
    # {N: N보다 무거운 것}
    # {N: N보다 가벼운 것}
# 각 숫자 순회하면서 최종 가중치 계산(가벼운 개수 - 무거운 개수) 
    # 이 수를 기준으로 내림차순 정렬하고, 가장 양 끝단에 있는 것들 제거 
# 다음 턴에서는 남은 수끼리 탐색 
# 모든 최종 가중치가 0이 나온다면 종료 
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
heavier = {}
lighter = {}

for i in range(N):
    heavier[i+1] = []
    lighter[i+1] = []

for _ in range(M):
    heavy, light = map(int, input().split())
    # light < heavy
    lighter[heavy].append(light)
    heavier[light].append(heavy)

for k, v in lighter.items():
    for i in v:
        if not i in lighter[k]:
            lighter[v].append(i)
print()
'''