# [BOJ] 17825. 주사위 윷놀이
# 풀이 시간: 00 분
# 실행 시간: 00 ms
# 메모리: 00 KB

from copy import deepcopy

def play(n, score, horse):
    global max_score

    # 종료 조건: 모든 게임의 턴(총 10턴)이 끝났을 때 
    if n == 10: 
        if score > max_score:
            # 최대 점수 갱신
            max_score = score
        return
    
    # 모든 말 각각 탐색
    for h in range(4):
        # 도착 지점의 말이 아닌 경우
        if horse[h][0] != -1: 
            # 말 정보 카피 
            temp = deepcopy(horse)
            temp[h][0] += dice[n] # 주사위만큼 이동하기

            # 파란 지점이라면
            if temp[h][1] == 0:
                # 점수가 10인 지점
                if temp[h][0] == 5: 
                    temp[h][1] = 1 # road[1]의 길을 가기 때문에
                    temp[h][0] = 0
                # 점수가 20인 지점
                elif temp[h][0] == 10: 
                    temp[h][1] = 2 # road[2]의 길을 가기 때문에
                    temp[h][0] = 0
                # 점수가 30인 지점
                elif temp[h][0] == 15: 
                    temp[h][1] = 3 # road[3]의 길을 가기 때문에
                    temp[h][0] = 0

            # 도착지점이라면
            if temp[h][0] >= len(road[temp[h][1]]):
                # 말이 도착 체크 
                temp[h][0] = -1 
                play(n + 1, score, temp)
            # 도착 지점이 아니라면
            else:
                # 이동할 곳에 말이 있으면 이동 X
                frag = False # 이동 지점에 말이 있는지 체크할 변수
                visit = road[temp[h][1]][temp[h][0]] # 움직이려는 말이 있는 점수판의 점수

                # 말 정보 탐색
                for v in range(len(temp)):
                    # 도착 지점한 말이라면 패스 
                    if temp[v][0] == -1: continue 

                    if v != h and visit == road[temp[v][1]][temp[v][0]]:
                        if visit == 30: 
                            if temp[h] == [0, 3] and temp[v] == [0, 3]:
                                frag = True
                                break
                            elif temp[h] != [0, 3] and temp[v] != [0, 3]:
                                frag = True
                                break
                        elif visit in [16, 22, 24, 26, 28]: 
                            if temp[h] == temp[v]:
                                frag = True
                                break
                        else: 
                            frag = True
                            break

                # 이동하려는 칸에 이미 다른 말이 있다면 패스 
                if frag: 
                    continue

                play(n + 1, score + road[temp[h][1]][temp[h][0]], temp)

# road : 게임판의 점수를 저장한 리스트
road = [
    [i * 2 for i in range(21)],
    [10, 13, 16, 19, 25, 30, 35, 40],
    [20, 22, 24, 25, 30, 35, 40],
    [30, 28, 27, 26, 25, 30, 35, 40]
]

# 전체의 최댓값
max_score = 0 

# 말 정보 
# 해당 road 인덱스(위치), road
horse = [[0, 0] for _ in range(4)] 

dice = list(map(int, input().split()))

# 완탐
# 모든 경우의 윷놀이 진행하는 경우 
play(0, 0, horse) 

print(max_score)