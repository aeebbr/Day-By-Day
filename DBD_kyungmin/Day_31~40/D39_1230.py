# [Swea] 1230. 암호문3
# 풀이 시간: 90 분

import sys
sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline()

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input().rstrip())
    crypto = list(map(int, input().split()))
    cnt = int(input().rstrip())
    command = list(input().split())

    # 각 명령어 확인 
    # 명령어의 시작 찾기 
    idx = 0
    while idx < len(command):
        # 명령어의 시작
        cur = command[idx] 
        
        if cur == 'I':
            x = int(command[idx + 1])
            y = int(command[idx + 2])
            s = command[idx+3:idx+3+y]

            front = crypto[:x+1]
            back = crypto[x+1:]

            front.extend(s)
            front.extend(back)
            crypto = front

            idx += (3 + y)
        elif cur == 'D':
            x = int(command[idx + 1])
            y = int(command[idx + 2])

            del crypto[x+1:x+y+1]

            idx += 3
        elif cur == 'A':
            y = int(command[idx + 1])
            s = command[idx+2:idx+2+y]

            crypto.extend(s)
            
            idx += (2 + y)

    print(f"#{test_case} ", end="")
    for i in range(1, 11):
        print(crypto[i], end=" ")
    print()
