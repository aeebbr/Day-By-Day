# [BOJ] 1405. 미친 로봇
# 풀이 시간 : 90++ 분

# 단순한 경우: 같은 곳을 다시 방문하지 않는 경우 
# 최대 14번 이동 => 29 * 29 visited
# 해당 방향으로의 확률이 0이 아니라면 확률 계산하면서 일단 고

# 동 서 남 북 
# 우 좌 하 상
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def recur(cnt, cr, cc, percent): 
    global answer 

    if cnt == N:
        # print(percent)
        answer += percent
        return 
    
    for dir in range(4):
        if P[dir] == 0:
            continue

        nr = cr + dr[dir]
        nc = cc + dc[dir]

        # 조건 확인 
        # 방문한 곳이라면 탈락 
        if visited[nr][nc]:
            continue

        # 이동 
        visited[nr][nc] = True
        
        recur(cnt + 1, nr, nc, percent * P[dir])
        visited[nr][nc] = False

visited = [[False] * 29 for _ in range(29)]
visited[14][14] = True

tmp = list(map(int, input().split()))
N = tmp[0]
P = tmp[1:]
answer = 0

for i in range(4):
    P[i] *= 0.01

recur(0, 14, 14, 1)
print(answer)