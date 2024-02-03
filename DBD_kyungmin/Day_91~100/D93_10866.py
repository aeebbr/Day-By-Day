# [BOJ] 10866. 덱
# 풀이 시간 : 05 분 

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
q = deque()

for _ in range(N):
    line = list(input().split())
    command = line[0]

    if command == 'push_front':
        q.appendleft(line[1])
    elif command == 'push_back':
        q.append(line[1])
    elif command == 'pop_front':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif command == 'pop_back':
        if not q:
            print(-1)
        else:
            print(q.pop())
    elif command == 'size':
        print(len(q))
    elif command == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif command == 'front':
        if not q:
            print(-1)
        else:
            front = q.popleft()
            print(front)
            q.appendleft(front)
    elif command == 'back':
        if not q:
            print(-1)
        else:
            rear = q.pop()
            print(rear)
            q.append(rear)