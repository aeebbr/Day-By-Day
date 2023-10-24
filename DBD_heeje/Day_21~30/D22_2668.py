# [BOJ] 2668. 숫자고르기
# 풀이 시간: 60 분
# 실행 시간: 48 ms
# 메모리: 31256 KB

N = int(input())
numbers = [0] + [int(input()) for _ in range(N)]
arr_set = set()

for i in range(1, N + 1):
    if i not in arr_set:
        home = set()
        away = set()

        home.add(i)
        number = numbers[i]
        away.add(number)
        while number not in home:
            home.add(number)
            number = numbers[number]
            away.add(number)
        
        if home == away:
            arr_set = arr_set | home | away

print(len(arr_set))
print(*sorted(list(arr_set)), sep="\n")
    

# def dfs(idx:int, list1:list, list2:list) -> None:
#     if idx == N:
#         print(list1, list2)
#         str_list2 = "".join(list(map(str, list2)))
#         if "".join(list(map(str, list1))) == str_list2:
#             global max_nums
#             if len(max_nums) < len(str_list2):
#                 max_nums = str_list2
#         return
    
#     dfs(idx + 1, list1, list2)
#     list1[idx + 1] += 1
#     list2[numbers[idx]] += 1
#     dfs(idx + 1, list1, list2)
#     list1[idx + 1] -= 1
#     list2[numbers[idx]] -= 1


# N = int(input())
# numbers = [int(input()) for _ in range(N)]
# max_nums = ""

# dfs(0, [0] * (N + 1), [0] * (N + 1))

# print(len(max_nums))
# answer = []
# for i in range(len(max_nums)):
#     if max_nums[i] != "0":
#         answer.append(i + 1)
    
# print(*answer, sep="\n")