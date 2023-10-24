# [BOJ] 2668. 숫자고르기
# 풀이 시간: 90++ 분
# 실행 시간: 44 ms
# 메모리: 31256 KB

# 입력
N = int(input())			
# 두번째 줄 숫자 입력
# 0번 인덱스는 비우고, 1번 인덱스부터 숫자 넣기 
# => 각 인덱스는 첫째 줄 숫자와 동일해짐 
arr = [0]				
for _ in range(N):
    arr.append(int(input()))

# 결과 담을 set
answer = set()				

# first: 첫째줄 집합, second: 둘째줄 집합, num: 탐색 수 
def dfs(first, second, num):
    first.add(num)			# 첫번째 줄 집합에 num 추가
    second.add(arr[num])		# 두번째 줄 집합에 arr[num] 추가

    # 종료 조건
    # 탐색하는 첫째줄 숫자의 둘째줄 숫자가 첫번째 줄 집합에 있다면
    # = 탐색하는 둘째줄 숫자와 같은 수가 첫째줄 집합에도 있다면
    if arr[num] in first:		
        # 두 집합이 완전히 일치한다면 답 갱신
        if first == second:	
            # 현재까지 탐색한 첫째줄 집합으로 결과 집합 갱신
            answer.update(first)	
            # return True
            # return
        
        # 첫번째 줄 집합과 두번째 줄 집합이 다르다면 False 반환
        # return False
        return
    
    # 다음 dfs 실행
    return dfs(first, second, arr[num])

# 1 ~ N까지 dfs 실행 
for i in range(1, N+1):
    # 현재 수가 결과 집합 안에 없는 경우만 실행 
    if i not in answer:			
        dfs(set(), set(), i)

print(len(answer))
print(*sorted(list(answer)), sep='\n')

# # 조합
# # N이 7이면
# # 1 2 3 4 5 6 7
# # 3 1 1 5 5 4 6

# # 둘째줄에 해당하는 입력 수들을 리스트에 담고, 
# # 특정 수를 조합할 때 해당 수 -1번 인덱스에 해당하는 수를 따지기

# import copy

# # 최대 개수
# max_nums = []

# # 조합
# def combi(n, total):
#     global max_nums 

#     # 종료 조건
#     if n == N:
#         if len(total) > len(max_nums):
#             # 둘째 줄에 해당하는 수들
#             secondary = []
#             for i in total:
#                 secondary.append(nums[i - 1])

#             secondary.sort()

#             # 첫째줄과 둘째줄이 일치하는지 확인
#             # for i in range(len(total)):
#             #     if total[i] != secondary[i]:
#             #         break
#             # # 모든 지점이 일치했다면
#             # else:
#             #     if len(total) > len(max_nums):
#             #         max_nums = copy.deepcopy(total)
#             if total == secondary:
#                 # print()
#                 # if len(total) > len(max_nums):
#                 max_nums = copy.deepcopy(total)

#         return 
    
#     total.append(n + 1)
#     combi(n + 1, total)
#     total.pop()
#     combi(n + 1, total)
    
#     # n ~ 마지막 숫자까지
#     # for i in range(n + 1, N + 1):
#     #     tmp = copy.deepcopy(total)
#     #     tmp.append(i)
#     #     print()
#     #     combi(n + 1, tmp)

# N = int(input())

# nums = []
# for _ in range(N):
#     nums.append(int(input()))

# # 조합 호출
# # 숫자 1에서 시작
# for i in range(1, N):
#     combi(i, [i])

# print(len(max_nums))

# for n in max_nums:
#     print(n)