# [BOJ] 3980. 선발 명단
# 풀이 시간: 10 분
# 실행 시간: 116 ms
# 메모리: 31256 KB

import sys
input = sys.stdin.readline

def dfs(idx, position:set, power):
    if idx == 11:
        max_power_list[tc] = max(max_power_list[tc], power)
        return

    for i in range(11):
        if players[idx][i] != 0 and i not in position:
            position.add(i)
            dfs(idx + 1, position, power + players[idx][i])
            position.remove(i)


T = int(input())
max_power_list = [0] * T
for tc in range(T):
    players = [list(map(int, input().split())) for _ in range(11)]
    dfs(0, set(), 0)

print(*max_power_list, sep="\n")