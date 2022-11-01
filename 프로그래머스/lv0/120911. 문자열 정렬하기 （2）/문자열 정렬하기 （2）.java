import java.util.Arrays;

class Solution {
    public String solution(String my_string) {
        String lower = my_string.toLowerCase();
        char[] chars = lower.toCharArray();
        Arrays.sort(chars);
        return new String(chars);
    }
}