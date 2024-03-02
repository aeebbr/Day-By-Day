# [BOJ] 2295. 수 찾기   
# 풀이 시간 : 60 분 

# 세 개를 고르는 방법을 중첩 반복문이 아닌, 이분탐색으로 고르기 
    # 이 때, 타겟이 되는 수는 뭐지...? 
    # 타겟은 큰 수부터 작은 수로 순회 
    # 타겟 = 10이라면, 세 개의 범위는 10보다 작은 수들이며 해당 범위 내에서 세 개를 고른다. 그리고 세 수의 합이 타겟이 되어 배열 안에 있는지 확인 

'''
a + b + c = d
target = d 일 때, 
d - c = a + b

2, 3, 5, 10, 18을 
두 개씩 합한 배열: [5, 7, 12, 20, 8, 13, 21, 15, 23, 28]

target = 18 일 때, 범위: 2, 3, 5, 10
18 - 2 = 16이 있나? => 16을 나머지 수 중 두 개의 조합으로 만들 수 있나? 
18 - 3 = 15? => 있음! 3 + (5 + 10) = 18
'''
import sys
input = sys.stdin.readline

def binary_search(target):
    start, end = 0, len(sum_arr) - 1

    while start <= end:
        mid = (start+end) // 2

        if sum_arr[mid] < target:
            start = mid + 1
        elif sum_arr[mid] > target:
            end = mid - 1
        else:
            return True
        
    return False

N = int(input())
U = [int(input()) for _ in range(N)]
sum_arr = []

for i in range(N):
    for j in range(i, N): # 중복 선택이 가능한 것을 유의해서 범위 잡기  
        sum_arr.append(U[i] + U[j])

U.sort()
sum_arr.sort()

# 큰 수부터 순회 
for u in range(N-1, -1, -1): # target
    for i in range(u):
        if binary_search(U[u] - U[i]):
            print(U[u])
            exit(0)
