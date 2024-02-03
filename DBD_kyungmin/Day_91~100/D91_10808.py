# [BOJ] 10808. 알파벳 개수     
# 풀이 시간 : 05 분 

S = input()
answer = [0] * 26

for s in S:
    idx = (ord(s) - 97)
    answer[idx] += 1

print(*answer)

'''
S = input()
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
answer = [0] * 26

for s in S:
    i = alpha.index(s)
    answer[i] += 1

print(*answer)
'''