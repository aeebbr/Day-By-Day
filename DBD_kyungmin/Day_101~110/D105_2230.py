# [BOJ] 2230. 수 고르기   
# 풀이 시간 : 40 분 

# 투 포인터 
import sys
input = sys.stdin.readline

answer = float("inf")

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

end = 0

for start in range(N):
    while end < N and arr[end] - arr[start] < M:
        end += 1
    if end == N:
        break
    
    answer = min(answer, arr[end] - arr[start])

print(answer)

'''
# 이분 탐색 
import sys
input = sys.stdin.readline

def binary_search(target):
    # 시작, 끝 인덱스 
    start, end = 0, len(arr)-1
    while start <= end:
        mid = (start+end) // 2
        # mid에 따라서 조정
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            # target found
            return True
    return False
        
N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

while True:
    for i in range(N):
        if binary_search(arr[i] + M):
            print(M)
            exit(0)
    M += 1
'''
