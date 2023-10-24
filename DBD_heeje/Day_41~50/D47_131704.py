# [Programmers] 131704. 택배상자
# 풀이 시간 : 00 분

def solution(order):
    stack = []
    answer = 0
    idx = 1

    for o in order:
        if o >= idx:
            stack.extend(range(idx, o))
            idx = o + 1
            answer += 1
        else:
            if stack[-1] == o:
                stack.pop()
                answer += 1
            else:
                break
    return answer