// [BOJ] 18428. 감시 피하기
// 풀이 시간: 00 분
// 실행 시간: 0 ms
// 메모리: 0 KB

import java.io.*;
import java.util.*;

public class avoid_cctv_18428 {

    public static class Point {
        int i, j;

        Point(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }

    public static int[][] dir = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
    public static int answer = Integer.MAX_VALUE;
    public static ArrayList<Point> empties;
    
    public static char[][] map;
    public static int N;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        N = Integer.parseInt(br.readLine());

        map = new char[N][N];
        empties = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            String temp = br.readLine();
            for (int j = 0; j < N; j++) {
                map[i][j] = temp.charAt(j);
                if (map[i][j] == 'X') {
                    empties.add(new Point(i, j));
                }
            }
        }

        for (int i = 0 ; i < N; i++) {
            System.out.println(Arrays.toString(map[i]));
        }

        int[] arr = new int[empties.size()];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = i;
        }

        boolean[] visit = new boolean[arr.length];
        comb(arr, visit, 0, 0, 3);
        System.out.println(answer == Integer.MAX_VALUE ? -1 : answer);
    }

    public static void comb(int[] arr, boolean[] visit, int idx, int depth, int r) {

        if (r == depth) {
            bfs(arr, visit);
            return;
        }

        for (int i = idx; i < arr.length; i++) {
            if (!visit[i]) {
                visit[i] = true;
                comb(arr, visit, i+1, depth+1, r);
                visit[i] = false;
            }
        }
    }

    public static void bfs(int[] arr, boolean[] visit) {

        int[][] tmp = new int[N][N];

        for (int i = 0; i < N; i++) {
            System.arraycopy(map[i], 0, tmp[i], 0, N);
//            for (int j = 0; j < N; j++) {
//                tmp[i][j] = map[i][j];
//            }
        }
    }
}
