# [Programmers] 92344. 파괴되지 않은 건물
# 풀이 시간: ++90 분

def solution(board, skill):
    answer = 0
    
    # 누적합 초기 배열 만들기 
    sum_board = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    
    # 각 스킬
    for type, r1, c1, r2, c2, degree in skill:
        # type이 1이라면 degree 감소 
        if type == 1:
            degree *= -1
        
        # 시작 지점에 삽입
        sum_board[r1][c1] += degree
        # 행 기준 누적합을 위한 삽입
        sum_board[r1][c2 + 1] += -degree
        # 열 기준 누적합을 위한 삽입
        sum_board[r2 + 1][c1] += -degree
        sum_board[r2 + 1][c2 + 1] += degree
        
    # 누적합
    # 행 기준 누적합
    for i in range(len(sum_board) - 1):
        for j in range(len(sum_board[0]) - 1):
            # 다음 열 = 현재 열 + 다음 열
            sum_board[i][j + 1] += sum_board[i][j]
        
    # 열 기준 누적합
    for i in range(len(sum_board[0]) - 1): # 열
        for j in range(len(sum_board) - 1): # 행
            # 다음 행 = 현재 행 + 다음 행
            sum_board[j + 1][i] += sum_board[j][i]

    # 누적합 끝
    # 각 원본 배열 칸에 누적합 합하기 
    for i in range(len(board)):
        for j in range(len(board[0])):
            # 합하면서 파괴되지 않은 건물 카운트하기
            if 1 <= board[i][j] + sum_board[i][j]:
                answer += 1
            
    return answer