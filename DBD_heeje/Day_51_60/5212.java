import java.util.*;
import java.io.*;

class Main {
    public static StringTokenizer st;
    public static int R, C, min_y, min_x, max_y, max_x;
    public static char[][] matrix, copied_matrix;
    public static int[][] direction = new int[][] { {-1, 0}, {0, -1}, {1, 0}, {0, 1} };
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        min_y = R - 1;
        min_x = C - 1;
        max_y = 0;
        max_x = 0;
        matrix = new char[R][C];
        copied_matrix = new char[R][C];

        for (int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            String row = st.nextToken();
            for (int j = 0; j < C; j++) {
                matrix[i][j] = row.charAt(j);
            }
        }

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (matrix[i][j] == 'X') {
                    if (isSinked(i, j)) {
                        copied_matrix[i][j] = '.';
                    } else {
                        min_y = Math.min(min_y, i);
                        min_x = Math.min(min_x, j);
                        max_y = Math.max(max_y, i);
                        max_x = Math.max(max_x, j);
                        copied_matrix[i][j] = 'X';
                    }
                } else {
                    copied_matrix[i][j] = '.';
                }
            }
        }
        
        for (int i = min_y; i <= max_y; i++) {
            for (int j = min_x; j <= max_x; j++) {
                sb.append(copied_matrix[i][j]);
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }

    public static boolean isSinked(int y, int x) {
        int ground = 0;
        int ny, nx;
        for (int[] dir: direction) {
            ny = y + dir[0];
            nx = x + dir[1];

            if (ny < 0 || ny >= R || nx < 0 || nx >= C) continue;
            if (matrix[ny][nx] == 'X') {
                ground += 1;
            }
        }
        
        return ground <= 1;
    }
}