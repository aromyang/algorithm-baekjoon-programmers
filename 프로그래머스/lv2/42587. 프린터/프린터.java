import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        Queue<Paper> q = new LinkedList<>();

        for (int i = 0; i < priorities.length; i++) {
            q.add(new Paper(i, priorities[i]));
        }

        int answer = 0;

        while (!q.isEmpty()) {
            Paper paper = q.stream()
                    .max(Comparator.comparingInt(Paper::getPri))
                    .get();

            if (q.peek().equals(paper)) {
                Paper now = q.poll();
                answer++;
                if (now.getIndex() == location) {
                    return answer;
                }
            } else {
                while (!q.peek().equals(paper)) {
                    q.add(q.poll());
                }
            }
        }

        return answer;
    }
    
    static class Paper {
        int index, pri;

        public Paper(int index, int pri) {
            this.index = index;
            this.pri = pri;
        }

        public int getIndex() {
            return index;
        }

        public int getPri() {
            return pri;
        }
    }

}