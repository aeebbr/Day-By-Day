// [BOJ] 15683. 감시
// 풀이 시간: 00 분
// 실행 시간: 0 ms
// 메모리: 0 KB

import java.io.*;
import java.util.*;

public class Main {
    public static int N, M, Ans;
    public static int[][] map;

    // 오, 아, 왼, 위
    public static int[] dy = {0, 1, 0, -1};
    public static int[] dx = {1, 0, -1, 0};
    public static int[][][] cctv = { {{}},
            {{0}, {1}, {2}, {3}},
            {{0, 2}, {1, 3}},
            {{0, 1}, {1, 2}, {2, 3}, {0, 3}},
            {{0, 1, 2}, {1, 2, 3}, {0, 2, 3} ,{0, 1, 3}},
            {{0, 1, 2, 3}}};
    public static class Camera{
        int r, c, t;
        Camera(int r,int c, int t){
            this.r=r;
            this.c=c;
            this.t=t;
        }
    }
    public static ArrayList<Camera> cams;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map= new int[N][M];
        cams = new ArrayList<>();

        for (int r = 0; r < N; r++) {
            st = new StringTokenizer(br.readLine());
            for (int c = 0; c < M; c++) {
                map[r][c]=Integer.parseInt(st.nextToken());
                if(map[r][c] >= 1 && map[r][c] <= 5) {
                    cams.add(new Camera(r, c, map[r][c]));
                } else if (map[r][c] == 0) {
                    Ans++;
                }
            }
        }
        solving(0, map);
        System.out.println(Ans);
    }

    private static void solving(int idx, int[][] map) {
        //basis part
        // 모든 카메라로 지도를 검색했다면
        if(idx == cams.size()) {
            // 지도의 사각지대를 구한다
            int cnt = 0;
            //print(map);
            for (int r = 0; r < N; r++) {
                for (int c = 0; c < M; c++) {
                    if(map[r][c] == 0) cnt++;
                }
            }
            Ans = Math.min(Ans, cnt);
            return;
        }

        //inductive part
        Camera cam = cams.get(idx);
        int r = cam.r;
        int c = cam.c;

        for (int i = 0; i < cctv[cam.t].length; i++) {
            int[][] tmap = new int[N][M];
            for(int k = 0; k < N; ++k) {
//                System.arraycopy(map[k], 0, tmap[k], 0, N);
                tmap[k] = map[k].clone();
            }

            for (int d = 0; d < cctv[cam.t][i].length; d++) {
                int dir = cctv[cam.t][i][d];

                int dr = r + dy[dir];
                int dc = c + dx[dir];

                while(true) {

                    if (dr < 0 || dr >= N || dc < 0 || dc >= M) break;
                    if (tmap[dr][dc] == 6) break;

                    tmap[dr][dc] = 9;

                    dr += dy[dir];
                    dc += dx[dir];
                }
                solving(idx + 1, tmap);
            }
        }
    }
}

