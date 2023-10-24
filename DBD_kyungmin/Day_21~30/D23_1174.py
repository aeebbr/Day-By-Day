# [BOJ] 1174. 줄어드는 수
# 풀이 시간: 90++ 분
# 실행 시간: 52 ms
# 메모리: 31256 KB

# 줄어드는 수들
result = []
# 탐색하고 있는 현재 (줄어드는) 수 
arr = []

def dfs():
    # 현재 탐색하는 수가 줄어드는 수라면 줄어드는 수 리스트에 삽입 
    if len(arr) > 0:
        result.append(int("".join(map(str, arr))))

    # 0부터 9까지 탐색
    for i in range(0, 10):
        # 현재 수의 가장 오른쪽 자리수보다 작다면 줄어드는 수
        if len(arr) == 0 or i < arr[-1]:
            # 현재 수에 덧붙이기 
            arr.append(i)
            dfs()
            # 다음 수로 이동 
            # 백트래킹
            arr.pop()

# 입력 
N = int(input())

dfs()

# 줄어드는 수가 N보다 적다면(N번째 줄어드는 수가 없다면)
if len(result) >= N:
    # 줄어드는 수 오름차순 정렬
    # N번째 줄어드는 수 출력
    result.sort()
    print(result[N - 1])
# 줄어드는 수가 없다면 -1 출력
else:
    print(-1)

# def dfs(n, nth):
#     # 0부터 9까지 n과 비교해서, n보다 작은 수만 재귀
#     for i in range(0, 10):
#         if i < int(str(n)[-1]):
#             # print(int(str(n)[-1]))
#             print()
#             # n의 다음 자릿수로?...
#             # N번째라면 종료 
#             if nth + 1 == N:
#                 print(n)
#                 # return 
#                 exit(0)
            
#             dfs(int(str(n) + str(i)), nth + 1)

# # 입력
# N = int(input())

# for i in range(0, 10):
#     dfs(i, 0)