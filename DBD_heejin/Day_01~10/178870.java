// [Programmers] 178870. 연속된 부분 수열의 합
// 풀이 시간: 24분

import java.util.*;

class Solution {
    public int[] solution(int[] sequence, int k) {
        
        int left = sequence.length - 1;
        int right = sequence.length - 1;
        int sum = sequence[sequence.length - 1];
        
        while(true) {
            if(sum == k) {
                break;
            }
            
            else if(sum > k) {
                if (left != right) {
                    sum -= sequence[right--];
                }
                else {
                    sum += sequence[--left];
                }
            }
            else {
                sum += sequence[--left];
            }
        }
        
        while(left > 0 && right > 0 && sequence[left-1] == sequence[right]) {
            left--;
            right--;
          
        }
        int[] answer = {left, right};
        return answer;
    }
}
