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
        
        if (ny, nx) not in visited:
            visited.add((ny, nx))
            dfs(ny, nx, cnt + 1, per * info[idx])
            visited.remove((ny, nx))

direction = [(0, -1), (0, 1), (1, 0), (-1, 0)]

info = list(map(int, input().split()))

for i in range(1, 5):
    info[i] /= 100

visited = set()
visited.add((0, 0))
answer = 0

dfs(0, 0, 0, 1)
print(answer)