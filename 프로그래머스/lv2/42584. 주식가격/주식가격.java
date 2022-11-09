import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        Queue<Integer> q = new LinkedList<>();
        for (int p : prices) {
            q.add(p);
        }

        int index = 0;
        int[] answer = new int[prices.length];

        while (!q.isEmpty()) {
            int time = 0;
            Integer now = q.poll();
            for (int i = index + 1; i < prices.length; i++) {
                time++;
                if (now > prices[i]) {
                    break;
                }
            }
            answer[index] = time;
            index++;
        }

        return answer;
    }
}