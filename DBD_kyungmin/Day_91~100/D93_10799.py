# [BOJ] 10799. 쇠막대기  
# 풀이 시간 : 20 분 

# 인접한 쌍 => 레이저를 의미 
# 인접하지 않고, 사이에 다른 괄호들을 둔 쌍 => 쇠막대기의 양쪽 끝을 의미 

# 여는 괄호 => 쇠의 개수 1 증가 

# 닫는 괄호 => 해당 괄호의 -1번째 괄호가 여는 괄호라면 
    # 레이저 닫는 괄호 => 쇠의 개수 1 감소(여는 괄호로 증가시킨 쇠의 개수 무마하기), 현재 남아있는 쇠의 개수만큼 증가 
# 아니라면 
    # 쇠의 끝 닫는 괄호 => 아무 일도 일어나지 않음 

# 스택 사용하지 않음 
brackets = list(input())
cur_stick_cnt = 0
total_stick_cnt = 0

for i in range(len(brackets)):
    if brackets[i] == '(':
        cur_stick_cnt += 1
        total_stick_cnt += 1
    else:
        cur_stick_cnt -= 1
        # 레이저 닫는 괄호
        if brackets[i-1] == '(':
            # 현재 남아있는 쇠막대의 개수를 모두 반영 and 여는 괄호로 증가시킨 쇠 개수 1 무마 
            total_stick_cnt += cur_stick_cnt - 1

print(total_stick_cnt)

'''
# 스택 사용 
brackets = list(input())
stack = []
total_stick_cnt = 0

for i in range(len(brackets)):
    if brackets[i] == '(':
        stack.append('(')
        total_stick_cnt += 1
    else:
        stack.pop()
        # 레이저 닫는 괄호
        if brackets[i-1] == '(':
            # 현재 남아있는 쇠막대의 개수를 모두 반영 and 여는 괄호로 증가시킨 쇠 개수 1 무마 
            total_stick_cnt += len(stack) - 1

print(total_stick_cnt)
'''