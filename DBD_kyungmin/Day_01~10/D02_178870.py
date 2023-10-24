# [Programmers] 178870. 연속된 부분 수열의 합
# 풀이 시간: ?? 분
# 실행 시간: 0 ms
# 메모리: 0 KB

def solution(sequence, k):
    # [좌 포인터, 우 포인터]
    answer = []
    
    total = 0
    # 우 포인터 
    right = 0
    
    # 수열의 길이만큼 반복
    # left는 시작 지점
    for left in range(len(sequence)):
        # 수열의 시작 요소를 시작으로, 오른쪽 요소를 하나씩 더해가기
        # 반복 조건
            # 1) 오른쪽 포인터가 배열 범위 내일 것 
            # 2) 합이 k보다 작을 것
        while right < len(sequence) and total < k:
            # 합 갱신: 합 + 우 포인터 요소 
            total += sequence[right]
            # 오른쪽 포인터 갱신: 하나 뒤로 옮기기
            right += 1
            
        # 합이 k라면 
        if total == k:
            # answer가 비어다면
            if not answer:
                # 두 포인터 저장
                answer = [left, right - 1]
            
            # answer가 이미 있다면 현재 answer를 갱신할지 말지 체크
            else:
                # 현재 포인터들이 가리키는 길이가 저장된 길이보다 작다면, 현재 포인터로 갱신
                if right - 1 - left < answer[1] - answer[0] :
                    answer = [left, right - 1]
            
        # 마지막 요소까지 탐색 끝
        # 합 갱신: 합 - 왼쪽 포인터 
        total -= sequence[left]
                       
    return answer