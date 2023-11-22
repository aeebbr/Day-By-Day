# [Programmers] 42577. 전화번호 목록   
# 풀이 시간 : 20 분

def solution(phone_book):
    answer = True
    phone_book.sort()    
    
    # 현재 - 다음 인덱스를 비교하는 것 
    for i in range(len(phone_book) - 1):
        cur = phone_book[i]
        near = phone_book[i+1]
        
        # 일단 cur보다 near의 길이가 같거나 길어야 함
        if len(cur) > len(near):
            continue
        # cur가 near에 완전히 속해야 함 
        for j in range(len(cur)):
            if cur[j] != near[j]:
                break
        else:
            answer = False
            break
    
    return answer