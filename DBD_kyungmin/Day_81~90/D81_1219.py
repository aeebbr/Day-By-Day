# [SWEA] 1219. 길 찾기     
# 풀이 시간 : 20 분 

import sys
sys.stdin = open("input_1219.txt", "r")

def dfs(cur):
    if cur == 99:
        return 1

    for i in range(len(linked_list[cur])):
        if dfs(linked_list[cur][i]): return 1
    return 0

for _ in range(10):
    test_num, length = map(int, input().split())
    input_data = list(map(int, input().split()))
    linked_list = [[] for _ in range(100)] 

    for i in range(length * 2):
        if i % 2 != 0:
            continue
        linked_list[input_data[i]].append(input_data[i+1])

    print(f"#{test_num} {dfs(0)}")