// [BOJ] 17141. 연구소 2
// 풀이 시간: 42 분
// 실행 시간: 252 ms
// 메모리: 30940 KB

import java.io.*;
import java.util.*;

public class Main {

    public static int[][] dir = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
    public static int answer = Integer.MAX_VALUE;
    public static ArrayList<Virus> viruses;
    public static int[][] map;
    public static int N;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        map = new int[N][N];
        viruses = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if (map[i][j] == 2) {
                    viruses.add(new Virus(i, j, 0));
                    map[i][j] = 0;
                } else if (map[i][j] == 0) {
                    map[i][j] = -1 ;
                } else {
                    map[i][j] = -2;
                }
            }
        }

        int[] arr = new int[viruses.size()];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = i;
        }

        boolean[] visit = new boolean[arr.length];
        comb(arr, visit, 0, 0, M);
        System.out.println(answer == Integer.MAX_VALUE ? -1 : answer);

    }

    public static void comb(int[] arr, boolean[] visit, int idx, int depth, int r) {

        if (r == depth) {
            // 바이러스 퍼뜨리기
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

        int [][] tmp = new int[N][N];

        for(int i = 0; i < N; i++) {
//            System.arraycopy(tmp[i], 0, map[i], 0, N);
            for(int j = 0; j < N; j++) {
                tmp[i][j] = map[i][j];
            }
        }

        Queue<Virus> q = new ArrayDeque<>();

        for (int i = 0; i < arr.length; i++) {
            if (visit[i]) {
                q.add(viruses.get(i));
            } else {
                Virus virus = viruses.get(i);
                tmp[virus.i][virus.j] = -1;
            }
        }

        while (!q.isEmpty()) {
            Virus temp = q.poll();

            tmp[temp.i][temp.j] = temp.time;

            for (int i = 0; i < 4; i++) {
                int di = temp.i + dir[i][0];
                int dj = temp.j + dir[i][1];

                if (di < 0 || dj < 0 || di >= N || dj >= N) continue;
                if (tmp[di][dj] == -1) {
                    tmp[di][dj] = temp.time + 1;
                    q.add(new Virus(di, dj, temp.time + 1));

                }
            }
        }

        int max = Integer.MIN_VALUE;
        boolean check = false;

        for (int i = 0; i < N; i++) {
            if (check) break;
            for (int j = 0; j < N; j++) {
                if (tmp[i][j] == -1) check = true;
                if (tmp[i][j] > max) max = tmp[i][j];
            }
        }
        if (!check && answer > max) answer = max;
    }

    public static class Virus {
        int i, j, time;

        Virus(int i, int j, int time) {
            this.i = i;
            this.j = j;
            this.time = time;
        }
    }
}
