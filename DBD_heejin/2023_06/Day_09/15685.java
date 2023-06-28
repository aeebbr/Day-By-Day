// [BOJ] 15685. 드래곤 커브
// 풀이 시간: 45 분
// 실행 시간: 84 ms
// 메모리: 11788 KB

import java.io.*;
import java.util.*;

public class Main {

    // → ↑ ← ↓
    public static int[][] dt = { {0, 1}, {-1, 0}, {0, -1}, {1, 0} };
    public static boolean[][] grid = new boolean[101][101];
    public static ArrayList<Integer> dragon;
    public static int di, dj;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        dragon = new ArrayList<>();

        for (int tc = 0; tc < N; tc++) {

            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            int g = Integer.parseInt(st.nextToken());

            dragon.clear();

            grid[y][x] = true;

            // 0세대
            di = y + dt[d][0];
            dj = x + dt[d][1];

            grid[di][dj] = true;

            dragon.add(d);

            for (int i = 0; i < g; i++) {
                dragonCurve();
            }
        }

        int answer = 0;

        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                if (grid[i][j] && grid[i+1][j] && grid[i][j+1] && grid[i+1][j+1]) answer++;
            }
        }
        System.out.println(answer);
    }

    public static void dragonCurve() {

        int size = dragon.size();

        for (int i = size - 1; i >= 0; i--) {
            int dir = (dragon.get(i) + 1) % 4;

            di += dt[dir][0];
            dj += dt[dir][1];

            grid[di][dj] = true;

            dragon.add(dir);
        }
    }
}
