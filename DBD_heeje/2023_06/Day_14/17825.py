# [BOJ] 17825. 주사위 윷놀이
# 풀이 시간: 3시간..ㅠㅠ
# 실행 시간: 500 ms
# 메모리: 31256 KB

# 인접그래프를 통해 해당 배열 안에 적힌 인덱스로 이동

# 인접그래프
graph = [[1], [2], [3], [4], [5], [6, 21], [7], [8], [9], [10], [11, 25], [12], [13], [14], [15], [16, 27], [17], [18], [19], [20], [32], [22], [23], [24], [30], [26], [24], [28], [29], [24], [31], [20], [32]]

scores = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 25, 22, 24, 28, 27, 26, 30, 35, 0]
dice = list(map(int, input().split()))
max_score = 0
def dfs(turn, score, piece):
    if turn >= 10:
        global max_score
        max_score = max(max_score, score)
        return
    
    for i in range(4):
        x = piece[i]
        if len(graph[x]) == 2:
            x = graph[x][1]
        else:
            x = graph[x][0]
        for _ in range(1, dice[turn]):
            x = graph[x][0]
        if x == 32 or (x < 32 and x not in piece):
            before = piece[i]
            piece[i] = x
            dfs(turn + 1, score + scores[x], piece)
            piece[i] = before
dfs(0, 0, [0, 0, 0, 0])
print(max_score)

# from collections import defaultdict

# def dfs(turn, score):
#     if score >= 150:
#         print(pieces, turn, score)
#     # 10턴에 종료
#     if turn == 10:
#         global max_score
#         max_score = max(max_score, score)
#         return
    
#     # 중복된 piece일 시 동작 x
#     piece_set = set()
#     for idx, piece in enumerate(pieces):
#         if tuple(piece) in piece_set:
#             continue

#         piece_set.add(tuple(piece))
#         # for key, val in dices:
#         #     if val != 0:
#         #         dices[key] -= 1
        
#         # idx에 현재 주사위 수만큼 더했을 때 
#         if piece[1] + dices[turn] >= len(roads[piece[0]]):
#             removed_piece = pieces.pop(idx)
#             dfs(turn + 1, score)
#             pieces.insert(idx, removed_piece)
        
#         else:
#             breaker = False
#             for other_idx, other_piece in enumerate(pieces):
#                 if idx == other_idx:
#                     continue

#                 if [piece[0], piece[1] + dices[turn]] == other_piece:
#                     breaker = True
#                     break
            
#             if breaker:
#                 continue

#             tmp = pieces[idx][:]
#             piece[1] += dices[turn]
#             if piece[0] == "road":
#                 if roads[piece[0]][piece[1]] == 10:
#                     pieces[idx] = ["sc1", 0]
#                 elif roads[piece[0]][piece[1]] == 20:
#                     pieces[idx] = ["sc2", 0]
#                 elif roads[piece[0]][piece[1]] == 30:
#                     pieces[idx] = ["sc3", 0]
                
#             dfs(turn + 1, score + roads[pieces[idx][0]][pieces[idx][1]])
#             pieces[idx] = tmp
                
#                 # dices[key] += 1
                    

                

# dices = list(map(int, input().split()))
# pieces = [["road", 0] for _ in range(4)]
# roads = {
#     "road": list(range(0, 41, 2)),
#     "sc1": [10, 13, 16, 19, 25, 30, 35, 40],
#     "sc2": [20, 22, 24, 25, 30, 35, 40],
#     "sc3": [30, 28, 27, 26, 25, 30, 35, 40]
#     }
# max_score = 0

# dfs(0, 0)
# print(max_score)