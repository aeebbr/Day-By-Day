import sys
sys.stdin = open("input_1210.txt", "r")

# 우선 순위대로 방향 정렬
# 좌 우 상
    # 좌/우와 상을 동시에 만난 상황이라면 좌/우가 우선되어야 함 
    # 좌와 우를 동시에 만나는 상황은 없으니 좌/우 간 순위는 상관 없음 
dr = [0, 0, -1]
dc = [-1, 1, 0]

for _ in range(10):
    test_num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    cr, cc = 99, 0
    cc = arr[99].index(2)

    # 사다리 타기 시작 
    while cr != 0:
        # 방향 이동
        for dir in range(3):
            nr = cr + dr[dir]
            nc = cc + dc[dir]

            # 이동 조건
            # 범위 내일 것, 이동 지점의 값이 1일 것 
            if 0 <= nr < 100 and 0 <= nc < 100 and arr[nr][nc] == 1:
                cr, cc = nr, nc
                # 방문 처리 
                arr[cr][cc] = 3
            
    print(f"#{test_num} {cc}")
            
'''
# 최적화 전 코드 

# 우 좌 상
dr = [0, 0, -1]
dc = [1, -1, 0]

for _ in range(10):
    test_num = int(input())
    cr, cc = 99, 0
    arr = [list(map(int, input().split())) for _ in range(100)]
    cc = arr[99].index(2)
    
    # 2에서 출발해서 역으로 올라가기
    # 이동 규칙
        # 기본 방향: 위
        # 위로 가다가, 좌 / 우를 만나면 해당 방향으로 이동, 해당 방향 이동 끝나면 위로 방향 바꿔서 이동 
        # 0행에 도달하면 끝 
    dir = 2
    while True:
        # 상 방향이라면 좌우 전환 확인
        if dir == 2:
            for d in range(2):
                nr = cr + dr[d]
                nc = cc + dc[d]
                # 좌 우 사다리 확인
                if 0 <= nr < 100 and 0 <= nc < 100 and arr[nr][nc] == 1:
                    # 방향 전환
                    dir = d
                    cr, cc = nr, nc
                    break
            # 좌우 전환 없다면 상 방향으로 쭉 가기 
            else:
                cr += dr[dir]
                cc += dc[dir]
        # 좌우 방향이라면 해당 방향으로 쭉 가기 
        else:
            nr = cr + dr[dir]
            nc = cc + dc[dir]
            # 현재 방향 끝 도달 확인
            if (0 <= nr < 100 and 0 <= nc < 100 and arr[nr][nc] == 0) or (0 > nc or nc >= 100):
                    # 상 방향으로 전환 
                    dir = 2
                    cr += dr[dir]
                    cc += dc[dir]
            else:
                cr, cc = nr, nc

        if cr == 0:
            print(f"#{test_num} {cc}")
            break
'''