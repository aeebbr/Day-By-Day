import sys
sys.stdin = open("input_1213.txt", "r")

for _ in range(10):
    test_num = int(input())
    search = input()
    str = input()
    print(f"#{test_num} {str.count(search)}")