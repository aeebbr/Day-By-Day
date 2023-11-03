# [BOJ] 2467. 용액
# 소요 시간 : 30 분

N = int(input())
liquids = list(map(int, input().split()))
start = 0
end = N - 1
answer = [0, float("inf")]
while start < end:
    mixed_liquid = liquids[start] + liquids[end]
    if abs(sum(answer)) > abs(mixed_liquid):
        answer[0], answer[1] = liquids[start], liquids[end]

    if mixed_liquid == 0:
        break
    elif mixed_liquid < 0:
        start += 1
    else:
        end -= 1

print(*answer)