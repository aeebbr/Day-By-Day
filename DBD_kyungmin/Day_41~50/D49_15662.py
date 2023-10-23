# [BOJ] 15662. 톱니바퀴 (2)
# 풀이 시간 : 00 분

# 맞닿아있는 위치 (0부터): 2, 6번째 
# 2번은 6번과, 6번은 2번과 맞닿아있음 
# 인접한 두 리스트의 2번과 6번 확인 ~~~ 

# 움직이는 톱니 숫자를 큐에 집어넣고 순회하면서 돌리기 

# 회전은 덱 사용(로테이트 메소드)
from collections import deque

T = int(input())
wheel = []

for i in range(T):
    q = deque(map(int, input()))
    wheel.append(q)

K = int(input())
rotated = [list(map(int, input().split())) for _ in range(K)]

# 회전 조건 돌기 
for i in range(K):
    # 회전 바퀴 번호, 방향 
    num, dir = rotated[i]
    num -= 1

    # 회전하는 바퀴들 큐
    tmp_q = deque()
    q = deque()
    tmp_q.append((num, dir))
    q.append((num, dir))
    visited = [False] * T
    visited[num] = True

    # 큐에 없을 때까지 순회 
    while tmp_q:
        cur_n, cur_d = tmp_q.popleft()
        # 인접바퀴 탐색
        # 인접 바퀴가 회전해야 한다면 큐에 (넘버, 방향)으로 넣기 

        # 현재 바퀴의 6번 vs 현재 바퀴 - 1의 2번
        if cur_n != 0:
            left_n = cur_n-1

            if not visited[left_n]:
                cur_6 = wheel[cur_n][6]
                left_2 = wheel[left_n][2]

                # 서로 다른 극이라면 회전 바퀴에 삽입
                if cur_6 != left_2:
                    if cur_d == 1: 
                        left_d = 0 
                    else:
                        left_d = 1 

                    tmp_q.append((left_n, left_d))
                    q.append((left_n, left_d))
                    visited[left_n] = True

        # 현재 바퀴의 2번 vs 현재 바퀴 + 1의 6번
        if cur_n != T - 1:
            right_n = cur_n+1

            if not visited[right_n]:
                cur_2 = wheel[cur_n][2]
                right_6 = wheel[right_n][6]

                # 서로 다른 극이라면 회전 바퀴에 삽입
                if cur_2 != right_6:
                    if cur_d == 1: 
                        right_d = 0 
                    else:
                        right_d = 1 

                    tmp_q.append((right_n, right_d))
                    q.append((right_n, right_d))
                    visited[right_n] = True

    # 바퀴 돌리기 
    while q:
        n, d = q.popleft()

        # 시계
        if d == 1:
            wheel[n].rotate(1)
        # 반시계
        else:
            wheel[n].rotate(-1)
            
cnt= 0
for w in wheel:
    if w[0] == 1:
        cnt += 1

print(cnt)