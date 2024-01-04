import sys
sys.stdin = open("input_1209.txt", "r")

# 각 행, 열, 대각선 => 총 12개의 총합 저장할 수 있는 리스트 
    # 리스트 저장 순서: 0 ~ 99행, 0 ~ 99열, 좌하로 오는 대각선, 우하로 오는 대각선 
# 100 * 100 전체 순회하면서 해당하는 위치를 총합 리스트에 누적하기 
    # 행 리스트: 0 ~ 99번 인덱스
    # 열 리스트: 100 ~ 199번 인덱스 
    # 좌하 대각선: 200번 인덱스 
    # 우하 대각선: 201번 인덱스 
    # 좌하 대각선에 포함되는 값: [0][99], [1][98], [2][97], [3][96] [4][95] ... [99][0]
    # 우하 대각선에 포함되는 값: [0][0], [1][1] ... [99][99]

for _ in range(10):
    test_num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    total_arr = [0] * 202

    for i in range(100):
        for j in range(100):
            cur = arr[i][j]
            total_arr[i] += cur
            total_arr[j+100] += cur # 0열: 100번, 1열: 101번
            # 대각선 누적 
            if i == j:
                total_arr[201] += cur
            if i + j == 99:
                total_arr[200] += cur
    print(f"#{test_num} {max(total_arr)}")