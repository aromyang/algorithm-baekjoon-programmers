import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> q = new PriorityQueue<>();
        for (int s : scoville) {
            q.add(s);
        }

        int answer = 0;

        while (q.size() >= 2) {
            Integer first = q.poll();
            if (first >= K) {
                return answer;
            }

            int hotter = first + q.poll() * 2;
            q.add(hotter);
            answer++;
        }

        return (q.poll() >= K) ? answer : -1;
    }
}