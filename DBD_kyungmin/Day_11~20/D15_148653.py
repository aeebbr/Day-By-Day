# [Programmers] 148653. 마법의 엘리베이터
# 풀이 시간: 70 분
# 실행 시간: 00 ms
# 메모리: 00 KB

# 고려할 경우: 1) 위로 올라가거나 2) 밑으로 내려가거나
def solution(storey):
    answer = []
    
    # st: 층, count: 마법의 돌 개수 
    def dfs(st, count):
        # 종료 조건: 0층 도달 
        if st == 0:
            answer.append(count)
            return
        
        one = st % 10
        up, down = 10 - one, one
        
        # up 이나 down 둘 중 더 적게 움직이는 쪽으로 이동
        if up < down:
            dfs(st // 10 + 1, count + up)
        elif down < up:
            dfs(st // 10, count + down)
        else:
            # 같다면 두 방향 모두 이동
            for i in range(2):
                dfs(st // 10 + i, count + up)
    
    dfs(storey, 0)
    # 최소값 반환
    return min(answer)