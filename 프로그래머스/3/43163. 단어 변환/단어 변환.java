import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
           boolean[] visited = new boolean[words.length];
        Deque<Current> deque = new ArrayDeque<>();
        deque.add(new Current(begin, 0));

        while (!deque.isEmpty()) {
            Current current = deque.pollFirst();

            if (current.word.equals(target)) {
                return current.step;
            }

            for (int wordIdx = 0; wordIdx < words.length; wordIdx++) {
                if (visited[wordIdx]) {
                    continue;
                }

                int count = 0;
                for (int charIdx = 0; charIdx < words[wordIdx].length(); charIdx++) {
                    if (words[wordIdx].charAt(charIdx) != current.word.charAt(charIdx)) {
                        count++;
                    }
                }

                if (count == 1) {
                    visited[wordIdx] = true;
                    deque.add(new Current(words[wordIdx], current.step + 1));
                }
            }
        }

        return 0;
    }

    private static class Current {
        private final String word;
        private final int step;

        public Current(String word, int step) {
            this.word = word;
            this.step = step;
        }
    }
}