# [BOJ] 15688. 수 정렬하기 5  
# 풀이 시간 : 25 분 

# 오름차순 정렬

# merge sort 직접 구현
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

# 병합
def merge(left, right):
    # 정렬하여 병합
    l, r = 0, 0 # 각각 left, right의 전방 원소를 가리키는 포인터 
    sorted_arr = []

    # 두 배열의 맨 앞만 비교 
    # 조건: 배열 범위 벗어나지 않기 
    while l < len(left) and r < len(right):
        # left가 right보다 작다면
        if left[l] < right[r]:
            sorted_arr.append(left[l])
            # left 포인터 뒤로 이동
            l += 1
        # right가 left보다 작거나 같다면
            # (같은 경우도 포함: 두 원소의 우선순위가 같으니 left의 원소를 넣든 right의 원소를 넣든 상관 없음)
        else:
            sorted_arr.append(right[r])
            r += 1

    # 두 배열 중에 남은 원소가 있다면 
    # left 배열에서 남은 원소가 있다면
    while l < len(left):
        sorted_arr.append(left[l])
        l += 1
    # left 배열에서 남은 원소가 있다면
    while r < len(right):
        sorted_arr.append(right[r])
        r += 1

    # 병합 완료 
    return sorted_arr
        
# 분할 
def division(arr):
    # 기저 조건
    # 더 이상 분할될 수 없는 길이일 때 종료  
    if len(arr) <= 1:
        return arr 
    
    # 리스트 분할 
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # 분할한 리스트를 재귀로 ~ 
    divided_left = division(left)
    divided_right = division(right)

    # 각 깊이에서 분할되어 있는 배열을 병합 
    # 최종 병합이 끝나면, 최종 정렬된 배열이 현재 함수를 아예 벗어나면서 return 됨 
    return merge(divided_left, divided_right)

answer = division(arr)
for i in answer:
    print(i)

'''
# sort 내장 함수 사용 
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()

for i in arr:
    print(i)'''