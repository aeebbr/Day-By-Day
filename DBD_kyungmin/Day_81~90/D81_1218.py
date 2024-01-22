# [SWEA] 1218. 괄호 짝짓기    
# 풀이 시간 : 20 분 

import sys
sys.stdin = open("input_1218.txt", "r")

open_bracket = ['(', '[', '{', '<']
close_bracket = [')', ']', '}', '>']

def test_validation(length, arr):
    stack = []
    for i in range(length):
        cur = arr[i]

        if cur in open_bracket:
            stack.append(cur)
        else:
            if not stack:
                return 0

            top = stack.pop()
            index = open_bracket.index(top)
            if cur != close_bracket[index]:
                return 0
    return 1


for test_num in range(1, 11):
    length = int(input())
    arr = list(input())
    stack = []
    
    print(f"#{test_num} ", end="")
    print(test_validation(length, arr))