import sys
sys.stdin = open("input_1215.txt", "r")

for test_num in range(1, 11):
    length = int(input())
    board = [list(input()) for _ in range(8)]
    answer = 0

    for i in range(8):
        for j in range(8-length+1):
            # 가로 방향 
            row_tmp = board[i][j:j+length]
            # 세로 방향 
            col_tmp = []
            for k in range(length):
                col_tmp.append(board[j+k][i])
            
            if row_tmp == row_tmp[::-1]:
                answer += 1
            if col_tmp == col_tmp[::-1]:
                answer += 1

    # # 열
    # for i in range(8):
    #     # 행 
    #     # 8개 중 5개 => 3번까지만 
    #     for j in range(8-length+1):
    #         tmp = []
    #         for k in range(length):
    #             tmp.append(board[j+k][i])
    #         reverse_tmp = tmp[::-1]

    #         if str(tmp) == str(reverse_tmp):
    #             answer += 1
    print(f"#{test_num} {answer}")