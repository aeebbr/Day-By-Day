// [Programmers] 169199. 리코쳇 로봇
// 풀이 시간: 40 분

import java.util.*;

class Solution {
    public static class Point {
        int i, j;
        
        Point(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }
    public static int R;
    public static int C;
    public int solution(String[] board) {
        R = board.length;
        C = board[0].length();

        // 이거 필수로 물어보기.... 코드 너무 마음에 안듦 고구마 백개 먹은 듯한 느낌
        return bfs(findRobot(board), board);
    }
    
    public Point findRobot(String[] board) {
        Point robot = null;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (board[i].charAt(j) == 'R') {
                    robot = new Point(i, j);
                    
                    return robot;
                }
            }
        }
        return robot;
    }
    
    public int bfs(Point robot, String[] board) {
        // python은 dir라는 예약어가 있어서 네이밍 이렇게 안하는데 java는 없나? 자동완성 안되니까 모르겠네..
        int[][] dir = { {-1, 0}, {0, -1}, {1, 0}, {0, 1} };
        int[][] v = new int[R][C];
        Queue<Point> queue = new LinkedList<>();
        queue.add(robot);
        v[robot.i][robot.j] = 1;
        
        while (!queue.isEmpty()) {
            Point point = queue.poll();
            
            if (board[point.i].charAt(point.j) == 'G') {
                return v[point.i][point.j] - 1;
            }
            
            for (int d = 0; d < 4; d++) {
                int ny = point.i + dir[d][0];
                int nx = point.j + dir[d][1];
                
                // 요거보다 밑에가 더 깔끔한 듯
                // int ny = point.i;
                // int nx = point.j;
                
                // while (inRange(ny + dir[d][0], nx + dir[d][1]) && board[ny + dir[d][0]].charAt(nx + dir[d][1]) != 'D') {
                //     ny += dir[d][0];
                //     nx += dir[d][1];
                // }                
                
                while (inRange(ny, nx) && board[ny].charAt(nx) != 'D') {
                    ny += dir[d][0];
                    nx += dir[d][1];
                }
                
                // 대신 더한 것 하나 빼줘야 한다는 아쉬움..
                ny -= dir[d][0];
                nx -= dir[d][1];
                
                if (v[ny][nx] == 0) {
                    // Point 쓰니까 변수명이 살짝 마음에 안드는데??
                    // 원래는 v[ny][nx] = v[y][x] + 1 요렇게 썼었는뎅..
                    v[ny][nx] = v[point.i][point.j] + 1;
                    queue.add(new Point(ny, nx));
                }
            }   
        }
        
    return -1;
    }
    
    public boolean inRange(int y, int x) {
        return y >= 0 && y < R && x >= 0 && x < C;
    }
}