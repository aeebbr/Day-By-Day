# [SWEA] 1223. 계산기2  
# 풀이 시간 : 30 분 

import sys
sys.stdin = open("input_1223.txt", "r")

def priority(s):
    # 연산자의 순위 리턴
    if s == '*':
        return 2
    elif s == '+':
        return 1
    return 0

for test_num in range(1, 11):
    length = int(input())
    str = list(input())
    after = []
    stack = []
    answer = 0

    # 후위 표기식 생성
    for i in range(length):
        cur = str[i]

        if cur == '*' or cur == '+':
            if len(stack) == 0:
                stack.append(cur)
                continue
            
            top = stack.pop()
            
            # 연산자 순위 계산해서 스택의 연산자를 삽입할지 말지 결정 
            if priority(top) > priority(cur): # top이 현재보다 높다면  
                after.append(top)      
                # 스택에 남은 (낮은 등급의) 연산자 모두 식에 넣기 
                while len(stack) != 0:
                    after.append(stack.pop())
            elif priority(top) == priority(cur): # top과 현재가 동등하다면
                after.append(top)
            else: # top이 현재보다 낮다면
                stack.append(top) # 도로 스택에 집어넣기 

            # 연산자 순위 관계 없이 현재는 무조건 stack에 삽입 
            stack.append(cur)
        else:
            after.append(cur)

    while len(stack) != 0:
        top = stack.pop()
        after.append(top)

    # 후위 표기식 계산 
    for i in range(length):
        cur = after[i]

        if cur == '*': 
            top = int(stack.pop())
            top *= int(stack.pop())
            stack.append(top)
        elif cur == '+':
            top = int(stack.pop())
            top += int(stack.pop())
            stack.append(top)
        else:
            stack.append(cur)

    print(f"#{test_num} {stack[0]}")
            
        
