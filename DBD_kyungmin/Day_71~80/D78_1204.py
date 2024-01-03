import sys
sys.stdin = open("input_1204.txt", "r")

T = int(input())

for _ in range(T):
    num = int(input())
    dic = {}
    arr = list(map(int, input().split()))
    answer = 0
    max_cnt = 0

    for n in arr:
        if n in dic:
            dic[n] += 1
        else:
            dic[n] = 1
        
    for k, v in dic.items():
        if v > max_cnt:
            answer = k
            max_cnt = v
        elif v == max_cnt and k > answer:
            answer = k
            
    print(f"#{num} {answer}")