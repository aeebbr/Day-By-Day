import sys
sys.stdin = open("input_1206.txt", "r")

for test in range(10):
    N = int(input())
    arr = list(map(int, input().split()))
    answer = 0

    # 양쪽으로 2 인덱스 인접한 숫자 중에서 가장 큰 수와 높이를 빼기 
    for i in range(2, len(arr)):
        cur = arr[i]
        near = arr[i-2:i]
        near.extend(arr[i+1:i+3])
        # 차이 
        diff = cur - max(near)
        if diff > 0:
            answer += diff
        
    print(f"#{test + 1} {answer}")