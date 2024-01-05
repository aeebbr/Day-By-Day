import sys
sys.stdin = open("input_1216.txt", "r")

def main(length):
    for i in range(100):
        for j in range(100 - length + 1):
            # 가로 방향 
            row_arr = board[i][j:j+length]
            if row_arr == row_arr[::-1]:
                return True

            # 세로 방향
            col_arr = []
            for k in range(length):
                col_arr.append(board[j+k][i])
            if col_arr == col_arr[::-1]:
                return True
    return False

for _ in range(10):
    test_num = int(input())
    board = [list(input()) for _ in range(100)]
                
    # 회문 길이를 100부터 역으로 줄여서 지정하기 => 제일 먼저 나오는 회문의 길이가 가장 긴 길이가 되는 것임 
    for length in range(100, -1, -1):
        if main(length):
            print(f"#{test_num} {length}")
            break
