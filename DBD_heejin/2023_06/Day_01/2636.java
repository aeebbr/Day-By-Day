// [BOJ] 2636. 치즈
// 풀이 시간: 28 분
// 실행 시간: 116 ms
// 메모리: 13412 KB

import java.io.*;
import java.util.*;

public class Main {

    static class Point {
        int i, j;

        public Point(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }

    public static int[][] dir = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
    static int[][] grid;
    static boolean[][] v;
    static int N, M, time, sum;
    static boolean check;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        time = 0;
        grid = new int[N][M];
        check = false;

        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < M; j++) {
                grid[i][j] = Integer.parseInt(st.nextToken());
                if (grid[i][j] == 1) {
                    sum++;
                }
            }
        }

        while(!check) {
            v = new boolean[N][M];
            bfs();
            time++;
        }
        System.out.println(time);
        System.out.println(sum);
    }

    private static void bfs() {
        int[][] newGrid = new int[N][M];

        for(int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {
                newGrid[i][j] = grid[i][j];
            }
        }

        Queue<Point> q = new ArrayDeque<>();

        q.add(new Point(0, 0));
        v[0][0] = true;

        while(!q.isEmpty()) {
            Point p = q.poll();

            for(int d = 0; d < 4; d++) {
                int ni = p.i + dir[d][0];
                int nj = p.j + dir[d][1];

                if(ni < 0 || nj < 0 || ni >= N || nj >= M) continue;
                if(v[ni][nj]) continue;
                if(grid[ni][nj] >= 1) grid[ni][nj]++;
                if(grid[ni][nj] == 0) {
                    v[ni][nj] = true;
                    q.add(new Point(ni, nj));
                }
            }
        }

        int count = 0;
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {
                if(grid[i][j] >= 2) {
                    newGrid[i][j] = 0;
                    count++;
                }
                grid[i][j] = newGrid[i][j];
            }
        }
        if (sum - count != 0) sum -= count;
        else check = true;
    }
}
