import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<Integer> q = new LinkedList<>();
        for (int w : truck_weights) {
            q.add(w);
        }
        Queue<Integer> present = new LinkedList<>();
        for (int i = 0; i < bridge_length; i++) {
            present.add(0);
        }
        
        int answer = 0;

        while (!q.isEmpty()) {
            present.poll();
            int sum = present.stream().mapToInt(i -> i).sum();
            if (sum + q.peek() <= weight) {
                present.add(q.poll());
            } else {
                present.add(0);
            }
            answer++;
        }

        return answer + bridge_length;
    }
}