# [Programmers] 176962. 과제 진행하기
# 풀이 시간: 90++ 분

def solution(plans):
    answer = []
    
    # 시작 시간을 분으로 변환 
    for i in range(len(plans)):
        start = plans[i][1]
        h = int(start[0:2])
        m = int(start[3:])    
        total = h * 60 + m
        plans[i][1] = total
        plans[i][2] = int(plans[i][2])
        
    # plans의 start를 기준으로 정렬
    plans.sort(key = lambda x:x[1])
    
    stack = []
    
    for i in range(len(plans)):
        # 현 과제가 마지막 과제인지 
        if i == len(plans) - 1:
            # 현 과제 대기열로 
            stack.append(plans[i])
            break
        
        # 현재 과목
        cur_sub, cur_start, cur_time = plans[i]
        # 다음 과목
        next_sub, next_start, next_time = plans[i + 1]
        
        # 현재 과제가 끝나고 나서 다음 과제가 시작한다면
        if cur_start + cur_time <= next_start:
            # 현재 과제 종료
            answer.append(cur_sub)
            
            # 다음 과제 시작까지 남은 시간
            tmp_time = next_start - (cur_start + cur_time)
            
            # 다음 과제까지 시간이 있고, 대기열이 있다면
            while tmp_time != 0 and stack:
                waiting_sub, waiting_start, waiting_time = stack.pop()
                
                # 남은 시간동안 대기 과제 수행할 수 있다면
                if tmp_time >= waiting_time:
                    # 대기 과제 종료 
                    answer.append(waiting_sub)
                    
                    # 남은 시간 갱신 
                    tmp_time -= waiting_time
                # 대기 과제 완전히 수행할 수 없다면 
                else:
                    # 대기 과제 다시 대기열로 
                    stack.append([waiting_sub, waiting_start, waiting_time - tmp_time])
                    tmp_time = 0
        # 현 과제 중에 다음 과제 시작한다면 
        else:
            # 현 과제 시간 갱신 
            plans[i][2] = cur_time - (next_start - cur_start)
            # 현 과제 대기열로 
            stack.append(plans[i])
                
    # 시작 시간에 맞춰서 시작했음에도 대기열에 남은 과제 처리 
    while stack:
        sub, start, time = stack.pop()
        answer.append(sub)
    
    return answer


# from collections import deque

# def solution(plans):
#     answer = []
    
#     # 시작 시간을 분으로 변환 
#     for i in range(len(plans)):
#         start = plans[i][1]
#         h = int(start[0:2])
#         m = int(start[3:])    
#         total = h * 60 + m
#         plans[i][1] = total
        
#     # plans의 start를 기준으로 정렬
#     plans.sort(key = lambda x:x[1])

#     # 진행 중인 과제 인덱스 
#     cur_idx = 0
#     # 대기열 
#     waiting = deque()

#     while len(plans) > 0 or waiting:
#         if len(plans) - 1 == cur_idx:
#             next_start = 0
#         elif len(plans) - 1 < cur_idx:
#             break
#         else:
#             i = 1
            
#             while True:
#                 if plans[cur_idx + i][1] == 0:                
#                     next_start = plans[cur_idx + i][1]
            
#         cur_start = plans[cur_idx][1]
#         cur_time = int(plans[cur_idx][2])
                
#         # 진행 중인 과제 중에 다음 과제가 시작해야 하는가 
#         # 시작: 700, 종료: 700 + 40 = 740, 다음 과제 시작: 730 => 다음 과제 시작
#         if cur_start + cur_time > next_start:
#             # 다음 과제 시작
#             # 현재 과제는 대기열에 삽입
#             waiting.append(cur_idx)
#             # 현재 과제의 남은 시간 갱신 
#             plans[cur_idx][2] = next_start - cur_start
            
#             # 현재 과제 갱신 
#             cur_idx += 1
#         # 진행 과제 종료와 다음 과제 시작이 같거나, 진행 종료 후에 다음 과제 시작이라면 
#         else:
#             # 현재 과제 종료 
#             answer.append(plans[cur_idx][0])
#             plans[cur_idx][2] = 0
            
#             # 종료된 시점이 다음 과제 시작이라면 
#             if cur_start + cur_time == next_start:
#                 # 다음 과제 시작
#                 cur_idx += 1
                
#             # 멈춘 과제있다면  
#             elif waiting:
#                 # 현재 과제 갱신 
#                 cur_idx = waiting.pop()

#     return answer