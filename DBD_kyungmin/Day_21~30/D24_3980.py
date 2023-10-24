# [BOJ] 3980. 선발 명단
# 풀이 시간: 40 분
# 실행 시간: 124 ms
# 메모리: 31256 KB

# player: 현재 몇 번째 선수인지 
# score: 현재까지의 점수 
def perm(player, score):
    global max_kepa

    # 종료 조건
    # 마지막 선수라면 종료 
    if player == 11:
        # 최대 능력치 갱신
        max_kepa = max(max_kepa, score)
        return 
    
    # 각각의 모든 포지션 탐색 
    for i in range(11):
        # 가지 치기 
        # 해당 포지션에 선수가 이미 배치되어 있거나, 현재 선수는 해당 포지션 능력치가 0이라면 패스 
        if visited[i] or not kepa[player][i]:
            continue 

        # 방문 체크
        visited[i] = 1

        # 재귀 호출
        perm(player + 1, score + kepa[player][i])

        # 방문 체크 되돌리기 
        visited[i] = 0

# 입력
C = int(input())

# 하나의 케이스는 11개
# 각 케이스 별로 입력받기 
for i in range(C):
    # 능력치 
    kepa = [list(map(int, input().split())) for _ in range(11)]

    max_kepa = 0
    # 선수가 포지션에 있는지 방문 확인(해당 포지션이 선수가 선택된 포지션인지 확인)
    visited = [0] * 11

    # 순열 함수 호출
    # 첫번째 선수부터 
    perm(0, 0)

    # 현재 케이스의 최대치 출력
    print(max_kepa)
