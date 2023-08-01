// [Programmers] 131130. 혼자 놀기의 달인
// 풀이 시간: 40 분

import java.util.*;

class Solution {
    public static int cntBoxes = 1;
    public static boolean[] visited;
    public int solution(int[] cards) {
        int N = cards.length;
        int[] groups = {0, 0};
        visited = new boolean[N];
        
        for (int i = 0; i < N; i++) {
            if (!visited[i]) {
                dfs(cards, i);
                
                // 더 쉽게 할 수 있는 방법?
                if (groups[0] < cntBoxes) {
                    groups[1] = groups[0];
                    groups[0] = cntBoxes;
                } else if (groups[1] < cntBoxes) {
                    groups[1] = cntBoxes;
                }
                
                cntBoxes = 1;
            }
        }

        return groups[0] * groups[1];
    }
    
    public void dfs(int[] cards, int n) {
        visited[n] = true;
        if (visited[cards[n] - 1]) return;
        cntBoxes += 1;
        dfs(cards, cards[n] - 1);
    }
    
}