// [Programmers] 152996. 시소 짝꿍
// 풀이 시간: 40 분

class Solution {
    public long solution(int[] weights) {
        long[] cArr = new long[1001];
        int N = cArr.length;
        long answer = 0;
        
        for (int weight: weights) {
            cArr[weight] += 1;
        }
        
        for (int i = 100; i < N; i++) {
            
            if (cArr[i] == 0) continue;
            
            // 같은 몸무게 짝꿍 수
            answer += cArr[i] * (cArr[i] - 1) / 2;
            
            // 2:3 비율의 몸무게 짝꿍 수
            if (i % 2 == 0 && i / 2 * 3 < N) {
                answer += cArr[i] * cArr[i / 2 * 3];
            }
            
            // 2:4 비율의 몸무게 짝꿍 수
            if (i * 2 < N) {
                answer += cArr[i] * cArr[i * 2];
            }
            
            // 3:4 비율의 몸무게 짝꿍 수
            if (i % 3 == 0 && i / 3 * 4 < N) {
                answer += cArr[i] * cArr[i / 3 * 4];
            }
        }
        return answer;
    }
}