# [SWEA] 1228. 암호문1  
# 풀이 시간 : 30 분 

import sys
sys.stdin = open("input_1228.txt", "r")

for test_num in range(10):
    N = int(input())
    origin = list(input().split())
    commd_cnt = int(input())
    tmp_commd = list(input().split())
    commd = []

    one_commd = []
    for s in tmp_commd:
        if s == 'I' and one_commd:
            commd.append(one_commd)
            one_commd = [s]
            continue

        one_commd.append(s)
    commd.append(one_commd)

    for c in commd:
        x = int(c[1])
        y = int(c[2])
        s = c[3:]

        left = origin[:x]
        right = origin[x:]
        origin = left
        origin.extend(s)
        origin.extend(right)

    print(f"#{test_num+1} ", end="")
    for i in range(10):
        print(origin[i], end=" ")
    print()