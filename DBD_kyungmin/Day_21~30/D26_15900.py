# [BOJ] 15900. 나무 탈출
# 풀이 시간: 00 분
# 실행 시간: 00 ms
# 메모리: 00 KB

# 뭐가 리프 노드지? 
    # 양방향 리스트 완성 후, 연결된 노드가 한 개면 리프 
# 1번 루트 노드를 기준으로 자식 노드를 어떻게? 
    # 양방향 리스트 
    # 1번 루트 노드를 기준으로 연결된 노드들을 체크 
    # 방문 처리해서 이미 봤던 노드(부모 노드)는 안 보기 
    # => 각각의 루프 노드에서 시작하기(시작 노드 두 개 조합)
    # dfs: 루프에서 시작해서 부모 노드로 dfs 

import sys 

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

# cur: 현재 탐색하는 노드 
def dfs(cur):
    # 현재 노드 방문 처리 
    visited[cur] = True

    # 현재 노드에 연결된 노드들 탐색 
    # 그 중에서도 자식 노드를 탐색해야 함
    for link in tree[cur]:
        # 방문 여부 탐색하여 부모 노드를 제외
        if visited[link]:
            continue

        # 자식 노드 깊이 
        # 부모 노드의 깊이에 1 누적해야 함 
        depth[link] = depth[cur] + 1

        # link와 연결된 노드 탐색하러 
        dfs(link)

# 입력
N = int(input())

# 각 노드들의 연결된 노드들을 담는 리스트 
tree = [[] for _ in range(N + 1)]
# 각 노드들의 깊이를 담는 리스트 
depth = [0 for _ in range(N + 1)]
# 각 노드의 방문 여부
visited = [False for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# 1번 루프 노드에서 시작 
dfs(1)
# 모든 노드들의 깊이 계산 완료 

answer = 0
# 모든 리프 노드의 깊이를 합하기 
# 루트 노드를 제외하고 2번 노드부터 마지막 노드까지 탐색
for i in range(2, N + 1):
    # 리프 노드 찾기 
    # 연결된 노드가 1개라면 리프 노드임
    if len(tree[i]) == 1:
        answer += depth[i]

# 선공이기 때문에 모든 리프 노드의 깊이가
    # 짝 => 패배
    # 홀 => 승리 
if answer % 2 == 0:
    print("No")
else:
    print("Yes")
