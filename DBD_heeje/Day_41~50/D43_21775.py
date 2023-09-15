# [BOJ] 21775. 가희와 자원 놀이
# 풀이 시간 : 00 분

from collections import deque
import sys
input = sys.stdin.readline

N, T = map(int, input().split())
turns = list(map(int, input().split()))
deck = deque(input().split() for _ in range(T))
resources = [set() for _ in range(N + 1)]
hands = [[] for _ in range(N + 1)]
r_set = set()
answer = []

for turn in turns:
    if hands[turn]:
        card = hands[turn]
    else:
        card = deck.popleft()
    answer.append(card[0])
    if card[1] == "acquire":
        if card[2] in r_set and card[2] not in resources[turn]:
            hands[turn] = card[:]
        else:
            r_set.add(card[2])
            resources[turn].add(card[2])
            hands[turn] = []
    elif card[1] == "release":
        hands[turn] = []
        resources[turn].remove(card[2])
        r_set.remove(card[2])

print(*answer, sep="\n")