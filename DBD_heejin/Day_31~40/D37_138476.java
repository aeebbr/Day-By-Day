// [Programmers] 138476. 귤 고르기
// 풀이 시간: 30 분

import java.io.*;
import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {

        Map<Integer, Integer> min = new HashMap<>();

        for (int i = 0; i < tangerine.length; i++) {
            min.put(tangerine[i], min.getOrDefault(tangerine[i], 0) + 1);
        }

        List<Map.Entry<Integer, Integer>> enrtyList = new ArrayList<>(min.entrySet());
        enrtyList.sort((o1, o2) -> o2.getValue() - o1.getValue());

        int sum = 0;
        int answer = 0;

        for (Map.Entry<Integer, Integer> temp : enrtyList) {
            if (sum >= k) break;
            answer++;
            sum += temp.getValue();
        }
        return answer;
    }
}