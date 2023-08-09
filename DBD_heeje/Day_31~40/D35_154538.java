// [Programmers] 154538. 숫자 변환하기
// 풀이 시간: 60 분

// 수정 전 코드
import java.util.*;

class Solution {
    public int solution(int x, int y, int n) {
        return bfs(x, y, n);
    }

    public int bfs(int sx, int y, int n) {
        Set<Integer> visited = new HashSet<Integer>();
        visited.add(sx);
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[] {sx, 0});
        
        while (!q.isEmpty()) {
            int[] arr = q.poll();
            int x = arr[0];
            int time = arr[1];
            
            if (x == y) {
                return time;
            }
            
            // lambda 함수 같은 거 없나
            // 반복문 돌리고 싶은데 어떻게 쓰지
            if (x + n <= y && !visited.contains(x + n)) {
                q.add(new int[] {x + n, time + 1});
                visited.add(x + n);
            }
            
            if (x * 2 <= y && !visited.contains(x * 2)) {
                q.add(new int[] {x * 2, time + 1});
                visited.add(x * 2);
            }
            
            if (x * 3 <= y && !visited.contains(x * 3)) {
                q.add(new int[] {x * 3, time + 1});
                visited.add(x * 3);
            }
        }
        
        return -1;
    }
}

// 수정 후 코드
import java.util.*;

class Solution {
    public int solution(int x, int y, int n) {
        return bfs(x, y, n);
    }
    
		// 이게 맞나..?
    @FunctionalInterface
    public interface IntFunction {
        int apply(int x);        
    }
    public int bfs(int sx, int y, int n) {
        Set<Integer> visited = new HashSet<Integer>();
        visited.add(sx);
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[] {sx, 0});
        IntFunction[] funcs = {(int x) -> x + n, (int x) -> x * 2, (int x) -> x * 3};
        
        while (!q.isEmpty()) {
            int[] arr = q.poll();
            int x = arr[0];
            int time = arr[1];
            
            if (x == y) {
                return time;
            }
            
            for (IntFunction func: funcs) {
                int nx = func.apply(x);
                if (nx <= y && !visited.contains(nx)) {
                    q.add(new int[] {nx, time + 1});
                    visited.add(nx);
                }                
            }

        }
        
        return -1;
    }
}