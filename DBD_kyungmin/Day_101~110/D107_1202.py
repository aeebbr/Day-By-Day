# [BOJ] 1202. 보석 도둑    
# 풀이 시간 : 40 분 

# heapq
import sys
input = sys.stdin.readline
import heapq

answer = 0
N, K = map(int, input().split())
# 보석: heapq
jew = []
for _ in range(N):
    # 무게가 작은 것부터 
    heapq.heappush(jew, list(map(int, input().split()))) # 무게, 가격 

# 가방 
bag = [int(input().rstrip()) for _ in range(K)]
# 가방 오름차순 
bag.sort()

# 가능한 모든 보석의 가격 담기 
    # heapq, 가격이 높은 것부터 
    # 이전 가방에서 담겼던 가격들이 다음 턴에도 유지됨 
        # (작은 가방, 작은 보석 순으로 순회하기 때문에 이전 턴에서 통과된 보석은 다음 가방에도 담길 수 있기 때문)
available_price = []

# 가방 순회 
for b in bag:
    # 가방보다 큰 보석이 나타다면 탈출(이후의 보석들도 클테니까 더 볼 필요 없음)
    while jew and b >= jew[0][0]:
        # 현재까지의 가장 작은 보석의 가격 담기 
            # 이 때, 가격이 높은 것부터 담겨야 함 
        heapq.heappush(available_price, -heapq.heappop(jew)[1])

    # 가능한 보석이 있다면
    if available_price:
        # 최대힙이기 때문에 첫번째가 무조건 최대 가격임
        max_price = -heapq.heappop(available_price)
        # answer에 누적 
        answer += max_price

    # 가능한 보석이 없는데 jew에 남은 것도 없다면 탈출 
    elif not jew:
        break
    
print(answer)
    
'''
# 시간 초과 
import sys
input = sys.stdin.readline

answer = 0
N, K = map(int, input().split())
# 보석
arr = [list(map(int, input().split())) for _ in range(N)]
# 가방 
bag = [int(input().rstrip()) for _ in range(K)]

# 가방 오름차순 
bag.sort()
# 보석 가격 기준 내림차순
arr = sorted(arr, key = lambda x: x[1], reverse=True)

# 가방 순회 
for b in bag:
    # 가방보다 작거나 같다면 
    for i in range(len(arr)):
        weight, price = arr[i] # 무게, 가격

        # 성공
        if b >= weight:
            # 총 가격 증가 
            answer += price
            # 현재 보석 지우기 
            del arr[i]
            # 다음 가방으로 
            break
    # else: 현재 가방에 맞는 보석 없음, 다음 가방으로 

print(answer)
'''