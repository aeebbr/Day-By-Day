// [BOJ] 15683. 감시
// 풀이 시간: ?? 분 (실험 좀 많이 함)
// 실행 시간: 236 ms
// 메모리: 53968 KB

import java.io.*;
import java.util.*;

public class Main {

    static class Camera {
        int y, x, t;

        Camera(int y, int x, int t) {
            this.y = y;
            this.x = x;
            this.t = t;
        }
    }

    static int N, M, Ans;
    static int[][] map;
    // 오, 아, 왼, 위
    public static int[] dy = {0, 1, 0, -1};
    public static int[] dx = {1, 0, -1, 0};
    
    public static int[][][] cctv = { {{}},
            {{0}, {1}, {2}, {3}},
            {{0, 2}, {1, 3}},
            {{0, 1}, {1, 2}, {2, 3}, {0, 3}},
            {{0, 1, 2}, {1, 2, 3}, {0, 2, 3} ,{0, 1, 3}},
            {{0, 1, 2, 3}}};

    static ArrayList<Camera> cams = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map= new int[N][M];
        cams = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                map[i][j]=Integer.parseInt(st.nextToken());
                if(map[i][j] >= 1 && map[i][j] <= 5) {
                    cams.add(new Camera(i, j, map[i][j]));
                } else if (map[i][j] == 0) {
                    Ans++;
                }
            }
        }
        solving(0, map);
        System.out.println(Ans);
    }

    public static void solving(int idx, int[][] map) {
        if(idx == cams.size()) {

            int cnt = 0;
            for(int i = 0; i < N; i++) {
                for(int j = 0; j < M; j++) {
                    if(map[i][j] == 0) cnt++;
                }
            }
            Ans = Math.min(Ans, cnt);
            return;
        }

        Camera cam = cams.get(idx);

        for(int i = 0; i < cctv[cam.t].length; i++) {
            int[][] tmap = new int[N][M];
            for(int k = 0; k < N; k++) {
                System.arraycopy(map[k], 0, tmap[k], 0, M);
            }

            for(int d = 0; d < cctv[cam.t][i].length; d++) {
                int di = cam.y;
                int dj = cam.x;
                int nd = cctv[cam.t][i][d];

                while(true) {
                    di += dy[nd];
                    dj += dx[nd];

                    if (di < 0 || di >= N || dj < 0 || dj >= M) break;
                    if (tmap[di][dj] == 6) break;

                    tmap[di][dj] = 9;
                }
            }
            solving(idx+1, tmap);
        }
    }
}
