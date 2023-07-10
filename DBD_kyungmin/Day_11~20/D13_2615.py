# [BOJ] 2615. 오목
# 풀이 시간: 00 분
# 실행 시간: 44 ms
# 메모리: 31256 KB

# 탐색하다가 바둑알이 나오면 바둑알 카운트 시작
# 발견한 바둑알을 기준으로 사방, 대각선으로 탐색

# 카운트
# 카운트가 5라면, 육목 확인

# cr: 현재 행, cc: 현재 열
def findOmok(cr, cc): 
    # 현재 바둑알 
    target = board[cr][cc]

    # 사방(우, 하, 우하, 우상) 탐색
    # 사방인 총 네 번 반복
    for dir in range(4):
        # 같은 색 바둑알 카운트 
        # 이미 바둑알 하나가 발견되어 이 함수가 호출된 것이므로 초기 카운트 1
        cnt = 1

        # 이동한 위치
        nr = cr + dr[dir]
        nc = cc + dc[dir]

        # 오목 판별
        # 조건: 1) 이동 위치가 바둑판 범위 내인가, 2) 같은 색의 바둑알인가
        # 오목을 판별하는 이 반복문에서 바둑알 카운트를 해야 함
        while 0 <= nr < 19 and 0 <= nc < 19 and board[nr][nc] == target:
            # 조건에 부합한다면 카운트 증가
            cnt += 1

            # 오목이 되었다면 
            if cnt == 5:
                # 육목 판별
                # 1) 탐색 위치가 바둑판 범위 내인가
                # 2) 현재 탐색 방향, 역방향으로 같은 색의 바둑알이 있는가
                # 역방향
                if 0 <= cr - dr[dir] < 19 and 0 <= cc - dc[dir] < 19 and board[cr - dr[dir]][cc - dc[dir]] == target:
                    # 육목이라면 탐색 종료, 실패 
                    break
                if 0 <= nr + dr[dir] < 19 and 0 <= nc + dc[dir] < 19 and board[nr + dr[dir]][nc + dc[dir]] == target:
                    # 육목이라면 탐색 종료, 실패 
                    break

                # 육목이 아니라, 오목임
                print(target)
                print(cr + 1, cc + 1)
                exit(0)

            # 오목 카운트까지 올라가지 않았다면(아직 탐색 중이라면) 이동 방향으로 계속 이동
            nr += dr[dir]
            nc += dc[dir]

# 사방 
# 우 하 우하 우상
dr = [0, 1, 1, -1]
dc = [1, 0, 1, 1]

board = []

for i in range(19):
    board.append(list(map(int, input().split())))

# 바둑알 찾기 
for i in range(len(board)):
    for j in range(len(board[i])):
        # 바둑알 발견 
        if board[i][j] != 0:
            findOmok(i, j)

# 무승부
print(0)