// [Programmers] 5014. 스타트링크
// 풀이 시간: 23 분
// 실행 시간: 140 ms
// 메모리: 36292 KB

import java.io.*;
import java.util.*;

public class Main {

    public static class Floor {
        int now, sum;

        Floor(int now, int sum) {
            this.now = now;
            this.sum = sum;
        }
    }

    public static int F, S, G, U, D =  0;
    public static boolean[] visit;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        F = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());
        G = Integer.parseInt(st.nextToken());
        U = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());

        visit = new boolean[F+1];

        bfs(S);
    }

    public static void bfs(int start) {

        ArrayDeque<Floor> q = new ArrayDeque<>();
        q.add(new Floor(start, 0));
        visit[start] = true;

        while (!q.isEmpty()) {
            Floor temp = q.poll();

            if (temp.now == G) {
                System.out.println(temp.sum);
                return;
            }

            if (temp.now + U <= F && !visit[temp.now + U]) {
                visit[temp.now + U] = true;
                q.add(new Floor(temp.now + U, temp.sum+1));
            }

            if (temp.now - D > 0 && !visit[temp.now - D]) {
                visit[temp.now - D] = true;
                q.add(new Floor(temp.now - D, temp.sum+1));
            }
        }
        System.out.println("use the stairs");
    }
}
