// [BOJ] 2615. 오목
// 풀이 시간: 00 분
// 실행 시간: 80 ms
// 메모리: 11596 KB

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int arr[][] = new int[20][20];

        for (int i = 1; i < 20; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 1; j < 20; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int ans = 0;
        int ans2 = 0;
        boolean c = false;

        for (int i = 1; i < 20; i++) {
            for (int j = 1; j < 20; j++) {
                if (arr[i][j] == 1) {
                    ans = check(1, i, j, arr);
                    if (ans == 1 || ans == 2 || ans == 3 || ans == 4) {
                        c = check2(1, ans, i, j, arr);
                        if(c) ans2 = 1;
                    }
                }

                else if (arr[i][j] == 2) {
                    ans = check(2, i, j, arr);
                    if (ans == 1 || ans == 2 || ans == 3 || ans == 4) {
                        c = check2(2, ans, i, j, arr);
                        if(c) ans2 = 2;
                    }
                }
                if(c) {
                    System.out.println(ans2);
                    System.out.println(i+" "+j);
                    c = false;
                    i = 20;
                    break;
                }
            }
        }
        if (ans == 0) System.out.println(ans);
    }

    private static int check(int k, int i, int j, int arr[][]) {

        int di = i;
        int dj = j;
        int cnt = 0;

        // 오른쪽
        while (dj+1 < 20 && arr[di][++dj] == k) {
            cnt++;
        }
        if (cnt == 4)
            return 1;
        else {
            cnt = 0;
            di = i;
            dj = j;
        }
        // 아래
        while (di+1 < 20 && arr[++di][dj] == k) {
            cnt++;
        }
        if (cnt == 4)
            return 2;
        else {
            cnt = 0;
            di = i;
            dj = j;
        }

        // 아래 대각선
        while (di+1 < 20 && dj + 1 < 20 && arr[++di][++dj] == k) {
            cnt++;
        }
        if (cnt == 4)
            return 3;
        else {
            cnt = 0;
            di = i;
            dj = j;
        }

        // 위 대각선
        while (di-1 >= 0 && dj+1 < 20 && arr[--di][++dj] == k) {
            cnt++;
        }
        if (cnt == 4)
            return 4;
        else
            return 0;
    }

    private static boolean check2(int k, int ans, int i, int j, int arr[][]) {
        switch (ans) {
            // 오른쪽
            case 1:
                if(arr[i][j-1] != k) return true;
                else return false;

                // 아래
            case 2:
                if(arr[i-1][j] != k) return true;
                else return false;

                // 아래 대각선
            case 3:
                if(arr[i-1][j-1] != k) return true;
                else return false;

                // 위 대각선
            case 4:
                if(arr[i+1][j-1] != k) return true;
                else return false;
        }
        return false;
    }
}
