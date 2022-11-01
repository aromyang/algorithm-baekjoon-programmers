class Solution {
    public int solution(String[] s1, String[] s2) {
        int count = 0;

        for (String value : s1) {
            for (String s : s2) {
                if (value.equals(s)) {
                    count++;
                }
            }
        }
    
        return count;
    }
}