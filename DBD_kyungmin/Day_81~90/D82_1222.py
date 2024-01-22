# [SWEA] 1222. 계산기1    
# 풀이 시간 : 40 분 

import sys
sys.stdin = open("input_1222.txt", "r")

for test_num in range(1, 11):
    length = int(input())
    str = list(input())
    stack = []
    flag = False
    answer = 0

    # 후위 표기식 생성 
    for i in range(length):
        if flag:
            flag = False
            continue
        cur = str[i]

        if cur == '+':
            next = str[i+1]
            stack.append(next)
            stack.append(cur)
            # i를 한 칸 띄워주기 위한 flag
            flag = True
        else:
            stack.append(cur)
    
    # 후기 표기식 계산 
    for i in range(length-1, -1, -1):
        if flag:
            flag = False
            continue
        cur = stack[i]

        if cur == '+':
            pre = int(stack[i-1])
            # 앞의 문자를 누적 
            answer += pre
            flag = True
        else:
            answer += int(cur)

    print(f"#{test_num} {answer}")

'''
# 후위 표기식 X

for test_num in range(1, 11):
    length = int(input())
    str = input()
    answer = 0

    for i in range(length):
        if i % 2 == 0:
            answer += int(str[i])

    print(f"#{test_num} {answer}")
'''
