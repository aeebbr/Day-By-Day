import sys
sys.stdin = open("input_1208.txt", "r")

for test in range(10):
    dump = int(input())
    tmp_arr = list(map(int, input().split()))
    arr = [0] * 101 

    for n in tmp_arr:
        arr[n] += 1

    lowest = 0
    highest = 0

    for i in range(len(arr)):
        if arr[i] > 0:
            lowest = i
            break
    for i in range(100, -1, -1):
        if arr[i] > 0:
            highest = i
            break

    for _ in range(dump):
        arr[highest] -= 1
        arr[highest-1] += 1
        arr[lowest] -= 1
        arr[lowest+1] += 1

        if arr[lowest] == 0:
            lowest += 1
        if arr[highest] == 0:
            highest -= 1

        if highest - lowest in [0, 1]:
            break
        
    print(f"#{test+1} {highest - lowest}")
    # print(lowest, highest, highest - lowest)
'''
# 정렬을 활용한 풀이(시간 비효율)
for test in range(10):
    dump = int(input())
    arr = list(map(int, input().split()))

    for i in range(dump):
        arr.sort()
        arr[0] += 1
        arr[-1] -= 1
        
        # 평탄화 완료 확인
        if arr[-1]-arr[0] in [0, 1]:
            break
    
    arr.sort()
    print(f"#{test+1} {arr[-1]-arr[0]}")
    # print(arr[-1]-arr[0], arr)
'''