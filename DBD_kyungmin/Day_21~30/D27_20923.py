# [BOJ] 20923. 숫자 할리갈리 게임
# 풀이 시간: 90++ 분
# 실행 시간: 472 ms
# 메모리: 146980 KB

from collections import deque

def win():
    if len(do_deque) == len(su_deque):
        print("dosu")
    elif len(do_deque) > len(su_deque):
        print("do")
    else:
        print("su")

    exit(0)

def game():
    open = 0

    for round in range(M):
        # 짝수 라운드 => 도도 턴
        # 홀수 라운드 => 수연 턴
        if round % 2 == 0:
            # 도도 턴
            # 도도 카드 내려놓기 
            if len(do_deque) > 1:
                open = do_deque.pop()
            # 이 때 덱의 길이가 1이라면 카드를 냈을 때 개수가 0이 될 것
            elif len(do_deque) == 1:
                print("su")
                exit(0)

            # 도도 그라운드에 삽입
            do_ground.append(open)
        else:
            # 수연 턴
            if len(su_deque) > 1:
                open = su_deque.pop()
            elif len(su_deque) == 1:   
                print("do")
                exit(0)

            # 수연 그라운드에 삽입
            su_ground.append(open)

        # 그라운드 확인
        do_top = 0
        su_top = 0
        if len(do_ground):
            do_top = do_ground.pop()
        if len(su_ground):
            su_top = su_ground.pop()

        # 도도 종 치기 조건
        if do_top == 5 or su_top == 5:
            # 도도 종 치기 
            # 수연 그라운드 가져오기 
            while su_ground:
                do_deque.appendleft(su_ground.popleft())
            if su_top:
                do_deque.appendleft(su_top)

            # 도도 그라운드 가져오기 
            while do_ground:
                do_deque.appendleft(do_ground.popleft())
            if do_top:
                do_deque.appendleft(do_top)
            
        # 수연 종 치기 조건
        # 그라운드가 비어있지 않아야 함(그라운드에서 top을 뺀 상태이니 top이 0이라면 비어있는 그라운드임)
        elif do_top and su_top and do_top + su_top == 5:
            # 수연 종 치기 
            # 도도 그라운드 가져오기 
            while do_ground:
                su_deque.appendleft(do_ground.popleft())
            if do_top:
                su_deque.appendleft(do_top)

            # 수연 그라운드 가져오기 
            while su_ground:
                su_deque.appendleft(su_ground.popleft())
            if su_top:        
                su_deque.appendleft(su_top)
        # 누구도 종을 치지 않았다면 top을 다시 각 그라운드에 넣기 
        else:
            if do_top:
                do_ground.append(do_top)
            if su_top:
                su_ground.append(su_top)

        # 다음 라운드로

    win()

# 입력
N, M = map(int, input().split())

# 도도 덱
do_deque = deque()
# 수연 덱
su_deque = deque()

# 도도 그라운드 
do_ground = deque()
# 수연 그라운드 
su_ground = deque()

for _ in range(N):
    a, b = map(int, input().split())
    do_deque.append(a)
    su_deque.append(b)

game()