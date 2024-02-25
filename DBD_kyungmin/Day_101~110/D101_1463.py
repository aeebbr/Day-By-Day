# [BOJ] 1463. 1로 만들기   
# 풀이 시간 : 90++분 

# dp로 풀이 
N = int(input())
d = [0] * (N + 1)

for i in range(2, N+1):
    d[i] = d[i-1] + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)

print(d[N])

'''
# 재귀로 풀이 

answer = float("inf")
def dfs(num, cnt):
    global answer
    # 가지치기
    if cnt >= answer:
        return 

    if num == 1:
        # 최소값 갱신 
        answer = min(answer, cnt)
        return 
    
    if num % 3 == 0:
        dfs(num // 3, cnt + 1)
    if num % 2 == 0:
        dfs(num // 2, cnt + 1)
    dfs(num - 1, cnt + 1)

N = int(input())

dfs(N, 0)
print(answer)
'''