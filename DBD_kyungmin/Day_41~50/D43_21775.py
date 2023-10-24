# [BOJ] 21775. 가희와 자원 놀이
# 풀이 시간 : 00 분

import sys 
input = sys.stdin.readline

N, T = map(int, input().split())
person = list(map(int, input().split()))
card = [list(input().split()) for _ in range(T)]

# 사람별로 가지고 있는 연산 카드를 저장 
# 1번 인덱스 = 1번 사람 
command_dic = {0:[]}
for i in range(1, N+1):
    command_dic[i] = []
get_card = set()

# 0번 인덱스를 가장 위에 있는 카드로 
card = card[::-1]

for i in range(T):
    # 현재 사람 
    cur_person = person[i]

    # 가지고 있는 연산 카드가 없다면 
    if command_dic[cur_person] == []:
        # 연산 카드 뽑기 
        top = card.pop()
    # 연산 카드가 있다면 
    else:
        # 한 사람당 연산 카드를 2개 이상 가질 수 없음
            # 가지고 있는 연산 카드를 사용해야만 새 연산 카드를 뽑을 수 있기 때문 
        # 연산 카드 제거  
        top = command_dic[cur_person].pop()

    c_id = top[0]
    command = top[1]
    if len(top) == 3:
        n = top[2]
    
    if command == 'acquire':
        # 다른 사람에게 n이 있는지 확인 
        if n in get_card:
            # 연산 카드 가지기 
            command_dic[cur_person].append(top)
        else:
            # 자원 카드 가지기 
            get_card.add(n)

    elif command == 'release':
        # 가지고 있는 n 자원 카드 버리기 
        get_card.remove(n)

    print(c_id)