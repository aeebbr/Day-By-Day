# [BOJ] 1107. 리모컨
# 풀이 시간: 90 분
# 실행 시간: 1116 ms
# 메모리: 31256 KB

# 이동하려는 채널
N = int(input())

# 고장난 버튼의 개수
M = int(input())

# 고장난 버튼들
broken_btn = input().split() if M > 0 else []
cnt = 0

min_cnt = abs(100 - N)
for num in range(1000001):
    for i in str(num):
        if i in broken_btn:
            break
    else:
        min_cnt = min(min_cnt, abs(num - N) + len(str(num)))

print(min_cnt)
