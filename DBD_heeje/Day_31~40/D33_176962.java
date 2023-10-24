// [Programmers] 176962. 과제 진행하기
// 풀이 시간: 90 분

import java.util.*;

class Solution {
    public String[] solution(String[][] plans) {
        int N = plans.length;
        String[] answer = new String[N];
        int ansIdx = 0;
        for (String[] plan: plans) {
            int hour = Integer.valueOf(plan[1].substring(0, 2));
            int minute = Integer.parseInt(plan[1].substring(3));
            plan[1] = String.valueOf(hour * 60 + minute);
        }
        
        Arrays.sort(plans, (p1, p2) -> Integer.parseInt(p1[1]) - Integer.parseInt(p2[1]));
        Stack<String[]> stack = new Stack<>();
        
        int time = 0;
        int idx = 0;
        while (idx < N) {
            int nextTime = Integer.parseInt(plans[idx][1]);
            int diff = nextTime - time;
            time = nextTime;
            
            while (diff > 0 && !stack.isEmpty()) {
                int rTime = Integer.parseInt(stack.peek()[2]);
                if (rTime <= diff) {
                    diff -= rTime;
                    answer[ansIdx] = stack.pop()[0];
                    ansIdx += 1;
                } else {
                    stack.peek()[2] = String.valueOf(rTime - diff);
                    diff = 0;
                }
            }
            
            stack.push(plans[idx]);
            idx += 1;
        }
        
        while (!stack.isEmpty()) {
            answer[ansIdx] = stack.pop()[0];
            ansIdx += 1;
        }

        return answer;
    }
}