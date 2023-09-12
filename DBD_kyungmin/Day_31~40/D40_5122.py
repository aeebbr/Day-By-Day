# [SWEA] 5122. 수열 편집
# 풀이 시간: 00 분

# import sys 
# sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline 

T = int(input())

for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    nums = list(map(int, input().split()))

    for _ in range(M):
        tmp = list(input().split())
        command, idx = tmp[0], int(tmp[1])
        if len(tmp) == 3: new = int(tmp[2])

        if command == 'I':
            nums.insert(idx, new)
        elif command == 'D':
            del nums[idx]
        elif command == 'C':
            nums[idx] = new

    print(f'#{test_case}', end=" ")
    if len(nums) <= L:
        print(-1)
    else:
        print(nums[L])