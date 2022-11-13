import java.util.Arrays;

class Solution {
    public int[] solution(int n, String[] words) {
        int person = 0;
        int order = 0;

        for (int i = 1; i < words.length; i++) {
            person = (i % n) + 1;
            order = (i / n) + 1;
            if (words[i].charAt(0) != words[i - 1].charAt(words[i - 1].length() - 1)) {
                return new int[]{person, order};
            } else {
                for (int j = 0; j < i; j++) {
                    if (words[i].equals(words[j])) {
                        return new int[]{person, order};
                    }
                }
            }
        }

        return new int[]{0, 0};
    }
}