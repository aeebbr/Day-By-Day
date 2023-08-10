// [Programmers] 12936. 줄 서는 방법
// 풀이 시간: 40 분

import java.util.*;

class Solution {
    public int[] solution(int n, long k) {
        ArrayList<Integer> arr = new ArrayList<Integer>();
        int[] answer = new int[n];
        
        long nFact = 1;
        for (int i = 1; i <= n; i++) {
            arr.add(i);
            nFact *= i;
        }
        
        for (int i = 0; i < n; i++) {
            int num;
            if (k == 0) {
                num = 0;
            } else {
                nFact /= n - i;
                num = (int) ((k - 1) / nFact);
                k = (k - 1) % nFact + 1;
            }
            answer[i] = arr.get(num);
            arr.remove(num);

        }
        
        return answer;
    }
    
    public long factorial(int n) {
        long res = 1;
        for (int i = 1; i <= n; i++) {
            res *= i;
        }
        
        return res;
    }
    
    // 이거 왜 stackoverflowerror 나지...
    // public long factorial(int n) {
    //     if (n == 1) return 1;
    //     return n * factorial(n - 1);
    // }
}