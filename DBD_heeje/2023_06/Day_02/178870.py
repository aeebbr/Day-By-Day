# [Programmers] 178870. 연속된 부분 수열의 합
# 풀이 시간: 20 분


def solution(sequence, k):
    answer = []
    left, right = 0, 0
    sum = sequence[left]
    while left < len(sequence):

        # 부분 수열의 합이 k보다 작으면 right 증가
        if sum < k:
            right += 1
            if right < len(sequence):
                sum += sequence[right]
            else:
                break

        # 부분 수열의 합이 k보다 크면 left 증가
        elif sum > k:
            sum -= sequence[left]
            left += 1

        # 부분 수열의 합이 k와 일치하면 길이 비교
        else:
            if answer:
                if answer[1] - answer[0] > right - left:
                    answer = [left, right]
            else:
                answer = [left, right]

            right += 1
            if right < len(sequence):
                sum += sequence[right]
            else:
                break
    return answer
