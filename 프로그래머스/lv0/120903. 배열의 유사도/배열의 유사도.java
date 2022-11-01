class Solution {
    public int solution(String[] s1, String[] s2) {
        int count = 0;

        if (s1.length >= s2.length) {
            for (String value : s1) {
                for (String s : s2) {
                    if (value.equals(s)) {
                        count++;
                    }
                }
            }
        } else {
            for (String value : s2) {
                for (String s : s1) {
                    if (value.equals(s)) {
                        count++;
                    }
                }
            }
        }
        return count;
    }
}