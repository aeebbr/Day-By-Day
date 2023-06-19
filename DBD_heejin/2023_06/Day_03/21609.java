// [BOJ] 21609. 상어 중학교
// 풀이 시간: 00 분
// 실행 시간: 0 ms
// 메모리: 0 KB

import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class Main {

    // 왼 아 오 위
    public static int[][] dt = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

    public static void main(String[] args) throws IOException {
        // | r1 - r2| + | c1 - c2 | = 1
        // 사방탐색 -> 인접

        // 무지개 0
        // 검은색 -1

        // 가장 큰 그룹 찾기

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] map = new int[N][N];
        ArrayList<Cood> targets = new ArrayList<>();
        ArrayList<Cood> remove = new ArrayList<>();

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
                    int maxJ = first.j;
                    int coodSum = 1;
                    int coodRainbow = 0;

                    Queue<Cood> q = new ArrayDeque<>();

                    q.offer(first);
                    group.add(first);

                    System.out.println(first.i);
                    System.out.println(first.j);

                    visit[first.i][first.j] = true;

                    while (!q.isEmpty()) {
                        System.out.println("********start**********");
                        Cood temp = q.poll();

                        for (int j = 0; j < 4; j++) {
                            int di = temp.i + dt[j][0];
                            int dj = temp.j + dt[j][1];

                            if (di >= 0 && dj >= 0 && di < N && dj < N && (map[di][dj] == 0 || map[di][dj] == map[first.i][first.j]) && !visit[di][dj]) {
                                System.out.println("map = " + map[di][dj]);
                                visit[di][dj] = true;
                                q.offer(new Cood(di, dj));

                                if (map[di][dj] == 0) {
                                    coodRainbow++;
                                }
                                else {
                                    System.out.println("di = " + di);
                                    System.out.println("dj = " + dj);
                                    System.out.println("maxJ = " + maxJ);

                                    if (di > maxI) maxI = di;
                                    if (dj > maxJ) maxJ = dj;
                                }
                                coodSum++;
                                group.add(new Cood(di, dj));

                            }
                        }
                    }
                    System.out.println("maxJ = " + maxJ);

                    if (group.size() > 1) {
                        coods.add(new Coods(maxI, maxJ, coodRainbow, coodSum, group));
                    }
                }
            }

            if (coods.size() > 0) {

                System.out.println("coods size === "+coods.size());

                Collections.sort(coods);

                System.out.println(coods.size());
                System.out.println(coods.get(0).sum);
                Coods choose = coods.get(0);
                System.out.println("=== size ? " + targets.size());

                sum += (coods.get(0).sum * coods.get(0).sum);
                System.out.println("sum = " + sum);

                for (int j = 0; j < choose.sum; j++) {

                    Cood cood = choose.group.get(j);
                    System.out.println("i === " + cood.i + " ,  j === " + cood.j);
                    map[cood.i][cood.j] = -2;
                }

                targets.clear();
                down(map, N, false, targets);
                rotate(map, N);
                down(map, N, true, targets);
//                start = start + coods.get(0).sum - 1;
            } else {
                break;
            }


            for (int i = 0; i < N; i++) {
                System.out.println(Arrays.toString(map[i]));
            }

            System.out.println("**********************");
            System.out.println("왜 시작 안해주냐고오오오옹");
            System.out.println(size);
//            System.out.println(start);
            System.out.println(targets.size());


        }

    }

    public static void rotate(int[][] map, int N) {
        int [][] tmp = new int[N][N];

        for(int i = 0; i < N; ++i) {
            for(int j = 0; j < N; ++j) {
                tmp[N-j-1][i] = map[i][j];
            }
        }
        for(int i = 0; i < N; ++i) {
            System.arraycopy(tmp[i],0,map[i],0,N);
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

        System.out.println("down ===========");
        for (int i = 0; i < N; i++) {
            System.out.println(Arrays.toString(map[i]));
        }
        System.out.println("down end ===========");




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
                        if (this.j - o.j > 0) return 1;
                        else if (this.j - o.j < 0) return -1;
                        return 0;
                    }
                }
            }
        }
    }
}
