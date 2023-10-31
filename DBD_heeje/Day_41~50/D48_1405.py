# [BOJ] 1405. 미친 로봇
# 풀이 시간 : 15 분

def dfs(y, x, cnt, per):
    if cnt == info[0]:
        global answer
        answer += per
        return

    for idx, d in enumerate(direction, start=1):
        if info[idx] == 0: continue
        ny, nx = y + d[0], x + d[1]
        
        # if (ny, nx) not in visited:
        if not visited[ny][nx]:
            # visited.add((ny, nx))
            visited[ny][nx] = True
            dfs(ny, nx, cnt + 1, per * info[idx])
            # visited.remove((ny, nx))
            visited[ny][nx] = False

direction = [(0, -1), (0, 1), (1, 0), (-1, 0)]

info = list(map(int, input().split()))

for i in range(1, 5):
    info[i] /= 100

# visited = set()
# visited.add((0, 0))
visited = [[False] * (2 * info[0] + 1) for _ in range(2 * info[0] + 1)]
visited[info[0]][info[0]] = True

answer = 0

dfs(info[0], info[0], 0, 1)
print(answer)