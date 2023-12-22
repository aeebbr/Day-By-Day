# [BOJ] 12907. 거스름돈   
# 풀이 시간 : 30 분 

def solution(n, money):
    dp = [0] * (n + 1)
    
    # money 순회 
    for i in money:
        # 현재 돈을 상대로 현재 돈부터 n까지 순회
        for j in range(i, n + 1):
            # dp에 누적
                # j - 현재 돈의 수(현재 돈에서 모자라는 액수)에 해당하는 dp 값을 누적하기 
                # 모자라는 액수 없다면 누적이 아닌 1 증가
            if j == i:
                dp[j] += 1
            else:
                dp[j] += dp[j - i]
    
    return dp[n]