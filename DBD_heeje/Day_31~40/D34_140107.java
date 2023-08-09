// [Programmers] 140107. 점 찍기
// 풀이 시간: 40 분

import java.util.*;

// 사분원의 경계에서부터 깎아내려갈 예정

class Solution {
    public long solution(int k, int d) {
        long dots = 0;
        
        // d보다 작거나 같으면서 k의 배수인 i 찾기
        int i = d;
        while (i % k != 0) {
            i -= 1;
        }
        
        // (i, j)부터 시작하여 우측 하단으로 하강하는 느낌?
        for (int j = k; j < d; j += k) {
            
            // (i, j)와 원점과의 거리가 d보다 크다면 i에 k 빼줌
            while (!check(i, j, d)) {
                i -= k;
            }
            
            // d보다 작거나 같다면 i / k 만큼의 점을 dots에 더해주기
            dots += i / k;
        }
        
        // d / k는 x 또는 y가 0인 부분, + 1은 원점
        return dots + 2 * (d / k) + 1;
    }
    
    public boolean check(int y, int x, int d) {
        return Math.pow(Math.pow(y, 2) + Math.pow(x, 2), 0.5) <= d;
    }
}