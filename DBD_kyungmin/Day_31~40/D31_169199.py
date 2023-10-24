# [Programmers] 169199. 리코쳇 로봇
# 풀이 시간: 70 분

from collections import deque

# bfs
def solution(board):
    # 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    N = len(board)
    M = len(board[0])
    
    # bfs 함수 
    def bfs(sr, sc):
        # 큐 초기화 
        q = deque()
        # 방문 배열 초기화
        # 방문 배열에 이동 횟수 카운트 
        visited = [[0] * M for _ in range(N)]
        
        q.append((sr, sc))
        # 시작 지점은 이동 횟수가 0이어야 하지만, 시작 지점의 방문 처리를 위해 1로 설정
        visited[sr][sc] = 1
        
        while q:
            # 큐에서 하나 빼기 
            cr, cc = q.popleft()
            
            # 종료 지점이라면 
            if board[cr][cc] == 'G':
#                 for k in visited:
#                     print(k)
                # 시작을 1로 시작했기 때문에 1 빼주기
                return visited[cr][cc] - 1
            
            # 사방 탐색
            for dir in range(4):
                nr = cr
                nc = cc
                
                # 현재에서부터 한번 쭉 직진할 수 있는 끝 지점만 찾기
                # 끝 지점만 큐에 넣기
                # (직진하는 중간 지점들을 넣으면, 그 지점들에 대한 사방 탐색이 이루어지기 때문)
                
                # 조건에 맞는다면 현재 방향으로 쭉 직진
                while True:
                    # 한 칸 이동
                    nr += dr[dir]
                    nc += dc[dir]
                                        
                    # 1. 탐색 지점이 이동할 수 있는 곳인가? 
                    # 2. 탐색 지점이 이동할 수 없는 곳인가?: 탐색 지점이 범위 외거나, D인 경우 
                    # 3. 탐색 지점이 (직진)이동을 끝내는 곳인가?: while문 밖(쭉 직진할 경로를 뚫은 상태)
                    # => 2번과 3번의 구분이 중요함 
                    
                    # 조건 확인
                    # 범위 외
                    if 0 > nr or nr >= N or 0 > nc or nc >= M:
                        # 이동 안 함, 이동 되돌리기 
                        nr -= dr[dir]
                        nc -= dc[dir]
                        
                        break
                    # 장애물
                    elif 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 'D':
                        # 이동 안 함, 이동 되돌리기 
                        nr -= dr[dir]
                        nc -= dc[dir]
                        
                        break
                        
                    # 이동 안 한다면 nr nc는 한 칸 이전의 지점이 되면서 while 탈출 => 이 지점이 방문하지 않은 지점이라면 끝 지점이 됨
                    
                # 직진 끝       
                # 미방문한 곳이라면
                if not visited[nr][nc]:
                    # 이동 
                    q.append((nr, nc))
                    visited[nr][nc] = visited[cr][cc] + 1

        return -1                    
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                return bfs(i, j)