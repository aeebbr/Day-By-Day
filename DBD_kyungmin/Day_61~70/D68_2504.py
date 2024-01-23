# [BOJ] 2504. 괄호의 값    
# 풀이 시간 : 90++ 분 

'''
[()[]] 라면, 
3 * (2 + 3)를 (3 * 2) + (3 * 3)으로 생각해서 구현하기 
'''

open_b = ['', '', '(', '[']
close_b = ['', '', ')', ']']

brackets = list(input())
stack = []
answer = 0
tmp = 1

for i in range(len(brackets)):
    cur = brackets[i]

    if cur in open_b:
        stack.append(cur)
        # 여는 괄호라면 무조건 곱하기 
        tmp *= open_b.index(cur)
    else: # 닫는 괄호 
        if not stack:
            answer = 0
            break

        top = stack.pop()
        type = open_b.index(top) # 스택에 있는 여는 괄호의 종류  

        # 괄호 쌍이 맞지 않다면
        if cur != close_b[type]: 
            answer = 0
            break

        # 괄호 쌍이 맞다면 
        # 직전의 괄호가 여는 괄호라면 => 현재 괄호 안에 괄호가 없다면 answer에 값 누적하기 
            # 현재 괄호: 닫는 괄호, 직전 괄호: 여는 괄호, ex: []
        if brackets[i-1] in open_b:
            answer += tmp

        # 괄호 쌍이 맞다면, 괄호 열 때 곱했던 수를 나눠서 tmp를 원상복구 시키기 
        tmp //= type

if stack:
    print(0)
else:
    print(answer)
