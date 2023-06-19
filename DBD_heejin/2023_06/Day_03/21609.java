// [BOJ] 21609. 상어 중학교
// 풀이 시간: 102 분
// 실행 시간: 200 ms
// 메모리: 26588 KB

import java.io.*;
import java.util.*;

public class Main {

    public static int[][] dt = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] map = new int[N][N];
        ArrayList<Cood> targets = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if (map[i][j] > 0) {
                    targets.add(new Cood(i, j));
                }
            }
        }

        int sum = 0;
        int size = targets.size();

        while (true) {

            ArrayList<Coods> coods = new ArrayList<>();

            for (int i = 0; i < targets.size(); i++) {

                boolean[][] visit = new boolean[N][N];
                Cood first = targets.get(i);

                if (!visit[first.i][first.j]) {
                    ArrayList<Cood> group = new ArrayList<>();

                    int maxI = first.i;
                    int minJ = first.j;
                    int coodSum = 1;
                    int coodRainbow = 0;

                    Queue<Cood> q = new ArrayDeque<>();

                    q.offer(first);
                    group.add(first);

                    visit[first.i][first.j] = true;

                    while (!q.isEmpty()) {
                        Cood temp = q.poll();

                        for (int j = 0; j < 4; j++) {
                            int di = temp.i + dt[j][0];
                            int dj = temp.j + dt[j][1];

                            if (di >= 0 && dj >= 0 && di < N && dj < N && (map[di][dj] == 0 || map[di][dj] == map[first.i][first.j]) && !visit[di][dj]) {
                                visit[di][dj] = true;
                                q.offer(new Cood(di, dj));

                                if (map[di][dj] == 0) {
                                    coodRainbow++;
                                }
                                else {
                                    if (di < maxI) maxI = di;
                                    if (dj < minJ) minJ = dj;
                                }
                                coodSum++;
                                group.add(new Cood(di, dj));

                            }
                        }
                    }

                    if (group.size() > 1) {
                        coods.add(new Coods(maxI, minJ, coodRainbow, coodSum, group));
                    }
                }
            }

            if (coods.size() > 0) {

                Collections.sort(coods);
                Coods choose = coods.get(0);

                sum += (coods.get(0).sum * coods.get(0).sum);
                
                for (int j = 0; j < choose.sum; j++) {

                    Cood cood = choose.group.get(j);
                    map[cood.i][cood.j] = -2;
                }

                targets.clear();
                down(map, N, false, targets);
                rotate(map, N);
                down(map, N, true, targets);
            } else {
                break;
            }
        }
        System.out.println(sum);
    }

    public static void rotate(int[][] map, int N) {
        int [][] tmp = new int[N][N];

        for(int i = 0; i < N; ++i) {
            for(int j = 0; j < N; ++j) {
                tmp[N-j-1][i] = map[i][j];
            }
        }
        for(int i = 0; i < N; ++i) {
            System.arraycopy(tmp[i], 0, map[i], 0, N);
        }
    }

    public static void down(int[][] map, int N, boolean check, ArrayList<Cood> targets) {

        for (int i = N - 1; i >= 0; i--) {
            for (int j = 0; j < N; j++) {
                if (map[i][j] == -2) {
                    for (int k = i - 1; k >= 0; k--) {
                        if (map[k][j] > -1) {
                            map[i][j] = map[k][j];
                            map[k][j] = -2;
                            break;
                        } else if (map[k][j] == -1) {
                            break;
                        }
                    }
                }

                if (check && map[i][j] > 0) {
                    targets.add(new Cood(i, j));
                }
            }
        }
    }

    private static class Cood {
        int i, j;

        public Cood(int i, int j) {
            this.i = i;
            this.j = j;
        }

        @Override
        public boolean equals(Object obj) {
            return (i == ((Cood) obj).i && j == ((Cood) obj).j);
        }
    }

    private static class Coods extends Cood implements Comparable<Coods> {
        int rainbow, sum;
        ArrayList<Cood> group;

        public Coods(int i, int j) {
            super(i, j);
        }

        public Coods(int i, int j, int rainbow, int sum, ArrayList<Cood> group) {
            super(i, j);
            this.rainbow = rainbow;
            this.sum = sum;
            this.group = group;
        }

        @Override
        public int compareTo(Coods o) {
            if (this.sum - o.sum < 0) return 1;
            else if (this.sum - o.sum > 0) return -1;
            else {
                if (this.rainbow - o.rainbow < 0) return 1;
                else if (this.rainbow - o.rainbow > 0) return -1;
                else {
                    if (this.i - o.i < 0) return 1;
                    else if (this.i - o.i > 0) return -1;
                    else {
                        if (this.j - o.j < 0) return 1;
                        else if (this.j - o.j > 0) return -1;
                        return 0;
                    }
                }
            }
        }
    }
}
