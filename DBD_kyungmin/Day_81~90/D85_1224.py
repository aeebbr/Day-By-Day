# [SWEA] 1224. 계산기3  
# 풀이 시간 : 20 분 

import sys
sys.stdin = open("input_1224.txt", "r")

# 연산자 우선순위 
def priority(s):
    if s == '*':
        return 2
    elif s == '+':
        return 1
    return 0
    
for test_num in range(1, 11):
    length = int(input())
    str = list(input())
    after = [] # 후위표기식
    stack = []

    # 후위 표기식 생성 
    for i in range(length):
        cur = str[i]
        
        # 연산자라면
        if cur == '*' or cur == '+':
            # 스택이 비었다면 
            if len(stack) == 0:
                stack.append(cur)
                continue
            
            top = stack.pop()
            
            if priority(top) > priority(cur):
                # top을 식에 삽입, 
                after.append(top)
                # 순위가 높은 top 연산자를 삽입한 뒤에, stack에 남아있던 모든 연산자를 식에 삽입 
                while len(stack) != 0:
                    tmp_top = stack.pop()
                    if tmp_top == '(':
                        stack.append(tmp_top)
                        break
                    after.append(tmp_top)
                    
            elif priority(top) == priority(cur):
                # top을 식에 넣고, cur를 stack에 
                after.append(top)
            else:
                # top을 다시 스택에 넣기 
                stack.append(top)
            
            # 현재 연산자를 스택에 넣기 
            stack.append(cur)

        # 괄호라면 
        elif cur == '(' or cur == ')':
            if cur == '(':
                stack.append(cur)
            elif cur == ')':
                # 여는 괄호가 나올 때까지 stack에 남은 연산자 모두 식에 삽입 
                    # 이 때, 괄호는 식에 삽입하지 않음
                while True:
                    top = stack.pop()
                    if top == '(':
                        break
                    after.append(top)

        else: 
            after.append(cur)

    # stack에 남아있는 연산자 전부 식에 삽입 
    while len(stack) != 0:
        after.append(stack.pop())

    # for j in after:
    #     print(j, end="")
    # print()

    # 후위 표기식 계산 
    for i in range(len(after)):
        cur = after[i]

        
        if cur == '*' or cur == '+':
            top = stack.pop()
            if cur == '*':
                stack.append(top * stack.pop())
            elif cur == '+':
                stack.append(top + stack.pop())
        else:
            stack.append(int(cur))
        
    print(f"#{test_num} {stack[0]}")