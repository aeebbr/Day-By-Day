# [BOJ] 1174. 줄어드는 수
# 풀이 시간: 20 분
# 실행 시간: 68 ms
# 메모리: 34112 KB

from collections import deque

def bfs():
    queue = deque(list(range(10)))
    cnt = 10
    while queue:
        num = queue.popleft()
        n = num % 10
        for i in range(n):
            cnt += 1
            queue.append(num * 10 + i)

            if cnt == N:
                return queue[-1]

    return -1

N = int(input())
if N <= 10:
    print(N - 1)
else:
    print(bfs())