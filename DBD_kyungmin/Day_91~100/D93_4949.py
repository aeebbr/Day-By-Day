# [BOJ] 4949. 균형잡힌 세상     
# 풀이 시간 : 10 분 

import sys
input = sys.stdin.readline

open_bracket = ['(', '[']
close_bracket = [')', ']']

def bracket_test(line):
    stack = []

    for s in line:
        if s in open_bracket:
            stack.append(s)
        elif s in close_bracket:
            if len(stack) == 0 or close_bracket[open_bracket.index(stack.pop())] != s:
                return False
    else:
        return True if len(stack) == 0 else False

while True:
    line = input().rstrip()

    if line == '.': break

    print("yes") if bracket_test(line) else print("no")