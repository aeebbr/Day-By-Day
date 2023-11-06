// [Programmers] 92344. 파괴되지 않은 건물
// 풀이 시간: 60 분

class Solution {
    public int solution(int[][] board, int[][] skill) {
        
        int N = board.length;
        int M = board[0].length;        
        
        int[][] sum = new int[N + 1][M + 1];
        // 1 / 0, 0 / 3, 4 / 4
        for (int i = 0; i < skill.length; i++) {
            
            int type = skill[i][0];
            int y1 = skill[i][1];
            int x1 = skill[i][2];
            int y2 = skill[i][3];
            int x2 = skill[i][4];
            int value = skill[i][5];
            
            if (type == 1) {
                sum[y1][x1] -= value;
                sum[y1][x2 + 1] += value;
                sum[y2 + 1][x1] += value;
                sum[y2 + 1][x2 + 1] -= value;
            } else {
                sum[y1][x1] += value;
                sum[y1][x2 + 1] -= value;
                sum[y2 + 1][x1] -= value;
                sum[y2 + 1][x2 + 1] += value;
            }  
        }
        
        // ↓
        for (int i = 0; i <= M; i++) {
            for (int j = 1; j <= N; j++) {
                sum[j][i] += sum[j-1][i];
            }
        }
        
        // →
        for (int i = 0; i <= N; i++) {
            for (int j = 1; j <= M; j++) {
                sum[i][j] += sum[i][j-1];
            }
        }
        
        int answer = 0;
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                board[i][j] += sum[i][j];
                if (board[i][j] > 0) answer++;
            }
        }
        return answer;
    }
}
