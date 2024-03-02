# [BOJ] 1920. 수 찾기   
# 풀이 시간 : 15 분 

# 이중 반복문이 아니라, 이분탐색으로 풀어서 시간 복잡도를 낮추기 
import sys 
input = sys.stdin.readline

def binary_search(target):
    # 시작, 끝 인덱스 
    start, end = 0, N-1

    # 시작, 끝 인덱스가 역전되지 않는다면 반복
    while start <= end: # start = end = mid = target인 경우가 있기 때문에 start == end도 포함 
        # 중간값
        mid = (start+end) // 2

        # mid를 따져서 시작, 끝을 조절
        if Ns[mid] < target:
            # mid가 target보다 왼쪽에 있다면 범위 오른쪽으로 -> start를 증가 
            start = mid + 1
        elif Ns[mid] > target:
            # mid가 target보다 오른쪽에 있다면 범위 왼쪽으로 -> end를 감소 
            end = mid - 1
        else:
            # 성공 
            return 1
        
    return 0

N = int(input())
Ns = list(map(int, input().split()))
M = int(input())
Ms = list(map(int, input().split()))

# 이분탐색 => 정렬 
Ns.sort()

for m in Ms:
    # N 안에 m이 있는가? 
    print(binary_search(m))
        