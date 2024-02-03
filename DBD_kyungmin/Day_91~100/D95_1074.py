# [BOJ] 1074. Z 
# 풀이 시간 : 50 분 

N, r, c = map(int, input().split())
answer = 0

while N != 0:
    # 배열을 4등분 
    N -= 1

    # 1사분면 
    if r < 2 ** N and c < 2 ** N:
        # 1사분면의 시작 
        answer += (2**N) * (2**N) * 0

    # 2사분면
    elif r < 2 ** N and c >= 2 ** N:
        # 2사분면의 시작 
        answer += (2**N) * (2**N) * 1
        # 4등분 쪼갠만큼 좌표 이동
        c -= (2**N)

    # 3사분면
    elif r >= 2 ** N and c < 2 ** N:
        # 3사분면의 시작 
        answer += (2**N) * (2**N) * 2
        r -= (2**N)

    # 4사분면
    else:
        # 4사분면의 시작 
        answer += (2**N) * (2**N) * 3
        r -= (2**N)
        c -= (2**N)

print(answer)