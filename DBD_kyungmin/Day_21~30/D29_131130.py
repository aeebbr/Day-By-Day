# [Programmers] 131130. 혼자 놀기의 달인
# 풀이 시간: 70 분

# cards: 연결 리스트 
# 인덱스 - 값
# 상자 - 카드 
def solution(cards):
    visited = [False] * (len(cards) + 1)
    # 각 그룹의 상자 수 
    box_cnt = [0]

    cards.insert(0, 0)
    
    # 1번 상자부터 차례대로 순회하면서 사이클 확인
    # 사이클 확인하면서 방문 처리 => 이미 방문된 노드는 탐색하지 않음
    # 하나의 사이클 확인되면 그 사이클의 길이(노드의 개수) 저장
    for i in range(1, len(cards)):
        if not visited[i]:
            # 현재 탐색하는 상자
            cur = i
            # 사이클 내의 노드 수 
            cnt = 0
            
            # 사이클 확인 
            while cur <= len(cards):
                # 현재 상자 방문 확인
                if not visited[cur]:
                    cnt += 1                    
                    visited[cur] = True
                    
                    # 상자의 카드 번호를 다음 상자 번호로 갱신 
                    cur = cards[cur]
                # 사이클 발견 
                else:
                    # 이 사이클에 모든 상자가 포함되었다면 게임 종료 
                    if cnt == len(cards) - 1:
                        return 0
                    
                    box_cnt.append(cnt)
                    break
    
    # 가장 큰 두 수를 맨 앞에 오도록 정렬하고, 곱한 값을 리턴
    box_cnt.sort(reverse = True)
    return box_cnt[0] * box_cnt[1]